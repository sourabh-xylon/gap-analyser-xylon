fifty_common_fields = [
    "invoice_number",
    "invoice_date",
    "invoice_type_code",
    "invoice_transaction_type_code",
    "invoice_currency_code",
    "payment_due_date",
    "business_process_type",
    "specification_identifier",
    "payment_means_type_code",
    "seller_name",
    "seller_electronic_address",
    "seller_electronic_identifier",
    "seller_legal_registration_identifier",
    "seller_legal_registration_identifier_type",
    "seller_tax_identifier_trn",
    "seller_tax_scheme_code",
    "seller_address_line_1",
    "seller_city",
    "seller_country_subdivision",
    "seller_country_code",
    "buyer_name",
    "buyer_electronic_address",
    "buyer_electronic_identifier",
    "buyer_tax_identifier_trn",
    "buyer_tax_scheme_code",
    "buyer_address_line_1",
    "buyer_city",
    "buyer_country_subdivision",
    "buyer_country_code",
    "sum_of_invoice_line_net_amount",
    "invoice_total_amount_without_tax",
    "invoice_total_tax_amount",
    "invoice_total_amount_with_tax",
    "amount_due_for_payment",
    "tax_category_taxable_amount",
    "tax_category_tax_amount",
    "tax_category_code",
    "tax_category_rate",
    "vat_line_amount",
    "invoice_line_identifier",
    "invoiced_quantity",
    "unit_of_measure_code",
    "invoice_line_net_amount",
    "item_net_price",
    "item_gross_price",
    "item_price_base_quantity",
    "invoiced_item_tax_category_code",
    "invoiced_item_tax_rate",
    "item_name",
    "item_description"
]


additional_fields_required_for_supplies_under_reverse_charge_mechanism = [
    "reverse_charge_statement",
    "rcm_codes",
    "vat_zero_rating_reason_text_fields",
    "payment_settlement_details",
    "invoice_period_dates",
    "buyer_identification_and_scheme_identifier",
    "tax_category_code"
]

additional_fields_required_for_supplies_under_profit_margin_scheme = [
    "no_separate_vat_amount",
    "mandatory_statement",
    "specific_tax_category_code",
    "additional_fields_for_original_purchase_details"
]


additional_fields_required_for_supplies_under_a_free_zone = [
    "transaction_type_code_flag",
    "vat_treatment_for_goods_declaration",
    "vat_treatment_for_services_declaration",
    "declaration_for_beneficiary",
    "proof_of_movement_documentation",
    "tax_category_code_for_vat_treatment"
]



additional_fields_required_for_exports = [
    "transaction_type_code",
    "vat_treatment_status",
    "export_specific_fields",
    "buyer_information_and_transmission_details",
    "proof_of_export_documentation"
]


additional_fields_required_for_imports = [
    "customs_declaration_number",
    "customs_declaration_date",
    "vat_handling_details",
    "tax_category_code",
    "vat_line_amount"
]

additional_fields_required_for_self_billed_invoice = [
    "self_billing_agreement_reference",
    "invoice_document_type_code",
    "mandatory_statement",
    "true_reflection_of_supply"
]

additional_fields_required_for_credit_note = [
    "document_title",
    "unique_reference_number",
    "reference_to_original_invoice",
    "description_of_adjustments",
    "financial_details",
    "reason_for_issuance"
]

additional_fields_required_for_debit_note = [
    "document_title",
    "unique_reference_number",
    "reference_to_original_invoice",
    "reason_for_issuance",
    "financial_details"

]


additional_fields_required_for_third_party_billing_on_behalf_of_another_party = [
    "transaction_type_code",
    "agent_and_principal_identification",
    "mandatory_statement",
    "legal_documentation"

]

additional_fields_required_for_b2c_invoicing = {
    "conditional_fields" : [
    "reverse_charge_vat_reason_code",
    "incoterms",
    "export_license_number",
    "continuous_supply_period_dates",
    "self_billing_agreement_reference",
    "self_billed_document_type_code"
],
"optional_fields" : [
    "order_reference",
    "contract_reference",
    "discounts_and_charges",
    "hsn_codes"
]
}

additional_fields_required_for_intra_gcc_supplies = [
    "reverse_charge_mechanism_statement",
    "vat_treatment_details",
    "buyers_vat_details",
    "transaction_type_code",
    "legal_note"

]

additional_fields_required_for_uae_government_invoicing = [
    "government_entity_identifier",
    "transaction_type_code",
    "electronic_transmission_requirement"

]

fields_required_for_commercial_invoice = [
    "invoice_number",
    "invoice_date",
    "invoice_type_code",
    "invoice_transaction_type_code",
    "invoice_currency_code",
    "payment_due_date",
    "business_process_type",
    "specification_identifier",
    "payment_means_type_code",
    "seller_name",
    "seller_electronic_address",
    "seller_electronic_identifier",
    "seller_legal_registration_identifier",
    "seller_legal_registration_identifier_type",
    "seller_tax_identifier_trn",
    "seller_tax_scheme_code",
    "seller_address_line_1",
    "seller_city",
    "seller_country_subdivision",
    "seller_country_code",
    "buyer_name",
    "buyer_electronic_address",
    "buyer_electronic_identifier",
    "buyer_tax_identifier_trn",
    "buyer_tax_scheme_code",
    "buyer_address_line_1",
    "buyer_city",
    "buyer_country_subdivision",
    "buyer_country_code",
    "sum_of_invoice_line_net_amount",
    "invoice_total_amount_without_tax",
    "invoice_total_tax_amount",
    "invoice_total_amount_with_tax",
    "amount_due_for_payment",
    "tax_category_taxable_amount",
    "tax_category_tax_amount",
    "tax_category_code",
    "tax_category_rate",
    "invoice_line_identifier",
    "invoiced_quantity",
    "unit_of_measure_code",
    "invoice_line_net_amount",
    "item_net_price",
    "item_gross_price",
    "item_price_base_quantity",
    "invoiced_item_tax_category_code",
    "invoiced_item_tax_rate",
    "item_name",
    "item_description",
    "terms_of_sale_incoterms",
    "shipping_details",
    "country_of_origin",
    "legal_attestation",
    "tax_status"
]

fields_required_for_payment_receipt = [
    "supplier_name",
    "supplier_address",
    "supplier_tax_registration_number_trn",
    "unique_serial_number_or_invoice_number",
    "date_of_issue",
    "description_of_goods_or_services",
    "total_amount_inclusive_of_vat",
    "total_vat_amount",
    "applicable_vat_rates"
]

fields_required_for_tax_refunds_and_adjustments = [
    "tax_registration_number_trn",
    "legal_name_of_entity",
    "total_amount_of_excess_refundable_tax",
    "amount_to_be_refunded",
    "details_of_applicable_penalties",
    "authorized_signatory_details",
    "declaration_of_accuracy",
    "tax_return_period_being_amended",
    "detailed_description_of_error",
    "financial_impact_of_adjustment",
    "supporting_documentation_for_correction"
]