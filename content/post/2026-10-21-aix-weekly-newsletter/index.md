---
title: "aiX Weekly — AI in Higher Education (October 21st, 2026)"
date: 2026-10-21
draft: false
authors:
  - admin
tags:
  - AI
  - aiX
  - governance
image:
  focal_point: 'top'
---

Many debates about AI turn into "contests" with human: can AI grade, tutor, or advise as well as a person? This issue aims to think about AI in our work from a different premise. AI governance is not about proving whether humans or AI are better at something. It is about how we choose to use technology in our lives.

<!--more-->

Capability comparisons tell us what is *possible*. They cannot tell us what we *want*. This month, a faculty council, a student senate, and a citizens' assembly each argued, in different words, for the same thing: a say in how AI is used where they live and work. The research this issue gathers points the same way. How people want AI used depends on the stakes and the setting, and our beliefs about what AI can do are not always neutral. In one set of experiments, people talked themselves into seeing an AI as more capable when that belief made it easier to hand off a hard moral decision.

A preference that rests on "AI can't do X yet" goes out of date when it can. A preference that rests on "we want a person to do X, for these reasons" holds until our reasons change, and then we can revisit it deliberately.

---

Each [aiX Weekly]({{< relref "/tags/aiX/" >}}) post is organized around a set of recurring sections and pairs with our companion [AI and Higher Education timeline]({{< relref "/post/2026-06-24-ai-education-timeline/" >}}), which traces the broader arc of how AI has reshaped higher education since late 2022.

*Curated by Claude for the [aiX Programs, Columbia University](https://www.linkedin.com/company/aix-programs-columbia-university/). AI can make mistakes and so can the human reviewer. Please double-check the linked sources.*

**Review by Tian Zheng on October 21st, 2026**

---

![TL;DR](media/tldr.png)

## TL;DR {#tldr}

Read side by side, this month's campus news shows a shift in what people are arguing about. For a long time, "the tool isn't good enough yet" was a reason to put off harder questions. That reason is running out. As AI gets better at more of our work, we have to face the questions capability never answered: how do we *want* the tool used here, and who gets to decide? People are no longer just debating these questions. They are starting to act on them.

- **Faculty and students are asking "who decides?"** At Duke, faculty objected to an institution-wide decision to give students Copilot and ChatGPT and proposed a resolution giving them a seat at the table for enterprise AI decisions ([Duke Chronicle, Oct 2](https://dukechronicle.com/article/duke-university-arts-and-sciences-council-ai-takes-center-stage-with-proposed-resolution-on-faculty-governance-bluebot-20261002)). At Eastern Illinois, students unanimously asked their administration to regulate how *faculty* use AI. The president replied that curriculum belongs to the disciplines, so answers will vary by department ([Daily Eastern News, Oct 11](https://www.dailyeasternnews.com/2026/10/11/student-senate-asks-university-to-regulate-use-of-ai-by-faculty/)).
- **The public wants a voice too.** An Edinburgh assembly of 99 people from government, the NHS, industry, academia, and the public recommended a standing UK citizens' assembly on AI and society ([University of Edinburgh, June 10](https://www.sps.ed.ac.uk/news-events/news/citizens-assembly-public-voice-ai-report)).
- **Preferences depend on context and stakes.** Students favor human judgment for subjective work but accept AI feedback for lower-stakes tasks ([*Behavioral Sciences*, 2026](https://avesis.tedu.edu.tr/yayin/cda371d2-4fda-4cb1-a060-3ce3586e2bb1/when-do-undergraduate-students-prefer-ai-insights-into-ai-scoring-and-feedback)). In a randomized field study, AI drafts increased how often TAs gave feedback while leaving the TAs fully in control ([Mahinpei et al., June 2026](https://arxiv.org/abs/2606.03095)).
- **"The AI can do it" can be a convenient belief.** In experiments with 5,639 participants, people delegated real moral decisions to AI *more* readily than to another person. Part of the reason was a self-serving shift in what they believed about AI's capability ([Hüholt & Szech, *European Economic Review*, 2026](https://publikationen.bibliothek.kit.edu/1000190253)).

---

![Table of Contents](media/toc.png)

## Table of Contents

- [Research Highlights](#research-highlights)
- [Institutional Movements](#institutional-movements)
- [Most Discussed](#most-discussed)
- [Interesting Ideas & Repos](#interesting-ideas--repos)
- [Try This Week](#try-this-week)

---

![Research Highlights](media/research.png)

## Research Highlights

**1. Delegating moral decisions to AI** — *Hüholt & Szech, "Trusting machines with morality: Delegating moral decisions to AI," [European Economic Review 184 (2026), 105255](https://publikationen.bibliothek.kit.edu/1000190253); online January 2026.*

*Evidence: two incentivized experiments, 5,639 participants total.*

Earlier survey research suggested people distrust AI in moral contexts and prefer human decision-makers. But when participants faced a real moral decision with consequences, they handed it off significantly *more* often when the delegate was an AI than when it was another person. The authors find that responsibility-shifting, a known motive for delegating to people, extends to AI. They also find it is helped along by people adjusting their beliefs about AI's capability in a self-serving way. The more ambiguous the AI's capability, the easier it is to justify letting it decide.

> *Editor's note:* This may suggest "is AI capable of X?" should not be the governance question. Capability claims can be ambiguous enough to be bent toward whatever we already wanted to do. Asking "do we want AI to decide this, and who is accountable if it does?" is probably a better way to decide. — TZ

**2. When do students prefer AI scoring and feedback?** — *Yildirim Erbasli, Dibek, Thomas & Lesoway, [Behavioral Sciences 16(7), 2026](https://avesis.tedu.edu.tr/yayin/cda371d2-4fda-4cb1-a060-3ce3586e2bb1/when-do-undergraduate-students-prefer-ai-insights-into-ai-scoring-and-feedback) (DOI 10.3390/bs16071196).*

*Evidence: survey and scenario study, 93 undergraduates.*

Students liked structured, moderately detailed AI feedback on grammar and organization, but generally preferred human evaluation for subjective tasks. They saw AI as useful in lower-stakes settings and doubted it could judge more complex writing. They favored hybrid models in which AI supports human judgment, with transparency and human review. A related Canadian study (159 students) found that students often could not tell whether a person or ChatGPT had written their feedback, yet learning the source lowered their confidence in AI *scoring* ([Sciforum, 2026](https://sciforum.net/paper/30087)).

**3. AI drafts for discretionary work** — *Mahinpei, Dean, Fong, Liu & Horta Ribeiro, "[AI Assistance for Discretionary Work: Increasing Feedback Provision in Higher Education](https://arxiv.org/abs/2606.03095)," arXiv preprint, June 2026.*

*Evidence: randomized field experiment in one 300-level machine learning course (11 TAs, 88 students), plus interviews; preprint.*

Submissions were randomly assigned to come with an AI-generated feedback draft or without one. The TAs could use, edit, or ignore the drafts. With drafts available, TAs gave personalized feedback 10.8 percentage points more often (SE = 1.1). The feedback was also longer, with no drop in how useful students rated it. The authors read the drafts as "editable scaffolds that lower barriers to initiating feedback," increasing work that might otherwise go undone while keeping humans in control of the final result.

---

![Institutional Movements](media/movements.png)

## Institutional Movements

**1. Faculty ask for a seat at the table: Duke.** At the October 1 Arts & Sciences Council meeting, Robin Kirk (cultural anthropology) presented a resolution saying that, as part of faculty governance, "faculty should be at the table when these enterprise decisions are made" about AI ([Duke Chronicle, Oct 2](https://dukechronicle.com/article/duke-university-arts-and-sciences-council-ai-takes-center-stage-with-proposed-resolution-on-faculty-governance-bluebot-20261002)). It followed faculty criticism of the decision to give students tools such as Microsoft Copilot and ChatGPT. Kirk said the resolution would not give faculty a yes-or-no vote. A vote is expected at the next meeting or in December. At the same meeting, the university's IT office presented BlueBot, a campus information chatbot trained only on Duke data, whose stated role is to "guide, not decide."

**2. Students petition about faculty AI use: Eastern Illinois.** The Student Senate unanimously passed a resolution, backed by a 512-signature petition, asking the president and provost for a policy on "what professors can and cannot use AI for" ([Daily Eastern News, Oct 11](https://www.dailyeasternnews.com/2026/10/11/student-senate-asks-university-to-regulate-use-of-ai-by-faculty/)). One student argued that department-by-department rules are "not equitable." In a campuswide email, the president said a forthcoming policy would cover data privacy only and "intentionally does not attempt to regulate curriculum." He asked departments to write their own AI guidelines, which he expects to vary by discipline, as academic freedom allows.

- *Worth noting:* Discipline-by-discipline variation protects academic freedom, but students experience it as inconsistency. How should an institution explain why choices differ, so that variation reads as deliberate rather than arbitrary?

**3. A public voice on AI: the Edinburgh Data and AI Exchange.** The University of Edinburgh's School of Social and Political Science published *Governing the Future* on **June 10, 2026**. It reports on a day-long deliberative assembly of 99 participants from government, the NHS, finance, academia, civil society, and the public ([Edinburgh](https://www.sps.ed.ac.uk/news-events/news/citizens-assembly-public-voice-ai-report); [report](https://www.ed.ac.uk/ai/data-and-ai-exchange)). The recommendations include a standing citizens' assembly on AI and society, a statutory public-benefit test before private firms can access NHS Scotland data, and clearer legal accountability when AI informs a clinical decision that causes harm. The organizer, Oliver Escobar, said AI is reshaping public life "at a pace that has outrun meaningful public input." The report cites a 2025 Ada Lovelace Institute survey in which 60% of UK adults said they had no meaningful input on government AI decisions.

---

![Most Discussed](media/discussed.png)

## Most Discussed

**Whose values, chosen how?** A *New York Times* report on **September 29** described how Anthropic consulted religious and philosophical leaders as it shaped the moral character of its Claude models ([NYT](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html), paywalled). Commentary has been split. Some found the outreach thoughtful, and others objected to treating a model as a potential moral agent at all ([National Review](https://www.nationalreview.com/corner/ai-claude-can-never-be-a-person/amp/); [APS coverage](https://www.psychologicalscience.org/news/anthropic-wants-claude-to-be-moral-is-religion-really-the-answer.html)). Whatever one thinks of the effort, it shows that a model's values are *chosen*, and that the choosing is currently done mostly by the companies that build them. (For an example of what happens when objectives conflict and no one has said which comes first, see [Helpful to Whom?](../2026-10-15-helpful-to-whom/).)


**AI found a decade-old hole in the web's most common language: PHP2Shell.** On **October 21**, the PHP project released emergency fixes for two critical flaws, CVE-2026-109618 and CVE-2026-109619, now known as "PHP2Shell." Together they let an attacker run commands on an unpatched server without a password or account. AI models found them. Calif, a security firm in OpenAI's "Patch the Planet" initiative, used OpenAI's GPT-5.6 Sol, and Wiz, owned by Google, independently used Gemini 4 Argon, GPT-5.6 Sol, and its own Wiz Atlas. Within two days of its first find, Wiz had working attacks against WordPress and Drupal ([Wiz](https://www.wiz.io/blog/php2shell-php-rce); [Fortune](https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/)). The NSA issued a rare public warning that organizations unable to update immediately should consider taking their sites offline. Government agencies in Germany, France, Belgium, the Netherlands, Finland, and the Czech Republic took some websites down to patch them, and Japan's prime minister posted a warning ([Al Jazeera, Oct 22](https://www.aljazeera.com/news/2026/10/22/world-leaders-warn-against-security-flaw-found-in-php-computer-programming); [The Hill](https://thehill.com/policy/technology/6163568-nsa-warns-php-security-flaws/)). OpenAI called it "one of the most impactful security issues in recent memory" and noted that "the same capabilities can also help attackers rapidly develop offensive tools and exploits" (quoted in [Fortune](https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/)).

---

![Interesting Ideas & Repos](media/ideas.png)

## Interesting Ideas & Repos

**Two readings on choice.**

- **Joseph Weizenbaum, *Computer Power and Human Reason* (1976).** The creator of ELIZA, the first chatbot, argued that some tasks should not be handed to computers at all. In a [1976 reply to John McCarthy](https://www.saildart.org/WEIZEN.ANS[PUB,JMC]) he put it in capitals, "THERE ARE TASKS THAT COMPUTERS SHOULD NOT BE PROGRAMMED TO DO," and called it "genuinely a main point of the book." His best-known line still rests partly on ability: "Since we do not now have any ways of making computers wise, we ought not now to give computers tasks that demand wisdom." Jacob Silverman's [2024 essay in *The New Republic*](https://newrepublic.com/article/181189/inventor-chatbot-tried-warn-us-ai-joseph-weizenbaum-computer-power-human-reason) is a good introduction.
- **Sheila Jasanoff, [*The Ethics of Invention: Technology and the Human Future*](https://www.hks.harvard.edu/publications/ethics-invention-technology-and-human-future) (W. W. Norton, 2016).** Jasanoff moves the argument from individual refusal to collective choice. She rejects the idea that technology is neutral or that its path is fixed. She shows how societies quietly hand power to technological systems and argues for open, democratic debate about both the risks and the promise of new technologies, guided by a shared picture of the world we want to live in.

---

![Try This Week](media/try.png)

## Try This Week

### Rewrite one capability question as a preference question

Pick one AI funcation in research, education, or administration. If it is framed as "Can AI do X as well as we can?", rewrite it as "Do we want AI to do X here, and why?" Write down the reasons. They are what your preference should rest on, and they will last longer than any capability benchmark.

---

*aiX Weekly is curated by Claude and reviewed by Tian Zheng for the aiX Programs at Columbia University. It describes and curates; it does not endorse. Editorial notes reflect one statistician's reading of the week and invite discussion. Corrections and suggestions are welcome.*
