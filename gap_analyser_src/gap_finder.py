from llm.configure_llm import kimi_k2_llm
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import tempfile
import os
from prompts.gap_finder import gap_analyser

router = APIRouter()


def find_the_gap_in_invoice(invoice_csv, user_id, email_id, use_case):
    try:
        required_fields = []
        import pandas as pd
        df = pd.read_csv(invoice_csv)

        invoice_columns = df.columns.tolist()

        print(invoice_columns)
        from uae_invoicing.usecases import use_cases_which_require_fifty_common_fields, other_invoicing_use_cases, all_invoicing_use_cases
        from uae_invoicing.fields import fifty_common_fields
        
        if use_case in use_cases_which_require_fifty_common_fields:
            required_fields.extend(fifty_common_fields)
            additional_fields_name = f"additional_fields_required_for_{use_case}"
            from uae_invoicing.fields import __dict__ as fields_dict
            additional_fields = fields_dict.get(additional_fields_name, [])
            required_fields.extend(additional_fields)
        elif use_case in other_invoicing_use_cases:
            all_fields_name = f"fields_required_for_{use_case}"
            from uae_invoicing.fields import __dict__ as fields_dict
            all_fields = fields_dict.get(all_fields_name, [])
            required_fields.extend(all_fields)
        else:
            return {"message": "This use is not supoorted or not mentined in the expected format", "supported_use_cases":all_invoicing_use_cases}
        
        print("Invoice Columns", invoice_columns)
        from langchain_core.prompts import ChatPromptTemplate
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", gap_analyser),
            ("human", "Submitted invoice fields: {invoice_details}")
        ])
        chain = prompt_template | kimi_k2_llm
        from uae_invoicing.field_description import master_field_dictionary
        description_with_required_fileds = []

        for field in required_fields:
            description_with_required_fileds.append(field + ": " + master_field_dictionary.get(field) + "|")

        response = chain.invoke({
            "use_case": use_case,
            "required_fields": description_with_required_fileds,
            "invoice_fields" : invoice_columns
        })

        response_content = response.content
        print(response_content)
        import json
        missing_fields = json.loads(response_content[response_content.index("{"):response_content.rindex("}")+1])
        print(len(missing_fields["missing_fields"]))
        return missing_fields

    except Exception as e:
        return {"error": str(e)}

@router.post("/analyze-gap")
async def analyze_gap(
    file: UploadFile = File(...),
    user_id: str = Form(...),
    email_id: str = Form(...),
    use_case: str = Form(...)
):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name
    
    try:
        result = find_the_gap_in_invoice(temp_file_path, user_id, email_id, use_case)
        return result
    finally:
        os.unlink(temp_file_path)  


@router.get("/get_the_use_cases")
def get_the_use_cases(user_id: str):
    from uae_invoicing.usecases import all_invoicing_use_cases
    return {"use_cases": all_invoicing_use_cases}


        