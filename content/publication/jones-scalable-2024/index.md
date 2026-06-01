---
title: Scalable Community Detection in Massive Networks Using Aggregated Relational
  Data

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Timothy Jones
- owenward
- Yiran Jiang
- John Paisley
- admin

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-05-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-10-07T15:45:51.444473Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: '*Statistical Sinica*'
publication_short: ''

doi: 10.48550/arXiv.2108.01727

abstract: The mixed membership stochastic blockmodel (MMSB) is a popular Bayesian
  network model for community detection. Fitting such large Bayesian network models
  quickly becomes computationally infeasible when the number of nodes grows into hundreds
  of thousands and millions. In this paper we propose a novel mini-batch strategy
  based on aggregated relational data that leverages nodal information to fit MMSB
  to massive networks. We describe a scalable inference method that can utilize nodal
  information that often accompanies real-world networks. Conditioning on this extra
  information leads to a model that admits a parallel stochastic variational inference
  algorithm, utilizing stochastic gradients of bipartite graph formed from aggregated
  network ties between node subpopulations. We apply our method to a citation network
  with over two million nodes and 25 million edges, capturing explainable structure
  in this network. Our method recovers parameters and achieves better convergence
  on simulated networks generated according to the MMSB.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Network Analysis
- Aggregated Relational Data

# Display this page in a list of Featured pages?
featured: false

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
  url: http://arxiv.org/abs/2108.01727
---
