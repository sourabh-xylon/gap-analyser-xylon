master_field_dictionary = {
    # Fifty Common Fields
    "invoice_number": "Unique invoice identification number",
    "invoice_date": "Date when the invoice was issued",
    "invoice_type_code": "Code indicating the type of invoice",
    "invoice_transaction_type_code": "Transaction type classification code",
    "invoice_currency_code": "Currency code for invoice amounts",
    "payment_due_date": "Date when payment is due",
    "business_process_type": "Type of business process category",
    "specification_identifier": "Technical specification identifier",
    "payment_means_type_code": "Code for payment method type",
    "seller_name": "Legal name of the selling company",
    "seller_electronic_address": "Seller's electronic email address",
    "seller_electronic_identifier": "Seller's electronic identification code",
    "seller_legal_registration_identifier": "Seller's legal registration number",
    "seller_legal_registration_identifier_type": "Type of seller registration identifier",
    "seller_tax_identifier_trn": "Seller's tax registration number (TRN)",
    "seller_tax_scheme_code": "Seller's tax scheme classification code",
    "seller_address_line_1": "First line of seller's address",
    "seller_city": "City where seller is located",
    "seller_country_subdivision": "Seller's state or region subdivision",
    "seller_country_code": "ISO country code for seller",
    "buyer_name": "Legal name of the buying company",
    "buyer_electronic_address": "Buyer's electronic email address",
    "buyer_electronic_identifier": "Buyer's electronic identification code",
    "buyer_tax_identifier_trn": "Buyer's tax registration number (TRN)",
    "buyer_tax_scheme_code": "Buyer's tax scheme classification code",
    "buyer_address_line_1": "First line of buyer's address",
    "buyer_city": "City where buyer is located",
    "buyer_country_subdivision": "Buyer's state or region subdivision",
    "buyer_country_code": "ISO country code for buyer",
    "sum_of_invoice_line_net_amount": "Total sum of all invoice line net amounts",
    "invoice_total_amount_without_tax": "Total invoice amount before tax",
    "invoice_total_tax_amount": "Total amount of all taxes",
    "invoice_total_amount_with_tax": "Final total amount including all taxes",
    "amount_due_for_payment": "Outstanding amount due for payment",
    "tax_category_taxable_amount": "Amount subject to taxation",
    "tax_category_tax_amount": "Tax amount for specific category",
    "tax_category_code": "Classification code for tax category",
    "tax_category_rate": "Percentage rate for tax category",
    "vat_line_amount": "VAT amount for specific line item",
    "invoice_line_identifier": "Unique identifier for invoice line item",
    "invoiced_quantity": "Quantity of items being invoiced",
    "unit_of_measure_code": "Code for unit of measurement",
    "invoice_line_net_amount": "Net amount for invoice line item",
    "item_net_price": "Net price per item unit",
    "item_gross_price": "Gross price per item unit",
    "item_price_base_quantity": "Base quantity for item pricing",
    "invoiced_item_tax_category_code": "Tax category code for invoiced item",
    "invoiced_item_tax_rate": "Tax rate applicable to invoiced item",
    "item_name": "Name or title of the item",
    "item_description": "Detailed description of the item",

    # Reverse Charge Mechanism Fields
    "reverse_charge_statement": "Statement for reverse charge mechanism",
    "rcm_codes": "Reverse charge mechanism codes",
    "vat_zero_rating_reason_text_fields": "Reason text for zero VAT rating",
    "payment_settlement_details": "Details of payment settlement terms",
    "invoice_period_dates": "Start and end dates of invoice period",
    "buyer_identification_and_scheme_identifier": "Buyer identification scheme details",

    # Profit Margin Scheme Fields
    "no_separate_vat_amount": "Flag indicating no separate VAT amount",
    "mandatory_statement": "Required mandatory statement text",
    "specific_tax_category_code": "Specific tax category classification",
    "additional_fields_for_original_purchase_details": "Original purchase transaction details",

    # Free Zone Fields
    "transaction_type_code_flag": "Flag for transaction type classification",
    "vat_treatment_for_goods_declaration": "VAT treatment declaration for goods",
    "vat_treatment_for_services_declaration": "VAT treatment declaration for services",
    "declaration_for_beneficiary": "Declaration statement for beneficiary",
    "proof_of_movement_documentation": "Documentation proving goods movement",
    "tax_category_code_for_vat_treatment": "Tax category for VAT treatment",

    # Export Fields
    "transaction_type_code": "Code classifying transaction type",
    "vat_treatment_status": "Status of VAT treatment application",
    "export_specific_fields": "Fields specific to export transactions",
    "buyer_information_and_transmission_details": "Buyer info and transmission details",
    "proof_of_export_documentation": "Documentation proving export status",

    # Import Fields
    "customs_declaration_number": "Official customs declaration number",
    "customs_declaration_date": "Date of customs declaration",
    "vat_handling_details": "Details of VAT handling procedures",

    # Self-Billed Invoice Fields
    "self_billing_agreement_reference": "Reference to self-billing agreement",
    "invoice_document_type_code": "Code for invoice document type",
    "true_reflection_of_supply": "Flag for true supply reflection",

    # Credit/Debit Note Fields
    "document_title": "Title or heading of the document",
    "unique_reference_number": "Unique reference identification number",
    "reference_to_original_invoice": "Reference to original invoice number",
    "description_of_adjustments": "Description of financial adjustments",
    "financial_details": "Detailed financial information",
    "reason_for_issuance": "Reason for document issuance",


    "agent_and_principal_identification": "Identification of agent and principal",
    "legal_documentation": "Required legal documentation",

    "reverse_charge_vat_reason_code": "Reason code for reverse charge VAT",
    "incoterms": "International commercial terms",
    "export_license_number": "Export license identification number",
    "continuous_supply_period_dates": "Dates for continuous supply period",
    "self_billing_agreement_reference": "Reference to self-billing agreement",
    "self_billed_document_type_code": "Document type code for self-billing",
    "order_reference": "Reference to purchase order",
    "contract_reference": "Reference to contract agreement",
    "discounts_and_charges": "Applied discounts and additional charges",
    "hsn_codes": "Harmonized System Nomenclature codes",

    # Intra-GCC Supplies Fields
    "reverse_charge_mechanism_statement": "Statement for reverse charge mechanism",
    "vat_treatment_details": "Detailed VAT treatment information",
    "buyers_vat_details": "Buyer's VAT registration details",
    "legal_note": "Required legal note or disclaimer",

    # UAE Government Invoicing Fields
    "government_entity_identifier": "Government entity identification code",
    "electronic_transmission_requirement": "Electronic transmission requirements",


    "terms_of_sale_incoterms": "Terms of sale using Incoterms",
    "shipping_details": "Shipping and delivery information",
    "country_of_origin": "Country where goods originated",
    "legal_attestation": "Legal attestation statement",
    "tax_status": "Current tax status classification",


    "supplier_name": "Name of the supplier company",
    "supplier_address": "Physical address of supplier",
    "supplier_tax_registration_number_trn": "Supplier's tax registration number",
    "unique_serial_number_or_invoice_number": "Serial number or invoice identifier",
    "date_of_issue": "Date when document was issued",
    "description_of_goods_or_services": "Description of supplied goods/services",
    "total_amount_inclusive_of_vat": "Total amount including VAT",
    "total_vat_amount": "Total VAT amount charged",
    "applicable_vat_rates": "VAT rates applied to transaction",


    "tax_registration_number_trn": "Tax registration number (TRN)",
    "legal_name_of_entity": "Legal registered name of entity",
    "total_amount_of_excess_refundable_tax": "Total excess tax amount for refund",
    "amount_to_be_refunded": "Actual amount to be refunded",
    "details_of_applicable_penalties": "Details of any applicable penalties",
    "authorized_signatory_details": "Details of authorized signatory",
    "declaration_of_accuracy": "Declaration of information accuracy",
    "tax_return_period_being_amended": "Tax return period under amendment",
    "detailed_description_of_error": "Detailed description of identified error",
    "financial_impact_of_adjustment": "Financial impact of the adjustment",
    "supporting_documentation_for_correction": "Supporting docs for correction"
}