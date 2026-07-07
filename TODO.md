# ABAG AI Assistant — Roadmap & TODO

This document outlines planned improvements and expansion areas for the ABAG AI Assistant. Items are grouped by category and roughly ordered by priority within each section.

---

## Phase 1 — Foundation (Current)

- [x] Write README with project overview and structure
- [x] Define SYSTEM_PROMPT.md with behavioral guidelines
- [x] Build initial KNOWLEDGE.md covering all core ABAG services
- [x] Create EXAMPLES.md with representative Q&A pairs
- [x] Establish repository structure for future expansion

---

## Phase 2 — Knowledge Expansion

- [ ] **Deepen service-specific knowledge**
  - Add detailed FAQs for each service area (company formation, tax, banking, etc.)
  - Include common edge cases and scenarios (e.g., sole proprietors, nonprofit structures, holding companies)
  - Document typical timelines and cost ranges for each service (as general guidance)

- [ ] **Add sector-specific modules**
  - Technology / SaaS companies entering Italy
  - Manufacturing and industrial clients
  - Food & beverage and retail
  - Professional services (law, consulting, finance)
  - Tourism and hospitality

- [ ] **Expand regulatory knowledge**
  - Key EU directives and regulations relevant to U.S. businesses (GDPR, DORA, AI Act, etc.)
  - Italian labor law overview for companies planning to hire locally
  - Real estate and office leasing considerations
  - Intellectual property protection in Italy and the EU

- [ ] **Add a glossary of key Italian business and legal terms**
  - Bilingual (Italian / English) definitions for common terms encountered by clients

---

## Phase 3 — Interaction Quality

- [ ] **Develop conversation flows**
  - Structured intake flow for new clients (business type, country of origin, goals)
  - Qualification flow to route clients to the most relevant ABAG service
  - Follow-up prompts that guide clients toward scheduling a consultation

- [ ] **Add more EXAMPLES.md scenarios**
  - Multi-turn conversation examples (follow-up questions and clarifications)
  - Scenarios involving dual U.S.–Italy tax questions
  - Scenario for a client already operating in Italy seeking expansion to other EU countries
  - Example involving Italian labor law and hiring

- [ ] **Develop evaluation rubrics**
  - Define scoring criteria for accuracy, completeness, tone, and appropriateness of escalation
  - Create a set of adversarial or edge-case test questions (misleading queries, out-of-scope requests, sensitive topics)

---

## Phase 4 — Technical Integration

- [ ] **RAG (Retrieval-Augmented Generation) pipeline**
  - Structure KNOWLEDGE.md for chunking and vector indexing
  - Evaluate embedding models and vector database options
  - Implement retrieval layer to ground assistant responses in ABAG's knowledge base

- [ ] **Platform deployment**
  - Evaluate deployment platforms (OpenAI Assistants API, Anthropic Claude, Gemini, open-source LLMs)
  - Create platform-specific configuration files (e.g., OpenAI Assistant JSON spec)
  - Document deployment instructions for each supported platform

- [ ] **Website integration**
  - Define requirements for embedding the assistant on the ABAG website
  - Specify API and widget interface
  - Design conversation handoff flow to human advisors (live chat or email escalation)

- [ ] **CRM integration**
  - Connect assistant conversation summaries to ABAG's CRM
  - Automatically log client inquiries and identified service interests
  - Trigger follow-up workflows based on conversation outcomes

---

## Phase 5 — Multilingual Support

- [ ] **Italian-language knowledge base**
  - Translate KNOWLEDGE.md into Italian
  - Create Italian-language EXAMPLES.md
  - Adapt SYSTEM_PROMPT.md for Italian-speaking users

- [ ] **Language detection and routing**
  - Implement automatic language detection
  - Route to appropriate language-specific knowledge base
  - Ensure consistent quality across both English and Italian responses

- [ ] **Additional languages** (future consideration)
  - Spanish — for Latin American clients considering European expansion via Italy
  - French and German — for broader European market coverage

---

## Phase 6 — Governance and Maintenance

- [ ] **Knowledge review process**
  - Establish a quarterly review cycle for KNOWLEDGE.md to ensure regulatory accuracy
  - Define ownership for each service area within the ABAG team
  - Create a changelog to track knowledge base updates

- [ ] **Feedback loop**
  - Implement a thumbs-up/thumbs-down feedback mechanism on client-facing deployments
  - Review flagged responses and update knowledge base or system prompt accordingly
  - Define escalation paths for unanswered or poorly answered questions

- [ ] **Compliance and legal review**
  - Conduct an initial legal review of assistant responses to ensure appropriate disclaimers
  - Establish a review process for any changes to legal or tax-related content
  - Ensure GDPR compliance for any data collected during client interactions

---

## Open Questions

- What LLM platform(s) will ABAG use for production deployment?
- Will the assistant handle appointment scheduling, or redirect to an external booking tool?
- Should the assistant have access to real-time data (e.g., current Italian tax rates, exchange rates)?
- What is the escalation path when a client needs immediate human assistance?
- Should there be a distinct assistant persona for Italian-market clients vs. U.S.-market clients?

---

*This roadmap is a living document and will be updated as priorities evolve. For questions or contributions, contact the ABAG team.*
