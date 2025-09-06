---
# Leave the homepage title empty to use the site title
title: "TZstats Lab @ Columbia"
date: 2025-09-01
type: landing

design:
  # Default section spacing
  spacing: "1rem"

sections:
  - block: markdown
    content:
      title: 'TZstats Convergence Lab'
      subtitle: ''
      text: |-
        Where disciplines collaborate and research meets education: tackling real-world problems with data, tools, methods — and preparing the next generation of polymath researchers.
    design:
      columns: '1'
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: tianzheng
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/TianZheng.pdf
    design:
      # css_class: dark
      # Avatar customization
      avatar:
        size: large  # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
      # background:
      #   color: black
      #   image:
      #     # Add your image background to `assets/media/`.
      #     filename: blues.svg
      #     filters:
      #       brightness: 1.0
      #     size: cover
      #     position: center
      #     parallax: false
  # - block: markdown
  #   content:
  #     title: '📚 My Research'
  #     subtitle: ''
  #     text: |-
  #       Use this area to speak to your mission. I'm a research scientist in the Moonshot team at DeepMind. I blog about machine learning, deep learning, and moonshots.
  #       I apply a range of qualitative and quantitative methods to comprehensively investigate the role of science and technology in the economy.
  #       Please reach out to collaborate 😃
  #   design:
  #     columns: '1'
  - block: collection
    id: projects
    content:
      title: "Featured Projects"
      filters:
        folders:
          - project
        featured_only: true
    design:
      view: article-grid
      columns: 2
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  # - block: collection
  #   content:
  #     title: Recent Publications
  #     text: ""
  #     filters:
  #       folders:
  #         - publication
  #       exclude_featured: false
  #   design:
  #     view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     view: article-grid
  #     columns: 1
  - block: collection
    id: news
    content:
      title: "Recent Posts"
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 4
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      # view: date-title-summary
      view: article-grid
      columns: 2
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
