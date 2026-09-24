---
title: "aiX Weekly — AI in Higher Education (September 24th, 2026)"
date: 2026-09-24
draft: false
authors:
  - admin
tags:
  - AI
  - aiX
image:
  focal_point: 'top'
---

Collectively, universities stopped waiting for the research to settle before acting on AI. Students have already adopted it, and doing nothing is itself a decision.

<!--more-->

Florida moved toward requiring policies, Alaska's regents reviewed a draft, UT Austin made a syllabus statement mandatory, and a widely-read MIT report gave us a phrase — "cognitive surrender" — for a worry that had been mostly anecdotal. Underneath each is an instrument question: a disclosure rule assumes use can be observed, a detector assumes authorship can be classified, and a report on the illusion of learning assumes the illusion can be told from the real thing. Three items that arrived alongside the policy news make the stakes concrete: one, a position paper from 26 educators arguing that AI has not changed how expertise is built; two, a journal editor's account of asking authors to explain their own submissions; and third, an AI system produced a proof at the far end of mathematical difficulty. Combined, they raise the question of where the human expertise required to oversee such systems is supposed to come from.

---

Each [aiX Weekly]({{< relref "/tags/aiX/" >}}) post is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the [aiX Programs, Columbia University](https://www.linkedin.com/company/aix-programs-columbia-university/). AI can make mistakes and so can the human reviewer. Please double-check the linked sources.*

**Review by Tian Zheng on September 24th, 2026**

*Scope note: aiX Weekly is an observational digest for faculty and academic leaders. It curates and describes developments in AI and higher education; it does not advocate for particular policies, providers, or institutions. This issue covers items surfaced during approximately September 13–24, 2026; a few clearly-dated earlier items are included where they remain part of the current conversation and are flagged as such. Links point to primary sources wherever possible.*

---

![TL;DR](media/tldr.png)

## TL;DR {#tldr}

- A new preprint out of a single institution reports that generative-AI use is associated with **uneven** learning outcomes across student groups, and — in a counterintuitive twist — that some negative associations grew stronger among students with higher self-reported ability to evaluate AI output ([arXiv, Sept 16](https://arxiv.org/abs/2609.18676)).
- State systems and individual campuses moved on policy this week: Florida's Board of Governors issued a notice of intent to require public universities to adopt AI policies ([WLRN, Sept 16](https://www.wlrn.org/science-technology/2026-09-16/state-education-officials-looking-to-set-ground-rules-for-ai-in-higher-education-raise-questions-about-the-future)), the University of Alaska regents reviewed a draft systemwide policy ([Alaska Public Media, Sept 18](https://alaskapublic.org/news/education/2026-09-18/university-of-alaska-regents-consider-draft-ai-policy)), and the University of Texas at Austin began requiring an AI statement in every syllabus ([The Daily Texan, Sept 17](https://thedailytexan.com/2026/09/17/university-now-requires-ai-policy-in-professors-syllabi-some-professors-have-started-regulating-other-devices-too/)). They differ in how much they say about **what the policy is for** — compared side by side in [From My Desk](#from-my-desk).
- A widely-covered MIT committee report described "cognitive surrender" — students reaching for chatbots at the first sign of difficulty — while institutions from Ohio State to UC Berkeley responded in visibly different directions ([GV Wire, Sept 15](https://gvwire.com/2026/09/15/an-mit-report-warns-ai-is-causing-cognitive-surrender-universities-are-in-a-bind/)).
- An advocacy report argued that adoption of AI across admissions, teaching, and student services has moved faster than the protections around it ([Inside Higher Ed, Sept 18](https://www.insidehighered.com/news/quick-takes/2026/09/18/report-higher-eds-adoption-ai-outpaces-student-guards)).
- A position paper from 26 statistics, data science, and computer science educators argues that **generative AI has not changed how expertise is built** — it amplifies existing expertise and hinders novices, because "there is simply no substitute for good old-fashioned practice" ([AALAC workshop manuscript](https://beanumber.github.io/aalac2026/manuscript/)).
- A journal editor-in-chief met with authors of desk-rejected submissions and found several could not answer basic questions about their own papers — the same verification problem faculty are facing in the classroom, one rung further up the ladder ([TMLR Blog, Sept 16](https://blog.tmlr.org/2026/asking-authors-about-their-own-papers/)).
- OpenAI reported that an internal model produced a computer-checkable proof for the Navier–Stokes equations, one of the Millennium Prize problems — though specialists note it settles the problem as officially written rather than the version they most want answered, and the prize has not been awarded ([OpenAI, Sept 8](https://openai.com/index/navier-stokes-solution/); [Quanta, Sept 8](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/)). If AI now operates at the top of human research capability, the question this issue keeps circling — how expertise gets built — becomes a governance question, not only a pedagogical one.

---

![Table of Contents](media/toc.png)

## Table of Contents

- [This Week at a Glance](#this-week-at-a-glance)
- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [What's in the News](#whats-in-the-news)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [From My Desk](#from-my-desk)
- [Try This Week](#try-this-week)

---

![This Week at a Glance](media/glance.png)

## This Week at a Glance

If there is one thread running through this week's items, it is the gap between **how fast AI is being used** on campuses and **how slowly the surrounding structures — policy, evidence, and trust — are catching up**. Most of the stories are not about a new model or a dramatic capability; they are about institutions trying to describe, measure, and govern something that students have already adopted. Florida, Alaska, and UT Austin each took a step toward formal policy. A closely-read MIT report put language ("cognitive surrender") to a worry many faculty have voiced informally. And a fresh preprint added a note of statistical caution: the effects of AI on learning appear to vary across students in ways that a single average would hide. Running underneath all of it is a quieter argument, made most directly in a new multi-institution position paper: whatever AI has changed, it has not changed the fact that expertise is built slowly, by practice.

OpenAI announced a proof for the Navier–Stokes Millennium Prize problem. Read alongside the position paper on expertise, it poses a question we cannot answer but should not dodge — *if AI now works at the top of human research capability, and human expertise is the precondition for overseeing it, how is that expertise supposed to be trained now?*

*Relevant to faculty:* The week's items converge on the syllabus and the assignment. The UT Austin requirement makes an AI statement mandatory, and the "verification-first" conversation (below) is really a conversation about assessment design. Faculty who have already articulated where AI helps and where it substitutes may find this week's debates familiar rather than alarming.

*Relevant to academic leaders:* Several institutions are moving from *guidance* (suggested practices) to *policy* (binding requirements). The open questions are less about **whether** to have a policy and more about **what a policy can realistically observe and enforce**, and how it will be revised as evidence accumulates. A longer-horizon one, raised by the Navier–Stokes item: the committees, reviews, and evaluations through which an institution governs AI all draw on a supply of human expertise that the same tools may be shrinking. That is a faculty-development and curriculum question, not only a compliance one.

*Relevant to students:* The reports this week describe both benefits and costs of early, heavy reliance — and note that these are not distributed evenly. The recurring distinction is between using AI to *understand* something and using it to *avoid* understanding it.

---

![Research Highlights](media/research.png)

## Research Highlights

*Claude's note on this week's evidence: genuinely in-window, peer-reviewed studies on AI in higher education were thin. The strongest new items are a multi-institution position paper and a correlational preprint; I pair them with an earlier, more-developed study of the same phenomenon so the newer findings can be read in context. Evidence-strength labels are included for each.*

**1. Generative AI hasn't changed learning: it's still hard to become an expert** — *[AALAC workshop manuscript](https://beanumber.github.io/aalac2026/manuscript/), by 26 statistics, data science, and computer science educators from 11 liberal arts colleges and Carnegie Mellon University (An, Baumer, Dancey, De Veaux, and others), drafted at the Alliance to Advance Liberal Arts Colleges workshop at Wesleyan University, June 19–22, 2026.* **(Position paper; circulating this fall.)**

*Evidence: position paper; a synthesis of learning-science literature and teaching experience, not new data.*

The central claim is compact: **GenAI amplifies existing expertise but hinders novice development.** Because generative tools offer "a largely effortless way to accomplish tasks," they let novices bypass exactly the deliberate practice that builds the automated mental models expertise depends on. The authors catalogue why novices are the vulnerable case: they lack the background knowledge to evaluate AI output, they lack the triage skills experts use to decide what to check, and they are subject to a metacognitive failure in which performance declines while the feeling of learning goes up. Their analogy is a good amplifier — it makes an experienced guitarist sound better and does nothing for someone who has not practiced. Their line on mental models is the one worth keeping: "You can't be surprised by a symphony until you've developed a mental model for what symphonies are supposed to sound like." They also note a community cost, as solitary AI interaction displaces office hours, study groups, and mentorship. The recommendations are concrete: in-person, AI-free assessments aligned to stated learning goals; assignments whose connection to expertise-building is made explicit rather than appearing as "pointless busywork"; active re-encouragement of learning communities; and advocacy to stakeholders that AI-free foundational work is what makes later AI use productive.

> *Editor's note:* I agree with the position, and I want to add a corollary. Generative AI does not automatically make learning easy — it makes *producing output* easy, which is a different thing, and the paper is right that the gap between them falls hardest on novices. But the converse deserves saying too: AI can be used to build genuinely rich learning experiences. It just takes a great deal of work. In our [aiX programs]({{< relref "/tags/aiX/" >}}), the experiences that actually teach something are the ones where a lot of human design went in first — deciding what the student should struggle with, what the AI is allowed to do, and where a person has to show their reasoning. That design labor is the real cost, and it does not disappear because the tool is fluent. The authors' fourth recommendation — advocate to stakeholders — matters for the same reason: "use AI" is cheap to say and expensive to do well. — TZ

**2. The uneven impact of generative AI on student learning** — *[arXiv 2609.18676](https://arxiv.org/abs/2609.18676), submitted Sept 16, 2026 (Manikonda, Si, Munira, Seneviratne, Bennett).*

*Evidence: correlational; survey of 118 students across 12 AI-related courses at a single institution.*

The authors surveyed students and clustered them into four groups by how they engage with generative AI and what they perceive as its benefits. Reported academic benefits were associated with early reliance and using AI for task support; reported harms were associated with early reliance paired with attitudinal change. The finding that has drawn attention: negative associations *intensified* as students' self-reported "evaluation literacy" — their confidence in judging AI output — increased. The authors frame this as evidence that AI's effects on learning are unequal across students and argue for policy that distinguishes helpful from substitutive use.

> *Editor's note:* The counterintuitive result here is the interesting one, and it is also the one to read carefully. With 118 students at one institution and a cross-sectional design, this is a hypothesis-generating study, not a causal one. What the data suggest is a research question worth pursuing: does knowing more about a tool's limitations change how — and how much — a student leans on it? That is a measurement question before it is a policy question, and it may want a longitudinal design to answer well. — TZ

**3. Generative AI in higher education: evidence from an elite college** — *[arXiv 2508.00717](https://arxiv.org/abs/2508.00717), Contractor & Reyes; original 2025, latest revision April 15, 2026.* **(Older item, included for context.)**

*Evidence: correlational; survey-based, single selective institution.*

This earlier study is worth revisiting alongside the new preprint because it documents the baseline the newer work builds on: adoption reaching more than 80% within two years of ChatGPT's release, with wide variation across disciplines, demographic groups, and achievement levels. Its most-cited distinction is between **augmentation** (using AI for explanations and feedback), which students reported more often, and **automation** (generating whole assignments), which they reported less often. The authors conclude that effective policy has to separate uses that enhance learning from those that replace it.

> *Editor's note:* Reading these two surveys together, the through-line is variation. Both studies find that "students use AI" is nearly true and nearly useless as a summary — the action is in *which* students, for *which* tasks, in *which* courses. For those of us who teach, the augmentation-versus-automation distinction is a usable frame for a syllabus, even if it is hard to observe in practice. — TZ

---

![Institutional Movements](media/movements.png)

## Institutional Movements

**1. Florida's Board of Governors moves toward required AI policies.** The Board of Governors' AI and Cybersecurity Task Force met and issued a notice of intent to require public universities to adopt AI policies, while the state Department of Education separately weighs its own rule for public colleges. Reporting noted that only 8 of 40 public institutions had issued any AI guidance, with just two adopting formal policies ([WLRN, Sept 16](https://www.wlrn.org/science-technology/2026-09-16/state-education-officials-looking-to-set-ground-rules-for-ai-in-higher-education-raise-questions-about-the-future)). The proposed policies would address three areas: faculty disclosure of AI use, student disclosure, and permitted student uses in coursework.

- *Worth noting:* The three-part structure — faculty disclosure, student disclosure, permitted uses — is emerging as a common template across systems.
- *Open question:* What can a disclosure requirement realistically observe, given that much AI use leaves no trace? The policies may prove easier to write than to measure against — and, more importantly, what a disclosure rule *asks for* depends on what people think will be done with the answer.

> *Editor's note:* One measurement thought on the disclosure piece of this template. AI use is very hard to observe passively, so a disclosure requirement is not really a monitoring instrument — it is a self-report instrument, and self-reports respond to how people read the purpose behind them. If disclosure is understood mainly as a way to catch and regulate use, it tends to suppress the very reports it depends on: people under-report, report vaguely, or stop asking the questions that would reveal how they actually work. If it is framed around a shared aim — that we are collectively trying to understand these systems well enough to oversee and govern them, and that candid accounts of real use are the raw material for that — there is a much better chance of getting usable information back. The useful question when drafting is simply: does disclosing feel like exposure, or like taking part in something? None of this is an argument against disclosure, which I think is worth asking for. It is an argument for pairing it with its reason, so the data we collect is worth having. I return to this in [*From My Desk*](#from-my-desk) below, with a side-by-side look at which of this week's sources name a purpose and where each one carries it. — TZ

**2. University of Alaska regents review a draft systemwide policy.** The Board of Regents considered a draft that would require all three campuses to establish AI plans for students, faculty, and staff, organized around preserving human expertise, protecting data security, and expanding access. The university plans listening sessions and surveys this fall, with a finalized draft slated for approval in November ([Alaska Public Media, Sept 18](https://alaskapublic.org/news/education/2026-09-18/university-of-alaska-regents-consider-draft-ai-policy)). The CITO framed AI as amplifying longstanding institutional questions rather than creating wholly new ones; a regent raised the practical question of monitoring capacity.

- *Worth noting:* The "AI amplifies existing questions" framing is a useful one — data privacy and monitoring were institutional challenges before generative AI arrived.

**3. UT Austin requires an AI statement in every syllabus.** The University of Texas at Austin began requiring instructors to include an AI policy in their syllabi, and reporting noted some instructors extending their statements to other devices and tools ([The Daily Texan, Sept 17](https://thedailytexan.com/2026/09/17/university-now-requires-ai-policy-in-professors-syllabi-some-professors-have-started-regulating-other-devices-too/)).

- *Worth noting:* A required syllabus statement pushes the decision down to the course level, where disciplinary differences can be respected — a chemistry lab and a creative-writing seminar can land in different places.
A mandate to *state* a policy is not a mandate for any particular policy. The interesting variation will be in what instructors actually write.

---

![What's in the News](media/news.png)

## What's in the News

**1. An MIT report names "cognitive surrender."** A widely-covered committee report described students reaching for AI chatbots "at the first hint of struggle," producing what it called "the illusion of learning," alongside cultural shifts such as fewer visits to office hours and shared study spaces. Coverage catalogued a spectrum of institutional responses: Ohio State integrating AI across majors and Dartmouth's president warning of "irrelevance" for universities that do not, against the University of Chicago and UC Berkeley Law restricting AI in certain courses, and Cornell creating a workshop-based path to remediate minor misuse ([GV Wire, Sept 15](https://gvwire.com/2026/09/15/an-mit-report-warns-ai-is-causing-cognitive-surrender-universities-are-in-a-bind/); [The Philadelphia Inquirer, Sept 18](https://www.inquirer.com/education/artificial-intelligence-college-students-universities-approaches-mit-harvard-ohio-chicago-20260918.html)).

> *What's interesting here:* The phrase "illusion of learning" describes a real and familiar phenomenon — the gap between feeling fluent and being able to reproduce a result unaided. Coverage did not detail the report's methodology, so it reads as considered institutional observation rather than measured effect; the more durable contribution may be that it gives faculty shared language for something many have noticed.
>
> Most of this week's policy conversation is aimed at students hiding their lack of learning from instructors. I think **the larger danger** is that it stays hidden from *themselves* — that the illusion of learning is, first of all, a failure of self-assessment. A misled instructor gives one grade that is too high. A misled student decides what to review, what to practice, and whether they are ready for what they will be responsible for, all on bad information. That compounds, and nobody has to be dishonest for it to happen. The AALAC paper names the same mechanism: performance declining while the feeling of learning rises.
>
> The encouraging part is that if the problem is calibration rather than concealment, the most useful assessments are not the ones hardest to fool but the ones that show a student their own state — a retrieval attempt, a three-minute explanation, a closed-book restart on yesterday's "understood" problem. Framed as surveillance, they invite resistance. Framed as a mirror, most students want them. — TZ

**2. A journal editor asks authors to explain their own papers.** Nihar B. Shah, an editor-in-chief at *Transactions on Machine Learning Research*, offered ten authors of desk-rejected submissions a meeting before the decision became final; seven joined roughly 30-minute video calls, in which he asked both basic questions about setup and notation and deeper ones about specific results and design choices ([TMLR Blog, Sept 16](https://blog.tmlr.org/2026/asking-authors-about-their-own-papers/)). Three could not answer the basic questions about their own papers — two showed almost no substantive understanding of the contents, and one could not point to where a key claim from the abstract appeared in the text. Three more handled the basics but faltered on the methodological and theoretical choices. One author answered everything, though Shah found a major error in that paper's main claims. He notes that two of the struggling authors followed up with email that detectors classified as "100% AI," and concludes: "When authors could not answer questions about the technical parts, and sometimes even basic questions about the paper, it is difficult to see how they could have verified the paper's contents." *(Small n and self-selected: these were desk-rejected submissions, not a random sample of authors.)*

**3. An advocacy report argues protections lag adoption.** *Students at Stake: Risks of AI Deployment in Higher Education*, from Student Defense's SHAPE initiative, documented AI's spread across admissions, hiring, teaching, and student services, and argued that safeguards — around bias, data privacy, disclosure, and the erosion of learning communities — have not kept pace. It urged leaders to ask "what problem are we trying to solve?" before deploying, rather than adopting "AI first and ask questions later" ([Inside Higher Ed, Sept 18](https://www.insidehighered.com/news/quick-takes/2026/09/18/report-higher-eds-adoption-ai-outpaces-student-guards)).

**4. Three major labs float an AI standards body.** OpenAI, Anthropic, and Google are reported to be in talks to create an industry standards body ([France 24, Sept 15](https://www.france24.com/en/technology/20260915-openai-anthropic-and-google-in-talks-to-create-a-standards-body-as-ai-fears-rise)). 

> *What's interesting here:* For universities, the practical question is whether any such body produces the kind of documentation — data handling, evaluation methods, known limitations — that a procurement office or an IRB could actually use. Standards written for the industry are not automatically the standards education needs. — TZ

**5. University of Iowa launches an AI Discovery Initiative.** Iowa announced a campuswide initiative — more than \$1 million over three years — offering secure "AI tokens" for access to leading platforms, a faculty upskilling program with protected time and mentorship, a scholars' series, and an AI-in-education summit set for January 2027 ([University of Iowa, announced early Sept; covered by The Daily Iowan, Sept 15](https://ai.uiowa.edu/news/2026/09/ai-discovery-initiative-help-ui-faculty-staff-explore-ai)). *(Edge-of-window: the initiative was announced in the first days of September and re-surfaced in mid-September coverage.)*

> *What's interesting here:* The design choice worth noting is *protected time* for faculty to learn — a recognition that "upskilling" without workload relief tends not to happen. The token-based, institutionally-secured access model is also crucial to set up early: provide a sanctioned path so people do not route sensitive work through unvetted tools. — TZ

**6. An AI system produced a proof for a famous open problem in mathematics.** On September 8, OpenAI announced that an internal model — not publicly available, and running thousands of agents over roughly 88 hours — produced a proof concerning the Navier–Stokes equations, one of the Clay Mathematics Institute's seven Millennium Prize problems ([OpenAI, Sept 8](https://openai.com/index/navier-stokes-solution/); [Quanta, Sept 8](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/)). The proof was accompanied by a version written in Lean, a language in which a computer can check every step — so unlike most AI output, this claim could be verified mechanically.

I am not a specialist in this area, so I will keep the caveats to what the reporting makes clear. The version of the problem that was settled is the one the prize is officially written around, but mathematicians have noted it is not the version they most want answered; as one put it, "The Clay problem is settled, but the main problem for the Navier–Stokes equations is not" ([Scientific American](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)). The Clay Institute has not awarded the prize, and says its review is deliberately unhurried. There is also an unresolved dispute over credit and provenance with two mathematicians working on closely related results at the same time ([Axios, Sept 8](https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit)). What specialists do agree on is that the key idea came from people: the strategy the proof relies on is credited to Diego Córdoba and Luis Martínez-Zoroa, whom Charles Fefferman called "the heroes of the story." *(The record was still moving when this issue went out; check the sources before citing.)*

> *What's interesting here:* Every other item in this issue looks at the bottom of the ladder — what happens to novices who skip the practice. This one looks at the top, and the honest reading is that AI is now operating at the level of expert research practice. That matters for us because nearly every serious proposal for AI oversight and governance — peer review, procurement review, IRBs, accreditation, model evaluation, expert testimony — assumes a supply of humans whose judgment is at or above the level of the thing being judged. That judgment was built the slow way, in this case, by people who spent years on Navier–Stokes before any of this existed. If generative AI shortens the path to *producing* expert-looking output while lengthening the path to *holding* expert judgment — which is precisely the AALAC paper's claim — then we are drawing down a stock of expertise faster than we are replacing it. And you cannot supervise at a level you have never reached or do not have reliable tools. In this story, the Lean check where a claim can be made machine-verifiable, offers a potential solution to offer a form of oversight that does not need a scarce expert. This approach needs to be developed carefully and evaluated fiercely. — TZ

---

![Most Discussed](media/discussed.png)

## Most Discussed

**1. The embrace-versus-restrict split.** The MIT report became a lightning rod less for its findings than for the contrast it drew out: the same week produced Ohio State's move to weave AI through every major and Dartmouth's warning about irrelevance, alongside course-level bans at Chicago and Berkeley Law and Cornell's remediation workshops. The discussion has largely been about whether these are contradictory strategies or appropriate responses to different disciplines and missions.

> *Editor's note:* I read this less as a fight to be won than as evidence that "the right AI policy" is discipline- and goal-dependent. A program training future software engineers and a program training future poets are answering genuinely different questions, and a single institutional line would serve neither well. The healthier version of this debate treats the variation as a feature. — TZ

**2. From detection to verification.** A piece arguing to move "beyond the gotcha game" of AI detectors toward "verification-first" academic integrity circulated among teaching-and-learning audiences ([eCampus News, Sept 16](https://www.ecampusnews.com/ai-in-education/2026/09/16/beyond-the-gotcha-game-moving-from-ai-detection-to-verification-first/)). The argument: detectors are unreliable and adversarial, and integrity is better served by designing assessments whose process is observable — drafts, checkpoints, oral components — than by trying to catch AI after the fact.

> *What's interesting here:* This maps onto a measurement idea that predates AI: if you cannot observe a construct directly, you build an instrument that captures it indirectly and repeatedly. The shift from detection to verification is, in statistical terms, a shift from a single noisy classifier to a designed set of process measurements. That is a more defensible foundation, even if it asks more of the instructor. — TZ

---

![Interesting Ideas & Repos](media/ideas.png)

## Interesting Ideas & Repos

**1. AI-Teaching-Agent (open-source).** A public repository offering an open-source teaching agent for generating labs, exams, and grading workflows, built around structured domain-specific languages, explicit human review, and sandboxed evaluation, with CLI/MCP tooling and a local-first interface ([GitHub](https://github.com/littlecookie0722/AI-Teaching-Agent)). *(Release is undated; treat as exploratory and evaluate carefully before any classroom use.)*

**2. Restorative remediation for minor misuse.** Cornell's reported approach — routing minor AI-misuse cases through a workshop rather than straight to a disciplinary finding — is an idea more than a product, and a portable one. It reframes a first infraction as a teachable moment about what the tool is and is not for.

**3. Process-portfolio and oral-checkpoint assessment.** The concrete side of the "verification-first" conversation: assessments that grade the visible process — annotated drafts, brief oral defenses, in-class reasoning — rather than only the final artifact. No single repo owns this; it is a pattern faculty are assembling from ordinary tools.

> *Editor's note:* In a statistics course, an oral checkpoint where a student explains *why* they chose a model often reveals more than the finished write-up. The cost is time. — TZ

---

![From My Desk](media/fromdesk.png)

## From My Desk

Reading this week's items back to back, what struck me is how many are measurement problems wearing policy clothes. A disclosure requirement assumes we can observe use; a detector assumes we can classify authorship; a report on "cognitive surrender" assumes we can tell the illusion of learning from the real thing. Each is a claim about an instrument, and in my field the hardest part is rarely the decision rule — it is deciding what to measure with respect to the goal of an inquiry, and admitting how noisy and/or biased the measurement is. The preprint on uneven impact makes that concrete: its most interesting result, that harms tracked with *higher* evaluation literacy, is one I would want to understand better before acting on, since the instrument could be picking up confidence, competence, or candor.

Two items push past measurement to something stronger. The AALAC paper argues that generative AI has not changed how expertise is built, and what I would underline is what that implies about effort: AI makes producing output effortless, not learning, and the two are easily conflated. Building an AI-enabled experience that genuinely teaches is not less work than teaching without AI — in our aiX programs it has been considerably more, because someone has to decide what the student should struggle with, what the tool may do, and where a person must show their reasoning. The TMLR editor's meetings show the other end of the same story. Expertise is built from retained traces of effort; if little is retained there is little to build on, and the feeling of fluency removes the signal that would have told you to practice. The person most affected by that is not the instructor who receives a misleading essay but the student who receives a misleading estimate of themselves.

The Navier–Stokes item turns that pedagogical worry into an institutional one. Whatever its contested details, an AI system carried out an expert-level research program, and the ideas specialists credit for making it possible were human. Nearly every oversight mechanism we have proposed for AI is staffed by experts: someone reviews the paper, evaluates the model, signs the procurement, sits on the committee. Where the next cohort of those people comes from strikes me as a curriculum question rather than a distant one, and three partial answers occur to me. It may help to describe foundational, AI-free work as what it is — the training of people who will later have to supervise these systems — rather than as a concession to integrity. It is worth asking where verification can be made cheap: a computer-checkable proof is a claim anyone can confirm without being able to produce it, and the closer our own work comes to that form (reproducible code, preregistered analyses, held-out evaluations), the less oversight depends on a scarce expert. And for everything that cannot be formalized, which is most of what a university does, the instrument we have always had is apprenticeship — sitting with a novice, asking why, watching where they falter. That is the oral checkpoint and the editor's video call, and it does not scale, which makes expert attention spent on novices the resource worth budgeting for deliberately.

A smaller observation, about wording rather than substance. Requiring an AI policy is, in effect, requiring a value judgment to be made public, and the sources vary in how much of that judgment they say out loud — naturally enough, since documents written for different audiences carry their reasoning in different places. It is clarifying to set them side by side in their own language. (*Note: AI makes mistakes. Check the original source for accurate details.*)

| Source | What it asks for | The purpose it names | Where the *why* sits |
|---|---|---|---|
| **Florida Board of Governors** | Universities adopt policies covering faculty disclosure, student disclosure, and permitted uses | Not specified in the notice as reported; the rationale in coverage comes from observers rather than the Board — ensuring "students are still learning" and that work is "done by the student" | Left to each institution, along with the content |
| **University of Alaska** | Systemwide plans at all three campuses | Three named principles: "not replacing human talent," maintaining data security, and "leveraging AI to improve access to education services" | In the policy's own framing |
| **UT Austin** | An AI statement in every syllabus | Clarity for students, who "shared they were unclear in the past"; discipline-specific judgment about whether AI "furthers the achievement of learning"; students developing "deep fluency in AI, but also independence" | Articulated by the provost's office |
| **University of Iowa** | Nothing; it offers secure access, funding, and protected faculty time | Building capability, and providing a sanctioned path so sensitive work need not go through unvetted tools | Carried by the program design |
| **SHAPE / Student Defense** | That leaders ask "what problem are we trying to solve?" before deploying | Bias, data privacy, disclosure, and protecting learning communities | The document is itself about purpose |
| **AALAC position paper** | AI-free foundational assessment, and advocacy to stakeholders | Expertise-building: AI-free early work is what makes later AI use productive | Stated, and its fourth recommendation is to *say so* |
| **"Verification-first" argument** | Assessments whose process is visible | Integrity through design rather than detection | Stated as the argument's premise |

A requirement that arrives without its rationale can be *perceived* as surveillance even where none is intended — and read that way, it tends to produce careful, uninformative disclosures. That is the measurement point from [*Institutional Movements*](#institutional-movements) above: because AI use cannot be fully observed passively, disclosure is a self-report instrument, and self-reports move with how people read the purpose behind them. 

I believe students respond well to clarity, fairness across sections, and honesty about whether a tool will be used to judge them, while faculty respond well to disciplinary discretion, the link between AI-free work and expertise, and workload realism. The purpose I suspect is currently underused with both groups is the collective one: that we are trying to understand these systems well enough to oversee them, and that candid accounts of real use are the evidence for doing it. 

That is also where many of aiX fellows worked on — designing assignments whose process is visible — a shift toward better instruments. That asks less that we teach differently than that we be honest about what our old assessments were ever measuring. If AI has done one useful thing for the statistics of teaching, it is to make that question unavoidable. — TZ

---

![Try This Week](media/try.png)

## Try This Week

### Audit one assignment for what it measures

Take one assignment you already give and ask a single question of it: *if a student produced this entirely with AI, what would I have failed to learn about their understanding?* Then experiment — on one low-stakes **ungraded** assignment — with adding a small process component that closes that gap: a short explanation of one choice they made, a short annotated draft, or a "reasoning note" where they explain why an alternative approach was rejected.

One more thing worth trying: tell the student what you found. If the point of the process component is calibration rather than enforcement, then the student is the primary audience for the result — a short "here is where your explanation got thin" is more useful to them than the grade, and it reframes the exercise as a mirror rather than a check.

The goal is not to defend against AI but to see what the added measurement reveals. You may find the process artifact tells you more than the product did, or that it tells you nothing new and is not worth the time. Either way, you will have a little evidence about your own instrument, which is more than most of us have right now.

### Write the *why* line of your AI statement

If your institution requires an AI policy in your syllabus — and more of them will by spring — add one sentence saying what the policy is for. Not what is permitted, which you have presumably already written, but why: what you want students to be able to do unaided by the end of the term, and what that has to do with the rule. "No AI on the first three problem sets, because the point of those weeks is to build the intuition you will need to tell when an AI's answer is wrong" is a different document from the same rule stated alone, and it costs one sentence.

Then, if you have the chance, read it aloud in the first week and ask whether it sounds fair. That question — *does the reason hold up when said out loud to the people it governs* — is a cheap validity check, and it is the one thing a written policy never gets.

---

*aiX Weekly is curated by Claude and reviewed by Tian Zheng for the aiX Programs at Columbia University. It describes and curates; it does not endorse. Editorial notes reflect one statistician's reading of the week and invite discussion. Corrections and suggestions are welcome.*
