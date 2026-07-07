---
title: "aiX Weekly — AI in Higher Education (July 1st, 2026)"
date: 2026-07-01
draft: false
image:
  focal_point: 'top'
authors:
  - admin
tags:
  - AI
  - aiX
---
Welcome to the **inaugural issue** of *aiX Weekly* — a curated digest of research, institutional moves, and debate at the intersection of AI and higher education. 

<!--more-->

Each issue is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the aiX Programs, Columbia University. AI can make mistakes and so is the human reviewer. Please double-check the linked sources.*

**Reviewed by Tian Zheng on July 1st, 2026.**

---

## TL;DR — Questions This Issue Helps You Think About

- **How do we measure AI competency among faculty?** → New FALCON-AI scale attempts to offer a validated instrument ([Research Highlights](#research-highlights))
- **What does the evidence say about AI and critical thinking?** → New studies find a correlation with cognitive offloading — but self-efficacy may be a moderating factor ([Research Highlights](#research-highlights), [Most Discussed](#most-discussed))
- **How are large-scale AI deployments playing out?** → Cal State's $17M OpenAI contract is generating discussion about governance and consultation ([What's in the News](#whats-in-the-news))
- **What's the conversation around faculty autonomy in AI adoption?** → Writing teachers passed a resolution on the right to opt out; the broader discussion continues ([What's in the News](#whats-in-the-news))
- **What are we learning about AI detection tools?** → Accuracy and bias concerns are prompting scrutiny, lawsuits, and calls for review ([What's in the News](#whats-in-the-news))
- **What does a campus-wide AI fluency requirement actually look like?** → Ohio State's roadmaps across all colleges provide a model ([Institutional Movements](#institutional-movements))
- **How are other countries approaching this?** → China just mandated AI as a core university course nationwide ([Institutional Movements](#institutional-movements))
- **What tools are graduate students exploring for research?** → Tools gaining traction include Elicit, Consensus, and NotebookLM ([Interesting Ideas & Repos](#interesting-ideas--repos))

---

## Table of Contents

- [This Week at a Glance](#this-week-at-a-glance)
- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [What's in the News](#whats-in-the-news)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [What Changed](#what-changed)
- [Try This Week](#try-this-week)

---

## This Week at a Glance

This week's stories illustrate a field navigating the distance between AI adoption and the frameworks meant to support it.

New research is adding definition to the picture: cognitive offloading from AI use correlates with lower critical thinking scores, but a CMU/Microsoft finding — that *self-confidence* (not tool-confidence) is associated with more critical thinking — suggests pedagogical design may matter as much as the tools themselves. The FALCON-AI scale and the "AI Literacy Heptagon" offer new instruments for measuring AI competency among faculty and students.

On the ground, institutions are working through familiar tensions. Cal State's $17M OpenAI contract drew pushback from faculty and students. Writing teachers voted on a resolution supporting the right to opt out. AI detection tools face growing scrutiny over accuracy and bias. And 90% of faculty express concern about AI's impact on critical thinking, even as institutions from Stanford to Ohio State move forward with AI integration.

**Relevant to faculty:** Research increasingly suggests that *how* AI is integrated matters more than *whether* it is. Building student self-efficacy — not just tool fluency — appears linked to preserving critical thinking. The CCCC opt-out resolution reflects ongoing discussion about disciplinary autonomy in AI adoption.

**Relevant to institutional leaders:** The Cal State and NYC experiences highlight questions about sequencing — when governance frameworks and faculty consultation happen relative to deployment. The IREX finding that only 1 in 3 universities has a clear AI strategy offers a useful benchmark.

**Relevant to students and researchers:** Several AI research tools are gaining traction among graduate students (Elicit, Consensus, NotebookLM). Meanwhile, accuracy concerns around AI detectors — especially regarding non-native English speakers — are worth following.

---

## Research Highlights
![Research Highlights](media/research-highlights.png)

### FALCON-AI: A New Scale for Measuring Faculty AI Competency
`Instrument Development · Empirical Evidence`

**Why this research:** Institutions are pouring resources into faculty AI training, but how do you know it's working? Existing AI literacy instruments were built for students or the general public and miss the role-specific demands faculty face — teaching with AI, researching with AI, and governing its use in their departments are fundamentally different tasks.

Song, Moon, Yang & Kilgore (2026) developed the **FALCON-AI Scale**, a psychometrically validated instrument designed specifically for university faculty — addressing a gap the authors identify in existing instruments, which lacked role-embedded faculty indicators. Grounded in the Critical Tech-resilient Literacies (CTRL) framework, it maps 43 items across three literacies (functional, evaluative, ethical) and four faculty work domains (general, teaching, research, service).

**What remains unclear:** The scale measures self-reported competency, not demonstrated performance. Whether higher FALCON-AI scores actually predict better teaching or more effective AI integration is untested. The validation sample's demographic breadth also needs examination.

**Practice implications:** Faculty development programs can use FALCON-AI as a pre/post assessment to evaluate training effectiveness — a significant upgrade over satisfaction surveys. It could also help institutions identify which faculty domains (teaching vs. research vs. service) have the largest competency gaps, enabling targeted investment.

[Source: arXiv:2603.20220](https://arxiv.org/abs/2603.20220)

> 💬 **Editor's note:** *As a statistician, I find this kind of instrument development genuinely encouraging — we need validated measures before we can rigorously evaluate whether our faculty development efforts are working. What needs to happen next is meaningful predictive validity: do FALCON-AI scores actually correlate with observable differences in how effectively faculty integrate AI? Self-report is a good starting point, and pairing it with behavioral or outcome measures would strengthen the case. For measuring the usefulness of AI related faculty development programs, this could be a useful pre/post tool worth piloting. — TZ*


### AI-Overdependence and Cognitive Decline: New Evidence
`Systematic Review + Empirical Study`

**Why this research:** The central anxiety in AI education is whether AI tools are eroding the cognitive capacities they're supposed to support. Faculty sense it anecdotally — students seem less willing to struggle with hard problems — but the field has lacked synthesized evidence.

A 2026 review in *Computers in Human Behavior Reports* synthesizes findings suggesting that higher AI use correlates with greater cognitive offloading and lower critical thinking scores, with younger users most affected. A complementary Carnegie Mellon/Microsoft Research study reveals a crucial paradox: confidence in GenAI tools was associated with *less* critical thinking, while self-confidence was associated with *more*.

**What remains unclear:** Causality. Do students who already have weaker critical thinking skills gravitate toward AI, or does AI use actively degrade those skills? The review cautions about differenting between "correlational patterns derived from large-scale surveys and the causal mechanisms identified through controlled experiments." Longitudinal and experimental designs in realistic settings are urgently needed. The self-confidence finding also raises questions about what builds self-confidence in the first place — is it prior knowledge, pedagogy, or personality? 

**Practice implications:** The self-confidence finding is directly actionable. Course designs that build student self-efficacy — through mastery experiences, productive struggle, and scaffolded challenges — may protect against cognitive offloading more effectively than AI usage policies alone. This reframes the intervention target: don't just teach students *about* AI, build their confidence that *they* can think. 

[Source: Computers in Human Behavior Reports](https://www.sciencedirect.com/science/article/pii/S2451958826001764) | [Center for Engaged Learning](https://www.centerforengagedlearning.org/unlocking-the-link-between-generative-ai-confidence-and-critical-thinking-skills/)

> 💬 **Editor's note:** *The correlation between AI use and reduced critical thinking is a finding worth taking seriously, but as a statistician I want to emphasize the causal caveat here — correlation studies cannot tell us the direction. It's entirely plausible that students with weaker critical thinking skills are more likely to rely on AI, rather than AI causing the decline. We need randomized or longitudinal designs to disentangle this. That said, the self-confidence finding is intriguing and practically useful. In my own teaching, I've found that building students' confidence through structured hands-on problem-solving changes how they engage with any tool, AI included. We need to design AI systems and AI learning experiences that can help develop cognitive skills rather than replacing or supressing the use of these skills. — TZ*


### Critical Inker: Scaffolding Critical Thinking in AI-Assisted Writing
`System Design · Preprint · Interesting Concept`

**Why this research:** If students are going to use AI for writing regardless of policy, the question becomes: can we design the interaction itself to preserve cognitive engagement? Most AI writing tools optimize for output quality, not learning — the student gets a better essay but does less thinking.

**Critical Inker** takes a different approach: it uses Socratic questioning to interrupt the passive consumption of AI-generated text, prompting students to evaluate, question, and refine. The system intervenes at the point of cognitive offloading rather than trying to prevent AI use altogether.

**What remains unclear:** Much about effectiveness at scale. This is a preprint describing a prototype with early technical evaluation and a small-scale pilot — but there's no controlled study comparing learning outcomes with and without the intervention. Whether Socratic prompting actually changes cognitive engagement or becomes another thing students click through is an open question. The approach also assumes students are motivated to engage with the prompts, which may not hold.

**Practice implications:** Even without extensive evidence, the design principle is worth adopting: if you can't prevent AI use, design friction into the workflow that requires thinking. 

[Source: arXiv:2604.07167](https://arxiv.org/pdf/2604.07167)

> 💬 **Editor's note:** *I like the design thinking here — building reflection into the AI interaction rather than policing AI use after the fact. Reflection and Socratic questioning are both recurring design choices among the aiX program projects. The learning happens in the friction, not in the output. — TZ*


### AI Competency Strategies via LLM-Based Delphi Method
`Exploratory / Methodological`

**Why this research:** Identifying what AI competencies matter in higher education usually requires expensive, slow expert consensus processes. Can AI accelerate the process of defining what humans need to know about AI?

This *Frontiers in Education* study replaces human expert panels with an LLM-based Delphi methodology to identify essential AI competencies, examine integration barriers, and propose strategies.

**What remains unclear:** The fundamental validity question: when you ask an LLM what humans should know about AI, are you getting expert consensus or a mirror of the model's training data? 

**Practice implications:** Treat the output as a hypothesis generator, not a validated framework. The competencies identified could seed a traditional Delphi study or faculty survey, saving time on the initial brainstorming phase. 

[Source: Frontiers in Education](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1683909/full)

> 💬 **Editor's note:** *This is a creative methodological experiment, and I appreciate the attempt to speed up consensus-building. The meta-question — using AI to study AI education — is itself worth discussing with faculty as a case study in how to leverage AI rigorously and effectively in higher education. — TZ*

### Capability-Based Training Framework for GenAI in Higher Ed
`Conceptual Framework / Literature Review`

**Why this research:** Most AI literacy frameworks stop at "understanding" — can you define what a neural network is, can you identify bias. But faculty and students don't just need to understand AI; they need to *use* it effectively within their disciplines. The gap between knowing what AI is and knowing how to apply it in your field is where most training programs fall short.

This *Frontiers in Education* framework proposes moving from literacy to capability — structured training that develops the ability to use generative AI in discipline-specific contexts, not just comprehend it abstractly.

**What remains unclear:** The framework draws on literature and document analysis but still lacks implementation data, pilot results, or learning outcomes from actual deployments.

**Practice implications:** The literacy-to-capability framing is useful for program design even without the specifics. For a faculty development program, we need to move from teaching "what is ChatGPT," to teaching "here's how to use AI to do X in your discipline, and here's when not to." 

[Source: Frontiers in Education](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1594199/full)

> 💬 **Editor's note:** *The literacy-to-capability shift resonates with how I envisioned the aiX program. The shift suggests training should be co-designed with disciplinary faculty, not delivered generically. In Statistics, knowing what a p-value is differs enormously from knowing when and how to use one in one's research. The same applies to AI. Conceptual frameworks like this are useful for orienting program design. Our aiX program helps us explore what does "capability-based AI training" look like in a humanity department vs. a professional school. The cross-disciplinary community of the aiX program adds values to such frameworks. — TZ*


## Institutional Movements
![Institutional Movements](media/institutional-movements.png)

### Stanford: $1M Seed Grants for AI + Education Research
**The need:** Most AI-in-education evidence is either too technical (model performance) or too anecdotal (observational data via survey). There's a gap in rigorous, pedagogy-centered research on how AI actually changes learning.

Stanford's AIMES initiative and the Accelerator for Learning announced **$1 million in seed grants** for course development and research. A notable design choice: the call explicitly welcomes proposals from faculty skeptical of AI, not just advocates. 

[Source: Stanford Report](https://news.stanford.edu/stories/2026/04/seed-grants-ai-education)

> 💬 **Editor's note:** *The "skeptics welcome" framing is worth highlighting. Inviting skeptical faculty to study AI's effects — not just implement AI tools — is how we build a research base that includes null results and failures, which are just as important as successes. — TZ*


### Columbia: Reimagining Teaching and Learning Forum
**The need:** Faculty experimenting with AI in their courses often work in isolation — there's no natural venue to see what colleagues across disciplines are trying, what's working, and what's failing.

Columbia's CTL hosted **"Reimagining Teaching and Learning in the Age of AI,"** built around a Demo Expo where faculty showcased live AI-enabled course projects. **Stakeholders** ranged from educational leadership to students and external experts. 

[Source: Columbia CTL](https://ctl.columbia.edu/about/2026-reimagining-teaching-learning/)

> 💬 **Editor's note:** *Events like this are where the most valuable learning happens — faculty seeing each other's experiments, not just hearing about AI in the abstract. I attended this forum and came away with several ideas I'm exploring in my own courses. aiX program organizes cohort-based collaborations — where faculty from different departments co-develop and evaluate AI-integrated assignments over a semester, a combination of faculty development and evidence-building. — TZ*


### Ohio State: AI Fluency Initiative Reaches Milestone
**The need:** Requiring "AI fluency" is easy to announce; defining what it means in 200+ majors across 15 colleges is the hard part.

Ohio State pushed roadmap development to the college level: **all colleges have now produced academic roadmaps** showing how undergraduates in every major will build AI skills. The three-pillar model — foundational understanding, disciplinary application, ethical/societal impact — provides a common structure while allowing disciplinary customization.

[Source: Ohio State Academic Affairs](https://oaa.osu.edu/ai-fluency)

> 💬 **Editor's note:** *The decentralized approach here — common framework, discipline-specific execution — mirrors how I have used to think about integrating data science literacy or quantitative reasoning across disciplines (at LEAP, DSI, through the collaboratory program and the aiX program, etc). — TZ*


### AAC&U: Institute on AI, Pedagogy, and the Curriculum (2026–27)
**The need:** Individual institutions redesigning pedagogy for AI in isolation risk reinventing the same wheels — rethinking assessment, navigating academic integrity, training faculty. A cross-institutional learning structure accelerates the work.

AAC&U's seven-month, team-based Institute reports having served **316 teams from 296 institutions** over two years. **Stakeholders:** campus teams typically include faculty, administrators, and instructional designers. 

[Source: AAC&U](https://www.aacu.org/event/2026-27-institute-ai-pedagogy-curriculum)

> 💬 **Editor's note:** *296 institutions working through the same set of problems together is an extraordinary resource for cross-institutional learning. If even a fraction of participating teams published case studies with outcome data, the field would have a much richer evidence base for AI pedagogy decisions. — TZ*


### China: National "AI + Education" Action Plan Through 2030
**The need:** Tech sector is advancing AI capabilities faster than the education system can produce people to build, govern, and critically evaluate them. 

China's Ministry of Education's April 2026 action plan mandates AI as a **basic public course in all universities**, requires new interdisciplinary AI majors, and embeds AI in teacher qualification exams. The plan integrates research universities, tech enterprises, and national labs. **Stakeholders:** MoE, university leadership, and industry partners in a state-coordinated model. 

[Source: S&T Daily](https://www.stdaily.com/web/English/2026-04/28/content_509054.html) | [Global Times](https://www.globaltimes.cn/page/202604/1358611.shtml)

> 💬 **Editor's note:** *The scale of this initiative is remarkable and worth watching closely. — TZ*


### IREX/Development Gateway: Global AI Readiness Survey
**The need:** Universities are adopting AI tools rapidly, but "adoption" and "readiness" are not the same thing. Institutions needed a benchmark to understand where they actually stand relative to peers.

This global survey (Nov 2025–Jan 2026) found that only **1 in 3 universities has a clear AI strategy**, fewer than 1 in 5 have governance structures, and only 37% of respondents reported receiving ongoing AI-related professional development. **Stakeholders:** university leadership, faculty, and IT administrators across multiple countries. 

[Source: IREX](https://www.irex.org/news/irex-and-development-gateway-release-higher-education-ai-readiness-research)

> 💬 **Editor's note:** *There are both a gap and an opportunity — the institutions that invest in sustained, discipline-specific AI training for faculty are likely to see meaningfully different outcomes. — TZ*


## What's in the News
![What's in the News](media/whats-in-the-news.png)

### NPR: Cal State's $17M OpenAI Deal Draws Faculty and Student Discussion
California State University — the largest public university system in the U.S. — signed a **$17 million contract** with OpenAI for ChatGPT Edu, then renewed for another $13M/year over three years. NPR reports that the rollout generated significant discussion among faculty and students. A survey of over 94,000 people found that majorities of both groups expressed skepticism about AI's educational benefits. The story has become a reference point in discussions about the sequencing of institutional AI decisions.

[Source: NPR](https://www.npr.org/2026/05/25/nx-s1-5772820/artificial-intelligence-education-technology-california-state-university) | [VPM](https://www.vpm.org/npr-news/npr-news/2026-05-25/california-schools-spend-millions-on-chatgpt-edu-amid-faculty-and-student-skepticism)

**Reception:** Widely shared across faculty networks. Some commentators drew parallels to previous large-scale ed-tech rollouts; others defended the move as necessary experimentation at scale. The discussion highlighted different views on whether AI adoption is primarily an infrastructure decision or a pedagogical one.

**What's interesting here:** The story surfaces a governance question many institutions are working through — how and when faculty and students are consulted in large-scale AI decisions. Different institutions are finding different answers.

> 💬 **Editor's note:** *The conversation about governance is important; equally important is designing these deployments so we actually learn something from them. — TZ*


### Inside Higher Ed: Writing Faculty Push for the Right to Refuse AI
The Composition and Communication Teachers of America (CCCC) **overwhelmingly approved a resolution** at its annual convention supporting faculty's right to opt out of using generative AI in the classroom. The resolution reflects deep concern among writing educators that AI undermines the cognitive process of drafting, revising, and thinking through prose — the very skills their courses are designed to develop.

[Source: Inside Higher Ed](https://www.insidehighered.com/news/tech-innovation/teaching-learning/2026/03/16/writing-faculty-push-right-refuse-ai)

**Reception:** The resolution prompted discussion across faculty networks. Supporters emphasized that writing pedagogy centers on the process of thinking, not the product. Others noted the tension with preparing students for AI-integrated workplaces. The conversation has become part of a broader discussion about disciplinary autonomy in AI adoption.

**What's interesting here:** The debate reflects different views of what writing courses are designed to develop — cognitive process vs. communication product. Both perspectives have merit, and the field is still developing shared language for navigating between them.

> 💬 **Editor's note:** *I respect the reasoning behind this resolution. In statistics, the process of working through a problem — trying approaches, hitting dead ends, debugging your logic — is where learning happens. The final answer is almost beside the point. I can see why writing faculty feel the same way about drafting. The challenge is that this framing applies differently across disciplines: in some fields, using AI to handle routine production so students can focus on higher-order analysis may actually serve learning goals. What we need are discipline-specific conversations about where the cognitive work lives in each curriculum. — TZ*


### Chronicle & Inside Higher Ed: Faculty Are Overwhelmed — and Not in a Good Way
A January 2026 national survey found that **78% of faculty say AI-driven cheating is on the rise**, but they are deeply split on what counts as cheating — just over half said following a detailed AI-generated outline is cheating; just under half said it's legitimate or they're unsure. Meanwhile, **95% say AI will increase students' overreliance** on tools over time. The data reflects a profession navigating significant uncertainty about definitions and expectations.

[Source: Inside Higher Ed](https://www.insidehighered.com/news/faculty-issues/teaching/2026/01/21/survey-faculty-say-ai-impactful-not-good-way) | [Chronicle of Higher Education](https://www.chronicle.com/newsletter/teaching/2026-01-22)

**What's interesting here:** The split on "what counts as cheating" may be the most telling finding. Shared definitions of legitimate AI use are still emerging — not just across institutions, but within departments. Faculty are making individual judgment calls, and students are navigating varied expectations. Developing shared norms, beyond formal policies, remains an open challenge.

> 💬 **Editor's note:** *The 50/50 split on whether an AI-generated outline counts as cheating is striking. If we don't resolve this among faculty instructors, it means students in the same department may face opposite rules depending on which section they enrolled in. In my own thinking about AI policy for my introduction to statistics course, the most productive way starts with the indended learning outcomes of an assignment, here's what a student could do with AI, which uses replace learning and which ones don't? — TZ*


### False Accusations: AI Detectors and the Students Caught in Between
Multiple evaluations have found that AI detection tools **struggle with accuracy, particularly on paraphrased AI content**, and a Stanford study found they disproportionately flag non-native English speakers, whose structured prose can resemble AI-generated text. Turnitin claims a false positive rate below 1%, but acknowledges the tool should not be sole evidence in academic integrity cases. A Palo Alto family filed a civil rights suit after a false accusation; a non-native English speaker sued Yale alleging discriminatory treatment. Institutions have varied widely in how they deploy these tools — thresholds, review processes, and appeals paths differ significantly. UK universities saw AI misconduct cases rise nearly 400% in three years, though the role of detection tool accuracy in that increase is debated.

[Source: SF Standard](https://sfstandard.com/2026/05/11/ai-detection-cheating-palo-alto/) | [Stanford EE](https://ee.stanford.edu/james-zou-et-al-warn-objectivity-ai-detectors) | [Strauss Troy](https://www.strausstroy.com/articles/ai-and-academic-integrity-a-growing-crisis)

**Reception:** The topic has generated sustained discussion across faculty networks and social media. Some educators have called for pausing AI detection tools until accuracy and bias are better understood. Students have shared personal accounts of false accusations. Legal scholars have noted the evolving liability landscape.

**What's interesting here:** The situation illustrates broader questions about deploying automated tools for high-stakes decisions before validation is complete. The disproportionate impact on non-native English speakers has drawn particular attention. Both research findings and legal proceedings are contributing to how institutions are re-evaluating their approaches.

> 💬 **Editor's note:** *As a statistician, the detection accuracy numbers are the heart of this story. Tools with documented accuracy limitations and bias against non-native speakers raise serious questions about their use in high-stakes decisions about students' academic standing. This is a classification problem for high-stake decisions with well-understood tradeoffs between false positives and false negatives, which require ethical principles and debates. — TZ*


### NYC Schools: Parents Demand AI Pause Ahead of Governance Framework
New York City's Department of Education has been developing AI guidance for its school system — allowing teachers to use AI for brainstorming and lesson planning, while restricting AI for grading, disciplinary decisions, or biometric data collection. Reports indicate that parents have raised concerns about AI deployment timing, calling for stronger governance frameworks before broader rollout.

[Source: chalkbeat](https://www.chalkbeat.org/newyork/2026/05/01/parents-demand-ai-moratorium-in-schools-during-marathon-panel-for-educational-policy-meeting/) 

**What's interesting here:** Parents are emerging as an active stakeholder group in AI governance discussions. In higher ed, a parallel may be developing as students and families form views on how AI is used in instruction. The "pause until governance is ready" position reflects a sequencing question many institutions are navigating.

> 💬 **Editor's note:** *Governance first or adoption first? There's not a single right answer. AI is developing quickly. There is need for piloting AI tools in contained settings while governance frameworks are being developed. Either full deployment or full pause seems right. — TZ*


## Most Discussed
![Most Discussed](media/most-discussed.png)

### Stanford HAI 2026 AI Index: Education Chapter
The report finds that **four out of five U.S. high school and college students use AI for schoolwork**, and that master's graduates in AI-related fields rose 17% from 2023–2024. The report also examines how students are using AI, including for content creation and analysis — activities traditionally used to measure learning.

**Why it caught attention:** The scale. This is among the most comprehensive datasets on AI adoption in education, and the "four out of five" figure shifts the conversation from whether students use AI to how they use it. **Who's paying attention:** administrators referencing it for strategic planning, faculty citing it in assessment redesign discussions, and ed-tech companies noting market growth. **What it suggests:** adoption has moved quickly, and the question of whether institutions can redesign learning to match — so that students creating content with AI are still developing the skills that content creation was designed to teach — is becoming central.

[Source: Stanford HAI AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report/education)

> 💬 **Editor's note:** *The "four out of five" adoption number is interesting. However, as AI gets more uses in learning, it is important to further differenting use cases. "Using AI for schoolwork" covers everything from asking ChatGPT to explain a concept (probably fine) to having it write an essay (probably not fine, depending on the assignment). The question isn't whether to allow AI; it's whether our assessments still measure what we think they measure for the learners. — TZ*


### The 90% Faculty Concern
National survey data showing **90% of faculty believe AI will decrease students' critical thinking** is driving vigorous debate. An MIT study finding that brain activity was suppressed during AI-assisted essay writing (without proper guidance) has become a widely cited data point.

**Why it caught attention:** The near-unanimity — 90% agreement among faculty on any topic is notable, and the number has become a reference point in discussions about AI's cognitive impact. **Who's paying attention:** faculty across disciplines, administrators, and researchers examining survey methodology. **What it suggests:** the MIT study adds nuance — brain activity was suppressed *without proper guidance*, suggesting that pedagogical design may moderate the effect. The 90% figure captures a widespread concern; the accompanying research points toward possible design responses.

[Source: UW Arts & Sciences](https://artsci.washington.edu/news/2026-01/ai-classroom-faculty-its-complicated) | [EdWeek](https://www.edweek.org/technology/opinion-ai-is-different-from-other-ed-tech-heres-how/2026/02)

**Reception:** The 90% figure has been cited both as an important signal and questioned as a function of how the survey was framed. Some argue the real variable is assignment design, not AI itself. Others point to the MIT brain-activity data as evidence worth taking seriously. The conversation continues to evolve.

> 💬 **Editor's note:** *The MIT finding is where the actionable insight lives: brain activity was suppressed without proper guidance. It suggests the variable we can control is pedagogical design, not AI access. — TZ*

### OECD Digital Education Outlook 2026
The OECD report examines how GenAI tools interact with teaching expertise. Among its findings: GenAI may help **amplify teachers' capacity when integrated with their expertise**, with suggestive evidence that less experienced tutors can benefit from AI support. 

**Why it caught attention:** It offers a nuanced framing: AI may raise the floor for less experienced educators without diminishing the effectiveness of strong ones — though the specific evidence base for this claim warrants closer reading of the full report. **Who's paying attention:** policymakers and institutional leaders interested in evidence beyond efficiency gains, and faculty development directors exploring how training and AI tools interact. **What it suggests:** the interaction between expertise and AI may be more important than AI alone. The finding is consistent with investing in pedagogical expertise first, then exploring how AI tools complement it.

[Source: OECD](https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html)


## Interesting Ideas & Repos
![Interesting Ideas & Repos](media/interesting-ideas.png)

### AI-First Curriculum Design
**Why it's interesting:** Most institutions are bolting AI onto existing courses as an afterthought. This Faculty Focus piece articulates what it looks like to design courses with AI as a foundational assumption — AI handles repetitive mechanics (grammar feedback, rubric alignment) while faculty focus on mentoring and critical dialogue. The shift from "AI-permitted" to "AI-first" is a meaningful design philosophy change worth watching as it develops.

[Source: Faculty Focus](https://www.facultyfocus.com/articles/teaching-with-technology-articles/designing-the-2026-classroom-emerging-learning-trends-in-an-ai-powered-education-system/)


### Microsoft: Generative AI for Beginners (GitHub)
**Why it's interesting:** A 21-lesson open course covering prompt engineering through RAG pipelines, agents, and deployment. It's beginner-friendly but technically substantive — the sweet spot for faculty who want to understand what their students are actually doing with AI tools, not just read about it. Could serve as the backbone of a faculty development workshop series, and the open license means you can adapt it.

[Repository: microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)


### LLMs-from-Scratch
**Why it's interesting:** Builds a GPT-style model from scratch in PyTorch. In a research training context, this is uniquely valuable — it replaces the "magic black box" understanding of AI with mechanical comprehension. Faculty and graduate students who work through this will be better equipped to critically evaluate AI outputs because they understand what the model is actually doing. Pairs well with the cognitive offloading research above: deeper understanding may build the self-confidence that protects against uncritical AI dependence.

[Repository: rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)


### Open-Source AI Tutor with Spaced Repetition
**Why it's interesting:** The growing ecosystem of open-source AI tutors exploring spaced repetition, personalized examples, and adaptive pacing. What makes the space worth watching is the design pattern — learning tools that adjust to individual pace rather than delivering uniform content. For anyone designing AI-augmented learning experiences, browsing active projects in this space is more productive than starting from scratch.

[Browse: github.com/topics/ai-tutor](https://github.com/topics/ai-tutor) *(Topic page — browse for specific projects of interest.)*


### PhD Research Tool Stacks for 2026
**Why it's interesting:** Several AI research tools are gaining traction among graduate students, including **Elicit** (systematic literature search), **Consensus AI** (evidence-based answers from peer-reviewed research), and **NotebookLM** (synthesis and note-taking). This matters for research training because the tools students choose shape the research they produce — and most doctoral programs aren't teaching tool selection as a methodological skill. The key caveat: AI accelerates literature discovery but cannot replace manual verification. Programs that teach the stack without teaching verification are training speed without rigor.

[Source: Thesify (blog)](https://www.thesify.ai/blog/best-ai-tools-academic-research) *(Note: vendor/blog source — verify specific tool claims against the tools' own documentation.)*

## What Changed

*This section tracks what's notable this week in the context of the broader timeline. Future issues will note when earlier stories develop, when sources are corrected, or when our framing needs revisiting.*

This week's stories connect to several threads on the [aiX Timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}):

- **The evidence base is growing.** The cognitive offloading and FALCON-AI studies join a building body of research that started arriving in earnest in early 2025. Most findings remain correlational — the field is still waiting for experimental and longitudinal designs.
- **Governance questions are becoming concrete.** Cal State's contract discussion and the CCCC resolution move governance from abstract principle to specific institutional decisions. The IREX benchmark (1 in 3 with a clear strategy) provides a reference point.
- **Detection remains unsettled.** The accuracy and bias concerns around AI detectors continue to develop, now with legal proceedings adding a new dimension to what began as a validation question in 2023.
- **International approaches are diverging.** China's nationwide mandate and the OECD's expertise-interaction finding offer two very different data points for institutions considering their own directions.

## Try This Week

**Audit one assignment for AI vulnerability.** Pick a single assignment from your current or upcoming course. Ask yourself: could a student complete this entirely — and competently — using ChatGPT or Claude? If the answer is yes, consider whether the assignment is measuring something AI can already do. Try redesigning it to include something AI can't provide: a personal observation, a judgment call grounded in disciplinary experience, a connection to class discussion, or an original dataset. The goal isn't to make the assignment "AI-proof" — it's to make it worth doing even if AI exists.

---

*Curated by Claude for the aiX Programs, Columbia University. AI can make mistakes and so is the human reviewer. Please double-check the linked sources.*
