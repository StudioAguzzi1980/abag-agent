# ABAG AI Assistant

**American Business Advisory Group (ABAG)** — AI-Powered Business Advisory Agent

---

## Overview

This repository contains the knowledge base, behavioral guidelines, and documentation for the ABAG AI Assistant — a conversational AI designed to support American and international businesses seeking professional advisory services in Italy and Europe.

The assistant helps clients understand ABAG's service offerings, guides them through the initial stages of business formation and market entry, answers common questions about Italian and European regulatory requirements, and facilitates first contact with ABAG's expert team.

---

## Purpose

American Business Advisory Group specializes in helping U.S.-based companies and entrepreneurs establish, grow, and operate their businesses in Italy and across Europe. The ABAG AI Assistant acts as a first point of contact and knowledge resource, providing:

- Clear, accurate information about ABAG's professional services
- Guidance on Italian and European business regulations and procedures
- Answers to common questions about company formation, taxation, compliance, and banking
- Direction toward the appropriate ABAG specialist for deeper consultation

---

## Repository Structure

```
abag-agent/
├── README.md                          # Project overview (this file)
├── SYSTEM_PROMPT.md                   # AI assistant behavioral instructions
├── KNOWLEDGE.md                       # ABAG services and domain knowledge
├── EXAMPLES.md                        # Sample client interactions and ideal responses
├── TODO.md                            # Roadmap for future development
│
├── services/                          # Service descriptions and pricing
│   ├── overview.md
│   ├── company_formation.md
│   ├── tax_advisory.md
│   ├── accounting.md
│   ├── compliance.md
│   ├── banking_support.md
│   ├── market_entry.md
│   └── pricing_guide.md
│
├── sales/                             # Sales playbook, templates, and tools
│   ├── sales_playbook.md
│   ├── discovery_questions.md
│   ├── objection_handling.md
│   ├── proposal_template.md
│   └── pipeline_stages.md
│
├── marketing/                         # Brand, messaging, personas, and content
│   ├── brand_guidelines.md
│   ├── messaging_framework.md
│   ├── target_personas.md
│   └── content_strategy.md
│
├── linkedin/                          # LinkedIn strategy and content
│   ├── profile_optimization.md
│   ├── content_calendar.md
│   ├── outreach_templates.md
│   └── engagement_strategy.md
│
├── email_templates/                   # Ready-to-use email templates
│   ├── initial_inquiry_response.md
│   ├── follow_up_after_call.md
│   ├── proposal_delivery.md
│   ├── onboarding_welcome.md
│   ├── monthly_newsletter.md
│   └── consultation_confirmation.md
│
├── faq/                               # Frequently asked questions by topic
│   ├── general_faq.md
│   ├── company_formation_faq.md
│   ├── tax_faq.md
│   ├── banking_faq.md
│   ├── compliance_faq.md
│   └── market_entry_faq.md
│
├── italian_tax/                       # Italian tax system — detailed guides
│   ├── overview.md
│   ├── ires_irap.md
│   ├── vat_guide.md
│   ├── us_italy_tax_treaty.md
│   ├── transfer_pricing.md
│   ├── personal_income_tax.md
│   └── withholding_taxes.md
│
├── company_formation/                 # Company formation guides by entity type
│   ├── overview.md
│   ├── srl_guide.md
│   ├── branch_office.md
│   ├── required_documents.md
│   ├── incorporation_timeline.md
│   └── costs_and_fees.md
│
├── market_entry/                      # Market entry strategy and planning
│   ├── overview.md
│   ├── feasibility_assessment.md
│   ├── go_to_market_strategy.md
│   ├── distribution_channels.md
│   └── eu_incentives.md
│
├── banking/                           # Italian banking guides
│   ├── overview.md
│   ├── opening_corporate_account.md
│   ├── required_documents.md
│   └── fintech_alternatives.md
│
├── compliance/                        # Corporate compliance guides
│   ├── overview.md
│   ├── gdpr_guide.md
│   └── labor_law.md
│
├── case_studies/                      # Anonymized client case studies
│   ├── overview.md
│   ├── tech_startup_expansion.md
│   ├── food_beverage_distribution.md
│   ├── manufacturing_subsidiary.md
│   └── professional_services_firm.md
│
├── checklists/                        # Actionable checklists for key processes
│   ├── company_formation_checklist.md
│   ├── banking_setup_checklist.md
│   ├── annual_compliance_checklist.md
│   ├── market_entry_checklist.md
│   ├── tax_compliance_checklist.md
│   └── client_onboarding_checklist.md
│
├── client_onboarding/                 # New client onboarding materials
│   ├── overview.md
│   ├── welcome_pack.md
│   ├── kyc_requirements.md
│   └── discovery_questionnaire.md
│
└── documents/                         # Legal and business document templates
    ├── README.md
    ├── nda_template.md
    ├── engagement_letter_template.md
    ├── power_of_attorney_guide.md
    └── corporate_resolution_template.md
```

---

## Key Services Covered

- **Company Formation in Italy** — Incorporation of SRL, SPA, and branch offices
- **Market Entry Strategy** — Tailored strategies for entering the Italian and European markets
- **Tax Advisory** — Italian and cross-border tax planning and compliance
- **Accounting** — Bookkeeping, financial reporting, and statutory accounts
- **Corporate Compliance** — Ongoing regulatory and governance obligations
- **Banking Support** — Assistance opening business bank accounts in Italy
- **Business Expansion (U.S. to Italy/Europe)** — End-to-end support for American companies expanding abroad

---

## How to Use This Repository

This repository is organized to support multiple integration scenarios:

1. **AI Platform Configuration** — Use `SYSTEM_PROMPT.md` to configure the assistant's personality, tone, and scope on any LLM-based platform (OpenAI, Anthropic, Google, etc.).
2. **Knowledge Retrieval** — `KNOWLEDGE.md` serves as the assistant's structured knowledge base for RAG (Retrieval-Augmented Generation) pipelines.
3. **Evaluation & Testing** — `EXAMPLES.md` provides ground-truth Q&A pairs for evaluating assistant quality and consistency.
4. **Roadmap Planning** — `TODO.md` tracks planned improvements and expansion areas.

---

## Contributing

Contributions to the knowledge base and behavioral guidelines are managed by the ABAG team. To suggest updates, open an issue or submit a pull request with a clear description of the proposed change.

---

## Contact

**American Business Advisory Group**
For professional inquiries, visit [abag.us](https://abag.us) or contact the ABAG team directly.

---

*This project is maintained by the ABAG team. All information is intended for informational purposes and does not constitute legal, tax, or financial advice.*
