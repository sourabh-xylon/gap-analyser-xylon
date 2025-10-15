import streamlit as st
import pandas as pd
import json
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Invoice Gap Analyzer",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Invoice Gap Analyzer")

# Import necessary modules
try:
    from llm.configure_llm import kimi_k2_llm, gpt_4o_llm
    from prompts.gap_finder import gap_analyser
    from uae_invoicing.usecases import (
        all_invoicing_use_cases,
        use_cases_which_require_fifty_common_fields,
        other_invoicing_use_cases
    )
    from uae_invoicing.fields import (
        fifty_common_fields,
        __dict__ as fields_dict
    )
    from uae_invoicing.field_description import master_field_dictionary
    from langchain_core.prompts import ChatPromptTemplate

    modules_loaded = True
except ImportError as e:
    st.error(f"Error importing modules: {str(e)}")
    modules_loaded = False

def find_the_gap_in_invoice(invoice_columns, user_id, email_id, use_case):
    """Analyze gap between submitted invoice fields and required fields"""
    try:
        required_fields = []

        if use_case in use_cases_which_require_fifty_common_fields:
            required_fields.extend(fifty_common_fields)
            additional_fields_name = f"additional_fields_required_for_{use_case}"
            additional_fields = fields_dict.get(additional_fields_name, [])
            required_fields.extend(additional_fields)
        elif use_case in other_invoicing_use_cases:
            all_fields_name = f"fields_required_for_{use_case}"
            all_fields = fields_dict.get(all_fields_name, [])
            required_fields.extend(all_fields)
        else:
            return {
                "error": True,
                "message": "This use case is not supported",
                "supported_use_cases": all_invoicing_use_cases
            }

        # Prepare field descriptions
        description_with_required_fields = []
        for field in required_fields:
            description = master_field_dictionary.get(field, "No description available")
            description_with_required_fields.append(field + ": " + description + "|")

        # Create LLM chain
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", gap_analyser),
            ("human", "Submitted invoice fields: {invoice_fields}")
        ])
        chain = prompt_template | gpt_4o_llm

        # Invoke LLM
        response = chain.invoke({
            "use_case": use_case,
            "required_fields": description_with_required_fields,
            "invoice_fields": invoice_columns
        })

        response_content = response.content

        # Parse JSON response
        start_idx = response_content.index("{")
        end_idx = response_content.rindex("}") + 1
        result_data = json.loads(response_content[start_idx:end_idx])
        result_data['total_required'] = len(required_fields)
        return result_data

    except Exception as e:
        return {"error": True, "message": str(e)}

# Initialize session state
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

# Input tabs
tab1, tab2 = st.tabs(["📝 Text Input", "📁 File Upload"])

with tab1:
    invoice_fields_text = st.text_area(
        "Invoice Fields (comma-separated)",
        placeholder="invoice_number, invoice_date, customer_name, amount",
        height=100
    )
    if modules_loaded:
        selected_use_case = st.selectbox("Use Case", options=all_invoicing_use_cases)
        if st.button("Analyze", type="primary", key="manual"):
            if invoice_fields_text.strip():
                with st.spinner("Analyzing..."):
                    invoice_fields = [f.strip() for f in invoice_fields_text.split(",") if f.strip()]
                    result = find_the_gap_in_invoice(invoice_fields, "user", "user@email.com", selected_use_case)
                    st.session_state.analysis_result = result
                    st.session_state.submitted_count = len(invoice_fields)
            else:
                st.error("Please enter invoice fields")

with tab2:
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
    if uploaded_file and modules_loaded:
        df = pd.read_csv(uploaded_file)
        csv_columns = df.columns.tolist()
        first_row_values = df.iloc[0].tolist() if len(df) > 0 else []
        combined_fields = csv_columns + first_row_values
        file_use_case = st.selectbox("Use Case", options=all_invoicing_use_cases, key="file_case")
        if st.button("Analyze", type="primary", key="file"):
            with st.spinner("Analyzing..."):
                result = find_the_gap_in_invoice(combined_fields, "user", "user@email.com", file_use_case)
                st.session_state.analysis_result = result
                st.session_state.submitted_count = len(combined_fields)

# Display results
if st.session_state.analysis_result:
    result = st.session_state.analysis_result

    if result.get("error"):
        st.error(f"Error: {result.get('message')}")
    else:
        st.markdown("---")

        missing_fields = result.get("missing_fields", [])
        present_fields_dict = result.get("present_fields", {})
        total_required = result.get("total_required", 0)
        missing_count = len(missing_fields)
        present_count = len(present_fields_dict)
        gap_percentage = (missing_count / total_required * 100) if total_required > 0 else 0

        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Missing Fields", missing_count)
        col2.metric("Present Fields", present_count)
        col3.metric("Total Required", total_required)
        col4.metric("Gap %", f"{gap_percentage:.1f}%")
        
        # Side-by-side listing of mapping and missing
        col_left, col_right = st.columns(2)

        # Present fields mapping
        with col_left:
            st.subheader("✅ Present Fields Mapping")
            if present_fields_dict:
                present_df = pd.DataFrame([
                    {"Required Field": k, "User Provided Field": v}
                    for k, v in present_fields_dict.items()
                ])
                present_df.index = present_df.index + 1
                st.dataframe(present_df, use_container_width=True, hide_index=False, height=400)
                csv_present = present_df.to_csv(index=False)
                st.download_button(
                    "Download Present Fields Mapping",
                    data=csv_present,
                    file_name="present_fields_mapping.csv",
                    mime="text/csv",
                    key="download_present"
                )
            else:
                st.info("No present fields matched.")

        # Missing fields list
        with col_right:
            st.subheader("❌ Missing Mandatory Fields")
            if missing_fields:
                missing_df = pd.DataFrame(missing_fields, columns=["Missing Required Field"])
                missing_df.index = missing_df.index + 1
                st.dataframe(missing_df, use_container_width=True, hide_index=False, height=400)
                csv_missing = missing_df.to_csv(index=False)
                st.download_button(
                    "Download Missing Fields",
                    data=csv_missing,
                    file_name="missing_fields.csv",
                    mime="text/csv",
                    key="download_missing"
                )
            else:
                st.success("All required fields are present!")
