Title: The New Senior Developer Doesn't Just Write Code. They Design the System That Writes It.
Date: 2026-10-19 09:00
Tags: craft,ai,development,future,senior
Category: Future
Slug: the-new-senior-developer
Summary: Imagine you're a senior developer working on an account-management service. You ask a coding agent to add audit logging when users change their account details. It has access to the repository, you give it a few constraints, and you get on with something else.
featured_image: /images/future_dev/senior_whole_system_view.jpg

---

![whole system view]({static}/images/future_dev/senior_whole_system_view.jpg)

---

### Beyond the Code series
- [Part 1. Who Checked It Was the Right Code?](/who-checked-the-code.html)
- [Part 2. The New Senior Developer](/the-new-senior-developer.html)
- [TODO...](/the-new-senior-developer.html)

---

## The Pull Request You Didn't Write

Imagine you're a senior developer working on an account-management service. You ask a coding agent to add audit logging when users change their account details. It has access to the repository, you give it a few constraints, and you get on with something else.

An hour later, there's a pull request waiting. The agent has updated the endpoints, added tests and documented the change. CI is green. It would have taken you considerably longer to write all of that yourself.

You start reviewing and spot something odd. The agent has built a small logging mechanism of its own, even though the company already has an event pipeline for audit records. The new code looks reasonable in isolation. But you remember why the existing pipeline was designed that way: consistent event formats, retention rules and a carefully worked-out approach to retries and failures.

You send the agent back to use the existing pipeline. But that only fixes today's PR. How do you make sure the *next* change follows the same architecture without someone having to catch the mistake again?

For plenty of teams, AI-assisted engineering looks more like this than a fleet of autonomous agents building software overnight. One developer, one coding agent, a growing amount of delegated implementation, and a lot to learn about making that delegation reliable.

**Where should a senior developer spend their expertise now, and how do they stay close enough to the code to know when the agent has gone wrong?**

---

## What Made a Developer Senior in the First Place?

Think about the senior developers you've learned the most from. Chances are, their typing speed isn't what you remember. You remember the person who could look at a small feature request and spot that it touched three services, a database migration and an undocumented agreement with another team.

Some of that came from deep technical knowledge. They could untangle a production failure, explain why a particular database query was slow, or recognise that a seemingly harmless change would cause problems elsewhere. They'd spent enough time building and maintaining systems to understand the consequences of decisions that looked perfectly reasonable on paper.

Then there were the less visible parts of the job. They knew when to challenge a requirement, when to involve another team and when a simple solution was preferable to an ambitious one. They helped junior developers understand *why* an approach worked, rather than just showing them what to type. And when something went wrong, they took responsibility for helping put it right.

The title has never meant exactly the same thing everywhere. Some seniors are deeply hands-on specialists; others spend more time on architecture and mentoring. But the best ones I've worked with were valued for their judgment and responsibility, not the number of lines they produced.

Coding agents are changing how much time seniors need to spend on routine implementation. A task that once occupied an afternoon might now take a few prompts and a review. That creates room for more of the work senior developers were already supposed to do: make architectural choices, help colleagues and look beyond the immediate ticket.

![kings commission]({static}/images/future_dev/senior_kings_commission.jpg)

The opportunity is to apply that experience *before* an agent starts writing, rather than relying on someone to catch every mistake in a pull request.

---

## Before the Agent Writes a Line of Code

We could have avoided the audit-logging mistake in our opening example before the agent built anything. Yet it's surprisingly easy to hand over a ticket and assume the codebase will tell the agent everything it needs to know.

Consider the instruction: *“Add audit logging when customers update their account details.”* A capable coding agent could inspect the endpoints, add event records and write convincing tests. It might even discover the existing audit pipeline. But the request leaves some important decisions open. Which changes need recording? Should an unsuccessful attempt produce an event? What information can safely appear in the audit trail? And what should happen to the account update if the audit service is unavailable?

Those questions touch security, operations and decisions other teams may already have made.

An experienced engineer can establish the boundaries: use the existing event publisher, keep sensitive account details out of the payload, preserve the contract downstream consumers rely on, and agree what happens if publishing fails. Some answers may need a conversation with a security or product colleague. It's better to have that conversation before implementation begins.

This doesn't require a senior developer to write a miniature technical specification for every ticket. Often the better first step is to ask the agent to explore the relevant code and propose an approach **without making changes**. What existing components can it reuse? Which files and services will be affected? What assumptions is it making? What could break? Reviewing those answers gives the engineer a chance to challenge the plan while it's still a plan.

There's a balance to strike. Specify every function name and implementation detail and you may as well do much of the work yourself. Give the agent no constraints and you're relying on it to discover years of architectural decisions from whatever happens to be documented in the repository. The senior's skill is deciding which choices need to be made up front, which can safely be delegated, and which should trigger a question rather than an assumption.

Acceptance criteria matter just as much. “The endpoint returns success and the tests pass” tells us little about the audit requirement. We'd want evidence that the existing pipeline is used, sensitive values aren't exposed and failure behaviour matches the agreed policy. Those checks give the agent a meaningful target and the reviewer something to examine afterwards.

Of course, this preparation should reflect the stakes. Treating every minor change as a major architectural decision would quickly erase the time AI saves us.

A good brief can prevent one mistake in one pull request. The more interesting opportunity is to make those architectural decisions available to the *next* agent, on the *next* task, without having to explain them all over again.

![senior attention]({static}/images/future_dev/senior_engineering_attention.png)

---

## Make the Right Thing the Easy Thing

The corrected audit-logging PR is merged. A week later, another developer asks another agent to work on a different endpoint. It invents a second way of recording audit events.

If the same architectural decision needs explaining in every review, the system around the agent needs some attention too.

A useful starting point is a small `CLAUDE.md` file in the repository, or the equivalent project guidance for another coding agent. It can tell an agent how to run the application, where to find architectural documentation, and which conventions matter. In our example, it could point to the existing event publisher, its contract and an example of its use. That gives the agent a better starting point than hoping it will infer the team's intentions by browsing the code. A new human colleague benefits from the same documentation.

Some knowledge deserves to be shared more widely. Authentication, error-handling and data-protection standards can become reusable agent skills: instructions that guide particular kinds of work and can be updated when the underlying policy changes. Senior engineers have always tried to turn experience into patterns other developers can follow. Now some of those patterns can guide the agents too.

Instructions aren't enforcement. An agent can overlook a file or misread a convention. Important rules need checks outside the agent's own judgment: perhaps a contract test proving the existing consumer can process an audit event, a check for a forbidden dependency, or a required security test in CI. Hooks can give fast feedback while an agent works; CI and branch protections can block an unacceptable change from merging.

These controls have limits. Tests only cover the behaviour they exercise, and someone needs to maintain the checks as the architecture evolves.

There's a temptation to turn this into a project of its own: dozens of skills, pages of instructions and approval gates for every action. That would be a strange way to celebrate the time we've saved. Start with the recurring mistakes. Document the decisions that are easy to miss. Automate a check where the cost of failure justifies it. If a rule creates more friction than value, revisit it.

The payoff is that a senior developer's influence can extend beyond the PRs they personally review. A carefully made architectural decision can shape dozens of subsequent changes.

![right things easy]({static}/images/future_dev/senior_right_things_easy.png)

But with better instructions and stronger checks in place, **what evidence should we ask for before trusting the work?**

---

## Reviewing Evidence Instead of Watching the Cursor

A coding agent can give you a reassuring summary of its work. *Added audit events to three endpoints. Updated the tests. All checks passing.* That’s useful as a progress report, but it doesn’t tell you much about whether you should approve the pull request.

When the work arrives for review, I'd want to know what actually happened. Which commands ran? What did the tests exercise? Did the change use the existing event contract? If the agent says it checked the failure path, is there evidence of that behaviour, or just a paragraph saying everything looks fine?

Review can be more deliberate when the checks follow from decisions agreed before implementation. For the audit-logging feature, I'd look for a contract or integration test against the existing event system, evidence that sensitive fields are excluded and a test of publishing failure. CI logs and observed behaviour carry more weight than the agent's confidence in its own work.

A thorough report still needs interpretation. The feature and its tests may share the same flawed assumption. Checks based on an independently reviewed requirement, an existing service contract or a previous production failure offer a stronger challenge. A second agent's review can help, but its explanation is still a claim to verify.

And there are still times when you need to get into the code. Suppose the account update commits successfully, then publishing the audit event fails. The test suite might cover both operations separately while missing the gap between them. A senior developer who understands transaction boundaries and failure recovery is well placed to notice that risk. They might ask for a different implementation, a targeted test, or an explicit decision about whether that gap is acceptable. Sometimes the right response to a PR is to open the relevant files and follow the execution path yourself.

That leaves a practical question beyond the review itself: **when is it safe to let an agent proceed on its own, and when should an engineer step in?**

---

## Knowing When to Let Go - and When to Say No

It's possible to build an impressive set of instructions, tests and review checks, then spend the whole day supervising the agent anyway. Approve this command. Inspect that edit. Confirm another test run. At some point, you're doing the work of an unusually slow pair programmer, except your partner can type at extraordinary speed.

Giving an agent room to work is part of getting value from it. The harder question is how much room. I'd judge that by the possible impact of a mistake, how visible a failure would be, and how easily we could undo it. Changing a stylesheet and changing a permissions model belong in different categories.

For a contained change with good tests, an agent might investigate, edit and verify its work before opening a PR. Cross-service changes might need a reviewed plan. Production credentials, destructive database operations and live deployments call for tighter permissions and explicit authorisation. There's no requirement to grant the agent permission to execute every step simply because it can prepare them.

There are moments when the engineer needs to reject an approach that looks entirely reasonable. Imagine an agent fixing intermittent failures in a third-party API integration. It proposes retrying failed requests more aggressively, adds tests and reports success. But the engineer knows that the provider rate-limits requests, and that some operations might have succeeded even when the response was lost. More retries could increase the load or repeat an action that should happen only once. That's a good moment to say no, investigate the failure behaviour and agree on a safer approach.

Anthropic's engineers describe this kind of intervention in their [account of redesigning source control](https://www.anthropic.com/engineering/redesigning-source-control). They sometimes had to steer Claude away from plausible solutions that ignored wider system constraints, including unnecessary complexity introduced during adversarial review. Being able to explain *why* an approach is unsuitable matters more than simply vetoing it.

Intervention can become its own problem. A senior who approves every small design choice and adds a new rule after each odd suggestion will recreate the bottleneck they hoped to remove. Sometimes it's worth letting an agent try an approach in a branch and seeing what the tests reveal. Adjust the boundaries as the team learns where agents succeed and where they repeatedly go wrong.

Make the boundaries explicit: what can the agent decide alone, what needs review, and what should make it stop and ask? Those answers will vary across systems and evolve with experience.

![how much autonomy]({static}/images/future_dev/senior_how_much_autonomy.png)

A senior has to make those calls without becoming a permanent approval queue. But that presumes something we shouldn't take for granted: **the technical ability to judge the work we've delegated.**

---

## You Still Need to Understand the Machine

Six months into delegating most of your implementation work to coding agents, you're delivering features faster and getting good at reviewing plans and pull requests. Then a background-job queue starts growing in production.

An agent investigates the metrics and suggests adding workers. That sounds reasonable until you look more closely. Database CPU is relatively normal, but lock waits are climbing. You follow a few traces and discover that workers are competing to update the same records. Adding more workers could make the contention worse.

An agent could discover that too, given the right diagnostics. What matters is recognising when a proposed fix doesn't fit the evidence, and knowing where to investigate next.

I worry that this understanding could gradually fade if we aren't careful. When you spend years building systems, you accumulate a mental model of how they behave: where state lives, what happens when requests overlap, why a particular service has an awkward interface, which shortcuts have caused incidents before. Some of that knowledge comes from design discussions, but a lot comes from debugging your own mistakes and living with your earlier decisions.

Spend a year approving agent-generated plans without regularly tracing the code they produce, and your understanding may start to lag behind the actual system. The architecture diagrams still make sense. The summaries sound convincing. But when something breaks in an unfamiliar way, how quickly can you work out what's happening?

I wouldn't insist that seniors hand-write some arbitrary percentage of the code. But staying sharp will need to be intentional. Read the consequential parts of a diff. Trace a request across service boundaries. Investigate a production issue yourself before accepting an agent's diagnosis. Occasionally take a difficult implementation far enough to challenge what you think you know about the technology. And notice when an agent chooses a better approach than yours; sometimes it's the engineer who needs to learn.

The fundamentals still matter. Understanding transactions, concurrency, data modelling, security boundaries and failure modes gives you a way to reason about unfamiliar implementations. You won't know every library or framework an agent uses, and you shouldn't have to. But you need enough technical depth to ask useful questions, inspect evidence and recognise the limits of your own knowledge.

There's a mentoring problem here too. Junior developers have traditionally encountered these lessons while implementing features, fixing bugs and getting things wrong under supervision. If agents take on much of that routine work, we need to create other opportunities to develop the same understanding. Ask a less experienced developer to explain an agent's design, trace a failing test or investigate why two plausible approaches behave differently under load. Give them ownership of manageable decisions. We'll explore that properly in the next article.

Technical expertise won't maintain itself while we're busy delegating work. If it's the basis on which we make decisions, we need to keep using it.

![green checks fail]({static}/images/future_dev/senior_green_checks_fail.jpg)

And there's a final question: **when software is produced by an agent, who owns the outcome?**

---

## Who Owns the Outcome?

Months after our audit-logging feature ships, a customer disputes a change to their account. The team looks for the audit record and discovers it's missing. The pull request was merged long ago, the agent session is over, and all the tests passed at the time. Now somebody needs to find out what happened and prevent it happening again.

The first question in that investigation won't be who typed the code. It'll be what guarantees the system was supposed to provide, how its failure modes were assessed, and what evidence supported the decision to release it.

That responsibility is shared. Product teams need to establish the intended behaviour. Engineering leaders need to provide the time and tools for reliable delivery. Security and operations have expertise that a feature team may lack. The senior developer's contribution is to bring those concerns together in the technical decisions: choosing sensible boundaries, demanding useful evidence, and making sure a system can be understood when it fails.

As more implementation is delegated, some of this work will overlap with architecture and engineering leadership. A senior who improves the instructions, tests and safeguards used by an entire team can influence far more software than they could write alone. Their judgment still needs to be grounded in the systems those safeguards are supposed to protect.

There's another responsibility that comes with being senior: helping other developers develop that judgment. If agents increasingly handle the routine implementations and mistakes that once taught us how systems behave, where will the next generation gain their experience?

**We may be changing what senior developers do. We also need to think about how anyone becomes one.**
