---
layout: post
title: Ipe with the CGAL Ipelets is now ridiculously easy under Mac
author: Hugo Ledoux
category: blog
comments: true
---

*Update 2018-07-19:* this doesn't work anymore, go to the [new updated page]({{ site.url }}{{ site.baseurl }}{% post_url 2018-07-19-ipe-cgal-ipelets_part_deux %}).

- - -

![]({{ site.baseurl }}/img/ipe1.png)

My favourite drawing program for anything where triangles and geometry are involved is [Ipe](http://ipe7.sourceforge.net).
It's free, open-source, has built-in LaTeX support and is extensible.
One of the nicest extensions for me is the [CGAL Ipelets](http://doc.cgal.org/latest/CGAL_ipelets/index.html): all the power of CGAL easily accessible.

Until recently the main problem (at least under Mac) was the installation of these with Ipe.
I remember spending a whole morning a few years ago compiling everything---it worked but it was painful.
When Ipe and CGAL were upgraded a few months later, I was too lazy to do this again...

It's now ridiculously easy, thanks partly to [Homebrew](http://brew.sh).

First install both and their dependencies:

    $ brew install cgal
    $ brew install ipe

Second, download the latest [source code of CGAL](http://www.cgal.org/download.html) and then:

    $ cd CGAL_ipelets/demo/CGAL_ipelets/
    $ cmake .
    $ make

*Update 2016-01-24:* IPE now requires that the shared objects under Mac OS X are `*.dylib` and not the `*.so` that the makefile creates (CGAL should update their makefile, but they haven't yet). 
Thus, simply rename all the `*.so` to `*.dylib`, and it works.
<del>I had problems compiling `circle_pencils.cpp`, so I simply removed it (I'm lazy and I don't need it). 
All the other extensions compiled without issues.</del>

Third, launch ipe (`$ ipe`, it's now in your path) and go the menu 'Help/Show configuration' to see where you should put your newly created Ipe extensions.
Mine was `~/.ipe/ipelets` so I created that folder and copied the extensions:

    $ cp *.so ~/.ipe/ipelets/
    $ cp lua/*.lua ~/.ipe/ipelets/

Voilà, if you start Ipe again, the Ipelets should appear in the 'Ipelets' menu.

![]({{ site.baseurl }}/img/ipe2.png)
![]({{ site.baseurl }}/img/ipe3.png)
