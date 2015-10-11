---
layout: post
title: My setup for GIS research
author: Hugo Ledoux
category: blog
comments: true
---

I the spirit of [the Setup](https://usesthis.com) and [How I Work](http://lifehacker.com/tag/how-i-work), here's a list of the software I use for carrying out my research in (3D) GIS.

## Hardware?

In the last 10 years, I've moved from Windows, to Linux, to Mac OS X, which I use since 2010.
I have only one computer, a MacBook Pro 15" Retina with 256GB SSD and 16GB of RAM, and I use an external 24" monitor and an [external keyboard](http://www.apple.com/shop/product/MB110LL/B/apple-keyboard-with-numeric-keypad-english-usa) and [trackpad](https://www.apple.com/magictrackpad/), both at home (where I often work) and in the office.

I used to have other computers, eg iMacs, but maintaining my setup and configurations on different was taking way too much time. 
One computer is way more efficient and simpler.

## Backing up?

I have had 2 hard-drive failures in my life, one was rather dramatic: at the end of a semester at the university while I was following 7 courses. 
I lost *everything*, since back then backups meant more or less using floppy disks.
So I'm now rather obsessed with backing up.

  * All the code I write is in __[GitHub](https://github.com/hugoledoux/)__, many of it is private first, when it's in a serious state it's release under an open-source licence.
  * While the GitHub Desktop program is fine, I find that __[Tower](http://www.git-tower.com)__ is much more powerful (eg it allows searching commits), and branching, reverting and other git commands are easy to grasp (before Tower, git on the command line was one big scary thing for me, now I wouldn't work without it).
  * Most other documents are in __[Dropbox](https://www.dropbox.com)__, and I pay an annual subscription. It's expensive, but Dropbox has *never* failed me once in 5 years, which is worth a lot of money in my opinion.
  * I backup everyday my computer to a __[Time Machine](https://en.wikipedia.org/wiki/Time_Machine_(Mac_OS))__ at home, so if a disaster happens I should be fine.


## GIS software

  * __[QGIS](http://qgis.org)__ is my 'daily GIS'. I started using it in 2007, and back then you really had to stubborn to use it, because it was incomplete and buggy. But nowadays, it is stable, fast, simple and I don't feel that those using [ArcGIS](http://www.arcgis.com) have an advantage (quite the opposite).
  * __[FME](http://www.safe.com/fme/fme-desktop/)__ is my other GIS (while FME doesn't label itself as a GIS for strategic reasons, it is one). QGIS is pretty primitive for 3D and CityGML, and that's where FME compensates. Just to be able to visualise CityGML file properly in 3D under a Mac, it is worth it.


## Writing 

  * I use LaTeX for writing, and only Word when I'm forced to by coauthors or the editor of a journal.
  * __[Sublime Text](https://www.sublimetext.com)__ with the __[LaTeXTools](https://github.com/SublimeText/LaTeXTools)__ is pretty much the perfect LaTeX environment. My only quibble is that there is no option to see the table of content of a paper (a nice option with TextMate).
  * my bibliography is in BibTeX, and I use either __[BibDesk](http://bibdesk.sourceforge.net)__ and/or __[JabRef](http://jabref.sourceforge.net)__, both have nice features.
  * __[IPE](http://ipe.otfried.org)__ is great for drawing anything where geometries are involved. It creates figures directly in PDF (so no need to maintain 2 files), and one can write directly in LaTeX formulas. It's also extensible, and [the CGAL ipelets are easy to install]({{ site.baseurl }}/blog/ipe-cgal-ipelets/).
  * while I'm still a dummy with __[Blender](http://www.blender.org)__, I'm trying to use it more and more to produce nice figures in 3D. 
  * this blog/website is made with [Jekyll](http://jekyllrb.com), and its [source code is freely available](https://github.com/hugoledoux/mywebsite).
  * I write blog posts and other small bits in [Markdown](http://daringfireball.net/projects/markdown/) and use __[Marked 2](http://marked2app.com)__ to preview it (the features to check if the URLs are valid is very useful).


## Presenting

  * __[Keynote](https://www.apple.com/mac/keynote/)__ is much better than PowerPoint, and I like the fact that I can copy-and-paste tables/algorithms/figures in a PDF (created with LaTeX) and everything stays vectorial.
  * __[Beamer](https://bitbucket.org/rivanvx/beamer/wiki/Home)__, presentation made with LaTeX, is also useful for presentations with many mathematical equations and figures.
  * __[Caffeine](http://lightheadsw.com/caffeine/)__ prevents your computer from automatically going to sleep, for example when you answer questions at the end of a presentation.


## Programming 

  * for Python/CSS/HTML, I use __[Sublime Text](https://www.sublimetext.com)__.
  * for C++, I use both __[Xcode](https://developer.apple.com/xcode/)__ (to navigation code, suggestions, auto-complete, etc) and Sublime Text (both open at the same time) for the multiple selections feature (I don't even know anymore how I programmed/wrote without this).
  


## Miscellaneous 

  * __[Notational Velocity](http://notational.net)__ for taking notes (and searching them).
  * __[1Password](https://agilebits.com/onepassword)__ to easily manage different passwords for each website.
  * __[atext](http://www.trankynam.com/atext/)__ replaces abbreviations by full texts. Useful for so many things: difference signatures in emails, addresses, coding, phone numbers, etc
  * __[Annotate](https://www.driftt.com/annotate-mac)__ is very useful to quickly capture part of the screen, annotating it, uploading the result to Dropbox for instance, and copying the URL to your clipboard.
  * __[Jumpcut](http://jumpcut.sourceforge.net)__ is tiny and free application to that provides clipboard buffering. Can't imagine not having this installed.
  * Finder lacks the dual-panel power of [Midnight Commander](http://www.midnight-commander.org), so I use one of its __[ForkLift](http://www.binarynights.com/forklift/)__ 
  * __[Fluid](http://fluidapp.com)__ simply makes an application from one website, eg Gmail. However, you can have a separate cache, which means that I'm never logged in to Google in my browser, and yet use Gmail as my email in the web interface.

