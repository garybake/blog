Title: The Junior Developer Paradox
Date: 2026-11-20 09:00
Tags: craft,ai,development,future,senior
Category: Future
Slug: the-junior-developer-paradox
Summary: A coding agent can help a junior developer ship a feature and quietly do the very work that would have taught them how to look after it.
featured_image: /images/future_dev/medieval_scrolls_beyond_the_curtain_wall.jpg

---

![medieval scrolls]({static}/images/future_dev/medieval_scrolls_beyond_the_curtain_wall.jpg)

---

### Beyond the Code series
- [Part 1. Who Checked It Was the Right Code?](/who-checked-the-code.html)
- [Part 2. The New Senior Developer](/the-new-senior-developer.html)
- [Part 3. The Junior Developer Paradox](/the-junior-developer-paradox.html#the-junior-developer-paradox.html)

---

## The junior developer who shipped the feature

Imagine you’re the junior developer who added a CSV export to the reporting tool last week. Someone in finance sends you a screenshot. Their month-end report has said *Generating* for twenty minutes. “Should I click it again?”

You built the feature with a coding agent. It found an existing background job to use as a pattern. You checked the figures against the report on screen, caught a missing column and got the change through review. Finance has been using it all week.

You look up the job and find the CSV. The worker finished writing it, then a deployment restarted the process before it could mark the report as ready. You can account for everything on the screen. You’re still a little reluctant to tell someone to click that button again.

“I can see your file,” you reply. “Give me a minute.”

That minute interests me. A coding agent can help someone ship a feature early in their career. It can also do much of the investigating through which they’d learn to look after it. As a lead, I’d want to pay attention to what happens next.

## Where engineering judgement comes from

A colleague suggests trying it locally. “What do you reckon the worker will do when it comes back?”

You expect it to pick up the unfinished job. With the agent’s help, you stop it just after it writes the file, then restart it and watch. Nothing happens. You click *Export* again. A second job appears with a different ID. The first still says *Generating*.

You follow the second job through the code. It runs the query again, against whatever happens to be in the database now. If someone has corrected an invoice in the last twenty minutes, clicking again could give finance a different total.

That discovery changes what you say to the person waiting. “A second click would generate a fresh report. Do you need the figures as they were when you first ran it?” Yes, they do. They’ve already started reconciling the month.

An experienced engineer might have asked about the date of the figures before opening the logs. I’d like a junior to have the chance to arrive at that question the long way round at least once. Finding out where your own prediction went wrong gives you a reason to remember it.

## What cognitive ownership means

![scriptoriums new ledger]({static}/images/future_dev/the_scriptoriums_new_ledger.jpg)

I use *cognitive ownership* to mean understanding a change well enough to take responsibility for what it does. That includes being able to challenge a plausible suggestion from an agent, especially one that would pass review.

Take the obvious fix for the export. The agent suggests rerunning any job that’s been stuck for ten minutes. The status would go green. A download would appear. A test that checked both of those things would pass. You now know why you’d send that patch back. Finance needs the file it started reconciling, and the proposed fix could quietly replace it.

There’s engineering work in that conversation with the agent. You’ve uncovered a requirement, worked out who could settle it and used their answer to change the design. You can let the agent write every line of the recovery code and still be the person a reviewer comes to with “Why do we keep the old file here?” You can answer that today. If finance changes its process next year, you’ll also know which decision to reopen.

This is the part of cognitive ownership I find exciting. Once you’ve shown you can catch a fix that would quietly change finance’s figures, I’d trust you to delegate more of the next export to the agent. You know what a convincing test has to prove. That buys you time to take on a decision you haven’t had to make before.

## Give the ticket two objectives

Put yourself in the lead’s seat. Finance closes the books in half an hour. A senior engineer knows how to recover the original CSV, so you ask them to do it. Finance gets its file. There’s still a permanent fix to make, and you have a choice about who takes it.

### A team that leaves learning to chance

The senior already has the logs open. They ask the agent for a patch, check that recovery returns the original figures and put it up for review. The junior reads it, sees why the test passes and picks up the next ticket. You’ve met the **delivery objective**. Next month, finance can get to its report after a restart.

A fortnight later, an invoice email is stuck on *Sending*. The junior remembers the export and asks the senior, “Is this the same thing?” It’s a sensible question. On the export ticket, somebody else worked out how to tell which part was safe to repeat.

### A team that makes room for learning

This time you give the junior the follow-up. You have a **development objective** as well. You’d like them to be able to look at an interrupted job and work out what’s already happened. You leave the choice of test in their hands.

Their first test passes. Then they notice it would also pass with the agent’s original fix. The invoice data is identical on both runs, so who could tell whether the CSV was the original or a fresh copy? They change an invoice between the failed run and the recovery. Now the wrong fix fails for exactly the reason finance cares about.

Imagine that same email turning up a fortnight later. This time the junior asks, “Can we check whether the mail provider accepted it before we send another?” They might still need help finding the record. They’ve already worked out why it matters.

![what the sprint report misses]({static}/images/future_dev/what_the_sprint_report_misses.png)

Both teams shipped a working fix. If all I had was the sprint report, I’d struggle to tell them apart. Sitting in on that second conversation would tell me quite a bit about what the junior could take on next.

## When should the agent coach, and when should it get on with the work?

By the time the developer asks about the mail provider, another lesson on duplicate sends would be a peculiar reward for having learnt the first one. What’s unfamiliar is this provider’s behaviour. The developer might give the agent a narrower brief. “Show me where we store the provider’s reply. I want to try losing the connection just before it comes back.”

A local experiment gives them room to be wrong. Suppose the provider accepts the message but the reply never reaches the worker. The message ID in the database stays blank. They’d see the same blank field if the request had never reached the provider. An automatic resend now looks like a decision someone needs to make with the customer in mind.

Once the developer can show that, I’d happily let the agent take on more of the implementation. It can add the logging and exercise both failure cases. I’d bring the developer back for the question of who can authorise a second send when the outcome of the first is uncertain. Naming the test fixture can wait until review.

The developer gets a say in that arrangement. “I know this bit. It’s the timeout I want to look at” is a perfectly good reason for the agent to skip ahead. Equally, a senior engineer using this provider for the first time might want to sit with the trace for a while. The amount of help should change as people show what they understand and as the system gives them something new to learn.

## Try it on one ticket

![scribes triumph and rest]({static}/images/future_dev/scribes_triumph_and_rest.jpg)

At your next planning session, pick a ticket with a decision your team expects to face again. Ask the developer taking it on, “Which part would you like to be able to handle yourself next time?” A line beside the acceptance criteria is enough. *I want to be able to work out whether it’s safe to retry a job that stopped halfway through.*

Leave that decision open long enough for the developer to influence the patch. At review, ask what convinced them it was safe to ship. Then give them first look at the next related ticket. The question they ask on their own, a fortnight later, will tell you more about what stuck than another walkthrough of the pull request.

I’d like the junior who shipped the export button to become the colleague finance trusts with “Should I click it again?” Part of my job as a lead is recognising the moment when I could answer that question in thirty seconds and they could learn something worth keeping by working it out themselves.

*In Article 4, I’ll show how I built cognitive ownership into a Claude Code skill, including the instruction I care about most: give the developer a chance to make a prediction before offering an answer.*
