---
title: "aiX Weekly — AI in Higher Education (October 28th, 2026)"
date: 2026-10-28
draft: false
authors:
  - admin
tags:
  - AI
  - aiX
  - research
image:
  focal_point: 'top'
---

AI is making some old pressures in research louder: more proposals, more submissions, more reviews. That's a good prompt for a simple question. What problem do we actually want AI to solve, and how will we know it worked?

<!--more-->

This month brought a lot of news about volume. Journals paused submissions, funders capped applications, and reviewers turned to chatbots. Much of the pressure behind it is older than ChatGPT. A grant proposal already took about 34 working days for roughly a one-in-five chance of funding, and careers already ran on counting papers and grants. When entering a contest gets cheaper, people enter more. AI mostly turned up the volume.

So "too many submissions" is the symptom. The problems underneath are ones we've been debating for years: effort that goes into contests instead of science, careful review that's always in short supply, analytic choices no one else can see. Some of these are exactly where AI could help, if we aim it there.

[Last week]({{< relref "/post/2026-10-21-aix-weekly-newsletter/" >}}), the question was "when do we want a person to do this, and why?" This week, it's the other side: "we want to solve *this* problem with AI, and we'll call it a success when…" People will fill in that sentence differently, and that's fine. As you read, ask of each item: what problem is it solving, and how does it define success?

---

Each [aiX Weekly]({{< relref "/tags/aiX/" >}}) post is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the [aiX Programs, Columbia University](https://www.linkedin.com/company/aix-programs-columbia-university/). AI can make mistakes and so can the human reviewer. Please double-check the linked sources.*

**Review by Tian Zheng on October 28th, 2026**

---

![TL;DR](media/tldr.png)

## TL;DR {#tldr}

AI is turning up the volume on research's old pressures. That makes it a good time to name the problem we want it to solve.

- **The pressure predates AI.** A grant proposal took about 34 working days, about 1 in 5 got funded, and extra effort didn't improve the odds ([Herbert et al., 2013](https://bmjopen.bmj.com/content/3/5/e002800)).
- **AI turned up the volume.** Applications to 12 major funders rose 57% from ChatGPT's launch to late 2025 ([RoRI](https://researchonresearch.org/ai-agents-pose-existential-threat-to-research-funding/)). An estimated 21% of ICLR 2026 reviews were fully AI-written ([Pangram Labs](https://news.bensbites.com/posts/52410-pangram-labs-21-of-the-75800-peer-reviews-submitted-for-iclr-2026-a-major-ml-conference-were-fully-ai-generated-and-50-contained-signs-of-ai-use)).
- **Communities are stopping to redesign.** Six probability and statistics journals, including *Bernoulli*, paused new submissions until November 8 to rethink their policies ([EDP Sciences](https://www.edpsciences.org/en/news-highlights/3058-esaim-probability-and-statistics-takes-action-to-address-increasing-manuscript-submissions)).
- **AI can make review better.** In a blind test, AI reviews beat top-quality human reviews on every measure, with a third the error rate, while the publication call stayed with a human editor ([King & Worthington](https://gking.harvard.edu/peerless/)).

---

![Table of Contents](media/toc.png)

## Table of Contents

- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [Try This Week](#try-this-week)

---

![Research Highlights](media/research.png)

## Research Highlights

**1. What a grant proposal cost, before AI** — *Herbert, Barnett, Clarke & Graves, [BMJ Open 3(5), 2013](https://bmjopen.bmj.com/content/3/5/e002800).*

A new proposal took 38 working days on average, and a resubmission took 28. Across 3,727 proposals, that's about 550 working years, or AU$66 million in salaries, for a 21% success rate. And more time spent didn't raise anyone's odds. A [follow-up study](https://bmjopen.bmj.com/content/4/3/e004462) found that during grant season, proposals came before other work (97%) and family (87%).

**2. AI reviews vs. human reviews at their best** — *King & Worthington, "[AI Article Reviews Dominate Human Peer Reviews at Their Best](https://gking.harvard.edu/peerless/)," working paper, October 22, 2026.*

*Evidence: 124 manuscripts and 134 human reviews from Harvard IQSS's rapidPeer service; an AI judge on all pairs and three former journal editors on 10 pairs.*

The human reviews here were about as good as it gets: expert reviewers, paid well, asked to read the whole paper and be constructive. 88% of surveyed authors rated them high quality. Claude Opus 4.8 wrote an AI review for each paper, and GPT-5.5 judged the pairs blind. The AI review won all 132 decided pairs. Three former editors, who didn't know one review in each pair was AI-written, picked the AI review in 26 of 30 judgments. They agreed with the AI judge (87%) more than with each other (80%). The AI reviews cited no fabricated sources, and 5.5% of their claims about the manuscript were wrong, against 15.9% for the human reviews. Ten robustness checks, including length-matched pairs and swapping in other models, didn't change the picture.

The authors are careful about scope. They measured how much reviews help *authors improve papers*, not how *publication decisions* should be made. They also flag risks: science drifting toward the same conventional ideas, and authors gaming a journal's published AI prompt. In every option they sketch, the final call stays with "a human journal editor with the proper authority and responsibility."

**3. Reviewers use AI, rules or no rules** — *Pangram Labs on ICLR 2026, Kim et al., [ICML 2026 randomized experiment](https://arxiv.org/abs/2609.19420), arXiv preprint.*

*Evidence: AI-text detector on ICLR reviews; randomized AI-use policies for ICML reviewers, with a survey.*

At ICLR, about 21% of reviews were flagged as fully AI-generated and over half showed some AI use. Many were generic, and some cited references that don't exist. Detector accuracy is contested, so treat the numbers as rough. At ICML, 22.5% of surveyed reviewers who were told *not* to use AI used it anyway. Bans aren't holding. Put next to King and Worthington's results, the question isn't whether AI belongs in review but how it's used. Undisclosed, unstructured use that nobody stands behind is the weak version. The stronger one is designed on purpose, with clear roles, disclosure, and a human who's accountable.

---

![Institutional Movements](media/movements.png)

## Institutional Movements

**1. Six probability journals hit pause.** From **October 19 to November 8**, *Bernoulli*, *Electronic Journal of Probability*, *Electronic Communications in Probability*, *Stochastic Processes and their Applications*, *Annales de l'IHP (B)*, and *ESAIM: Probability and Statistics* were reported to stop taking new submissions ([EDP Sciences, Oct 19](https://www.edpsciences.org/en/news-highlights/3058-esaim-probability-and-statistics-takes-action-to-address-increasing-manuscript-submissions); [Proofs and Prompts](https://proofsandprompts.com/newsfeed/)). The reason given is a surge in submissions "driven largely by the rapid development of artificial intelligence." Revisions and ongoing reviews continue. The boards are using the time to revisit their aims and scope and their AI guidance for authors *and* reviewers.

**2. Funders ask what evaluation should measure.** At a [LERU seminar](https://www.leru.org/news/leru-talks-ai-and-research-grants-is-the-system-doomed-to-collapse) in June, James Wilsdon and Geraint Rees (UCL) warned that AI agents are pushing "the marginal cost of applications down to zero" ([RoRI](https://researchonresearch.org/ai-agents-pose-existential-threat-to-research-funding/); [*Nature*](https://www.nature.com/articles/d41586-026-01422-x)). When every proposal is polished, polish stops telling reviewers anything. Their suggestion: weight evaluation toward what an agent can't fake, like a researcher's track record of delivering on ideas.

**3. NIH caps applications.** Since September 2025, NIH has accepted at most six applications per investigator per year, citing submissions "some of which may have been generated with AI tools" ([Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-08-05/pdf/2025-14744.pdf)).

**4. arXiv tightens up on CS surveys.** Since late 2025, computer science review and position papers need prior peer review before arXiv will post them, after a wave of low-effort, AI-generated surveys ([404 Media](https://www.404media.co/arxiv-changes-rules-after-getting-spammed-with-ai-generated-research-papers/)). Some worry this hits early-career researchers hardest.

---

![Interesting Ideas & Repos](media/ideas.png)

## Interesting Ideas & Repos

**The attention economy, named in 1971.** Herbert Simon: "a wealth of information creates a poverty of attention" ("Designing Organizations for an Information-Rich World"). Research has always run on scarce attention from reviewers, editors, and readers. AI just made the information side nearly free.

---

![Try This Week](media/try.png)

## Try This Week

### Write the problem before the solution

Pick one practice you have a hand in: how your lab gives feedback on drafts, how your committee reads applications, or how your department weighs publications. Before deciding what AI should do, finish this sentence:

> *We want to solve [the real problem] with AI, and we'll call it a success when [an outcome for the research], as shown by [evidence we'll actually check]. People will still decide [this].*

If you can't fill in the first blank without naming a tool, you have a solution looking for a problem. Then ask a colleague to fill it in too. Where you differ, don't argue about who's right. Find one change you'd both try for a term.

---

*aiX Weekly is curated by Claude and reviewed by Tian Zheng for the aiX Programs at Columbia University. It describes and curates; it does not endorse. Editorial notes reflect one statistician's reading of the week and invite discussion. Corrections and suggestions are welcome.*
