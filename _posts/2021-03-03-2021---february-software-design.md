---
layout: post
title: '2021 - February: Software Design'
---

February's goal for myself was to focus on system design, specifically for a web application I'm building as a part of a small startup project. I had initially implemented an early version of this structure, but realized that my design wasn't too great, and relied on having too many nested JSON objects (MongoDB). So this month's overall goal was to start from scratch, and set things up a bit better.

At a high level, I've been working on a system that contains a series of courses, each broken up into smaller sections we've dubbed modules, with each module being broken up into different chapters. In addition to that, we're looking to build out a gamification system (experience + leveling), so we need to keep track of the modules and chapters that were completed.

![ODP System Design]({{ site.baseurl }}/images/system_design.jpg)

Without diving too much into the specifics, I've updated the structure of the system to have Master & User versions of these objects. For example, the MasterCourse object is made up of MasterModules, each containing their own MasterChapters. When a user enrolls in a course, a backend Express API generates a user specific copy of the MasterCourse structure, named UserCourse (+UserModules, +UserChapters). These objects will be fetched when a user loads any given course, and allows for us to track which of these are completed, and which are still pending for completion.

Hopefully this restructure is scalable enough for many users, though I guess we'll just have to see when things grow if there's any issue from a performance POV.
