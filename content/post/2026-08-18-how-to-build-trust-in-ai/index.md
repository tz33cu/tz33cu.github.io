---
title: "Can AI be trusted?"
date: 2026-08-18
draft: false
math: true
authors:
  - admin
tags:
  - AI
  - aiX
  - Agentic AI
summary: "AI keeps getting more capable, yet trusting it still feels difficult. What, exactly, should we trust: the model, the process around it, or the evidence it produces? A field guide to alignment, grounding, guardrails, harnesses, and explainability through a probabilistic lens."
---

AI systems have become remarkably capable. Yet our confidence in them has not grown at the same pace. Something still feels amiss.

Maybe "Can we trust AI?" is too broad a question. Are we trusting the model, the process around it, or the evidence supporting a particular result?

These questions became concrete while I was teaching [a short course on agentic AI at the STAI-X 2026 conference](https://statsupai.org/STAIX2026/short-courses.html#sc1) ([slides](https://docs.google.com/presentation/d/e/2PACX-1vTgzFQgnBTbxxOy4-0FOmMIkiAZrLgEdNKdaX8LSz_X6Estxbn0w2j1Lgs9vpGql7nDLZBoM9hFTuw4/pub?slide=id.p1), [open-source GitHub repository](https://github.com/TZstats-Columbia/STAI-X2026-AgenticAI-ShortCourse)). One design question kept coming up: **Which decisions shape what an agent can generate and do, and do those decisions match our intention?**

Two ideas were built into the course, and they kept surfacing as we worked through the exercises:

1. **Design the boundaries around generation and use.** Choices about the model, context, decoding, tools, permissions, and approval rules steer or constrain what a system can generate and do. Choices about review and application determine how those generations enter human decisions. Make both sets of choices intentional and visible.
2. **Demand evidence you can verify.** Confidence and a fluent account of reasoning provide weak evidence of reliability. Ask for sources, calculations, and intermediate artifacts you can inspect independently.

<!--more-->

To see why these ideas matter, let's start with the source of a large language model's flexibility.

In recent conversations about generative AI, I kept hearing a familiar description of a large language model (LLM):

> It generates the next token from a conditional probability distribution.

That description is correct, though it is only the starting point. The model has learned an approximation to a conditional distribution over possible continuations. This statistical perspective predates language models: linear regression estimates a conditional mean, while time-series models estimate a distribution over the next observation given the past. As Box and Draper put it, "Essentially, all models are wrong, but some are useful" (1987, p. 424; see also Box, 1976). An LLM's distribution can likewise be misspecified or biased. The decoding procedure then determines how a continuation is selected from that distribution. It may sample among alternatives or choose deterministically. In a multistep agent, each choice becomes part of the context for later steps, so small differences can ripple through an entire run.

If the distribution is conditional, **what exactly is it conditional on?** What space of possibilities does that conditioning create or rule out? And how should a person evaluate the output when that space can shift from one step to the next?

This helps explain why reliability remains such a practical concern. In an [ICML keynote](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work), [Arvind Narayanan](https://www.cs.princeton.edu/~arvindn/) argued that reliability should be measured separately from capability because the two can improve at different rates. The concern also appears in users' experiences. An [Anthropic study of 80,508 voluntary participants with Claude accounts](https://www.anthropic.com/features/81k-interviews) found that unreliability was the most commonly reported concern. It appeared in 26.7% of interviews and included hallucinations, inaccuracies, fake citations, and the burden of verification.

The same flexibility that makes generative AI useful also creates variation. Trustworthy design begins with deliberate choices about how much flexibility a task should allow, how the distribution should be steered or bounded, and how the resulting generations may be used.

Here is the path through the rest of the post. We will first examine the decisions that condition, steer, and bound generation, along with those that govern an agent's actions and the use of its output. We will then turn to the evidence needed to evaluate a particular result. From there, we will clarify what alignment, grounding, guardrails, harnesses, and explainability each contribute. We will end by distinguishing trust in a process from confidence in an outcome and asking how to keep AI's flexibility visible.

## Part 1: Decisions that shape generation and use

### What conditions the next token?

We can write next-token generation schematically as:

$$
P_\theta(t_{i+1}\mid C)
$$

Here, $C$ is the context available when the model generates the next token, and $\theta$ represents the model learned through training and post-training.

You might think of $C$ as the prompt typed into a chat box. In practice, the context available to the model may be much larger. It can include:

- system or developer instructions that the user did not write;
- the preceding conversation;
- retrieved documents or other material added by a knowledge system;
- outputs from tools such as search, code execution, or databases; and
- instructions that constrain format, tone, safety, or permissible actions.

The model responds to the user's prompt as part of a larger, augmented, and constrained context. Retrieval-augmented generation provides one concrete example: retrieved passages are supplied as additional information on which generation is conditioned ([Lewis et al., 2020](https://arxiv.org/abs/2005.11401)).

There is another source of difference too. Two models given the same visible prompt and supplemental context may still assign different probabilities to possible continuations. Their parameters, $\theta$, reflect different training data, architectures, fine-tuning, preference optimization, and other design choices. Work on [instruction tuning with human feedback](https://arxiv.org/abs/2203.02155) and [Constitutional AI](https://arxiv.org/abs/2212.08073), for example, shows how post-training changes model behavior. Training data shapes the model that interprets the context, even though it is usually absent from the context window itself.

This gives us two complementary questions:

1. **What information and instructions are conditioning this particular generation?**
2. **What model is doing the conditioning, and how was its behavior shaped?**

Together, these questions distinguish among models, interfaces, and deployments that might otherwise be grouped under "the LLM."

Each answer reflects a design decision. Training and post-training shape $\theta$. System instructions, retrieved material, memory, and tool results shape $C$. Decoding rules determine how the system selects among possible continuations. These choices steer or bound the conditional distribution from which a generation emerges. They also determine which parts of that process a user can see.

### Generation creates a space of flexibility

A prompt rarely determines a single continuation. It helps shape a space of possibilities, each with a different probability. Decoding choices affect how the system moves through that distribution. For example, top-*p*, or nucleus, sampling draws from a probability mass whose size changes with the distribution at each step ([Holtzman et al., 2020](https://arxiv.org/abs/1904.09751)).

Natural language adds even more room for interpretation. Unlike a fully specified mathematical expression, instructions such as "keep it brief," "focus on what matters," or "make it easy to understand" leave important dimensions unstated. A model can generate quite different, individually plausible interpretations of the same instruction depending on the audience, goal, and context it is given.

That room to generate is useful. It allows a model to translate, brainstorm, reframe, compare, draft, and explore.

So I find this question more useful: **Do I understand the room the system's design has given the model?**

When I delegate research to a colleague or student, I may give them considerable flexibility. I become uneasy when I cannot see where they exercised judgment, what assumptions they made, or how they moved from evidence to conclusion. The same concern applies to AI.

### Agentic AI raises the stakes on this question

An agent may plan, call tools, retrieve and write files, chain steps together, and decide when it is done. Depending on its harness, it may also compact earlier exchanges or select information to retain in memory. These less-visible operations alter the context available later, so a quiet choice about what to retain can shape everything downstream. Anthropic's work on [long-running agent harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), for example, describes compaction and the use of progress files and version history to preserve context across sessions.

This is why we kept returning to **decision boundaries around generation and use**. I use the phrase in a practical design sense, distinct from the boundary of a statistical classifier. One boundary concerns generation: what information conditions the model, how the distribution is steered, and which outputs are constrained or excluded. A second concerns action: which tools the agent may use, what it may change, and when it must ask for approval. A third concerns use: how people will review, interpret, and act on what the system produces.

These boundaries emerge from many choices made by model developers, system designers, institutions, and users. Some are embedded upstream in training or post-training. Others appear in prompts, retrieval systems, decoding settings, guardrails, tool permissions, memory rules, and escalation policies. Before handing over a task, ask who made each of these decisions, which decisions remain with the agent at runtime, and where consequential use requires human review.

Agentic AI adds a complication to the delegation analogy. People can flag uncertainty or say that a task exceeds their mandate, though they do not always do so. An agent may continue by filling gaps with generated assumptions. Its authority and escalation rules therefore need to be explicit and observable.

Visible decision boundaries show how an agent's discretion was constructed and where human review enters. Evaluating a particular result then requires concrete evidence that a person can inspect. This takes us from designing the space of generation and action to examining what the agent produced.

## Part 2: Build confidence through evidence

### Request an evidence trail

Imagine receiving a polished, confident analysis. It may sound expert because the model has learned patterns from textbooks, papers, and other training material. The practical question is: **What can it provide that would help a person evaluate the result?**

My own rule is simple: keep asking the AI to convince me. If it says it performed an analysis, I ask:

- What assumptions did you make?
- Which facts or passages mattered most to your conclusion?
- What steps would I follow to reproduce this analysis manually?
- What calculations, intermediate outputs, or comparisons support the result?
- Which sources support each substantive claim?
- What plausible alternatives did you consider, and why did you reject them?
- What evidence would change your conclusion?

One caveat matters here. A model-generated explanation is not necessarily a faithful account of the computation that produced its answer. Experiments have shown that stated reasoning can omit influential information or rationalize an answer after the fact ([Lanham et al., 2023](https://arxiv.org/abs/2307.13702); [Turpin et al., 2023](https://arxiv.org/abs/2305.04388)). I have also seen a model generate a chart and statistics that it claimed supported its conclusion even though the chart contradicted its description.

That is why I treat the explanation as **an inspectable set of claims**. Open the sources. Check the quotations. Rerun the calculations. Compare a plot with its description. Challenge assumptions and test alternatives.

What we want are artifacts a person can verify.

### Cross-examine the result

I find it useful to treat a polished AI answer as testimony to examine.

In practice, that workflow might look like this:

1. **Define the task and the permissible flexibility.** State what the model may infer, which assumptions are prohibited, and where exactness matters.
2. **Request an initial analysis.** Use the model's generative flexibility to explore the problem and identify possibilities.
3. **Request an evidence packet.** Ask for sources, key passages, assumptions, intermediate artifacts, calculations, alternatives, and uncertainty.
4. **Cross-check outside the model's prose.** Inspect primary sources, reproduce computations, compare outputs across prompts or models, and test whether the evidence actually supports the conclusion.
5. **Make and own the judgment.** Revise, reject, or adopt the output based on that review.

Over time, this can become a reusable template. Instead of simply asking the AI to "analyze this," we can ask it to return an analysis together with a structured evidence sheet. We can then improve the template as we learn which evidence is genuinely useful for review.

This process keeps responsibility in the right place. Whether a researcher, teacher, analyst, or decision-maker consults a colleague, textbook, or language model, the final judgment still belongs to the person accountable for the work. AI can widen the space we explore while leaving that responsibility intact.

The workflow above gives us three ingredients for trustworthy use: bounded discretion, inspectable evidence, and accountable judgment. The vocabulary of trustworthy AI names the mechanisms that support them. Seeing where each mechanism acts helps the pieces fit together and shows why no single technique can establish trust on its own.

## A vocabulary for trustworthy AI

Discussions of trustworthy AI often bundle together *alignment*, *grounding*, *guardrails*, *harnesses*, and *explainability*. The terms overlap, but they act on different parts of a system. As a working synthesis, the equation $P_\theta(t_{i+1}\mid C)$ gives us a useful high-level map, even though the categories blur in practice.

- **Training and post-training** change the model parameters, $\theta$.
- **Before and during inference**, a system assembles the context $C$, retrieves information, filters inputs, and may constrain decoding.
- **After generation**, a system can verify, redact, rewrite, route, or reject an output.
- **Across a multistep run**, an agent harness manages repeated model calls, tool calls, state, permissions, retries, and stopping rules.

Guardrail literature describes controls that monitor or filter model inputs and outputs, along with systems that constrain generation while it is underway ([Dong et al., 2025](https://doi.org/10.1007/s10462-025-11389-2)). A concrete pipeline may combine several of these functions; Wildflare GuardRail, for example, includes input-safety detection, grounding, output checks, and repair ([Han et al., 2025](https://arxiv.org/abs/2502.08142)). In practice, many techniques span more than one stage.

**Alignment** is the broad goal of making an AI system behave in accordance with intended values, instructions, and constraints. Methods such as [reinforcement learning from human feedback](https://arxiv.org/abs/2203.02155) and [Constitutional AI](https://arxiv.org/abs/2212.08073) alter $\theta$ during post-training. In this post, I use *alignment* more broadly than parameter adjustment alone. Alignment research may also evaluate whether trained or deployed systems exhibit the intended behavior and study how they can be steered or controlled; [Anthropic's Alignment Science program](https://alignment.anthropic.com/) illustrates that broader usage.

**Grounding** connects a response to external information relevant to the task. A system might retrieve documents before a model call, query a database or calculator during an agentic run, and retain provenance for the material it supplies. Retrieval-augmented generation is one influential implementation ([Lewis et al., 2020](https://arxiv.org/abs/2005.11401)) and is now used as a practical pattern for grounding responses in external content ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)). Grounding can improve factual support, but retrieval quality, source quality, and faithful use of the evidence still need evaluation.

**Guardrails** enforce policies at the system boundary. Input guardrails can detect unsafe requests or sensitive data; controls applied during generation can restrict possible outputs; and output guardrails can block, redact, repair, or route a response for review ([Dong et al., 2025](https://doi.org/10.1007/s10462-025-11389-2); [Han et al., 2025](https://arxiv.org/abs/2502.08142)). Their contribution depends on coverage and accuracy. A guardrail may miss a harmful output or block a legitimate one.

**A harness** is the surrounding software that turns model calls into an agentic workflow. Here, the term includes the software that assembles context, exposes tools, stores state, applies permissions, handles failures, and determines when to continue or stop. In Anthropic's experiments with long-running coding agents, progress files, version history, incremental work, and clean handoffs helped agents recover from errors and continue across context windows (["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)).

**Explainability** is an umbrella term for methods that help people understand a model or its output. A model-generated explanation is one such method, and it calls for special caution. Asking "why?" usually produces another generation conditioned on the conversation and answer. As the chain-of-thought studies cited above show, we still have to test whether that explanation faithfully reflects factors that affected the answer. Other forms of explainability, including attribution and mechanistic interpretability, study model behavior more directly and deserve separate treatment.

![An agentic loop in which human decisions set the task, constraints, authority, approvals, and use of outputs; grounding feeds the context; alignment shapes model behavior; guardrails and approval gates check proposed steps; tools return observations; and the harness records an evidence trace for human review.](diagram-vocabulary-pipeline.svg?rev=20260818-3)

*Figure 1. Where trust-building mechanisms act in an agentic loop.*

This vocabulary brings us back to the two practical questions from the beginning. None of these mechanisms configures itself. People decide which behavior to encourage through alignment, what evidence to add through grounding, which policies guardrails should enforce, what authority the harness should grant, where approval is required, and what explanations and evidence the system must preserve. Those choices shape the conditional distribution, the agent's permitted actions, and the eventual use of its generations. Together, they form the system's decision boundaries and give us a basis for assessing whether a result deserves confidence.

## Trust in a process and confidence in an outcome

Trust is relational. It depends on who is relying on a system, what they are using it for, and what they stand to lose if it fails ([Blanco, 2025](https://doi.org/10.1007/s43681-025-00690-z); [Durán & Pozzi, 2025](https://doi.org/10.1007/s13347-025-00843-2)). From this perspective, a benchmark score can inform the relationship, but it cannot describe the trustor's purpose, vulnerability, or consequences of failure.

Lee and See's influential account of trust in automation distinguishes three bases of trust: *performance* (what the system does), *process* (how it works), and *purpose* (why it was built) ([Lee & See, 2004](https://pubmed.ncbi.nlm.nih.gov/15151155/)). For this discussion, I find a related distinction helpful: confidence in a recurring *process* and confidence in a particular *outcome* require different evidence.

Confidence in a process grows through evaluation across many representative cases. It depends on a track record, known failure modes, monitoring, and evidence that the surrounding controls work. Once established, it can reduce the scrutiny required for routine cases, though high-stakes uses still warrant review.

Confidence in an outcome comes from evidence about the result at hand. We inspect its sources, rerun its calculations, examine alternatives, and ask whether the conclusion follows. This is the work described in Part 2, and it can be done even when the underlying process is new or imperfectly understood.

We already use both forms of confidence in everyday life. A colleague earns process trust over years of reliable work; a new colleague can still earn confidence in one memo through transparent methods and sound evidence. Alignment, guardrails, evaluations, and harness design can strengthen confidence in a process. Grounding, provenance, and inspectable artifacts can strengthen confidence in an outcome. Explainability may contribute to either, depending on the method and whether its claims can be validated.

![Two evidence streams support a reliance decision. Process evidence establishes baseline confidence in a workflow, while outcome evidence establishes confidence in the current result. These combine and are compared with a threshold set by the stakes and reversibility of the task.](diagram-trust-kinds.svg)

*Figure 2. Two evidence streams support one reliance decision.*

## Statistical thinking for more trustworthy AI

Statistical thinking gives us a practical way to connect generative flexibility with appropriate trust. An AI output is one realization from a conditional, imperfect model. Reliability can vary across tasks and contexts, and each step in an agentic workflow creates another opportunity for an assumption, retrieval, or generated choice to affect what follows. Seen this way, familiar statistical questions come to the front: What generated this result? What variation should we expect? Which assumptions matter? What evidence would change our conclusion?

The mechanisms discussed above become more useful when viewed through this lens. We can ask whether they reduce relevant errors across representative cases, preserve evidence and provenance, reveal uncertainty, and help a system recover when something goes wrong. We can also match the level of human review to the stakes, reversibility, and cost of failure.

Statistical thinking should therefore sit at the center of AI education. Students and practitioners need habits for reasoning under uncertainty, testing claims against evidence, and calibrating confidence to the decision at hand. Those habits provide a durable foundation for evaluating new models and tools, while keeping people accountable for the judgments made with them.

---

**References and further reading**

- S. Huang et al. (2026), ["What 81,000 People Want from AI."](https://www.anthropic.com/features/81k-interviews) Anthropic.
- A. Narayanan (2026), ["What will be left for us to work on?"](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work), ICML 2026 keynote transcript.
- G. E. P. Box (1976), ["Science and Statistics,"](https://doi.org/10.1080/01621459.1976.10480949) *Journal of the American Statistical Association*, 71(356), 791–799.
- G. E. P. Box & N. R. Draper (1987), *Empirical Model-Building and Response Surfaces*. Wiley, p. 424.
- A. Holtzman, J. Buys, L. Du, M. Forbes, & Y. Choi (2020), ["The Curious Case of Neural Text Degeneration."](https://arxiv.org/abs/1904.09751) *International Conference on Learning Representations*.
- L. Ouyang et al. (2022), ["Training language models to follow instructions with human feedback."](https://arxiv.org/abs/2203.02155)
- Y. Bai et al. (2022), ["Constitutional AI: Harmlessness from AI Feedback."](https://arxiv.org/abs/2212.08073)
- Anthropic, [Alignment Science](https://alignment.anthropic.com/), ongoing research program and blog.
- P. Lewis et al. (2020), ["Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."](https://arxiv.org/abs/2005.11401)
- Microsoft (2026), ["Retrieval-augmented generation (RAG) in Azure AI Search."](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- S. Han, S. Avestimehr, & C. He (2025), ["Bridging the Safety Gap: A Guardrail Pipeline for Trustworthy LLM Inferences."](https://arxiv.org/abs/2502.08142)
- Y. Dong et al. (2025), ["Safeguarding Large Language Models: A Survey."](https://doi.org/10.1007/s10462-025-11389-2) *Artificial Intelligence Review*, 58, article 382.
- Anthropic (2025), ["Effective harnesses for long-running agents."](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- T. Lanham et al. (2023), ["Measuring Faithfulness in Chain-of-Thought Reasoning."](https://arxiv.org/abs/2307.13702)
- M. Turpin et al. (2023), ["Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting."](https://arxiv.org/abs/2305.04388)
- J. D. Lee & K. A. See (2004), ["Trust in Automation: Designing for Appropriate Reliance,"](https://pubmed.ncbi.nlm.nih.gov/15151155/) *Human Factors*, 46(1), 50–80.
- S. Blanco (2025), ["Human Trust in AI: A Relationship Beyond Reliance."](https://doi.org/10.1007/s43681-025-00690-z) *AI and Ethics*, 5, 4167–4180.
- J. M. Durán & G. Pozzi (2025), ["Trust and Trustworthiness in AI."](https://doi.org/10.1007/s13347-025-00843-2) *Philosophy & Technology*, 38, article 16.
