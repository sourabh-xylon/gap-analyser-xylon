from llm.configure_llm import kimi_k2_llm
from fastapi import APIRouter, Form
from prompts.gap_finder import gap_analyser

router = APIRouter()


def find_the_gap_in_invoice_text(invoice_text: str, user_id: str, email_id: str, use_case: str):
    """
    Takes invoice JSON/text input, evaluates against required fields, and finds missing ones.
    """
    try:
        import json
        invoice_dict = json.loads(invoice_text)

        # Flatten top-level keys (handles dict input)
        def extract_keys(data, parent_key=""):
            keys = []
            if isinstance(data, dict):
                for k, v in data.items():
                    full_key = f"{parent_key}_{k}" if parent_key else k
                    keys.append(full_key)
                    keys.extend(extract_keys(v, full_key))
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    keys.extend(extract_keys(item, f"{parent_key}_{i}"))
            return keys

        invoice_columns = extract_keys(invoice_dict)

        required_fields = []
        from uae_invoicing.usecases import (
            use_cases_which_require_fifty_common_fields,
            other_invoicing_use_cases,
            all_invoicing_use_cases,
        )
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
            return {
                "message": "This use case is not supported or not mentioned in the expected format",
                "supported_use_cases": all_invoicing_use_cases,
            }

        from langchain_core.prompts import ChatPromptTemplate
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", gap_analyser),
            ("human", "Submitted invoice fields: {invoice_fields}")
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

        import json
        response_content = response.content
        missing_fields = json.loads(
            response_content[response_content.index("{"):response_content.rindex("}") + 1]
        )

        return missing_fields

    except Exception as e:
        return {"error": str(e)}


use_cases_mapping_to_the_invoices_data = [
"uae_standard_tax_invoice",
"uae_standard_tax_invoice",
"uae_standard_tax_invoice",
"supplies_under_reverse_charge_mechanism",
"supplies_under_reverse_charge_mechanism",
"supplies_under_reverse_charge_mechanism",
"supplies_under_profit_margin_scheme",
"supplies_under_profit_margin_scheme",
"supplies_under_profit_margin_scheme",
"supplies_under_a_free_zone",
"supplies_under_a_free_zone",
"supplies_under_a_free_zone",
"exports",
"exports",
"exports",
"imports",
"imports",
"imports",
"self_billed_invoice",
"self_billed_invoice",
"self_billed_invoice",
"credit_note",
"credit_note",
"credit_note",
"debit_note",
"debit_note",
"debit_note",
"third_party_billing_on_behalf_of_another_party",
"third_party_billing_on_behalf_of_another_party",
"b2c_invoicing",
"b2c_invoicing",
"intra_gcc_supplies",
"uae_government_invoicing",
"commercial_invoice",
"payment_receipt",
"tax_refunds_and_adjustments"
]

import pandas as pd

df = pd.read_json("/Users/sourabh/gap-analyser/all_invoices.jsonl",lines=True)

cols = list(df.columns)

import json

cols = list(df.columns)


result_maps = []
use_cases_maps = []

for (row, use_case) in zip(df.itertuples(index=False, name=None),
                           use_cases_mapping_to_the_invoices_data):
    row_obj = {c: v for c, v in zip(cols, row)}          
    text = json.dumps(row_obj, ensure_ascii=False)       
    res = find_the_gap_in_invoice_text(text, "test_user", "test@gmail.com", use_case)
    result_maps.append(res)
    use_cases_maps.append(use_case)

result = pd.DataFrame({"use_case":use_cases_maps, "missing_fileds":result_maps})

result.to_csv("gap_analyser_results_with_description.csv")