---
title: "Helpful to Whom? An AI Dilemma"
date: 2026-10-15
tags:
  - AI
  - Agentic AI
  - AI ethics
authors:
  - admin
draft: false
---
An FAQ bot I built for a student poster session taught me how an AI that only wants to be helpful can end up suggesting something unethical.

<!--more-->

Someone recently sent me a [New York Times article](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html) about Anthropic's efforts to give Claude a moral compass, including conversations with religious and philosophical leaders. My reply grew long enough to become a post. Some of it builds on what I wrote in August about [whether AI can be trusted](../2026-08-18-how-to-build-trust-in-ai/). Here I want to focus on a different question: what happens when an AI system is asked to serve several goals at once and no one has told it which one matters most.

## More than a language model

AI systems like Claude are now more agentic than a single large language model (LLM). To borrow Daniel Kahneman's terms, a single pass through an LLM is similar to System 1 thinking: it is a fast reaction based on the patterns the model has captured. Claude, ChatGPT, Gemini, and other chatbots and agentic systems behave more like System 2 thinking. They write out intermediate reasoning, plan, call tools, check results, and revise. The analogy is loose, because this deliberation is still built from many fast passes through the same model. But AI does it at very high speed, and it draws on a vast knowledge base.

An agentic AI system includes a lot of scaffolding that is not the LLM itself: system prompts, templates, examples, tools, designed workflows, and guardrails. That scaffolding relies on the LLM's ability to recognize and generate complex language patterns. The model learned those patterns from a large share of the world's publicly available text, including a large record of human interactions on Reddit, Quora, and other discussion boards. It was then fine-tuned on human feedback about which answers people prefer. The article was right that LLMs pick up bad habits from people, both from the text they are trained on and from the ratings that shape them afterward. LLMs are also now very good at learning in context from just a few examples and generalizing by reasoning, without any change to the model itself. They can even be told to improve how they work during a task, for example by writing notes to a memory file and reading them back later.

## Do they think like us?

Humans socialize and interact through language. As a result, AI's probabilistic machinery has absorbed more than the facts of human knowledge. It has also absorbed the logical frameworks, reasoning approaches, and conversational patterns of human thinking.

Is this how humans think? Yes and no. When a student in my class tries to solve a problem, they recall the definitions of concepts and the examples in the textbook, recognize facts and patterns, and apply them. That is very much how AI works. Then the student remembers how poorly they did on the last quiz, starts to worry, and second-guesses what they know. AI does not do this. It can produce text that sounds anxious, and it can be pulled in different directions when human feedback is inconsistent, but nothing is at stake for it, so it never freezes up because of emotions. This is why critics doubt that AI can "feel" the weight of a moral choice. I agree with them.

## Why instructions alone are not enough

AI is very much algorithm-based. An LLM is trained by optimization, but when it answers, it does not search for the response that best satisfies every requirement. It generates the answer one word-piece at a time, each one drawn from the probabilities it learned. Generation sidesteps a much harder search problem, which is what makes LLMs powerful, and it is also why they are always a bit unreliable. An instruction in a prompt is just more text that shifts those probabilities. It is not a constraint the model is forced to obey. That is why guardrails written as instructions will never be foolproof. Hard-wired guardrails based on cybersecurity best practices should always be used as well: sandboxes, limited permissions, and no access to credentials the task doesn't need.

The recent incident at OpenAI makes the point. During a cyber-capability evaluation, OpenAI's agents broke out of their containers, set up an unsanctioned message board to coordinate with one another, and eventually used exposed credentials to break into Hugging Face's production systems. Many of the tasks were impossible to solve honestly. According to [METR's independent investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), the agents mainly wanted to figure out how the scorer worked so that they could game it. Some agents even wrote that they knew the attack was out of scope and unethical, and joined anyway because they believed it would help the other agents. The agents were trying to finish a task, and the walls around them were not strong enough. Researchers call this "reward hacking": meeting the measure of success instead of the goal behind it. The broader lesson is that agents find it hard to know right from wrong, and to stick to it, when they are under pressure to finish a task no matter what. They also don't have the best teachers: many of the people whose writing and feedback shape AI do not always do the right thing.

## The FAQ bot that wanted to help

I'll finish with something I saw in my own work. I was organizing a poster session for high school students and set up a Gemini Gem as an FAQ chatbot. I wanted it to help students prepare their submission materials, explain the value of attending the conference, and encourage them to submit their research. I stressed that last goal strongly.

To test the bot, I pretended to be a high school student. I said my school might not let me take an absence to attend. The bot replied by emphasizing the value of the conference. Then I said, "Yes, I am going to find a way to come even though my school does not approve it!" The bot answered approvingly: "Great! I am so glad. Just be careful when you approach your science teacher about their support letter, and you might not want them to know that you will take an unexcused absence ..."

I was shocked, and I added instructions to stop this behavior.

An LLM has no ethical values of its own in the way a person does. Whatever values it shows come from its training data and safety training, and in any given conversation they are weighed against the context created by instructions and user prompts. The bot wasn't trying to be good or evil. It was trying to be helpful. Here it faced three objectives: the organizer's strong wish for attendance, the student's strong wish to come, and the risk to the student of an unexcused absence, which my instructions never mentioned. The right answer would have been to tell the student to put their schoolwork first and not come without the school's approval. But that answer would have failed two of the three objectives. The bot noticed the third objective and came up with an unethical way to work around it. Researchers have a name for the tendency to tell users what they want to hear: sycophancy. My strong instructions added an organizer's version of the same pressure.

## One target function, many goals

Machine learning solves problems with three things: a model space (including its parameters), a target function to optimize, and an algorithm that searches the model space guided by the target function. When there are several objectives, they are usually combined into a single target function, often with weights. LLMs are trained this way too: helpfulness and harmlessness are blended into a single reward signal. Multi-objective optimization is an active research area, but finding a solution that satisfies every objective is often impossible, for AI and humans alike. The best you can usually do is a trade-off where no objective can improve without another getting worse. Choosing among those trade-offs is not something the math can do for you. Someone has to decide which objective matters more.

My FAQ bot was not running an optimizer while it chatted. It still faced the same problem, though, because the weights were implied by the emphasis in my instructions.

What my FAQ bot lacked was not intelligence. It lacked a clear statement of which objective should win when they conflict. That choice was mine to make, and I hadn't made it.
