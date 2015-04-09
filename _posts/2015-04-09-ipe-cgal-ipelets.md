---
layout: post
title: Ipe with the CGAL Ipelets is now ridiculously easy under Mac
author: Hugo Ledoux
category: blog
comments: true
---

![]({{ site.baseurl }}/img/ipe1.png)

My favourite drawing program for anything where triangles and geometry is involved is [Ipe](http://ipe7.sourceforge.net).
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

I had problems compiling `circle_pencils.cpp`, so I simply removed it (I'm lazy and I don't need it). 
All the other extensions compiled without issues.

Third, launch ipe (`$ ipe`, it's now in your path) and go the menu 'Help/Show configuration' to see where you should put your newly created Ipe extensions.
Mine was `~/.ipe/ipelets` so I created that folder and copied the extensions:

    $ cp *.so ~/.ipe/ipelets/
    $ cp lua/*.lua ~/.ipe/ipelets/

Voilà, if you start Ipe again, the Ipelets should appear in the 'Ipelets' menu.

![]({{ site.baseurl }}/img/ipe2.png)
![]({{ site.baseurl }}/img/ipe3.png)
