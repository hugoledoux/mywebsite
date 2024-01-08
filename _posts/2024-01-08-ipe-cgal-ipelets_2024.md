---
layout: post
title: Compiling the CGAL Ipelets under macOS 14.2
author: Hugo Ledoux
category: blog
comments: true
date: 2024-01-08 15:07
---

![]({{ site.baseurl }}/img/dt2.png)

[CGAL Ipelets](http://doc.cgal.org/latest/CGAL_ipelets/index.html) are great, but with each CGAL and Ipe new releases I need to recompile them, and the procedure seems to be changing all the time.
The latest is that [Homebrew](https://brew.sh/) doesn't seem to have the source of Ipe anymore, it just pulls the official Ipe.app...

For CGAL 5.5.2 and Ipe 7.2.28, here are the steps that work (for me):

  1. download Ipe.app from [ipe.otfried.org](https://ipe.otfried.org/)
  1. install in `/Applications/`
  1. download the source of Ipe, the [code is on GitHub](https://github.com/otfried/ipe/), and you can download directly the latest: [v7.2.28.tar.gz](https://github.com/otfried/ipe/archive/refs/tags/v7.2.28.tar.gz)
  1. `$ brew install cgal`
  1. download the latest [source code of CGAL](http://www.cgal.org/download.html)
  1. `$ cd  CGAL-5.5.2/demo/CGAL_ipelets/`
  1. `$ cmake . -DIPE_INCLUDE_DIR=/Users/hugo/software/ipe-7.2.28/src/include -DIPE_LIBRARIES=/Applications/Ipe.app/Contents/Frameworks/libipe.dylib`
  1. `$ make`
  1. you must copy the `*.so` and `lua/*.lua` to your ipelets folder. Go to the menu 'Help/Show configuration' to see where you should put your newly created Ipe extensions. Mine was `~/.ipe/ipelets` so I created that folder and copied the extensions.
  1. `$ cp *.so ~/.ipe/ipelets/`
  1. `$ cp lua/*.lua ~/.ipe/ipelets/`
  1. voilà 🚀

![]({{ site.baseurl }}/img/dt1.png)

