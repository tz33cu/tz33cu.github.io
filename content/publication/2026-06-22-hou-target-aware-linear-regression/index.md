---
title: 'Target-Aware Linear Regression Under Distribution Shift'
authors:
- zhewenhou
- admin
author_notes: []
date: '2026-06-22'
publishDate: '2026-10-22T00:00:00Z'
publication_types: ["article"]
publication: '*arXiv preprint arXiv:2606.22775*'
publication_short: ''
doi: 10.48550/arXiv.2606.22775
abstract: 'Distribution shift between training and deployment is a pervasive challenge for modern AI systems. In many cases, the target marginals of covariates and response are known or specified through population-level observations, boundary conditions, properties of simulator configurations, or alignment-time distributional constraints. Such knowledge may provide valuable side information for regression estimation. We study this problem in the multivariate linear regression setting with a stable conditional mean $E[Y\mid X]$ across source and target, and identify the hybrid-loss estimator, which jointly incorporates both target marginals, as a benchmark target-aware estimator. Its direct computation, however, requires solving a coupled nonlinear optimization that is expensive at scale. Our main contribution is to develop and evaluate two computationally tractable alternatives: a constrained moment-matching estimator and a two-stage estimator that augments ordinary least squares with a calibration step. For all three estimators, we derive and compare closed-form asymptotic mean squared errors, yielding conditions under which the tractable alternatives match or closely approximate the hybrid benchmark, and regimes in which they do not. Monte Carlo experiments across three controlled shift regimes validate the theoretical results, investigate the accuracy-runtime tradeoffs among the three estimators, and translate into guidance on estimator choice. In particular, the two-stage estimator nearly matches the hybrid benchmark in the high signal-to-noise regime at essentially no additional cost, providing theoretical grounding for empirical observations in nonlinear settings.'
summary: ''
tags:
- Statistics
- Machine Learning
featured: false
url_pdf: 'https://arxiv.org/pdf/2606.22775'
url_code: 'https://github.com/TZstats-Columbia/target-aware-linear-regression'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
links:
- name: arXiv
  url: https://arxiv.org/abs/2606.22775
- name: GitHub (TZstats-Columbia)
  url: https://github.com/TZstats-Columbia/target-aware-linear-regression
---
