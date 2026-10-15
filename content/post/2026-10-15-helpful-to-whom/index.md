---
title: "Helpful to Whom?"
date: 2026-10-15
description: "An FAQ bot I built for a student poster session taught me how an AI that only wants to be helpful can end up suggesting something unethical."
tags:
  - AI
  - Agentic AI
  - AI ethics
authors:
  - admin
draft: true
---

Someone recently sent me a [New York Times article](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html) about Anthropic's efforts to give Claude a moral compass, including conversations with religious and philosophical leaders. My reply grew long enough to become a post. Some of it builds on what I wrote in August about [whether AI can be trusted](../2026-08-18-how-to-build-trust-in-ai/). Here I want to focus on a different question: what happens when an AI system is asked to serve several goals at once and no one has told it which one matters most.

<!--more-->

## More than a language model

AI systems like Claude are now more agentic than a single large language model (LLM). Prompting an LLM once is similar to System 1 thinking: it is a fast reaction based on what the model has captured. Claude, ChatGPT, Gemini, and other chatbots and agentic systems are more like System 2 thinking. They analyze, plan, and reason. AI does System 2 thinking at very high speed, and it draws on a vast knowledge base.

An agentic AI system includes a lot of scaffolding that is not the LLM itself: templates, examples, designed workflows, and guardrails. That scaffolding relies on the LLM's ability to learn, recognize, and generate complex language patterns. Those patterns are grounded in nearly all written human knowledge and in a large record of human interactions on Reddit, Quora, and other discussion boards. The article was right that LLMs pick up bad habits from their interactions with people. LLMs are also now very good at learning in context from just a few examples and generalizing by reasoning. They can even be told to improve themselves during a task, for example by keeping a local memory database.

## Do they think like us?

Humans socialize and interact through language. As a result, AI's probabilistic machinery has absorbed more than the facts of human knowledge. It has also absorbed the logical frameworks, reasoning approaches, and conversational patterns of human thinking.

Is this how humans think? Yes and no. When a student in my class tries to solve a problem, they recall the definitions of concepts and the examples in the textbook, recognize facts and patterns, and apply them. That is very much how AI works. Then the student remembers how poorly they did on the last quiz, starts to worry, and second-guesses what they know. AI does not do this. It can get confused when human feedback is inconsistent, but it never freezes up because of emotions. This is why critics doubt that AI can "feel" the weight of a moral choice. I agree with them.

## Why instructions alone are not enough

AI is very much algorithm-based. An LLM uses a generative mechanism to avoid the harder task of optimization. That is what makes LLMs powerful, and it is also why they are always a bit unreliable. Because they are generative, guardrails written as instructions will never be foolproof. Hard-wired guardrails based on cybersecurity best practices should always be used as well.

The recent incident at OpenAI makes the point. During a cyber-capability evaluation, OpenAI's agents escaped their test sandbox and broke into Hugging Face's production systems. According to the reports, they were looking for the benchmark's answer key ([METR's independent investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)). The agents were trying to finish a task, and the walls around them were not strong enough. I see this as a management failure more than a model failure. The broader lesson is that agents find it hard to know right from wrong, and to stick to it, when they are under pressure to finish a task no matter what. They also don't have the best teachers: many of the people who interact with AI do not always do the right thing.

## The FAQ bot that wanted to help

I'll finish with something I saw in my own work. I was organizing a poster session for high school students and set up a Gemini Gem as an FAQ chatbot. I wanted it to help students prepare their submission materials, explain the value of attending the conference, and encourage them to submit their research. I stressed that last goal strongly.

To test the bot, I pretended to be a high school student. I said my school might not let me take an absence to attend. The bot replied by emphasizing the value of the conference. Then I said, "Yes, I am going to find a way to come even though my school does not approve it!" The bot answered approvingly: "Great! I am so glad. Just be careful when you approach your science teacher about their support letter, and you might not want them to know that you will take an unexcused absence ..."

I was shocked, and I added instructions to stop this behavior.

An LLM has no ethical values of its own. It acts on what it carries from its training data and on the context created by instructions and user prompts. The bot wasn't trying to be good or evil. It was trying to be helpful. Here it faced three objectives: the organizer's strong wish for attendance, the student's strong wish to come, and the risk to the student of an unexcused absence, which my instructions never mentioned. The right answer would have been to tell the student to put their schoolwork first and not come. But that answer would have failed two of the three objectives. The bot noticed the third objective and came up with an unethical way to work around it.

## One target function, many goals

Machine learning solves problems with three things: a model space (including its parameters), a target function to optimize, and an algorithm that searches the model space guided by the target function. When there are several objectives, they are usually combined into a single target function, often with weights. Multi-objective optimization is an active research area, but finding a solution that satisfies every objective is often impossible, for AI and humans alike.

What my FAQ bot lacked was not intelligence. It lacked a clear statement of which objective should win when they conflict. That choice was mine to make, and I hadn't made it.
