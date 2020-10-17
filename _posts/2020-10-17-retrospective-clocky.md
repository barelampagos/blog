---
layout: post
title: 'Retrospective: Clocky & ClockyR'
tags: [retrospective]
---

Today, I'll be taking a look at one of my first side projects, Clocky.

Clocky is simple timer-meets-todo-list to help you manage your time and be productive. Inspired by the Momentum chrome extension.

- [Github](https://github.com/barelampagos/Clocky)

Here's a list of the features taken from the Github README:

- Clock: Displays current time of day.
- Timer: Create quick 1 or 2 hour timers.
- Task List: Fill in the form with a task and assign how long you would like to spend on this particular task. At the end of the timer, Clocky will notify you that your task timer is complete. Included is a quick pomodoro timer button (25 minutes).

![Clocky Task List](https://raw.githubusercontent.com/barelampagos/Clocky/master/media/taskList.gif)

![Clocky Timer](https://raw.githubusercontent.com/barelampagos/Clocky/master/media/timer.gif)

## Inspiration

I built Clocky back when I was focused mainly on applying for jobs postgrad. I found myself wanting to do multiple things every day, such as interview question preparation, taking online courses, and sending out job applications. I noticed that if I were to start working on any task, I would get tunnel vision on focusing on that one task, and before I knew it, my day would be over, and I would have only really accomplished that one item.

In order to help myself manage my time better, I came up with the Clocky concept, and it has helped me timebox whatever tasks I've set out for myself to complete.

## How it Works

Clocky is built with HTML and Javascript, utilizing some JQuery and some Bootstrap for styling. The logic behind Clocky is nothing more than a simple todo list that also takes a time parameter for each task.

The backgrounds featured on this application are sourced from my own photos taken from random trips/photoshoots I've done.

## ClockyR

More recently (in 2020), I've been doing some research into building out full stack web applications using the MERN stack. For the sake of learning, I've decided to rebuild Clocky (dubbed ClockyR = Clocky React) using the MERN stack. The application can be found here: [ClockyR](https://clocky-r.herokuapp.com/).

![ClockyR]({{ site.baseurl }}/images/clockyR.png)

Functionally, ClockyR retains the same feature set, though I've added a few features to make use of the more complex MERN architecture:

- Registration and Login system: Stores user objects on MongoDB, and enables storing of TODOs
- All TODOs (even for unregistered users) are stored in local storage, so upon returning to this page, one can resume their tasks
- Added a 'X' button to remove TODOs that are no longer valid
- Added a few more photos for use in the background from my more recent trips

Also, due to the structure of this application, this was one of the first I've worked on that required a bit more work for deployment. I've hosted this application on Heroku, and luckily they make it super simple to deploy.
