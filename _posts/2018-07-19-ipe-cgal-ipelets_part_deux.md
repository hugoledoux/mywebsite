---
layout: post
title: Compiling the CGAL Ipelets under macOS
author: Hugo Ledoux
category: blog
comments: true
date: 2018-07-19 19:50
---

![]({{ site.baseurl }}/img/cat.png)

[CGAL Ipelets](http://doc.cgal.org/latest/CGAL_ipelets/index.html) are great, but with each CGAL and Ipe new releases I need to recompile them, and the procedure seems to be changing all the time.
The latest is that [Homebrew](https://brew.sh/) doesn't have the source of Ipe anymore, it just pulls the official Ipe.app...

For CGAL 4.11 and Ipe 7.2, here are the steps:

  1. download Ipe.app from [ipe.otfried.org](https://ipe.otfried.org/)
  2. install in `/Applications/`
  3. `$ brew install cgal`
  4. download the latest [source code of CGAL](http://www.cgal.org/download.html)
  5. `$ cd  CGAL-4.11.2/demo/CGAL_ipelets/`
  6. `$ cmake . -DIPE_INCLUDE_DIR=/Applications/Ipe.app/Contents/Frameworks/Headers -DIPE_LIBRARIES=/Applications/Ipe.app/Contents/Frameworks/libipe.dylib`
  7. you must copy the `*.so` and `lua/*.lua` to your ipelets folder. To the menu 'Help/Show configuration' to see where you should put your newly created Ipe extensions. Mine was `~/.ipe/ipelets` so I created that folder and copied the extensions.
  8. `$ cp *.so ~/.ipe/ipelets/`
  9. `$ cp lua/*.lua ~/.ipe/ipelets/`
  10. voilà

![]({{ site.baseurl }}/img/catdt.png)

