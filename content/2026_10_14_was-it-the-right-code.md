Title: Your AI Wrote the Code. Who Checked It Was the Right Code?
Date: 2026-10-14 09:00
Tags: craft,ai,development,future
Category: Future
Slug: who-checked-the-code
Summary: AI can now generate clean, well-tested code in minutes, but who ensures we're building the right thing? This article explores why engineering judgment, challenging assumptions, and understanding business requirements are becoming increasingly important as AI transforms software development..
featured_image: /images/future_dev/robocop_colab.jpg

After 25 years as a software developer, I find myself increasingly wondering what the future holds for our profession. The pace of change in AI is exciting, but I'd be lying if I said it didn't also make me a little anxious. Where will my experience and skills add value in five or ten years? What will being a software engineer actually look like? I don't have all the answers, but I'm putting together a series of articles to collect my thoughts, challenge some of my assumptions, and explore where I think our profession is heading. As Kent Beck put it...

![recalibrate]({static}/images/future_dev/recalibrate.jpg)

---

![robo colab]({static}/images/future_dev/robocop_colab.jpg)

---

### Beyond the Code series
- [Part 1. Who Checked It Was the Right Code?](/who-checked-the-code.html)
- [TODO...](/who-checked-the-code.html)

---

## The Perfect Pull Request

Picture a routine feature request: *“Let customers know whenever their order status changes.”*

A developer handed it to an AI coding agent. Twenty minutes later, the agent had added an event listener, a notification service, unit tests, integration tests and a tidy pull request. The build was green. Every test passed. The code was readable, the error handling sensible, and the documentation surprisingly thorough.

The feature went live.

Then the complaints started.

Customers were receiving a string of emails as orders moved through internal states: *allocated*, *picked*, *packed*, *queued for dispatch*. Some received several messages in a matter of minutes. Others worried that their order had gone wrong because a status briefly changed and changed back.

The agent had done exactly what it was asked to do. It detected status changes and sent notifications. Its tests confirmed that behaviour in the cases they covered.

Nobody had stopped to ask which status changes customers actually cared about, or whether internal warehouse events should trigger an email at all. That assumption made its way into the implementation and then into the tests, where it was treated as expected behaviour.

**Who should have challenged that assumption before the feature reached production?**

![robo success]({static}/images/future_dev/robocop_success.jpg)

## Passing Tests Doesn't Mean You Built the Right Thing

Software engineering has long distinguished between **verification** and **validation**:

1. **Verification:** Are we building the product right?
2. **Validation:** Are we building the right product?

Our order notification feature sailed through verification. The tests checked that a status change produced an email, that the message contained the right details, and that failures were handled sensibly. They could all pass while customers were being bombarded with updates they never wanted.

There's an uncomfortable feedback loop here. Give a coding agent an ambiguous requirement and it will often make reasonable assumptions to keep moving. Ask that same agent to write the tests and those assumptions can become the definition of correct behaviour. CI then gives us a reassuring green tick against expectations nobody thought to challenge.

This isn't unique to AI. Developers have always written tests around their own understanding of a requirement. What's changing is how quickly an agent can turn that understanding into a substantial, apparently finished feature.

A useful review needs to reach beyond the test results. Who wanted this feature? What problem were they trying to solve? Which behaviours would surprise or frustrate them? For our notification system, a ten-minute conversation about those questions might have prevented an entire round of development and rework.

## We've Always Had This Problem. AI Just Makes It Faster.

Anyone who's worked in software for a while will recognise this story. Requirements have always been misunderstood. Product owners leave things unsaid, developers make assumptions, and users discover behaviours nobody intended. We've been arguing about how to prevent this for decades.

What's changed is the speed at which those assumptions become software.

A longer implementation cycle sometimes created opportunities to spot problems. A developer might question an edge case while writing the code; a tester might ask what happens when an order changes status twice. Sometimes those conversations happened far too late, and plenty of teams spent months building the wrong thing anyway. Time spent coding was never a reliable substitute for understanding users.

Now an agent can deliver a feature before anyone has had that conversation. If building one misguided feature is cheap, building ten is cheap too. The resulting rework might not be.

But speed cuts both ways. We can also produce three prototypes, put them in front of users and discard two before a traditional team has finished debating a design. That's a tremendous advantage, provided we treat those prototypes as questions to investigate rather than finished answers.

[Anthropic's AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) argues that planning, review and deployment are increasingly the bottlenecks around faster code generation. I'd add another question: **are we using that speed to learn what users need, or simply to produce more software?**

## The Engineer Who Knows When to Say No

![robo no nonsense]({static}/images/future_dev/robocop_no_nonsense.jpg)

There's a particular kind of experience that doesn't show up neatly in a unit test. It's the accumulated knowledge of why a system works the way it does, which shortcuts caused trouble last time, and which seemingly harmless changes will create problems six months from now.

That knowledge matters when you're reviewing code written by a colleague. It matters even more when an agent can produce hundreds of lines in minutes and present them with the confidence of someone who's solved the problem.

In [Anthropic's account of redesigning its source-control systems](https://www.anthropic.com/engineering/redesigning-source-control), the engineers who worked on that migration said they would rate Claude as better at writing code than themselves. That's a striking admission. Yet those same engineers remained essential to the project. They understood how the different systems fitted together, the constraints the migration had to respect, and the trade-offs necessary to operate at the intended scale.

One of their recurring jobs, they said, was telling Claude **“no.”**

### Good code, wrong approach

The team described agents trying to discover when a change had merged into the main branch by reading through the commit log one entry at a time. Their existing code review tool could answer that question directly.

You can imagine the generated code passing its tests. Given a suitable repository, it might even return the correct answer every time. But an engineer familiar with the wider environment could see the problem immediately: the solution was doing unnecessary work and bypassing a capability the organisation already had.

That's a different kind of review from checking whether a function returns the expected value. It asks whether the function should exist in that form at all.

In a mature system, these decisions accumulate. A direct database query may seem easier than using an existing service, until it bypasses authorisation rules or duplicates business logic. A new background worker might solve a timing problem while introducing another queue to operate. A caching layer might speed up a request but make stale data difficult to diagnose. None of those approaches is automatically wrong. Someone needs to understand the surrounding system well enough to choose between them.

### The danger of fixing every possible problem

The Anthropic engineers also reported an interesting failure mode with adversarial AI reviews. A reviewer became overly concerned about trusting another internal service, and Claude responded by adding excessive validation and complexity.

That sounds responsible at first. Defensive programming is usually praised, and security concerns deserve proper attention. But every additional check has a cost: more branches to test, more failure states to understand, more code to maintain, and sometimes a less clear contract between systems.

An experienced engineer has to distinguish a credible risk from a hypothetical one and judge whether the proposed defence is proportionate. That judgment depends on the trust boundary, the service contract, the potential impact of failure and the safeguards already in place.

It's also a useful warning about the idea of simply having one AI review another. An independent reviewer can catch genuine mistakes. It can also produce recommendations that are individually plausible but collectively make the system harder to operate. A list of findings still needs somebody to decide which findings matter.

### The questions behind the code

For our order-notification feature, the engineering questions extend beyond whether the event handler is reliable:

- Are internal order states meaningful to customers, or only to warehouse staff?
- What happens when an order moves backwards through a state, or changes several times in quick succession?
- Do customers need every update, or just the milestones that help them make decisions?
- Is the notification system the right place to decide which events are customer-facing?
- How will we know in production whether these emails are helpful rather than annoying?

Answering those questions might lead to an event filter, a set of customer-visible milestones or a conversation with operations before implementation begins.

Of course, AI can ask many of these questions too. We should encourage it to. A well-configured agent can challenge a vague specification, identify architectural alternatives and flag risks before implementation. The difficult part comes when answers are incomplete or constraints conflict. Someone has to seek out missing context, decide which trade-offs are acceptable, and take responsibility for the result.

### Experience is useful only if we apply it

It's tempting to turn this into a story about senior developers rescuing AI from its mistakes. That would give humans too much credit. Experienced engineers make poor architectural decisions, overlook requirements and over-engineer solutions as well. An agent that challenges our assumptions is valuable precisely because we're fallible.

The point is to change what we pay attention to. If an agent can competently implement a feature, watching it type every line is a poor use of an engineer's time. We'd be better off examining the proposed behaviour, the boundaries it crosses, the alternatives it rejected and the evidence that the result helps its users.

That also changes what it means to review a pull request. Anthropic's team described reviewing the **intent of each change** rather than reading every line. For changes with serious security, safety or operational consequences, close examination of implementation details will still be necessary. But the broader direction is worth considering: review effort should follow risk and uncertainty, rather than simply the size of the diff.

The ability to say “no” isn't a magic privilege granted by a senior job title. It's built through understanding systems, asking awkward questions, investigating failures and learning what happens after software reaches production. Junior and mid-level developers need those opportunities too, particularly if agents are taking on more of the straightforward implementation work.

As code becomes quicker to produce, I suspect one of our most important engineering skills will be knowing when a perfectly workable solution deserves a second question.

## Can We Just Ask Another AI to Check?

![robo helpers]({static}/images/future_dev/robocop_helpers.jpg)

If one agent writes the code, another can review it. Give the reviewer a fresh context window, ask it to challenge the implementation, and perhaps add a third agent to question the specification. That can work remarkably well. Independent review can expose missed edge cases, weak tests and questionable architecture without keeping another engineer occupied for hours.

But what exactly is the reviewer checking against?

A reviewer could read the order-notification requirement, confirm that the implementation satisfies it, and approve the change. The tests pass, the failure handling is sound, and customers still get too many emails.

This is a **common-cause failure** problem. Multiple checks provide less protection when they inherit the same flawed assumption. Fresh context windows can help an agent assess an implementation impartially, but they don't supply the missing business context.

A more useful second opinion might draw on different evidence: customer feedback, operational data, or a conversation with the people who requested the feature. An agent can help investigate all of those. It can ask whether warehouse statuses belong in customer emails or propose a user trial. When a business rule is undocumented or disputed, though, someone with the relevant responsibility needs to settle it. Another round of code review won't answer that question.

And as Anthropic's experience shows, adversarial review findings still need to be weighed carefully. A safeguard can be technically defensible and still add more complexity than the risk justifies.

I'd happily use agents to interrogate requirements, review code and gather evidence. I'd also want them to make uncertainty visible: *What don't we know? Which assumption drives this recommendation? Who can answer it?*

The role for engineers is to decide which questions need escalation, which risks justify complexity, and which decisions can safely be tested and reversed.

## The New Definition of Done

For years, we've treated a green build, passing tests and an approved pull request as reassuring signs that a feature is ready. They still matter. I certainly wouldn't want to ship software without them. But as coding agents take on more implementation work, those checks tell us only part of the story.

That suggests expanding our definition of done in both directions: examine intent before implementation, and check outcomes after release.

Before an agent writes code, we should be able to explain the problem in terms of the people affected by it. What outcome are we trying to achieve? Which assumptions are we making? Who can confirm them? A short conversation with the right person might be worth more than another hundred generated tests.

During implementation, we still need evidence that the software works. But we should also ask whether the approach fits the surrounding system, what trade-offs were made, and which risks remain. The agent can help assemble that evidence. It can show the alternatives it considered, run tests and flag unanswered questions. Engineers can then spend their review time where judgment is most needed.

And after release, we should check what actually happened. Did customers find the notifications useful? Did enquiries about order progress fall? Did we create a new operational headache? Production behaviour and user feedback are part of the answer, even if they don't fit neatly into a CI check.

Anthropic's AI-native SDLC playbook offers a useful way to make some of this visible: record the original intent, turn it into a reviewed specification, agree an implementation plan, and keep those decisions alongside the code. Not every two-line fix needs three Markdown documents. A change to a payments or permissions system deserves more scrutiny than a small copy edit. **The effort we spend validating a change should reflect the consequences of getting it wrong.** The principle is more important than the paperwork: make the reasoning behind a change something we can examine and challenge.

That would give us a more useful definition of done. The tests pass, the important assumptions have been examined, the risks are understood, and we have a way to find out whether the feature delivered what people needed.

## The Code Is Cheap. The Judgment Isn't.

![robo teamwork]({static}/images/future_dev/robocop_teamwork.jpg)

AI gives us the chance to spend less time on routine implementation and more time discovering whether an idea is worth implementing. We can build prototypes quickly, test assumptions early and change course while the cost is still small. That's an extraordinary improvement in how we can work.

It also demands something of us. When a coding agent produces a convincing implementation in twenty minutes, we're the ones deciding whether to accept its assumptions, challenge its design or put the result in front of users. The quality of our questions matters as much as the speed of its answers.

I suspect developers will increasingly be judged by the decisions they help teams make: the problems they clarify, the risks they recognise, the complexity they avoid and the outcomes they can demonstrate. That requires understanding the code and the system around it, even when someone - or something - else writes most of the implementation.

Which brings us to the next question in this series: **what does it mean to be a senior developer when writing code is no longer the hardest part of the job?**

---

### Further reading

- [Anthropic - Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control) - the engineering account behind the migration, architecture and adversarial-review examples.
- [Anthropic - The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) - the discussion of changing bottlenecks across planning, implementation, review and deployment.
