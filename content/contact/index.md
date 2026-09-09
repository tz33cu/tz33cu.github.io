---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
            + For collaboration or research inquiries, please fill out [this form](https://forms.gle/jTTRcGjpJD7STppG7). 
            + For mentored research opportunities, 
              + MA in Statistics students should go through the mentored research program. 
              + Other students, please review the [Projects](../project/) page and let me know how you would like to be involved. 
            + The PhD admission is done by a department-level committee. During the admission season, I incline not to engage with prospective students beyond your application materials.
      email: tian.zheng@columbia.edu
      phone: 212-851-2149
      fax: 212-851-2164
      address:
        street: 1255 Amsterdam, Room 1032, MC 4690
        city: New York
        region: NY
        postcode: '10027'
        country: United States
        country_code: US
      coordinates:
        latitude: '40.810312'
        longitude: '-73.958388'
      directions: Take the elevator to 10th floor, enter the double door, second office on the right.
      office_hours:
        - 'aiX Design Studio - see the live calendar below for the current time and room'
      # appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
    #   # Email form provider
    #   form:
    #     provider: netlify
    #     formspree:
    #       id:
    #     netlify:
    #       # Enable CAPTCHA challenge to reduce spam?
    #       captcha: false
    # design:
    #   columns: '1'

  - block: markdown
    content:
      title: aiX Design Studio
      subtitle: ''
      text: |
        {{< gcal src="c_dc1eb53aa392f7c7dac4e6bf681b4be24fa5fabb6d1d010ed3d59f67bd215a63@group.calendar.google.com" title="aiX Design Studio" mode="AGENDA" height="240" width="560" intro="Live from my calendar - always the current time and room." >}}
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text: |
        {{< aiwidget >}}
    design:
      columns: '1'
      background:
        image: 
          filename: convocation.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
