---
layout: post
title: 'Side Projects (Lo-Fi Radio, Birthday Bot)'
---

SIP continues to this day (8/17/20), and so I've been trying to take this opportunity as a time to continue developing my software skills. I've recently been trying to level up new technical coding skills (Javascript, React, Node), as well as basic deployment with Heroku.

We'll be taking a quick look at some small side projects that I've worked on this year. These small projects are the result of random weekends of inspiration, and generally the scope of functionality is quite small.

## Lo-Fi Radio (GIF Visualizer)

![Lo-fi Radio]({{ site.baseurl }}/images/lofi_radio.png)

The first side project that we'll be looking at is called the [Lo-Fi Radio](https://lofi-radio.herokuapp.com/). The goal was to create a relaxing/focused environment with chill vapor-wave visuals. This would come to life with a rotating GIF background, while an audio player would play a random radio stream of Lo-Fi hip hop.

The background system is built with React, and it renders a series of full screen GIF videos, all fetched via the [Tenor API](https://tenor.com/gifapi/documentation). The client side code fires a GET request (using Axios) to Tenor, and requests a collection of the top 50 results, matching with the search term 'chillwave vaporwave'. I've also added the functionality to change the search term used to source the background GIF collection.

Unfortunately, this project was never completed. I've yet to find a good solution for adding a Lo-Fi audio player. To me, there were two main requirements for the audio player feature:

1. To implement an audio player that would be minimal in it's design (to avoid distracting from the BG).
2. A source for the Lo-Fi tracks/radio that would occasionally change.

Trying to achieve these, I considered a few things:

- an audio API with a basic player --> required a static mp3 source ❌
- Sourcing the audio from YouTube embed/API --> large video player, ruined minimal design aesthetic ❌
- SoundCloud player API --> big intrusive player with lots of SoundCloud branding ❌

Unfortunately, I was never able to come up with a solid option for this, so Lo-Fi Radio will continue to exist without the "radio" part. (for now!?)

## Birthday Bot

One thing I've always been pretty bad at is remembering people's birthdays. No offense to anyone in my family or friends (nothing personal promise!), but bday dates were always something I would forget.

I always appreciated Facebook for it's ability to kinda act like one's personal bday calendar - though I've always felt like bday wishes through Facebook are a little less genuine, since you'd only know since you were already online checking other notifications.

I imagined the birthday bot because I wanted access to this same information, but instead of writing a bday msg via the Facebook notification, I'd be able to send them a personal message. Luckily, Facebook allows (not sure as of lately tho) anyone to download their own Facebook data, including their friends list and their bday data. I wrote a script to parse the .ics file from the data dump, converted that into a separate JSON file, mapping the day of the year to a list of friends who were born on that day.

To make use of this data, I wrote a Node.js script that would grab the current date, grab the corresponding list of friends for that day, then print that information. I utilized the Twilio API in order to have that information sent to me via text message once a day, and deployed this script to Heroku - set to run once a day, every day.

Now I'm able to get a quick glimpse of a couple people I could reach out every day, and hopefully pass along some good vibes to make their bday a bit more special. :)
