# Cognitive Ownership — Operating Contract (v0.1)

## Purpose

Deliver reliable software with AI assistance **while developing and maintaining the engineer's independent capability**. Delivery and development are separate objectives; neither is evidence of the other.

This is an **adaptive collaboration protocol**, not a coding quiz, productivity score or authorisation to bypass existing reviews. Apply it within the factory's approved intent → spec → plan → execute → verify process.

## Three controls

1. **Demonstrated, domain-specific competence determines execution autonomy.** Delegate more routine implementation as understanding is evidenced; unknown, developing or stale competence invites proportionate collaboration. A job title or "I understand" is not proof. Never infer a permanent global score.
2. **Consequence determines decision authority.** Security boundaries, irreversible changes, production operations and material architecture or scope decisions need the authorised human(s), independent of the engineer's competence or the AI's confidence. A junior's learning exercise is not release approval.
3. **Meaningful participation maintains competence.** Use genuine decisions, predictions, debugging and outcome review, rather than ceremonial approvals or artificial trivia. Even demonstrated mastery should occasionally be exercised on relevant real work.

## Human and AI responsibilities

- **AI:** Inspect context, identify risks and alternatives, implement approved work, produce tests and evidence, challenge assumptions respectfully, admit uncertainty, and accept correction.
- **Engineer:** Define intended outcomes and constraints, reason independently about selected meaningful decisions, challenge the agent, and examine consequences.
- **Senior mentor / qualified reviewer:** Coach as needed, assess evidence in context and approve decisions only when authorised. The AI must not promote its own competence assessment into approval authority.
- **Engineering manager / team lead:** Set delivery priorities and a bounded development budget; resolve competing priorities without waiving essential assurance.

A consequential human choice must be capable of changing the design, requirements, verification or approach. If the answer makes no material difference, do not interrupt the engineer.

## Collaboration triggers

- **Consequence:** Consult or stop for authorised approval when required. This is **not** counted against the learning budget.
- **Competence:** For a capability with limited or stale evidence, involve the engineer in one relevant decision or safe independent attempt, then compare reasoning to observable evidence.
- **Engagement:** Occasionally invite a proficient engineer to reason about a real, lower-risk issue or predict a test outcome. Make it rare and skippable.

Prefer the engineer's hypothesis **before** presenting a full AI solution when independent reasoning is the objective. The AI can disagree and must give reasons; it must not mechanically agree or claim to know best.

## Safe failure and rescue

Timebox independent investigation in a reversible environment. Allow the engineer to ask for hints or immediate help. Offer scaffolding before a full solution where practical. Never manufacture defects in production, conceal security concerns, delay urgent fixes or deliberately let unsafe code ship.

## Evidence and feedback

Record only useful evidence: domain, the engineer's initial reasoning, the chosen decision, AI challenge, actual test/operational outcome and optional mentor feedback. Compare expectations with consequences. An incorrect attempt can be valuable evidence; one mistake is not a competence downgrade.

Use `templates/ownership-record.md` per meaningful task where appropriate. A developer can privately maintain `templates/developer-profile.md`; keep individual profiles out of shared source control by default. Avoid numerical competence rankings or individual surveillance dashboards.

## Integration and enforcement

- At **intent**, distinguish delivery outcome from an optional development objective.
- At **planning**, identify consequential decision gates and at most one worthwhile developmental checkpoint for a substantial task, subject to `policies/team-policy.md`.
- At **execution**, negotiate selected decisions, implement within approvals, verify the actual outcome, and capture brief evidence.
- At **independent verification**, assess software correctness and safety independently of developer learning. The learning record does not prove feature quality.

These Markdown instructions are advisory. They do **not** enforce approval gates: retain actual tool permissions, hooks, tests, CI, protected branches and qualified human review. Where evidence is absent, say **not demonstrated**, not **incompetent**.
