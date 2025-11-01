---
title: 'TZstats Lab - Projects'
type: landing

sections:
  - block: portfolio
    content:
      title: 'TZstats Projects'
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      filters:
        folders:
          - project
      sort_by: date
      sort_ascending: false
      default_button_index: 0
      # Filter button toolbar (optional).
      # Add or remove as many buttons as you like.
      # To show all content, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the button toolbar, delete the entire `buttons` block.
      buttons:
        - name: All
          tag: '*'
        - name: Research
          tag: Research
        - name: Education
          tag: Education
        - name: AI
          tag: artificial intelligence
        - name: Design Studio
          tag: Design Studio
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      # Choose a listing view
      view: compact
---