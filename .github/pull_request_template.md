### GigaBookLM Pull Request Template

**Description**
Provide a concise summary of the changes introduced by this PR. Explain the technical problem being solved and the logic behind your specific implementation.

**Type of Change**
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Optimization (performance or memory improvement)
- [ ] Documentation update

**Technical Audit**
* **Logic Flow:** Briefly describe the data flow for this change.
* **Memory Impact:** What is the estimated RAM usage during execution? (Target ceiling is 8GB).
* **Dependencies:** Does this PR add any new libraries? If yes, provide a justification for why this cannot be handled with a local script.

**Submissions Checklist**
- [ ] **Air-Gapped:** I have verified that this code makes zero network calls/telemetry pings.
- [ ] **Formatting:** All strings use 'single quotes' and naming follows `logic_focused_conventions`.
- [ ] **Atomic Change:** This PR focuses on one specific feature or fix (no large, unrelated refactors).
- [ ] **Verification:** I have manually tested this logic and verified it works as intended.
- [ ] **Human Touch:** I have reviewed this code and can explain every line without relying on AI-generated justifications.

---
*Note: PRs that introduce unnecessary bloat or background connectivity will be closed.*
