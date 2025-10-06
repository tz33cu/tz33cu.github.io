---
title: 'ClimSim: An open large-scale dataset for training high-resolution physics emulators in hybrid multi-scale climate simulators'
author: Tian Zheng
date: '2024-04-21'
slug: climsim-an-open-large-scale-dataset-for-training-high-resolution-physics-emulators-in-hybrid-multi-scale-climate-simulators
categories: 
  - Climate Data Science
tags: []
author_notes:
  - First author
  -
  -
  -
  - Senior author
authors: 
  - Sungduk Yu
  - others
  - admin
  - 'more others'
  - Mike Pritchard
doi: ''
publishDate: '2024-04-21T19:25:53-04:00'
publication_types: ['paper-conference']
publication: NeurIPS 2023
publication_short: NeurIPS 2023
abstract: "Modern climate projections lack adequate spatial and temporal resolution due to computational constraints. A consequence is inaccurate and imprecise predictions of critical processes such as storms. Hybrid methods that combine physics with machine learning (ML) have introduced a new generation of higher fidelity climate simulators that can sidestep Moore's Law by outsourcing compute-hungry, short, high-resolution simulations to ML emulators. However, this hybrid ML-physics simulation approach requires domain-specific treatment and has been inaccessible to ML experts because of lack of training data and relevant, easy-to-use workflows. We present ClimSim, the largest-ever dataset designed for hybrid ML-physics research. It comprises multi-scale climate simulations, developed by a consortium of climate scientists and ML researchers. It consists of 5.7 billion pairs of multivariate input and output vectors that isolate the influence of locally-nested, high-resolution, high-fidelity physics on a host climate simulator's macro-scale physical state. The dataset is global in coverage, spans multiple years at high sampling frequency, and is designed such that resulting emulators are compatible with downstream coupling into operational climate simulators. We implement a range of deterministic and stochastic regression baselines to highlight the ML challenges and their scoring. The data and code are released openly to support the development of hybrid ML-physics and high-fidelity climate simulations for the benefit of science and society."
summary: The largest-ever dataset designed for hybrid ML-physics research.
featured: yes
url_pdf: https://arxiv.org/pdf/2306.08754
url_code: https://leap-stc.github.io/ClimSim
url_dataset: https://huggingface.co/datasets/LEAP/ClimSim_high-res
url_poster: 'https://neurips.cc/media/PosterPDFs/NeurIPS%202023/73569.png?t=1701755651.3560717'
url_project: https://leap-stc.github.io/ClimSim/
url_slides: ~
url_source: ~
url_video: ~
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: 
  - external-LEAP
slides: ''
---
