Title: Stop Building Your AI Product Around Today's Model
Date: 2026-8-31 09:00
Tags: leadership,ai,architecture,change_seams
Category: Leadership
Slug: stop-building-todays-model
Summary: The models will change. Your architecture shouldn't have to. Why engineering leaders should optimise AI systems for the cost of changing their mind, not for today's best model.
featured_image: /images/change_seams/roboevolve.png

![robo evolve]({static}/images/change_seams/roboevolve.png)

---

### Seams series
- [Part 0. Stop Building Your AI Product Around Today's Model](/stop-building-todays-model.html)
- [Part 1. Designing for Model Swaps](/seams1.html)
- [Part 2. The Tool Contract Layer](/seams2.html)
- [Part 3. The Observability Layer](/seams3.html)

---

## Ten minutes versus two days

A new model ships. On one team, someone edits an environment variable, runs a smoke test, and deploys. Ten minutes, done before lunch.

On another team, the same upgrade touches prompt formatting, tool-calling schemas, structured-output parsing, and a few hardcoded strings that turned out to be load-bearing. The PR balloons to 400 lines. QA takes two days. Something regresses in production anyway.

Same task. Same model. Wildly different cost.

The difference isn't the model. It's whether the model was allowed to become load-bearing architecture.

I've watched both versions of this story happen in systems I've worked on, and it's rarely a skills problem. It's a decision, made early and usually unconsciously, about how many parts of the application are allowed to know which model they're talking to.

---

## The question everyone asks, and the one nobody does

Most architecture conversations about AI spend their energy on one question: which model, which provider, which framework should we use?

It's a reasonable question. It's also the wrong one to spend all your time on, because in this space the answer has a short shelf life. The model that's clearly correct today is routinely not the model that's correct in six months. Pricing changes. A provider changes its tool-calling API. A new model shifts the cost-quality tradeoff enough that the old choice looks expensive in hindsight. Occasionally a security or procurement requirement rules out a provider you'd already built around.

None of that is a failure of judgement. It's just the operating environment. AI technology is moving faster than most teams' release cycles, and treating today's best answer as a permanent one is a bet you don't need to make.

So alongside "which model should we use," leadership should be asking a second question, and asking it just as seriously:

**What does it cost us if we're wrong, or if we're right today and wrong in six months?**

That's an architecture question, not a model-selection question. And it's the one that actually determines how expensive this technology choice turns out to be.

---

## Optimise for the cost of changing your mind

Good architecture has always cared about changeability, coupling, and how reversible a decision is - that's not new. What's different here is the assumption underneath it. Many conventional infrastructure choices are made assuming relative stability: you might keep a database, a framework, or a cloud platform for years without revisiting the decision. AI systems contain another class of dependency - one where you should assume the answer will change, not hope it won't.

So the useful question isn't "should we use OpenAI, Anthropic, or Gemini" - it's "what happens the day the correct answer changes?"

Don't optimise your architecture for today's best model. Optimise it for the cost of changing your mind.

That's the whole argument. Everything else in this piece is really just working out what that means in practice, and where it doesn't apply.

---

## Seams: deliberate places where change stays cheap

There's an old idea from Michael Feathers' *Working Effectively with Legacy Code*: a **seam** is a place in a system where you can change behaviour without editing the code at that location. It's a testing concept originally, but it maps almost exactly onto the problem above. A seam is a boundary you put in deliberately, at a point where you already know change is coming, so that the change stays local instead of spreading.

For an LLM-based product, I keep coming back to the same five seams:

| Seam | The question it answers for leadership |
|---|---|
| Provider / model | Can we move provider without rewriting the product? |
| Prompt | Can behaviour change without a software release? |
| Tools | Can capabilities be added or disabled safely? |
| Policy / config | Can behaviour be controlled operationally, not just in code? |
| Observability | When quality changes, can we tell why? |

None of these are exotic. Each one is just a narrow, explicit interface around a decision that is genuinely volatile - not a decision that might theoretically change one day, but one you already know will change, probably more than once.

The point of a seam isn't abstraction for its own sake. It's reducing blast radius. Take the provider seam on its own: without it, "the model" isn't really one dependency, it's a name that's leaked into your prompts, your tool schemas, your output parsing, and whatever business logic quietly learned to work around the old model's quirks. A model swap has to chase down every one of those places. With a provider seam in between, the swap stops there - the application never talked to the model directly, only to the seam.

![blast radius]({static}/images/change_seams/blast_radius.png)

The other four seams work the same way, independently, for their own kind of change - a prompt edit stops at the prompt seam, a new tool stops at the tools seam. None of them are stations a change passes through on its way somewhere else. Each is a separate boundary for a separate kind of volatility.

I wrote a companion technical series on exactly this - [Part 1 walks through a reference implementation](/seams1.html) with actual code, drills, and a checklist. This article isn't that. This is the "why should I care" version, for the person deciding whether the engineering time is worth spending.

---

## "Isn't this just premature abstraction?"

It's a fair objection, and I'd normally be the one raising it. My default position on architecture is pragmatic to the point of being boring: small teams, few moving parts, Postgres before a specialised database, a worker queue before an orchestration platform, Docker Compose before Kubernetes, until something concrete forces the upgrade. I don't think you should build an interface around every dependency on the off chance it might change someday.

The reason AI is different isn't that AI is special or magical. It's that for these five seams specifically, the volatility isn't hypothetical. It's routine. You will change models. You will change prompts, probably weekly. You will add and remove tools as the product evolves. Pretending otherwise and hardcoding the current choice everywhere isn't discipline, it's just deferring a cost you already know is coming.

The judgement call is scope, not whether to do it at all. Put a narrow seam where volatility is real. Don't build a generic plugin platform to avoid importing an SDK, and don't put a seam around something that's genuinely stable in your context. A good seam is boring. It's a function, a config value, a small interface - not a new subsystem. If your "seam" needs its own onboarding doc, you've overbuilt it.

---

## Cheap to change is not the same as safe to change

There's a trap on the other side of this, and it's worth naming directly: don't read "the mechanical change takes ten minutes" as "therefore ship it after a ten-minute smoke test."

Those are two different costs, and good architecture only collapses one of them.

**Mechanical cost** is how much of the system has to move to make the swap - how many files, how much redeploy, how many teams need to coordinate. A good seam makes this small and predictable.

**Validation cost** is how much evidence you need before you trust the new model in production - regression suites, evals against your actual traffic patterns, a canary period, a human review of edge cases. A good seam doesn't shrink this. In some ways it should grow it, because now you can actually afford to do it properly.

That second part matters more than it sounds. When the model isn't tangled through your codebase, you can run the old and new model side by side, deliberately, and compare them on real inputs instead of vibes. You can roll back to a known-good prompt version without a deploy. You can look at a bad output and know exactly which model, which prompt version, and which tools produced it, instead of guessing. The seam doesn't just make change cheaper - it makes change measurable, which is what actually lets you move fast without being reckless about it.

Teams that get this wrong tend to end up at one of two bad places: either changes are so entangled that nobody dares touch them, so the system calcifies around a model that's quietly becoming outdated, or changes are fast because nobody's checking, and quality drifts until a customer notices before anyone internally does. Seams are what let you be fast in the mechanical sense and careful in the validation sense, at the same time.

---

## What this actually buys you

Put in leadership terms rather than architecture terms: you stop betting the product on today's provider or framework, a model change becomes a task instead of a project, and you can run two models against each other and compare them properly instead of debating it in a meeting. There's also a quieter benefit that's easy to miss - genuine negotiating leverage with a vendor. Switching only counts as leverage if you could actually do it. A provider who knows you can't move is a provider who can move your pricing.

> The lifespan of your product should be longer than the lifespan of your current model.

If it isn't, the model has quietly become the architecture, and the product is just a wrapper around a dependency you don't control.

---

## Questions worth taking into your next architecture review

A short list, deliberately short:

- If we had to change model provider tomorrow, what would actually break?
- Where are provider-specific assumptions hiding - in prompts, in output parsing, in tool schemas, in business logic?
- If a customer reports a bad answer, can we say which model, prompt version, and tools produced it - from logs alone?
- Can we roll back model or prompt behaviour independently of a code deploy?
- Which of our current AI-related decisions would be expensive to reverse, and did we choose that on purpose?

If most of those have confident, specific answers, you're in reasonable shape. If they produce a pause and a "let me check," that pause is the actual cost of not having these seams - you just haven't paid it yet.

---

## The point

We don't know which models, providers, or frameworks we'll be using in two years. Nobody credibly does, and I'd be suspicious of anyone who claims otherwise with confidence.

That's fine. We shouldn't need to know. Good AI architecture doesn't try to predict the winning technology. It makes being wrong about the winning technology cheap.

Your model should be a dependency of your product. It shouldn't be the architecture of your product. The LLM landscape moves fast - your architecture doesn't have to.

If you want to see what this looks like at the code level - an actual provider seam, a tool contract layer, and an observability layer that survives a model swap - the technical series starts here: [Designing for Model Swaps](/seams1.html).
