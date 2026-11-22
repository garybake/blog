Title: How much can I hand to Claude and still own the feature?
Date: 2026-11-21 09:00
Tags: craft,ai,development,future,senior
Category: Future
Slug: how-much-can-i-hand-to-claude
Summary: I built a Claude skill to help developers keep cognitive ownership of a feature by giving them a say in the decisions they’ll have to explain when the requirements change.
featured_image: /images/future_dev/medieval_tapestry_of_two_maps.jpg

---

![medieval tapestry of the two maps]({static}/images/future_dev/medieval_tapestry_of_two_maps.jpg)

---

### Beyond the Code series
- [Part 1. Who Checked It Was the Right Code?](/who-checked-the-code.html)
- [Part 2. The New Senior Developer](/the-new-senior-developer.html)
- [Part 3. The Junior Developer Paradox](/the-junior-developer-paradox.html)
- [Part 4. How much can I hand to Claude and still own the feature?](/how-much-can-i-hand-to-claude.html)

---

## What does an empty list promise?

Imagine converting a report from PDF to Markdown. The sentence “as the chart below shows” comes through perfectly. The chart itself is gone.

[MarkItDown](https://github.com/microsoft/markitdown) is an open-source Python library from Microsoft that converts files such as PDFs and Word documents into Markdown. In my fork, I wanted to give developers a way to spot that kind of omission. The idea was an optional check for vector graphics that would flag pages worth a closer look. I wanted the warnings on the conversion result so callers could decide what to do with them. The Markdown itself would stay exactly as it was.

I suggested calling the field `warnings`. Then Claude pointed out a wrinkle. Suppose you’re writing the code that consumes my result and you get back an empty list. Did MarkItDown check the document and find nothing to flag? Did it even look?

The check was optional and off by default. If both paths returned `[]`, you could run the conversion with its default settings and quite reasonably read the result as an all-clear. We settled on `None` when the check hadn’t run, an empty list when it had run and found nothing to flag, and one warning per affected page when it found something.

An empty list would tell the caller the check had run. To find out whether a particular chart survived, they’d still have to look at the conversion.

## The part I want to keep

![medieval tapestry of the true crossing]({static}/images/future_dev/medieval_tapestry_of_the_true_crossing.jpg)

I want to be able to hand a piece of work to Claude and still call the result mine. For me, that means I understand what we’ve built well enough to explain why it behaves the way it does, spot when Claude has misunderstood the problem, and take over when the requirements change. That’s what I mean by **cognitive ownership**.

At one point in the MarkItDown session I asked Claude to carry on editing the files without checking with me each time. Earlier I’d been quite specific about what should count as a warning. A table border is a vector graphic too. Flag every border and someone converting a long report could end up inspecting dozens of perfectly ordinary tables. I wanted to leave borders and decorative lines out. Once we’d agreed on that, Claude could write it into the spec without asking me to approve the act of typing it.

Claude had spotted the ambiguity in the empty list. I’d brought the concern about table borders. Either of us could have read those decisions in a finished spec and thought they sounded sensible. Working through them together meant I also knew what would have made me choose differently.

## What I taught Claude to do

I wrote a Claude skill to make that kind of conversation deliberate. The MarkItDown session above ran with the skill switched off. It gives me a real decision to work from when I explain what I put in the instructions. Who needs to make this decision, given what happens if we get it wrong? How much of the work can Claude carry out on the strength of what we’ve already agreed? Is there something here the developer wants to get better at?

Take the rule about ignoring table borders. A chart can be drawn with straight lines too. Before proposing a way to tell the two apart, Claude could ask me, “If we can’t tell whether these lines belong to a table or a chart, which mistake would you rather we made?” I might accept an occasional unnecessary warning because a missed chart matters more to my callers. Someone whose job involves checking hundreds of flagged pages might give a different answer. Either answer should be able to change the code.

The order matters to me. If Claude has already recommended a threshold, the easiest thing in the world is to say it sounds reasonable. Ask me what a missed chart would cost first and I have to think about the person using the result. Claude can then challenge my answer. We could run the proposed rule against a two-page PDF with a ruled table on page one and a line chart on page two. I’d expect a warning for page two alone. Once we’ve settled the behaviour, I’m happy for Claude to wire it up and run the tests.

![Which mistake can our users live with?]({static}/images/future_dev/which_mistake.png)

How often should it pause? My twenty years in development tell Claude very little about how well I know the internals of a PDF. What I can predict about that particular file, and how I account for a surprising result, gives it something to go on. Once I’ve shown I understand the behaviour, Claude can take on more of the implementation. A change to what callers can rely on still comes back to me.

## The same decision, earlier in a career

Imagine a junior developer designing the warnings field. They suggest returning an empty list by default. It’s a reasonable choice. Anyone writing a loop over the warnings can get straight on with it, even if there’s nothing to display.

Here’s where I’d want Claude to give them a few minutes with their own design. Ask them to put a message on screen for the person who uploaded the PDF. They write “No issues found”, run a conversion with the check switched off, and see those words appear. Now they have a bug they can see from the user’s side. Two conversions that ought to produce different messages have given their code exactly the same information.

They might decide to add a field that says whether the check ran. That would work too. I’d be happy to review a pull request with a different design from mine if the developer could walk me through those two screens and explain how their code knows which one to show. Claude could write most of the patch. The developer would still be the person I’d want in that review.

## A month later, the requirement changes

Suppose someone comes back a month later with a reasonable request. “Some of our reports have whole pages saved as images. Could you warn us about those as well?”

I’d be tempted to add another warning type and give Claude the job. Before I did, though, I’d want to write down one example. I switch on the new check for scanned pages and leave the vector graphics check off. The report has no scanned pages, so I get an empty list. A colleague looking at that result asks, “Did we check for the missing chart?” With one optional check, I could answer that question from the result alone. Now I’d have to go and find the code that called the converter.

![travelers ferryway tapestry]({static}/images/future_dev/travelers_ferryway_tapestry.jpg)

That changes what I’d ask Claude to build. I’d want the result to say which checks ran, even when they found nothing. I’d start with a test that runs each check on its own against the same plain page. Both conversions should return an empty warnings list. The caller should still be able to tell the two results apart.

A month on, I might need Claude to find the relevant files again. I’m quite happy to ask. What I want to bring to that conversation myself is the reason for that test. I remember the promise we made about an empty list, I can see where it breaks, and I know what the person using this feature needs from me now. That’s the part I want to keep.

---

## Author’s note on the design of the skill

One choice took a bit of working through. Once a developer has shown they understand something, I want Claude to do *more* of the work. Asking someone to implement the next three variations by hand costs time they could spend on a part of the system they’ve yet to figure out. An occasional question about a familiar decision is enough, especially if something has changed since they last made it.

We also had to decide how long Claude should leave someone with a failing test. I settled on making room for one worthwhile learning opportunity on a substantial task. A developer can ask for a hint or hand the problem back. If someone’s fixing an incident, the lesson can wait.

The instruction I care most about is that disagreement can change the patch. If Claude asks which mistake our users can live with, it has to be prepared to change the implementation and the tests when it hears the answer. Otherwise it might as well have skipped the question.

---

The Claude skill and supporting file are linked below. 
(Note that they make some references to other files that I used in my development. You can remove these references.)


[SKILL.md]({static}/extra/SKILL.md)  
[COGNITIVE_OWNERSHIP.md]({static}/extra/COGNITIVE_OWNERSHIP.md)  

It was a small made up problem I created specifically to test the skill.  
You can see the PR [here](https://github.com/microsoft/markitdown/pull/2908)  