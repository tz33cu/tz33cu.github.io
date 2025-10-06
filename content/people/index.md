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
        
        This page is being updated. 

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
      title: 'Collaborators'
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Collaborators
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false
---