---
title: "Running a fediverse server (for (nearly) free!)"
date: 2023-07-09T09:30:00+03:00
draft: false
toc: true
images:
tags:
  - fediverse
---

Running a fediverse server is now easier than ever, you can run it on hardware as low spec as a Raspberry Pi. With the recent twitter drama, it is extremely lucrative to create a fediverse account now. While you may find it easier to create an account on a more well-estabilished server, it isn't exactly the best idea. Why? Well, if you're going to make an account on a [well estabilished instance](https://joinmastodon.org/servers), you're subject to their moderation policies, and, you can get banned for some nonsensical reasons. By hosting a server, you're practically becoming censorship-resistant.

## Prerequisites
* A domain name: I'd reccomend Cloudflare Domains or Porkbun. 
* A VPS: It's easy to get an Oracle Cloud Free Tier VPS.
* Some linux experience

## Basic setup
You will want to add your domain to Cloudflare, this isn't required, but it is reccomended as you may encounter bad actors trying to attack your instance. If you use Cloudflare Domains, this was already done for you.  
After you've added your domain to Cloudflare you must go to your ingress rules (instance page > vcn > subnet > security list) and add the following rules:
```sh
0.0.0.0/0	All Protocols				All traffic for all ports
```
You may think that it is insecure, but we will be adding a firewall on our server now. We'll be using ufw since it is the easiest to set up for newbies.
```sh
sudo apt-get install ufw
ufw allow 22
ufw allow 80
ufw allow 443
```

## Picking your poison
Oh well, this might be easy for some or hard for some, so I will cover each option.
* **Mastodon**: Mastodon is the most widely-used server software on the fediverse (we're still suffering from Eugen's decisions from 7 years ago), however, it isn't the greatest. Why?
  * **Uses a lot of resources:** Mastodon is fat, which may turn you away if you want to run more than just a simple Mastodon instance on your server. Here is a comparison between Mastodon and Pleroma:
  ![less is better](/pictures/mastodon-to-pleroma-comparison.png)
  * **Less costumizable:** At most you can just edit the stylesheet with the default FE and add a banner. Pleroma-FE beats the fuck out of Mastodon when it comes to costumization. You can even replace Pleroma-FE with another frontend, such as soapbox.

  If you still wish to use Mastodon, the documentation covers everything better than I could. https://docs.joinmastodon.org/admin/prerequisites/
* **Pleroma**: Pleroma is a more sensible option if you wish to have something more light-weight. There are 3 versions:
  * **Vanilla**: The base version of Pleroma, active development has ceased unfortunately and the only updates you'll get are security fixes. (https://docs-develop.pleroma.social/backend/)
  * **Akkoma**: A fork of Pleroma that allows users to be more expressive than on Pleroma. (https://docs.akkoma.dev/)
  * **Rebased**: An improved version of Pleroma. (https://soapbox.pub/install/)


  All of them are trivially easy to setup and have one thing in common, the way that they are ran:
  * **From source:** you're compiling the source code every time you run the software. This opens up the posibilities of editing the source code on your server, which you may find useful in some cases. Though, depending on your server's specifications, it may take a while to run it. 
  * **OTP**: OTP is the closest you can get to a binary release. It isn't compiled every time your run it, so startup times will be faster. Though, there are some limitations, most notably that you can't edit the source code

* **Misskey:** Misskey is by far the most feature-rich server we've covered, like Pleroma, it has many versions:
  * **Vanilla**: The base version of Misskey, without any forks. https://misskey-hub.net/en/
  * **Foundkey** Maintained by the same people who maintain Akkoma https://akkoma.dev/FoundKeyGang/FoundKey
  * **Calckey** A more advanced version of Misskey which implements the Mastodon API https://calckey.org/


  I'd personally use Calckey as it seems more estabilished than FoundKey at this point in time. I'd reccomend any Misskey version for beginners, as it is easier to run and setup than Pleroma or Mastodon.

## Conclusion
Making a fediverse server is simple, but the hard part is maintaining it. I have recently opened a fediverse server of my own. Within 3 months, I'll share my experience running it and some tips for those interested.
