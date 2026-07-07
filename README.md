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
├── README.md                              # Project overview (this file)
├── SYSTEM_PROMPT.md                       # AI assistant behavioral instructions
├── KNOWLEDGE.md                           # ABAG services and domain knowledge
├── EXAMPLES.md                            # Sample client interactions and ideal responses
├── TODO.md                                # Roadmap for future development
│
└── Knowledge Base/
    ├── 01_Company_Formation/              # Italian company formation guides and templates
    ├── 02_US_Companies_Entering_Italy/    # Resources for U.S. companies entering Italy
    ├── 03_European_Expansion/             # European market expansion materials
    ├── 04_Tax/                            # Italian and cross-border tax advisory content
    ├── 05_Accounting/                     # Bookkeeping, reporting, and statutory accounts
    ├── 06_Compliance/                     # Regulatory and corporate governance content
    ├── 07_Banking/                        # Business banking guidance and support materials
    ├── 08_Checklists/                     # Step-by-step process checklists
    ├── 09_Email_Templates/                # Client communication email templates
    ├── 10_LinkedIn_Posts/                 # LinkedIn content and social media posts
    ├── 11_Sales_Playbooks/                # Sales process guides and playbooks
    ├── 12_Client_FAQ/                     # Frequently asked questions by clients
    ├── 13_Case_Studies/                   # Client case studies and success stories
    ├── 14_Proposals/                      # Service proposals and pitch materials
    ├── 15_Standard_Operating_Procedures/  # Internal SOPs and process documentation
    ├── 16_AI_System_Prompts/              # AI assistant prompt library
    └── 17_Marketing/                      # Marketing materials and campaigns
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
