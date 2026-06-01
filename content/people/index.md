---
title: People
date: 2025-10-04

type: landing

sections:
  - block: hero
    content:
      title: TZstats Lab - Members and Collaborators
      image:
        filename: team2022.jpg
      text: |
       <br>

        Lab dinner photo - Summer 2022. 

        This page is nearly always outdated ... 

        <br>

  - block: people
    content:
      title: 'Current Members'
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Principal Investigator
          - Research Scientist
          - Students and Postdocs
          - Mentored Research Students
          - Administration
          - Design Studio Students
          # - Collaborators
          - Visitors
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true

  - block: people
    content:
      title: 'Current Collaborators'
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      text: |
        My work is highly collaborative and spans partnerships across disciplines and sectors. Below is a partial list of my current and frequent collaborators. A complete list of coauthors can be found through my publications.
        <br>
        <br>
      user_groups:
          - Collaborators
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false

  - block: people
    content:
      title: 'Recent Past Members'
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      text: |
        This group has been built through the efforts of many talented researchers. I am proud to have worked alongside the past members of TZStats and excited to follow their continued accomplishments. Because it is not feasible to maintain a complete list of all past mentees on this website, please see my {{< staticref "uploads/TianZheng.pdf" >}}CV{{< /staticref >}} for a comprehensive record. Here are a subset of recent mentees with whom I have coauthored publications.
        <br>
        <br>
      user_groups:
          - Past Members
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false
---