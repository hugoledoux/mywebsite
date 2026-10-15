---
layout: post
title: Converting a complex LaTeX book to Typst
---

{:toc}

The [book "Computational modelling of terrains"](https://tudelft3d.github.io/terrainbook/) (below just the "terrainbook") was released in 2019 as an open book.
My colleagues and I chose to self-publish it directly on GitHub/Zenodo because we know how to use a typesetter (LaTeX) and publisher would not bring much (or would just bring more trouble).

![](/img/tb_cover.jpg)

We first wrote the book using the great [kaobook](https://github.com/fmarotta/kaobook) class, which is based on the [PhD thesis of Ken](https://3d.bk.tudelft.nl/ken/en/thesis/) (Arroyo Ohori, my colleague and co-author of the terrainbook).
For years it was perfect: pretty, efficient use of the space, distinctive, etc. 

But the complexity of the kaobook class was visible: often there would be clashes between figures and notes in the margin, or small hiccups.

That was until ~2024 when I noticed that suddenly I couldn't compile anymore the book... New dependencies broke something, and since the kaobook is not super well maintained ([the last official release is 5 years ago](https://github.com/fmarotta/kaobook/releases))there were no (easy) solution. 

In short, the terrainbook was more or less holding with duct tape, and I was fearing the day.


At the same time, I got very interested in [Typst](https://typst.app) as a LaTeX replacement. 
It's written in Rust, is super fast, and testing it was a joy. 
Compiling the terrainbook in LaTeX from scratch was 2min+ on my laptop, so modifying something meant a lot of waiting.

Until last year was for me more something to test than a serious option to write a book, but I noticed that many of the MSc theses in Geomatics here were suddenly in Typst.

So last summer I decided to try to convert the terrainbook from LaTeX to Typst. I report here on the process.


## The final outcome

But let's start with the result: it is in my opinion *great*, probably nicer than the kaobook we obtained.

This has to do with the different fonts and the fact that I could more freely test options since the compilation takes <2
s when testing different options. 

It's fun to test options, it's almost like Word: different feedback.


## Complex LaTeX means that no standard conversion tool will work

I tried pandoc, tylax, the builtin one from Typst, but none could handle the specific tags that are in the terrainbook.

- \marginnote{}
- subfigure
- etc


GIS computing perspective: https://gisacp.duckham.org/open-access-chapters/ LaTeX + InDesign typesetting
