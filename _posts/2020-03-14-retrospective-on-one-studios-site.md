---
layout: post
title: 'Retrospective: On One Studios Site'
tags: [retrospective]
---

Back in highschool, I spent a lot of my free time participating in urban dance in various ways. Team Sarap (FSA) was my first dance team, and from there my excitement and hunger for becoming a better dancer began. I took various workshops throughout the bay area, but one workshop series that always stood out to me was the Monday Night Workshop. MNW was a smaller scale, grassroots-like urban dance space that brought out some of the bigger names in the community at the time. They really distinguished themselves for me by establishing a friendly, inviting vibe, and I felt more comfortable going to take class there vs. the bigger, more established dance studios with their "master classes".

Fast forward a few years to 2016, and MNW has grown into one of the biggest workshop series in San Jose. They had just completed their Kickstarter campaign for opening up their own dance studio, raising nearly \$60,000. Since I had been a MNW attendee for a while, I had a solid connection with their founder, Guino Dalit.

At the time, I had just recently graduated from USF, and was taking online courses in web development. I offered to help in any way I could, and in November 2016, I had been hired onto the OOS team, and would spend about the next year and a half building the site.

![oos garage]({{ site.baseurl }}/images/oos-garage.JPG)

## How it Works

[On One Studios Website](https://ononestudios.com/)

On One Studio’s website was built using the Wordpress CMS, and is hosted and deployed on a hosting package setup on GoDaddy. The site is using the [X Theme](https://theme.co/), which is a premium Wordpress theme that allows for a large amount of customization and design flexibility.

My responsibilities for the site included page creation/updates (primarily focusing on layout) for various studio programs, embedding tools like Google Analytics and Yoast SEO to help the marketing team, site integration with the MINDBODY framework for class registration, and maintaining site performance & security.

![Cornerstone]({{ site.baseurl }}/images/cornerstone.png)

Page creation was done with [Cornerstone](https://theme.co/cornerstone/), which came bundled with the 'X' theme. Cornerstone made it easy to build layouts using a simple drag-and-drop system. All that needed to be done to get a page made were to select the page elements you wanted (text field, image, button), customize the page with the appropriate copy, and layout the specific elements in a way that made sense.

Adding support for tracking customer engagement was made simple through the huge plugin ecosystem that Wordpress offers. To enable Google Analytics, we simply embedded our analytics ID into the Google Analytics plugin and we were good to go. We also used Yoast SEO to help us identify and enhance spots where our SEO information could be improved.

![MINDBODY]({{ site.baseurl }}/images/mindbody.png)

MINDBODY integration was rather straightforward as well. The MINDBODY webtools allowed us to create certain widgets that we simply needed to embed into their Wordpress plugin. Above you'll see a sample of the 'schedule' and 'registration' widget. MINDBODY is the system being used internally at OOS to keep track of class registration, and even allowed for customers to pay for their classes online. Because payment information was being transmitted through the site, I also worked towards obtaining an SSL certificate to ensure proper security was in place.

Lastly, site performance and security was a tough problem to resolve. We had opted for the base hosting package with GoDaddy, which meant we had limited resources to deal with. One way I was able to increase performance was through integration of a site caching plugin, W3, which enabled page caching on the client side. I also looked into image minification to help reduce page load times.

With regards to security - there was a period of time (maybe a month or so) when the site resources were always maxed out. After integrating the above mentioned performance enhancements, we still noticed a decent amount of site downtime. After I had installed a security plugin, Wordfence, I noticed a large amount of site visits from countries outside of the US. Luckily, after putting certain IPs on a blacklist, things were back to normal and site performance resumed.

## Outcome

After working with the OOS team for a while, I eventually stepped away in order to pursue other goals. This entire experience working with the OOS team was awesome, and it allowed me to build something for a community that I had once been super involved with. I'm glad to say that my work will help students experience the same passion for pursuing dance that I had. Special shout out to the OOS marketing team (Carly, Tad, Dan, Boogie, Kim, Brandon) for being so welcoming of me to the team, and special shout out to Kevin and Guino for putting me on this project.
