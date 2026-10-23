---
title: Graph-Enabled Efficient Federated Bayesian Modeling
authors:
- chenyangzhong
- shouxuanji
- admin
author_notes: []
date: '2024-08-01'
publishDate: '2026-06-01T00:00:00Z'
publication_types: ["article"]
publication: '*arXiv preprint arXiv:2408.02122*'
publication_short: ''
doi: 10.48550/arXiv.2408.02122
abstract: 'Federated Bayesian modeling requires combining evidence across distributed data holders while preserving posterior uncertainty and keeping local data decentralized. We propose Federated Latent Graph MCMC (FLaG-MCMC), a framework for sequential posterior transfer in which accumulated posterior information is represented by a reservoir of Monte Carlo samples. FLaG-MCMC constructs a graph that captures the geometry of the posterior reservoir and uses graph-enabled proposals whose per-iteration cost is independent of the reservoir size. Each data holder updates the inherited posterior using its local likelihood and returns an updated reservoir for subsequent inference. We apply FLaG-MCMC in two health science settings. Using mobile and wearable device data from GLOBEM, we investigate associations between depression status and behavioral patterns while sequentially accumulating posterior information across participants. FLaG-MCMC accurately reconstructs the corresponding pooled Bayesian posterior while closely tracking evolving posterior location and uncertainty in these associations. We also conduct a simulation study motivated by Bayesian evidence synthesis for opioid use disorder prevalence across studies, transferring posterior information from an Ohio study to a subsequent New York analysis under covariate shift. In this setting, FLaG-MCMC demonstrates reliable posterior transfer and favorable computational scaling. Theoretical results establish the validity and consistency of the framework.'
summary: ''
tags:
- Statistics
- MCMC
- Federated Learning
featured: false
url_pdf: 'https://arxiv.org/pdf/2408.02122'
url_code: ''
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
  url: https://arxiv.org/abs/2408.02122
---
