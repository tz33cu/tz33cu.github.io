---
title: "aiX Weekly — AI in Higher Education (July 22nd, 2026)"
date: 2026-07-22
draft: false
image:
  focal_point: 'top'
authors:
  - admin
tags:
  - AI
  - aiX
---
This week's post examines two converging disruptions: accountability when AI mediates consequential decisions, and AI's growing strain on the knowledge and talent ecosystems — peer review, open-source software — that it was built on.

<!--more-->

Each [aiX Weekly]({{< relref "/tags/aiX/" >}}) issue is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the [aiX Programs, Columbia University](https://www.linkedin.com/company/aix-programs-columbia-university/). AI can make mistakes and so is the human reviewer. Please double-check the linked sources.*

**Reviewed by Tian Zheng on July 21st, 2026.**

---

## TL;DR

- **A human-subjects study finds that reviewers told to verify AI output grew *more* confident in the system's answers — even when wrong — while a pre-registered experiment shows structured oversight can reduce AI research failures from 72% to 16%** ([Research Highlights](#research-highlights))
- **AI is disrupting the peer review system it was built on: journal submissions up 42% since ChatGPT, 21% of ICLR 2026 reviews fully AI-generated, and an Organization Science study finds AI-generated reviews are measurably narrower and lower quality** ([Research Highlights](#research-highlights))
- **Twenty-six Meta employees sue over AI-driven layoff selections, alleging algorithmic performance systems made the actual decisions while humans rubber-stamped the output** ([Most Discussed](#most-discussed))
- **Princeton's Arvind Narayanan argues at ICML 2026 that AI is a "normal technology" — powerful but unreliable — and warns that automating peer review is "a trap" that cedes control of research direction** ([Most Discussed](#most-discussed))

---

## Table of Contents

- [This Week at a Glance](#this-week-at-a-glance)
- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [What's in the News](#whats-in-the-news)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [What Changed](#what-changed)

---

## This Week at a Glance

Two disruptions converge in this week's material. The first is to accountability: when AI sits between a decision-maker and a consequence — scoring employees, reviewing research, verifying student work — who owns the judgment? The confirmation-bias paper shows individual verification can backfire. The "(Human) Attention" paper shows structured oversight works when designed as architecture. Meta's lawsuit puts the question in legal terms.

The second disruption is to the knowledge and talent ecosystem itself. AI is straining the very systems that produced it. The peer review process that validates research is being flooded with AI-generated submissions and degraded by AI-generated reviews. The open-source software ecosystem that AI's infrastructure depends on is being overwhelmed by AI-generated contributions that consume volunteer review time. And Narayanan's ICML keynote argues that if we automate the evaluation layer — peer review, human oversight, quality control — we cede the steering of research to the systems we're supposed to be directing.

Both disruptions share a common structure: AI is powerful enough to increase volume but not reliable enough to maintain quality, and the gap between the two is being absorbed by the human systems — reviewers, maintainers, faculty, students — that were already stretched thin.

*Relevant to faculty:* The peer review and open-source stories are not someone else's problem. Faculty depend on both systems — for the literature they teach from and the tools they build with. The confirmation-bias and "(Human) Attention" papers together suggest that "verify the output" needs structure, not just instruction.

*Relevant to institutional leaders:* The DEC's 6% faculty-support figure, and Handshake's 28% integration gap all point to an accountability distribution problem. The peer review crisis adds a research-infrastructure dimension: the quality of the knowledge pipeline institutions depend on is itself under pressure.

*Relevant to students and researchers:* Narayanan's "normal technology" framing — and his warning that automating peer review is "a trap" — is directly relevant to anyone entering a research field. The Meta lawsuit illustrates the same questions about algorithmic scoring and nominal human review that show up wherever data-driven systems shape outcomes.

---

## Research Highlights
![Research Highlights](media/research-highlights.png)

**[Confirmation Bias: A Challenge for Scalable Oversight](https://arxiv.org/abs/2507.19486)**
Across two human-subjects studies of simple oversight protocols, participants told that a model is "correct most of the time, but not all of the time" became more confident in the system's answers after conducting their own online research — even when those answers were incorrect. Showing arguments for both candidate answers improved accuracy in the cases where the model was wrong.
`Study type: human-subjects experiments ` 

*Editor's note:* This complicates the default pedagogical move of "have students check the AI." If the act of verifying can increase confidence in wrong answers, then oversight training may need to teach structured disconfirmation — actively seeking the case against — rather than open-ended checking. — TZ

**[(Human) Attention Is (Still) All You Need: Human Oversight Makes AI-Assisted Social Science Reliable](https://arxiv.org/abs/2606.12848)**
In a pre-registered 2×4 factorial experiment with 280 complete research runs across four datasets, researchers tested whether structured human oversight can make AI-assisted economic research reliable. An unconstrained multi-agent baseline produced critical failures — specification errors, hallucinated findings, unsupported conclusions — in 72% of runs. Their Human-in-the-Loop Economic Research (HLER) architecture, based on pre-commitment, decision sequencing, accountability, and attention allocation, reduced the failure rate to 16%.
`Pre-registered factorial experiment`

*Editor's note:* Oversight may work when it's designed as an architecture rather than an afterthought. For teaching, the four design principles (pre-commitment, sequencing, accountability, attention allocation) are transferable to how students interact with AI in research assignments. — TZ

**[Modeling Human Beliefs about AI Behavior for Scalable Oversight](https://arxiv.org/abs/2502.21262)**
This paper addresses a foundational challenge for AI oversight: human evaluators may form incorrect beliefs about what AI systems are actually doing in complex tasks, leading to unreliable feedback. The authors formalize how evaluator belief models interact with value learning and introduce "belief model covering" as a way to reduce dependence on precise belief models. Published in Transactions on Machine Learning Research.
`Theoretical/formal analysis`

*Editor's note:* This connects to the confirmation-bias paper earlier in this issue — both identify the same vulnerability from different angles. That paper shows evaluators growing more confident in wrong answers; this one formalizes *why*: their mental models of what the AI is doing can be systematically wrong. For teaching, it suggests that "check the AI's work" is insufficient without first helping students build accurate models of what the AI actually does. — TZ

**[More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review](https://pubsonline.informs.org/doi/10.1287/orsc.2026.ed.v37.n3)**
Journal submission volume is up 42% since ChatGPT's release, but the review system absorbing that volume is degrading in measurable ways. This Organization Science study finds Flesch Reading Ease scores in reviews dropped 1.28 standard deviations, and AI-generated reviews are narrower — more focused on theory, less on data — than human reviews. The scale of the problem came into sharper focus at ICLR 2026, where Pangram Labs estimated 21% of 75,800 reviews (roughly 15,900) were fully AI-generated, with over half showing some AI involvement. ICML 2026 desk-rejected approximately 500 papers for LLM policy violations.
`Published research
`
*Editor's note:* When AI simultaneously floods the submission pipeline and degrades the review process, the feedback loop protecting research quality weakens at both ends. — TZ

---

## Institutional Movements
![Institutional Movements](media/institutional-movements.png)

**[Digital Education Council survey: 6% of faculty fully agree their institution provides sufficient AI resources](https://www.digitaleducationcouncil.com/resource-library-items/ai-in-higher-education-global-survey-2026)**
In a survey of 1,681 faculty across 52 institutions in 28 countries, only 6% fully agreed that their institution had provided sufficient resources to build faculty AI literacy, even as 86% anticipated using AI in their teaching in the future. The gap points to a distance between institutional AI announcements and faculty-reported experience.

**Open question:** What forms of support (time, training, credit, community) actually move the 6% figure?

**[Handshake Class of 2026: 85% Use AI, 28% Say School Integrated It](https://joinhandshake.com/network-trends/class-of-2026-outlook/)**
Handshake's survey of 1,248 graduating seniors across nearly 500 institutions finds 85% used AI tools in college, but only 28% say their program "meaningfully integrated" AI. Fifty-eight percent say they'll need stronger AI skills to succeed at work. Meanwhile, 62% of seniors report feeling pessimistic about their careers (up from 46% in 2024), with almost half citing AI's impact as a factor. Three-quarters of students who use generative AI describe themselves as "reasonably skilled" or "very skilled" — a self-assessment that may or may not reflect professional readiness.

**Open question:** Is the 28% integration figure a supply-side failure (institutions not offering enough) or a recognition gap (students not identifying AI instruction they've received)?

---

## What's in the News
![What's in the News](media/whats-in-the-news.png)

**[Inside college AI cheating wars: surveillance, false accusations, confusion (Anchorage Daily News)](https://www.adn.com/nation-world/2026/06/21/inside-college-ai-cheating-wars-extreme-surveillance-false-accusations-jarring-confusion/)**
The report describes uneven and sometimes extreme anti-cheating practices — students asked to show their desks with mirrors during online tests, or to keep arms crossed during oral exams — alongside a rise in false accusations from probabilistic AI-detection tools. It frames the definition of "cheating" itself as unsettled.

**What's interesting here:** The same detection tools meant to restore trust are generating a new category of disputed cases, which changes the burden of proof students face.

**[The Open-Source Maintainer Crisis: AI-Generated Contributions as Denial of Service](https://www.axios.com/2026/03/10/ai-generated-code-open-source-projects)**
In the first three weeks of January 2026 alone, three major open-source projects took drastic defensive measures against AI-generated contributions. curl shut its six-year bug bounty program after being flooded with AI-fabricated vulnerability reports. Ghostty implemented a zero-tolerance policy for AI-generated code submissions. tldraw auto-closed all external pull requests. Maintainers describe the situation as a "denial-of-service attack" — a flood of superficially plausible but low-quality contributions that consume review time and degrade signal. The paradox: AI companies simultaneously depend on open-source infrastructure and are undermining the volunteer labor that sustains it.

**What's interesting here:** Open-source software is the foundation AI was built on — the frameworks, libraries, and training infrastructure are overwhelmingly open-source. AI is now degrading the very maintenance ecosystem it depends on.

---

## Most Discussed
![Most Discussed](media/most-discussed.png)

**[Meta Employees Sue Over AI-Driven Layoff Selections (Courthouse News Service)](https://www.courthousenews.com/meta-employees-sue-over-use-of-ai-in-workforce-reduction/)** | **[CNBC](https://www.cnbc.com/2026/07/14/meta-lawsuit-layoffs-ai.html)**
Twenty-six current and former Meta employees filed a federal lawsuit alleging the company used a constellation of internal AI systems — including "Metamate" (an LLM assistant tracking internal communications), employee-trained "second-brain" agents, keystroke and activity monitoring, AI-token-usage dashboards, and algorithmically assisted performance ranking — to score, rank, and select 8,000 employees for layoffs. The plaintiffs argue these systems penalized workers on protected medical or parental leave, whose reduced digital activity produced lower scores. Meta responded that "workforce management and organizational decisions were and are made by people, not AI." The case was filed July 13 in the Northern District of California.

*Editor's note:* When performance data passes through AI systems that aggregate, weight, and rank before a human reviews the output, what exactly did the human decide? Which features were selected, how were absences weighted, what thresholds triggered a flag? These are modeling choices, made somewhere in the pipeline, by someone — or by no one in particular. This is a challenge for any data-driven process, including education. When we use AI to summarize student engagement data, flag at-risk students, or even aggregate peer evaluations, the same questions apply: what assumptions went into the score, and who owns them? — TZ

**[Arvind Narayanan's ICML 2026 Keynote: "What Will Be Left for Us to Work On?"](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work)** | **[Annotated slides](https://www.cs.princeton.edu/~arvindn/talks/icml-2026-annotated-slides/)**
Princeton's Arvind Narayanan, in the highest-profile keynote at ICML 2026 (July 13), argued for treating AI as a "normal technology" — powerful but subject to the same decades-long adoption cycle as electricity or computing. His central claim: a "capability-reliability gap" means capability has shot upward while reliability has improved only 5–10 percentage points, so "for now, you can have only two of three: general-purpose, high-stakes, automated." Narayanan warned against automating peer review — calling it "a trap" that cedes control of research direction — and reframed expert work as "steering rather than rowing": effort shifts from production to evaluation.

*Editor's note:* Narayanan's "normal technology" framing is one of the most useful narratives about AI I've seen. His observation that code-writing was roughly a third of software engineering work and "never the bottleneck" applies directly to teaching — we need to identify which parts of learning are analogous to code-writing (automatable) and which are analogous to requirements, design, and evaluation (not). — TZ

---

## Interesting Ideas & Repos
![Interesting Ideas & Repos](media/interesting-ideas.png)

**[A Decoupled Human-in-the-Loop System for Controlled Autonomy in Agentic Workflows](https://arxiv.org/pdf/2604.23049)**
An architecture proposal that positions human checkpoints at specific, decoupled points in agentic workflows rather than assuming continuous oversight.

**[Scalable Oversight via Recursive Self-Critiquing](https://arxiv.org/abs/2502.04675)**
Explores whether AI systems can critique their own outputs recursively, a candidate mechanism for "human on the loop" rather than "human in the loop."
*Editor's note:* Worth pairing with this week's confirmation-bias paper — one asks whether humans can verify, the other whether machines can help. Neither is settled. — TZ

---

## What Changed

- **The disruption turned inward:** AI is now straining the knowledge systems it was built on — peer review flooded with AI-generated submissions and degraded reviews, open-source maintenance overwhelmed by AI-generated contributions. This is a new category of concern, distinct from the adoption and assessment stories of Issues #1–3.
- **The oversight problem deepens:** The confirmation-bias paper and the modeling-beliefs paper show, from different angles, that human verification itself can be unreliable — going beyond the "keep a human in the loop" framing of earlier issues.
- **A corrective framework arrives:** Narayanan's ICML keynote offers "normal technology" as an alternative to both hype and catastrophism, with the capability-reliability gap as its central diagnostic.
- **The accountability question sharpens** from "should we use AI?" to "who bears the consequences when we do?" — a shift the Meta lawsuit, the peer review crisis, and the open-source maintainer crisis all make concrete.

---

*aiX Weekly is curated by Claude and reviewed by Tian Zheng for the aiX Faculty Fellowship at Columbia University. Editorial notes reflect one statistician's reading of the week, offered to prompt discussion rather than to prescribe. Corrections and suggestions welcome.*
