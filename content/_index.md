---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-01
type: landing

sections:
  - block: hero
    content:
      title: |
        TZstats Convergence Lab @ Columbia
      image:
        filename: welcome.jpg
      cta:
        label: "Lab lead - Professor Tian Zheng"
        url: author/tian-zheng
      text: |
        <br>
        
        Where disciplines collaborate and research meets education: tackling real-world problems with data, tools, methods — and preparing the next generation of polymath researchers. 

        <br>
        
  - block: collection
    content:
      title: Latest Posts
      subtitle:
      text:
      count: 4
      filters:
        author: ''
        category: ''
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: showcase
      columns: '2'
  - block: portfolio
    content:
      title: "Featured Projects"
      filters:
        folders:
          - project
        featured: true
    design:
      view: masonry
      columns: '2'
      # Reduce spacing
  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
      
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: tzstats4.png
          filters:
            brightness: 0.9
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
