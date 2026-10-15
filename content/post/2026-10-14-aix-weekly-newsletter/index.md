---
title: "aiX Weekly — AI in Higher Education (October 14th, 2026)"
date: 2026-10-14
draft: false
authors:
  - admin
tags:
  - AI
  - aiX
image:
  focal_point: 'top'
---

Almost every institution now agrees that decisions and actions about AI in Education belongs inside the disciplines. The harder question is what each discipline needs from it, and what each needs to protect from it.

<!--more-->

A writing program worries about whether students still think on the page. A statistics course worries about whether students can still judge an analysis they did not build by hand. A medical school worries about accountability for a clinical judgment. A law school worries about fabricated citations and professional responsibility. A social-science core worries about independent thought and face-to-face argument. Different needs lead to different answers in the same university.

**From My Desk** closes with a question about how change happens at all: why permission to try is easier to get than agreement, and why small circles of practice matter.

---

Each [aiX Weekly]({{< relref "/tags/aiX/" >}}) post is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the [aiX Programs, Columbia University](https://www.linkedin.com/company/aix-programs-columbia-university/). AI can make mistakes and so can the human reviewer. Please double-check the linked sources.*

**Review by Tian Zheng on October 14th, 2026**

---

![TL;DR](media/tldr.png)

## TL;DR {#tldr}

- **Each discipline is protecting a different core practice.**  The social-science core at one university protects independent thought and discussion, enough to ban AI from it ([Chronicle](https://www.chronicle.com/article/u-of-chicagos-social-sciences-division-bans-tech-ai-in-core-courses)) while the same university's law school builds AI into electives ([UChicago Law](https://www.law.uchicago.edu/news/ai-advances-law-school-curriculum)).
- **Professional bodies are setting discipline-level expectations.** The AAMC's seven principles keep "human judgment" central in medical education ([AAMC, v2.0 July 2025](https://aamc.org/about-us/mission-areas/medical-education/principles-ai-use)). The ASA is planning a white paper on statistics curriculum for the AI era ([Amstat News, July 2026](https://magazine.amstat.org/blog/2026/07/01/presjuly/)). Lawyers already have an ethics opinion on generative AI ([ABA Formal Opinion 512](https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools)).
- **Course designs follow the discipline's need.** An AI tutor in premodern Japanese "asks guiding questions instead of giving translations." Chemical-engineering students keep "prompt journals" recording how they checked AI output ([Stanford CTL](https://ctl.stanford.edu/news/ai-education-grants-2026)). Mechanical-engineering students tutor a deliberately error-prone AI ([CMU](https://www.cmu.edu/news/stories/archives/2026/august/navigating-the-ai-era-with-a-cmu-focus-on-critical-thinking)).
---

![Table of Contents](media/toc.png)

## Table of Contents

- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [From My Desk](#from-my-desk)
- [Try This Week](#try-this-week)

---

![Research Highlights](media/research.png)

## Research Highlights

*Claude's note on the evidence: the course-level evidence is reasonably good, the curriculum-level evidence is thin, and comparative evidence across disciplines is nearly absent.*

**1. A meta-analysis of ChatGPT's effect on learning, and a retraction beside it** — *[Humanities and Social Sciences Communications](https://www.nature.com/articles/s41599-026-07019-z), published March 26, 2026.*

*Evidence: systematic review and meta-analysis of 35 experimental and quasi-experimental studies (4,193 students).*

The review reports a moderate overall positive effect of ChatGPT on learning (Hedges' g ≈ 0.67), with larger effects on cognitive outcomes such as critical thinking and problem-solving. It pools across subjects and education levels and draws mostly on short interventions.

**2. Randomized studies: design, not access, is the moderator** 

*Evidence: randomized and quasi-randomized trials, each in a single course or tool.*

- **Physics: an AI tutor.** A Harvard randomized crossover trial found a well-designed AI tutor outperformed in-class active learning on post-tests, in less time, with an effect of about 0.6 SD. The authors caution it may not generalize to tasks requiring complex synthesis ([Kestin et al., *Scientific Reports*, June 2025](https://www.nature.com/articles/s41598-025-97652-6)).
- **Mathematics: guardrails matter.** Students with *unguarded* GPT-4 did better during practice but about 17% **worse** on later unaided exams, while a guardrailed "tutor" version erased the harm ([Bastani et al.](https://hamsabastani.github.io/education_llm.pdf); covered in the August 12 issue).
- **Retention: a "cognitive crutch."** A ChatGPT-aided group scored lower on a surprise retention test 45 days later (57.5% vs. 68.5%, d ≈ 0.68) ([Barcaui, 2025](https://scale.stanford.edu/ai/repository/chatgpt-cognitive-crutch-evidence-randomized-controlled-trial-knowledge-retention)).
- **Tutoring: augmenting the human.** Stanford's Tutor CoPilot, an AI that assists *human* tutors, raised student topic mastery by about 4 points, with the largest gains for students of the lowest-rated tutors ([Tutor CoPilot](https://edworkingpapers.com/ai24-1054)).

> *Editor's note:* The consistent signal is that augmentation with guardrails and a human in the loop helps, while automating the cognitive work can quietly risk retention. — TZ

**3. Assessment and integrity in the generative-AI era** — *[AI and Ethics](https://link.springer.com/article/10.1007/s43681-025-00871-w), December 2025.* 

*Evidence: PRISMA systematic review of 56 studies.*

The review shows that work cannot be reliably attributed to student or AI, detection tools produce both false positives and false negatives, fairness concerns when students have unequal AI access, and the absence of clear institutional policy. Its recommended direction is process-based, higher-order, oral, and multi-stage assessment. What that looks like differs by field: an oral defense of an analysis in statistics, a drafting portfolio in writing, an observed clinical encounter in medicine.

**4. What is "AI literacy," and can it be measured?** — *[Gu & Ericson, arXiv preprint](https://arxiv.org/pdf/2503.00079), 2025.* 

*Evidence: integrative literature review; preprint.*

The review makes an uncomfortable point plainly: "AI literacy" is an umbrella term covering dissimilar but equally valid interpretations, which undermines measurement. Post-secondary intervention research is scarce, since most higher-education efforts are curricula or assessments that were never empirically tested.

---

![Institutional Movements](media/movements.png)

## Institutional Movements

This week the section is organized by discipline rather than by institution. For each field: what it needs to protect, what guidance exists, and what courses are trying.

**1. Statistics and data science: judgment about data and uncertainty.**

- *Need:* Students must still be able to judge an analysis: whether the data support it, whether the assumptions hold, and how uncertain the answer is, even when AI wrote the code.
- *Guidance:* A July 2026 ASA President's column describes a draft objective to produce a white paper on statistics curriculum for the AI era by JSM 2027. It argues that machine learning should be taught through a statistical lens, with attention to generalization, uncertainty, and assumptions ([Amstat News](https://magazine.amstat.org/blog/2026/07/01/presjuly/)). In 2025 policy comments, the ASA urged that statistics be a core pillar of AI literacy ([ASA](https://www.amstat.org/docs/default-source/amstat-documents/pol-ai_literacy-american_statistical_association.pdf)).
- *In practice:* Stanford's AIMES grants fund an integrated redesign of four introductory **Statistics** courses (Schramm, Fan, Sun, Palacios, and Taylor) that will *test which interventions improve learning and share the assessment methods* ([Stanford CTL](https://ctl.stanford.edu/news/ai-education-grants-2026)). Harvard Business School restructured its required first-year analytics course around AI ([Crimson](https://www.thecrimson.com/article/2026/4/11/hbs-ai-integration/)).

**2. Writing and the humanities: thinking on the page.**

- *Need:* In writing courses, drafting *is* the thinking. The worry is not that AI writes badly but that students skip the part that teaches them.
- *Guidance:* The MLA-CCCC Joint Task Force on Writing and AI has issued a series of working papers, starting with principles and recommendations in July 2023 and continuing with policy development and "building a culture for generative AI literacy" in language, literature, and writing ([MLA-CCCC](https://aiandwriting.hcommons.org/working-papers/)).
- *In practice:* Harvard made an AI module **required for all first-year students in Expository Writing** this spring, reaching the more than 90% of students who take Expos. It covers how LLMs work, AI's effects on learning, and environmental and privacy questions ([Harvard Crimson](https://www.thecrimson.com/article/2026/4/23/expository-writing-ai/)).

**3. Languages: the work of translation.**

- *Need:* Language learning depends on the effort of working out meaning. A tool that simply translates removes the exercise.
- *In practice:* A Stanford AIMES project built a premodern-Japanese AI tutor that "asks guiding questions instead of giving translations" ([Stanford CTL](https://ctl.stanford.edu/news/ai-education-grants-2026)). The design choice states the discipline's need directly.

**4. Engineering: verification.**

- *Need:* Engineers are responsible for whether a design works. The core skill is checking, not generating.
- *In practice:* Stanford chemical-engineering students keep "prompt journals" documenting how they checked AI output ([Stanford CTL](https://ctl.stanford.edu/news/ai-education-grants-2026)). In Carnegie Mellon's GAITAR program, mechanical-engineering students tutored a deliberately error-making AI and significantly outperformed the prior semester in three of four concept areas, one of the few *measured* outcomes in this issue ([CMU](https://www.cmu.edu/news/stories/archives/2026/august/navigating-the-ai-era-with-a-cmu-focus-on-critical-thinking)). Dartmouth's Thayer School added new AI tracks ([Dartmouth](https://home.dartmouth.edu/news/2026/03/dartmouth-launches-new-courses-artificial-intelligence)).

**5. Medicine and health: accountable clinical judgment.**

- *Need:* A clinician is accountable for a decision about a patient. AI can inform that decision but cannot hold the responsibility.
- *Guidance:* The AAMC's seven principles for AI in medical education start with "Maintain Human-Centered Focus," stating that "human judgment remains essential in determining the appropriate use and implementation of these tools." The others cover ethical and transparent use, equal access, faculty development, interdisciplinary curriculum, data privacy, and monitoring and evaluation ([AAMC, v2.0, July 2025](https://aamc.org/about-us/mission-areas/medical-education/principles-ai-use)). 
- *In practice:* Dartmouth's Geisel School added AI to required first- and second-year courses, including an "AI Patient Actor" for practicing clinical conversations ([Dartmouth](https://home.dartmouth.edu/news/2026/03/dartmouth-launches-new-courses-artificial-intelligence)). Michigan's Center for Academic Innovation funds field-specific projects in medicine, dentistry, nursing, music, and biochemistry ([Michigan CAI](https://ai.umich.edu/blog-posts/generative-ai-projects-teaching-learning/)).

**6. Law: verified authority and professional duty.**

- *Need:* A lawyer must stand behind every citation and every argument. AI that invents cases is not just a learning problem but a professional one.
- *Guidance:* ABA Formal Opinion 512 (July 29, 2024) applies lawyers' existing duties, including competence, confidentiality, and candor to the court, to generative AI ([National Law Review](https://natlawreview.com/article/american-bar-association-issues-formal-opinion-use-generative-ai-tools)).
- *In practice:* The University of Chicago Law School is embedding AI into four upper-level electives and planned 1L modules ([UChicago Law](https://www.law.uchicago.edu/news/ai-advances-law-school-curriculum)). Case Western Reserve's law school requires all 1Ls to complete an AI certification course ([ABA Journal](https://www.abajournal.com/web/article/class-is-in-session-how-some-law-schools-are-training-students-in-generative-ai)).

**7. A social-science core: independent thought and discussion.**

- *Need:* Core courses built on close reading and seminar argument depend on students forming their own views and defending them in person.
- *In practice:* The University of Chicago's Social Sciences Division **banned AI in required core courses** effective fall 2026, in a memo dated **August 1, 2026**, citing independent thinking and face-to-face discussion ([Chronicle](https://www.chronicle.com/article/u-of-chicagos-social-sciences-division-bans-tech-ai-in-core-courses)).

**How institutions are supporting the disciplines.** Several institutions have built structures that leave the substance to each field. MIT's August 13 report proposes "AI Intensive in the Major" courses, in which departments show how AI fits their own practices, plus departmental "AI Leads" and four course-policy templates: permit, limit, require, forbid ([MIT report](https://sites.mit.edu/ai-use/files/2026/08/AI-Committee-Final-Report-Aug-13.pdf)). Brown used locally run LLMs to audit roughly 3,000 syllabi across departments and found that more than half said nothing about AI use at all ([Brown](https://www.brown.edu/news/2026-08-20/brown-ai-teaching-learning)). Stanford, Yale ([Poorvu Center](https://poorvucenter.yale.edu/ai-course-revision-grant-mini-grants)), Michigan, and CMU fund faculty-proposed course redesigns. Cornell's AI Integration Pilots, announced **September 17, 2026**, let each college choose a core teaching element and test changes that may add *or deliberately reduce* AI ([Cornell](https://news.cornell.edu/stories/2026/09/ai-education-initiatives-emphasize-experimentation-balanced-use)).

---

![Most Discussed](media/discussed.png)

## Most Discussed

**Is "AI competency" one thing or many?** The stated aims across campuses use similar words: *judgment*, *critical and responsible use*, and *discipline-specific competency*. Penn calls humanistic and social-scientific perspectives "core competencies, not electives." Cornell frames the goal as *balanced* use, including using less AI where appropriate. But the field examples above suggest that judgment looks different in each discipline. For a statistician, it is recognizing when an analysis does not support its conclusion. For a writer, it is knowing what you think. For a clinician, it is owning a decision about a patient. A single campus-wide "AI literacy" requirement can teach the shared core, but it cannot teach these.

- *Open question:* Should institutions define a small common core and leave the rest to each discipline? 

---

![Interesting Ideas & Repos](media/ideas.png)

## Interesting Ideas & Repos

**1. Name the discipline's core practice first.** Several designs in this issue start from one sentence about what students must do themselves: "asks guiding questions instead of giving translations," "prompt journals" for checking output, "human judgment remains essential." Writing that sentence for your own field is a useful first step before choosing any tool ([Stanford CTL](https://ctl.stanford.edu/news/ai-education-grants-2026); [AAMC](https://aamc.org/about-us/mission-areas/medical-education/principles-ai-use)).

**2. A four-template policy menu.** MIT's *permit / limit / require / forbid* gives every department a shared vocabulary for describing course-level AI expectations, while leaving the choice to each discipline ([MIT report](https://sites.mit.edu/ai-use/files/2026/08/AI-Committee-Final-Report-Aug-13.pdf)).

**3. Intro → disciplinary → capstone module architecture.** A cross-disciplinary module set with a foundational unit, discipline-specific modules, and a final integration-and-reflection unit, designed to fit together ([AAAI/EAAI](https://ojs.aaai.org/index.php/AAAI/article/view/41523)). *(The published pilot is K-12; the architecture transfers more readily than its results.)*

**4. Error-finding as a discipline skill.** CMU's error-making AI tutor turns verification, the core skill in engineering, into the assignment itself ([CMU](https://www.cmu.edu/news/stories/archives/2026/august/navigating-the-ai-era-with-a-cmu-focus-on-critical-thinking)). The same idea fits statistics (find the flaw in this analysis) and law (find the fabricated citation).

**5. Evidence-required grants.** Stanford's "Innovation with Evidence" stream funds course development *only alongside* measurement of learning outcomes ([Stanford](https://news.stanford.edu/stories/2026/04/seed-grants-ai-education)).


---

![From My Desk](media/fromdesk.png)

## From My Desk

### Consent is easier than consensus

Since we launched the [aiX Faculty Fellowship Program]({{< relref "/post/2025-10-13-aixprogram/" >}}) last fall, I have kept coming back to a question: why do some changes around AI in education move quickly while others stall? If each discipline has to work out its own answer, how does any of them get started?

My answer: getting consensus to change is hard, but getting permission to try is good enough to start. The distinction comes from consent-based decision-making. As [Sociocracy For All](https://www.sociocracyforall.org/the-difference-between-whole-group-consensus-and-dynamic-governance-sociocracy/) puts it, "Consensus means a decision is made when everyone agrees. Consent means a decision is made when no one objects." Consensus asks everyone to share a view of AI in their field, and they don't. Consent asks a smaller question, one that practitioners sum up as "good enough for now, safe enough to try" ([Sociocracy 3.0](https://patterns.sociocracy30.org/consent-decision-making.html)). A project that runs for one term, can be reversed, and is reviewed at the end is much easier to say yes to.

As a statistician, I like that this turns decisions into experiments. Sociocracy 3.0 asks groups to "treat decisions as experiments" and to say in advance "what you would accept as evidence that your hypothesis is false" ([Principle of Empiricism](https://patterns.sociocracy30.org/principle-empiricism.html)). That is how an educational pilot should work: a stated hypothesis, a plan for evaluation, and a date to look at the results.

The experiments work best in small circles of practice: a few colleagues in the same discipline who try something, compare notes, and adjust. That is what our aiX cohorts have become. A circle can move at the speed of the technology. It also keeps the decision with the people who know what their discipline needs to protect. Permission to try gets a pilot started. Evidence from the circle, shared with people who are listening, is what lets it spread. — TZ

---

![Try This Week](media/try.png)

## Try This Week

### Write your discipline's one sentence

Finish this sentence for your field: "Whatever AI can do, our students must still be able to ___ themselves." Then look at one assignment and ask whether it actually requires that. The Stanford Japanese tutor, the chemical-engineering prompt journals, and the AAMC's first principle each started from a sentence like this.

### State your AI expectation in four words

Using MIT's four templates, decide whether AI is *permitted, limited, required, or forbidden* for each major assignment in one of your courses, and put that in the syllabus. Brown found that more than half of syllabi say nothing at all; a one-line statement per assignment is already more than most students get.

### Ask for permission to try, not agreement

If there is a change you want to make to a course, frame it as a bounded experiment: one term, a stated hypothesis, an evaluation plan, and a date to review. Then find two or three colleagues in your discipline to try it with you.

---

*aiX Weekly is curated by Claude and reviewed by Tian Zheng for the aiX Programs at Columbia University. It describes and curates; it does not endorse. Editorial notes reflect one statistician's reading of the week and invite discussion. Corrections and suggestions are welcome.*
