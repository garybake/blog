Title: Designing for Model Swaps
Date: 2026-2-25 10:25
Tags: development,change_seams
Category: Python
Slug: seams1
Summary: Part of the Change Seams series - architecture patterns for LLM applications that survive the real world.
featured_image: /images/change_seams/roboparts.png

![robo parts]({static}/images/change_seams/roboparts.png)  


---

## The Problem Story

It's a Tuesday. OpenAI quietly ships a new model version. You update one line in your `.env`:

```bash
LLM_MODEL=gpt-4o
```

Restart, smoke test, ship. Done in ten minutes. You feel great.

Six weeks later, a different Tuesday. Your team upgrades a different app - one without clear seams. The model change touches the prompt formatting, the tool-calling schema, the structured output parser, and three hardcoded magic strings buried in business logic. The PR balloons to 400 lines. QA takes two days. Two regressions slip to production.

The difference isn't the model. It's whether the app was *designed* to swap models - or whether the model is load-bearing.

---

## The Principle: Seam-Driven Architecture

In Michael Feathers' *Working Effectively with Legacy Code*, a **seam** is a place where you can alter behaviour without editing the code at that location. For LLM apps, the same idea applies - but the seams are different:

1. **Provider** - which company's API you call
2. **Prompt** - the instructions the model receives
3. **Tools** - what the model is allowed to do
4. **Policy / Config** - runtime flags like temperature, mode, feature gates
5. **Observability** - where traces and token counts go

If those five things are each behind a narrow interface, you can swap any one of them in under fifteen minutes without touching the others. If they're tangled together, you can't swap any of them safely.

This is the *only* principle in this post: **keep each seam narrow, explicit, and independently replaceable.**

---

## The App

A FastAPI reference app demonstrating how to build an LLM application where the provider, prompts, tools, config, and observability are each a **change seam** — a narrow interface you can swap without touching anything else.

[Github repo](git@github.com:garybake/change_seams.git)

![openai model]({static}/images/change_seams/app_screenshot1.png)

---

## The Architecture

Here's the system we're working with. Every chat request flows through all five seams:

<img src="{static}/images/change_seams/mermaid-flow-transparent.svg" height="800">

Each coloured box is a seam. The agent runner in `app/agent/runner.py` is the *only* file that touches all five - and it touches each one through its interface, not its internals.

---

## The Code Snippet

The entire provider seam lives in `app/providers/llm.py`. It's 32 lines:

```python
# app/providers/llm.py - Seam 1
from langchain_core.language_models.chat_models import BaseChatModel
from app.config import settings

def get_llm() -> BaseChatModel:
    provider = settings.llm_provider.lower()
    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            api_key=settings.openai_api_key or None,
        )
    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
        )
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {provider!r}")
```

To add a new provider (say, Google Gemini), you add one `elif` branch and one API key field in `app/config.py`. The agent runner, the tools, the prompts, and the observability pipeline are completely unaware that anything changed.

The runner calls it like this:

```python
# app/agent/runner.py (excerpt)
llm = get_llm()                                         # Seam 1 - provider
tools = get_enabled_tools(settings.enabled_tools)       # Seam 3 - tools
agent = create_agent(model=llm, tools=tools, system_prompt=system_content)
result = await agent.ainvoke(
    {"messages": [HumanMessage(content=message)]},
    config=RunnableConfig(callbacks=[otel_handler]),    # Seam 5 - observability
)
```

Five seams, five lines. The complexity lives *inside* each seam, not *between* them.

![robo parts]({static}/images/change_seams/roboreplace.png)  

---

## Skill-Hardening Drills

### Drill 1 - Swap the model provider in under 15 minutes

The goal: go from OpenAI to Anthropic (or back) without touching any file except `.env`.

```bash
# Step 1: Install the Anthropic provider package (if not already present)
pip install langchain-anthropic

# Step 2: Edit .env - two lines change
LLM_PROVIDER=anthropic
LLM_MODEL=claude-sonnet-4-5
ANTHROPIC_API_KEY=sk-ant-...

# Step 3: Restart the server
docker-compose restart backend

# Step 4: Smoke test
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is 2 + 2?"}'
```

Check the response's `spans[0].attributes.llm.provider` field - it should now read `anthropic`. If the app is well-seamed, that's the *entire change*. If you find yourself editing prompt templates or tool schemas to make the swap work, you've found a leaky seam worth fixing.

**Time target**: under 15 minutes including smoke test. If it takes longer, log where the time went - that's your refactoring backlog.

![openai model]({static}/images/change_seams/app_screenshot2.png)

Notice the tracing now shows the anthropic model in use.


curl -X POST http://localhost:8080/api/prompts -H "Content-Type: application/json" -d '{"key": "agent.system", "content": "You are a concise assistant. Keep responses under 2 sentences.", "purpose": "terse", "owner": "eng"}


---

### Drill 2 - Run a "model regression" and contain it with versioning

The goal: simulate output drift after a model change, then prove you can contain it using the prompt registry - without redeploying code.

**Setup**: seed two prompt versions for `agent.system`:
(Version 1 is the existing prompt)

```bash
# Version 2 - terse responses
curl -X POST http://localhost:8080/api/prompts \
  -H "Content-Type: application/json" \
  -d '{"key": "agent.system", "content": "You are a concise assistant. Keep responses under 2 sentences.", "purpose": "terse", "owner": "eng"}'

# Version 3 - verbose responses (simulates a regression)
curl -X POST http://localhost:8080/api/prompts \
  -H "Content-Type: application/json" \
  -d '{"key": "agent.system", "content": "You are a thorough assistant. Always explain your reasoning in detail.", "purpose": "verbose", "owner": "eng"}'
```

**Simulate the regression**: activate version 2, run a few queries, observe the output drift.

```bash
curl -X PUT http://localhost:8080/api/prompts/agent.system/3/activate
```

The model uses the verbose prompt.

![openai model]({static}/images/change_seams/app_screenshot_v3.png)

**Roll back in production - no code deploy, no restart**:

```bash
curl -X PUT http://localhost:8080/api/prompts/agent.system/2/activate
```
The model uses the terse prompt.

![openai model]({static}/images/change_seams/app_screenshot_v2.png)

Because the prompt is a seam, this is a *data change*, not a *code change*. The `ObservationLog` table records `prompt_version` on every request, so you can correlate output quality shifts with exact prompt versions after the fact. That's the point of seam-aware observability: when something breaks, you know *which seam* to blame.



---

## The Checklist

Copy-paste this into your next architecture review or PR template for any LLM feature:

- [ ] Can I swap the model provider by changing `.env` only - no code edits?
- [ ] Are prompts stored outside the codebase (DB, config service) so I can update them without a deploy?
- [ ] Is each tool registered independently, so I can disable one without touching others?
- [ ] Does every request log which model, which prompt version, and which tools were active?
- [ ] Is the observability backend swappable by changing one function - not scattered across the app?
- [ ] After a model upgrade, can I identify regressions from logs alone - without rerunning evals from scratch?

If you can check all six boxes, quarterly model swaps are a Tuesday afternoon task. If you can't, they're a two-day incident waiting to happen.

![robo evolve]({static}/images/change_seams/roboevolve.png)

---

## Where to Go From Here

Clone the reference app, run `docker-compose up`, and try both drills yourself. The test suite runs against SQLite with mocked LLM calls, so you don't need API keys to explore the seams.

Next post: **Seam 3 in depth** - writing tool contracts that survive model upgrades, and why `args_schema` is the most important five lines in your tool definition.

---

*The LLM landscape moves fast. Your architecture doesn't have to.*
