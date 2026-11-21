---
name: cognitive-ownership
description: >
  Adapt AI execution autonomy to demonstrated engineering competence while
  preserving consequential human decisions, independent reasoning, and targeted
  development opportunities. Use during substantive implementation planning and
  execution when the project's Cognitive Ownership team policy is enabled.
---

# Cognitive Ownership

Read `COGNITIVE_OWNERSHIP.md` and `policies/team-policy.md` before applying this skill. Preserve the existing factory's mandatory approvals, security controls and independent verification. This skill guides collaboration; it is **not** a permission or enforcement system.

## 1. Establish context

Use the approved intent/spec/plan, current task, codebase evidence, the team's development budget and any capability notes the engineer voluntarily shares. Ask for missing facts only when they materially alter delivery, safety or the selected learning opportunity.

Classify domain familiarity as `unfamiliar`, `developing`, `demonstrated` or `insufficient evidence`. Explain the evidence; do not invent a rating or infer mastery from titles, confidence or agreement with the AI. Absence of a profile means **insufficient evidence**, not low ability.

## 2. Separate three questions

- **Consequence:** What could cause architectural lock-in, sensitive-data exposure, operational harm, or difficult rollback? Identify the responsible human decision-maker and required independent assurance. Never spend the optional learning budget instead of getting approval.
- **Execution autonomy:** Which work is sufficiently understood and authorised for the AI to implement without interruptions? Delegate routine work freely where appropriate.
- **Development:** Which *real* decision, investigation or implementation step would improve/refresh this engineer's capability? Select at most one worthwhile checkpoint per substantial task within the time budget, unless the team policy says otherwise.

If no worthwhile learning opportunity exists, say so and continue delivery. Do not invent a quiz.

## 3. Choose an intervention

Prefer one of:
1. **Decision negotiation:** Ask for desired system behaviour or a trade-off *before* anchoring with the AI's preferred answer. Offer the AI's competing view with evidence and revise the plan if needed.
2. **Prediction then test:** Have the engineer predict a failure, boundary case or concurrent behaviour before showing the result. Test it using real evidence.
3. **Bounded independent diagnosis:** Give a real failing test and symptoms; let the engineer investigate in a safe environment, with optional hints and a rescue path.
4. **Mastery refresh:** Occasionally invite demonstrated engineers to explain or challenge an actual lower-risk decision; rarely, and always skippable.

Every intervention must have a useful answer that can change implementation, verification or the engineer's demonstrated understanding. Avoid repeated approvals, trivial naming questions, or asking people to rewrite AI boilerplate.

## 4. Negotiate, execute and verify

Capture the engineer's initial reasoning **before** revealing the AI's conclusion when independent assessment is intended. Challenge unsupported claims respectfully; actively consider that the AI may be wrong. A different reasoned human choice must be capable of influencing the design.

Implement within existing authorised scope. Observe tests or runtime behaviour and compare against the prediction. Keep *software verification* independent: neither a good learning outcome nor a mentor's praise substitutes for CI, tests, security review or the configured verifier.

For safe learning, allow a timeboxed attempt before giving a solution, but provide hints on request and rescue immediately when asked. Never delay urgent work or expose production to a learning failure.

## 5. Record and hand off

If a meaningful intervention happened, use `templates/ownership-record.md` for a brief record: task, domain, trigger, initial reasoning, alternatives, consequential decision, evidence, outcome and optional mentor feedback. Store completed individual learning notes privately unless explicitly shared.

Use a senior engineer for targeted coaching and qualified review when appropriate; do not invent a reviewer or approval. When evidence is insufficient, say so. A single failed attempt is a learning opportunity, not a competence downgrade.

Report the development time used and whether participation changed the outcome. Optional learning may be skipped; mandatory approval and technical verification may not.
