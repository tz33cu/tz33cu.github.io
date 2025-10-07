---
title: Stabilized Sparse Online Learning for Sparse Data

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Yuting Ma
- Tian Zheng

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2017-05-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-10-07T15:45:51.464687Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: '*Journal of Machine Learning Research*'
publication_short: ''

doi: 10.48550/arXiv.1604.06498

abstract: Stochastic gradient descent (SGD) is commonly used for optimization in large-scale
  machine learning problems. Langford et al. (2009) introduce a sparse online learning
  method to induce sparsity via truncated gradient. With high-dimensional sparse data,
  however, the method suffers from slow convergence and high variance due to the heterogeneity
  in feature sparsity. To mitigate this issue, we introduce a stabilized truncated
  stochastic gradient descent algorithm. We employ a soft-thresholding scheme on the
  weight vector where the imposed shrinkage is adaptive to the amount of information
  available in each feature. The variability in the resulted sparse weight vector
  is further controlled by stability selection integrated with the informative truncation.
  To facilitate better convergence, we adopt an annealing strategy on the truncation
  rate, which leads to a balanced trade-off between exploration and exploitation in
  learning a sparse weight vector. Numerical experiments show that our algorithm compares
  favorably with the original algorithm in terms of prediction accuracy, achieved
  sparsity and stability.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Machine Learning

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
- name: URL
  url: http://arxiv.org/abs/1604.06498
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
