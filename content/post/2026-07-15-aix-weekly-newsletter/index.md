---
title: "aiX Weekly — AI in Higher Education (July 15th, 2026)"
date: 2026-07-15
draft: false
image:
  focal_point: 'top'
authors:
  - admin
tags:
  - AI
  - aiX
---
This issue examines the widening gap between near-universal AI adoption and institutional readiness — from Microsoft and Gallup survey data to the platform competition at ISTE 2026 — and closes with a recap of June 2026.

<!--more-->

Each issue is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the aiX Programs, Columbia University. AI can make mistakes and so is the human reviewer. Please double-check the linked sources.*

**Reviewed by Tian Zheng on July 15th, 2026.**

---

## TL;DR

- **Microsoft's 2026 AI in Education Report finds 92% of students use AI for school — but 77% have received no formal training** ([Research Highlights](#research-highlights))
- **Nearly half of college students have considered switching majors over AI career concerns** — the Lumina-Gallup study documents workforce anxiety reshaping enrollment in real time ([Institutional Movements](#institutional-movements))
- **Google and Microsoft both launched major AI education tool suites at ISTE 2026** — the platform competition for classroom AI is now explicit ([What's in the News](#whats-in-the-news))
- **Frontier AI models now score ~30 points above human PhD experts on graduate-level science benchmarks** ([Most Discussed](#most-discussed))

---

## Table of Contents

- [This Week at a Glance](#this-week-at-a-glance)
- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [What's in the News](#whats-in-the-news)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [What Changed](#what-changed)
- [Monthly Recap: June 2026](#monthly-recap-june-2026)
- [Try This Week](#try-this-week)

---

## This Week at a Glance

This week's through-line is the gap between adoption velocity and institutional readiness. Microsoft and Gallup data both confirm near-universal AI use in higher education, but training, policy, and assessment redesign lag far behind. ISTE 2026 saw Google and Microsoft competing to define the AI classroom platform — a vendor landscape institutions will need to navigate carefully.

**Relevant to faculty:** The UK HEPI study finding that most university AI policies "promise support but deliver surveillance" may resonate beyond British universities.

**Relevant to institutional leaders:** The Lumina-Gallup major-switching data (47% considering, 16% already switched) signals enrollment pattern shifts worth planning for.

**Relevant to students and researchers:** GPQA Diamond saturation — AI models scoring 30 points above PhD experts — raises questions about what knowledge assessments measure.

---

## Research Highlights
![Research Highlights](media/research-highlights.png)

### 1. Microsoft 2026 AI in Education Report: Universal Adoption, Minimal Training
**[Microsoft's New AI in Education Report](https://news.microsoft.com/source/2026/06/24/microsofts-new-ai-in-education-report-highlights-widespread-adoption-and-increasing-demand-for-support/)**

Microsoft's third annual report surveyed 3,345 respondents across K-12 and higher education in six countries, released at ISTELive 2026. The headline finding: 92% of students and 88% of educators report using AI for school-related purposes, but 77% of students and 53% of educators have received no formal AI training. Two-thirds of educators want monthly or quarterly training. *(Industry-commissioned survey — sampling methodology and definition of "using AI" deserve scrutiny.)*

`Industry-commissioned survey · n=3,345 · Six countries · Directional evidence`

> 💬 **Editor's note:** *The 77% no-training figure is the number to sit with. We've moved past whether students use AI. The question is whether institutions will treat AI competency as something that develops by osmosis or something requiring intentional instruction. — TZ*

---

### 2. Digital Education Council LATAM Survey: 30,000 Responses Across 29 Institutions
**[AI in Higher Education LATAM Survey 2026](https://www.digitaleducationcouncil.com/post/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026)**

Surveying over 30,000 respondents (22,941 students, 7,319 faculty) across 29 Latin American institutions, the study found 92% of students and 79% of faculty actively engage with AI. Notably, 65% of students worry AI may make learning "too shallow" — mirroring RAND's US findings from Issue #2 in a completely different cultural and linguistic context. A 31-point gap emerged between students wanting AI-assisted feedback (50%) and faculty providing it (19%).

`Large-scale survey · n=30,260 · 29 institutions · Strong sample, convenience sampling`

> 💬 **Editor's note:** *When students in both the US and Latin America independently voice the same worry about AI and cognitive engagement, that's a signal worth taking seriously. The feedback gap — students want more AI feedback than faculty provide — suggests a concrete opportunity for experimentation. — TZ*

---

### 3. HEPI Policy Note: What UK University AI Policies Actually Do
**[What UK University AI Policies Actually Do: A Study of 96 Institutions](https://www.hepi.ac.uk/reports/what-uk-university-ai-policies-actually-do-a-study-of-96-institutions/)**

Professor Sam Illingworth computationally analyzed AI policies of 96 UK degree-awarding institutions — 41% had no publicly accessible AI policy at all. Of those that did, 86% appeared education-focused by keyword count, but close reading of a subset found nearly half were actually detection-and-discipline frameworks using educational language as a veneer. Full data and coding framework available on [GitHub](https://github.com/sam-illingworth/uk-university-ai-policies).

`Policy analysis · n=96 institutions · Innovative methodology`

> 💬 **Editor's note:** *"Promise support but deliver surveillance" is recognizable beyond the UK. The open dataset on GitHub makes this replicable — someone should do this analysis for US research universities. The aiX Fellowship community is well positioned to attempt it. — TZ*

---

## Institutional Movements
![Institutional Movements](media/institutional-movements.png)

### 1. Lumina-Gallup: 47% of Students Have Considered Switching Majors Due to AI
**[College Students Weigh AI's Impact on Majors and Careers (Gallup)](https://news.gallup.com/poll/704087/college-students-weigh-impact-majors-careers.aspx)**

The Lumina Foundation-Gallup 2026 study surveyed 6,010 US adults including 3,801 enrolled students. Nearly half (47%) have given serious consideration to switching majors because of AI, and 16% have already done so. Technology (70%) and vocational fields (71%) show the highest consideration rates. Male students (60%) are more likely to consider changes than female students (38%).

**Open question:** Whether major-switching based on AI workforce perceptions actually predicts better career outcomes, or whether students are moving to fields that may also face AI exposure.

> 💬 **Editor's note:** *The 57% weekly AI use combined with 53% of students saying their institution discourages or prohibits AI creates a notable disconnect. Students are using the technology daily while institutions officially frown on it — a gap worth addressing proactively. — TZ*

---

### 2. University of Surrey: AI Embedded in Every Degree from September 2026
**[AI to Be Embedded in Every University of Surrey Degree](https://www.surrey.ac.uk/news/ai-be-embedded-discipline-specific-ways-every-university-surrey-degree-september-2026-training)**

Surrey has undertaken a systematic redesign of every degree program to embed discipline-specific AI teaching, shifting assessment toward process over outputs. English literature students, for example, will submit annotated close-reading extracts alongside essays. The approach applies to current students, not just incoming ones — a level of institutional commitment few universities have executed.

**Open question:** Whether Surrey has the faculty development infrastructure to support process-based assessment across all departments, and whether students perceive the change as meaningful.

> 💬 **Editor's note:** *The assessment shift — from evaluating what students produce to evaluating how they produce it — may be the most consequential decision here. It's also the most labor-intensive for faculty. Surrey's real test will be whether it provides sufficient support for implementation. — TZ*

---

### 3. FutureEd: 71 AI Education Bills Across 27 States
**[Legislative Tracker: 2026 State AI in Education Bills (FutureEd)](https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/)**

FutureEd's 2026 tracker now monitors 71 bills across 27 states addressing AI in classroom instruction, up from 52 bills earlier in the session. Approaches range from AI literacy graduation requirements (Hawaii) to written parental opt-in consent (South Carolina) to district-level AI policies before 2027-28 (Oklahoma). The patchwork creates compliance complexity for multi-state institutions.

**Open question:** Which bills actually pass and how implementation unfolds — legislative intent and classroom reality often diverge significantly.

> 💬 **Editor's note:** *Whatever states decide for K-12 today shapes what universities receive tomorrow. Higher ed leaders in states with active legislation may want to monitor these bills, as the downstream effects on incoming student AI literacy are direct. — TZ*

---

## What's in the News
![What's in the News](media/whats-in-the-news.png)

### 1. Google Unveils Connected AI Tools for Classrooms at ISTE 2026
**[Building AI Tailored for Education, with Educators in the Lead (Google Blog)](https://blog.google/products-and-platforms/products/education/iste-2026-educator-updates/)**

Google announced a major expansion of AI tools across Google Classroom, Chromebooks, and Gemini at ISTE 2026 — a Classroom app in Gemini, "study notebooks" for personalized learning, and teacher-led AI activities grounded in school curricula. Google also announced funding for aiEDU to support Title I districts.

**What's interesting here:** The competition between Google and Microsoft to define the classroom AI platform is now explicit, creating both opportunity (free tools) and risk (vendor lock-in, data dependencies) for institutions.

> 💬 **Editor's note:** *"With educators in the lead" is the tagline, but product design choices determine how much leading educators actually get to do. Faculty should test these tools with an eye toward which pedagogical decisions the platform has made for them. — TZ*

---

### 2. Microsoft Releases Third Annual AI in Education Report at ISTE
**[Microsoft's New AI in Education Report (Microsoft Source)](https://news.microsoft.com/source/2026/06/24/microsofts-new-ai-in-education-report-highlights-widespread-adoption-and-increasing-demand-for-support/)**

Alongside the survey data (covered in Research Highlights), Microsoft announced new AI features in Microsoft 365 Education at no additional cost: AI-assisted Unit Plans, Student AI Guidelines in Assignments, and a no-cost AI Literacy for Educators credential pathway.

**What's interesting here:** Both Google and Microsoft launched at ISTE simultaneously, signaling this is now a market-share battle, not just a product launch cycle. The "no additional cost" framing was strategic positioning.

> 💬 **Editor's note:** *The free credential pathway is worth watching. If Microsoft successfully positions AI Literacy for Educators as a recognized credential, it shapes the definition of AI literacy itself — around Microsoft's tools and framing. Who defines AI literacy in education is a substantive question. — TZ*

---

### 3. Gallup Data: Students Use AI Weekly, Institutions Discourage It
**[AI Is Routine for College Students, Despite Campus Limits (Gallup)](https://news.gallup.com/poll/704090/routine-college-students-despite-campus-limits.aspx)**

The Lumina-Gallup study found 57% of students use AI weekly, with 20% using it daily — while 53% say their institution discourages (42%) or prohibits (11%) AI. Only 7% say AI use is freely encouraged. Additionally, 29% say their school isn't adequately preparing them to use AI after graduation.

**What's interesting here:** The prohibition-versus-reality gap has moved from anecdote to data. The 42% "discourage" figure suggests many institutions occupy an uncomfortable middle ground — not banning AI, but not supporting it either.

> 💬 **Editor's note:** *The 29% who feel their institution isn't preparing them for AI is the number administrators should note. Students are increasingly viewing AI preparation as part of what they're paying for — and eventually an enrollment question. — TZ*

---

### 4. Times Higher Education: University AI Policies "Promise Support but Deliver Surveillance"
**[University AI Policies 'Promise Support but Deliver Surveillance' (THE)](https://www.timeshighereducation.com/news/university-ai-policies-promise-support-deliver-surveillance)**

THE's coverage of the HEPI study (detailed in Research Highlights) emphasized the gap between policy rhetoric and policy function. Faculty shared it widely, many adding "this is us" commentary. University communications teams largely stayed silent — the finding is difficult to rebut without substantively redesigning policies.

**What's interesting here:** There's growing recognition that the first generation of university AI policies — written quickly under pressure — may need wholesale revision, either proactively or under regulatory pressure.

> 💬 **Editor's note:** *The study's open dataset on GitHub is an underappreciated resource. Any institution can compare its own AI policy against the coding framework. This is the rare study that provides both the diagnosis and the diagnostic tool. — TZ*

---

## Most Discussed
![Most Discussed](media/most-discussed.png)

### 1. GPQA Diamond Saturation: AI Models Now 30 Points Above Human PhD Experts
**[GPQA Diamond Benchmark Leaderboard (Artificial Analysis)](https://artificialanalysis.ai/evaluations/gpqa-diamond)**

Seven frontier AI models now score between 93.2% and 94.6% on GPQA Diamond — a graduate-level science benchmark where human PhD experts average approximately 65%. The benchmark is widely considered saturated, with top-model differences falling within measurement noise. *(Previously covered in Issue #2 — August AI's 100% USMLE score raised similar questions about professional exam benchmarks.)*

> 💬 **Editor's note:** *The 37% gap between lab benchmark scores and real-world deployment performance is an essential counterpoint. But faculty should sit with the data: if exam performance can be replicated by a token-processing system, what is the exam actually testing? — TZ*

---

### 2. Anthropic's 2026 Agentic Coding Trends Report
**[2026 Agentic Coding Trends Report (Anthropic)](https://resources.anthropic.com/2026-agentic-coding-trends-report)**

Anthropic's report documents the shift from AI as coding assistant to autonomous agent team, arguing 2026 marks the transition where engineers move from writing code to orchestrating systems that write it. Developers use AI in ~60% of work but can "fully delegate" only 0-20% of tasks. Non-technical roles — product managers, designers, marketers — are also adopting coding agents.

> 💬 **Editor's note:** *The expansion to non-technical roles is the underreported finding. When product managers use coding agents to build prototypes, the boundary between "technical" and "non-technical" work blurs. Programming exposure may need to extend beyond CS departments. — TZ*

---

### 3. Early-Career Employment Decline in AI-Exposed Occupations
**[Software Developer Employment for Ages 22-25 Falls Nearly 20% Since 2022](https://frontierwisdom.com/ai-impact-on-software-engineer-jobs-2026/)**

Employment data shows that early-career workers in AI-exposed occupations — software development, clerical work, content creation — have experienced 16% relative employment declines since 2022, while employment for experienced workers remains stable. NBER projects approximately 502,000 AI-related job cuts in 2026, roughly 9x the estimated 55,000 in 2025. *(Previously covered in Issue #2 — "experience creep" debate.)*

> 💬 **Editor's note:** *The aggregate labor market is stable (3M jobs added); the composition is shifting. That distinction matters for career advising — not dismissing the data, not catastrophizing, but contextualizing. — TZ*

---

## Interesting Ideas & Repos
![Interesting Ideas & Repos](media/interesting-ideas.png)

### 1. DeepTutor: Agent-Native Personalized Tutoring Platform
**[DeepTutor (GitHub)](https://github.com/HKUDS/DeepTutor)**

An open-source, agent-native learning workspace from HKU connecting tutoring, problem-solving, quiz generation, and research. Features EduHub, a community hub for sharing teaching-oriented agent skills — Socratic tutors, flashcard builders, essay feedback, exam blueprints.

> 💬 **Editor's note:** *The EduHub sharing model is the standout — faculty can build, share, and iterate on tutoring agents within their disciplinary community. Worth exploring for any department considering AI tutoring. — TZ*

---

### 2. AI Engineering from Scratch: 503 Lessons, 320 Hours
**[AI Engineering from Scratch (GitHub)](https://github.com/rohitg00/ai-engineering-from-scratch)**

A comprehensive open-source curriculum covering 20 phases from fundamentals to advanced AI engineering, with 503 lessons across ~320 hours. The repository has attracted 55,593 monthly visitors and 7.5K stars, suggesting significant community adoption.

> 💬 **Editor's note:** *The full 320-hour scope is daunting. For faculty development, curating a "greatest hits" subset of 20-30 hours focused on understanding AI systems (not building them) might be more practical. — TZ*

---

### 3. LearnHouse: Open-Source Learning Platform with AI Integration
**[LearnHouse (GitHub)](https://github.com/learnhouse/learnhouse)**

A next-generation open-source learning platform featuring a block-based content editor, AI-generated interactive elements, code execution with auto-grading in 30+ languages, collaborative whiteboards, and context-aware AI for learning and teaching. An open-source alternative to proprietary LMS platforms.

> 💬 **Editor's note:** *The "context-aware AI" feature — where the AI understands course content and student progress — addresses a key limitation of general-purpose AI in education. Whether it improves learning outcomes is an open empirical question. — TZ*

---

## What Changed

- **The adoption-training gap is now quantified across multiple countries.** Microsoft (77% no training), LATAM (similar patterns), and Gallup (53% discouraged) all independently document the same readiness gap from Issues #1 and #2.
- **Entry-level employment data hardens.** NBER's 502,000 projected AI-related job cuts (9x 2025) adds specificity to the "experience creep" narrative from Issue #2.
- **AI detection policy scrutiny deepens.** The HEPI finding that university AI policies often function as detection-and-discipline frameworks extends the detection controversy from Issues #1 and #2 into institutional policy design.
- **Professional exam benchmarks continue saturating.** GPQA Diamond data extends Issue #2's USMLE milestone — frontier models now exceed PhD experts by ~29 percentage points.

No corrections this week.

---

## Monthly Recap: June 2026

### Key Themes

June was defined by three intersecting developments: hard data on AI's learning impact, acceleration of institutional policy responses, and growing evidence of workforce disruption affecting students.

### Most Significant Developments

1. **Grade-and-learning research convergence** — Three independent studies (Berkeley, Chinese longitudinal, EDUCAUSE) all documented higher grades alongside lower demonstrated learning — moving the conversation from anecdote to multi-source evidence.
2. **SUNY's systemwide AI policy** — The first system-level mandate across 64 campuses, requiring AI literacy in general education for Fall 2026.
3. **Lumina-Gallup workforce anxiety data** — 47% of students considering major switches and 16% already changed fields — first quantified evidence of AI reshaping enrollment patterns.
4. **ISTE 2026 platform competition** — Google and Microsoft both launched comprehensive AI education tools in the same week.
5. **HEPI's policy analysis** — Systematic documentation that university AI policies often prioritize detection over education, with open data enabling replication.

### Looking Ahead to July

- EU AI Act high-risk provisions approach August 2026 enforcement
- UK OfS/Advance HE survey closes July 10
- SUNY implementation approaches Fall 2026 deadline
- Q2 2026 workforce data will begin emerging

---

## Try This Week

### AI Policy Audit: Is Your Syllabus Statement Educating or Surveilling?

Inspired by the HEPI study, try a simplified version of its analysis on your own AI syllabus statement. **Time:** 15-20 minutes.

1. Pull up your current AI syllabus statement (or department policy). If you don't have one, that's data too.
2. Count how many sentences describe: (a) what students should *learn* about AI, (b) how students are *allowed to use* AI, (c) consequences for *misuse*.
3. Calculate the ratio. The HEPI study found nearly half of educational-sounding policies were actually detection-and-discipline frameworks.
4. Draft one sentence describing an AI learning outcome for your course — something students should be able to do *with* AI by the end of the term.

**Share with the aiX community:** Post your ratio and drafted learning outcome to the aiX Fellowship discussion channel.

---

*aiX Weekly is produced for the aiX Faculty Fellowship at Columbia University. Stories and analysis reflect developments in AI and higher education; editorial notes represent analytical commentary, not institutional positions. All links were verified at time of publication. For corrections or suggestions, contact the aiX Fellowship team.*
