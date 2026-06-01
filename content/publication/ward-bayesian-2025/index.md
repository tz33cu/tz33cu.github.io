---
title: 'Bayesian Modeling for Aggregated Relational Data: A Unified Perspective'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- owenward
- annasmith
- admin

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-06-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-10-07T15:45:51.440089Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: '*arXiv*'
publication_short: ''

doi: 10.48550/arXiv.2506.21353

abstract: Aggregated relational data is widely collected to study social network theory.
  It has been used to address a variety of key problems in fields such as sociology,
  public health and economics. ARD models enable researchers to estimate the size
  of hidden populations, estimate personal network sizes, understand global network
  structures and fit complex latent variable models to massive network data. Many
  of the successes of ARD models have been driven by the utilisation of Bayesian modeling,
  which provides a principled and flexible way to fit and interpret these models for
  real data. In this work we create a coherent collection of Bayesian implementations
  of existing models for ARD, within the state of the art Bayesian sampling language,
  Stan. Our implementations incorporate within-iteration rescaling procedures by default,
  eliminating the typical post-processing step and improving algorithm run time and
  convergence diagnostics. Bayesian modelling permits natural tools for model criticism
  and comparison, which is largely unexplored in the ARD setting. Using synthetic
  data, we demonstrate how well competing models recover true personal network sizes
  and subpopulation sizes and how well existing posterior predictive checks compare
  across a range of Bayesian ARD models. We implement and provide code to leverage
  Stan's modelling framework for leave-one-out cross-validation, which has not previously
  been examined for ARD models.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Statistics

# Display this page in a list of Featured pages?
featured: true

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: arXiv
  url: http://arxiv.org/abs/2506.21353
---
