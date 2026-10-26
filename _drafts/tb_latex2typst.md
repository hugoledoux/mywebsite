---
layout: post
title: Converting a complex LaTeX book to Typst
---

{:toc}

The [book "Computational modelling of terrains"](https://tudelft3d.github.io/terrainbook/) (below just the "terrainbook") was released in 2019 as an open book.
My colleagues and I chose to self-publish it directly on GitHub/Zenodo because we know how to use a typesetter (LaTeX) and publisher would not bring much (or would just bring more trouble).

![](/img/tb_cover.jpg)

We first wrote the book using LaTeX and the great [kaobook](https://github.com/fmarotta/kaobook) class, which is based on the [PhD thesis of Ken](https://3d.bk.tudelft.nl/ken/en/thesis/) (Arroyo Ohori, my colleague and co-author of the terrainbook).
For years it was perfect: pretty, efficient use of the space, distinctive look, etc. 

But the complexity of the kaobook class was visible: often there would be clashes between figures and notes in the margin, or small hiccups.

That was until ~2024 when I noticed that suddenly I couldn't compile anymore the book... New dependencies broke something, and since the kaobook is not super well maintained ([the last official release is 5 years ago](https://github.com/fmarotta/kaobook/releases)) there were no (easy) solution. Ouch.

In short, the terrainbook was more or less holding with duct tape, and I was fearing the day where I wouldn't be able to compile it (or spend a lot of time each time).


At the same time, I got very interested in [Typst](https://typst.app) as a LaTeX replacement. 
It's written in Rust, is super fast, and testing it was a joy. 
Compiling the terrainbook in LaTeX from scratch was long (about 1min15sec on my laptop), so modifying something meant a lot of waiting.

Until last year, Typst was for me something to tinker with and to test, it wasn't a serious option to write a book. 
However, the beginning of 2026, I got more interested and wrote an MSc Geomatics thesis template with it, and  I noticed that many of the MSc theses in Geomatics here were suddenly in Typst. And they looked fine and students reported very few bugs or hiccups.

So last summer I decided to try to convert the terrainbook from LaTeX to Typst. I report here on the process.


## The final outcome

But let's start with the result: it is in my opinion *great*, probably nicer than what we obtained with  the kaobook.


It's fun to test options, it's almost like Word where you get instant feedback.
By using `typst watch myfile.typ` you can write the template/code of the book, and upon saving a file of the project the PDF gets recompiled on-the-fly. 
It takes <1s to see the results, which I deem instant feedback here (especially coming from LaTeX!).

This has to do with the different fonts and the fact that I could more freely test options since the compilation takes <1s when testing different options. 


## Complex LaTeX means that no standard conversion tool will work

I tried pandoc, tylax, the builtin one from Typst, but none could handle the specific and non-standard tags that are in the terrainbook.

- marginnote
- marginfigure
- I used a lot of sub-figures (different files get figure a) b) c) etc.) using the subcaption package
- specific algorithms written with 'algorithm2e'

```tex
\begin{marginfigure}
  \centering
  \includegraphics[width=\linewidth]{figs/kdtree}
  \caption{Example of $k$d-tree in 3D, with the dimension used at each level.}%
\labfig{fig:kdtree}
\end{marginfigure} 
```

```tex
As shown in \reffig{fig:pyramids}, 
\begin{figure}
  \centering
  \begin{subfigure}[b]{0.65\linewidth}
    \centering
    \includegraphics[width=\textwidth]{figs/pyramids.pdf}
    \caption{}
  \end{subfigure}
  \qquad%
  \begin{subfigure}[b]{0.2\linewidth}
    \centering
    \includegraphics[width=\textwidth]{figs/pyramids2.pdf}
    \caption{}
  \end{subfigure}
\caption{\textbf{(a)} The pyramid for a given raster file. \textbf{(b)} One $4\times4$ raster downsampled twice with average-method.}%
\labfig{fig:pyramids}
\end{figure}
```

Some figures took the full width, including the margin:
```tex
\begin{figure*}
  \includegraphics[width=\linewidth]{figs/destm}
  \caption{The DSM (green), DTM (pink), and nDSM (blue) for a profile view of a point cloud in Delft, the Netherlands.}%
\label{fig:dtmdsm}
\end{figure*}
```

I ended up writing my own specific Python converter for each chapter using regex. 
I say "I", but I basically converted 2-3 chapters manually with the packages in Typst I wanted to use (more on this below), and then used a LLM to write Python code.
This took a few hours of trying and tweaking, and the result is `tex2typ_v2.py`.
It uses tylax for the mathematical equations, and the rest is the regex to convert the text to the specific Typst commands I wanted to use. 

It skips the algorithms, which I rewrote manually. There are not that many and I thought that automatic those would take more time then manual rewrite.

The Python script is also not perfect, I used it to convert the other chapters but for each I need to manually fix errors and a few commands escaped the conversion (eg LaTeX commands inside a caption of a subfigure).

But in general it went pretty well, and for each chapter the amount of manual was certainly <1h per chapter.

## The template

The template was written from scratch in Typst, and the result is in the file `template.typ`, which contains a bit more than 500 lines of code.

Most of it was written manually while verifying visually the results in the PDF.

I tried to use a LLM to help me, and it was really hit-and-miss.
Some parts like numbering the subfigures and applying a specific format to the caption, the LLM proved great and saved me a lot of time.
For many other things it was hopeless and I ended up testing and googling.

### The fonts: IBM Plex superfamily

For the font, I wasn't sure if I wanted to keep Palatino. 
In the end, I asked several people (colleagues, family, students) which one they liked the most and the version with the [IBM Plex superfamily](https://github.com/IBM/plex) of fonts won. 
This is the result you see in the printscreens here.
I liked that the serif is great, the sans-serif not bad, but also that the mono font fits with the rest, and ditto for the math font. 
In hindsight: an easy choice.

The font is free and openly available, and it is bundled with the source of the book (in folder `./fonts/`) so that the PDF renders identically on every machine (macOS, Linux, CI).

### The Typst packages 

The main packages I used are the following

```typ
//-- engine for the page setup and margins
#import "@preview/marginalia:0.3.1" as marginalia: note, notefigure, wideblock
//-- for the mini-toc of each chapter
#import "@preview/suboutline:0.3.0": suboutline
//-- for the information boxes
#import "@preview/showybox:2.0.4": showybox
//-- headers to get context (page and chapter/section titles)
#import "@preview/hydra:0.6.2": hydra
//-- helper for numbering of figures and tables
#import "@preview/headcount:0.1.1": dependent-numbering, reset-counter
//-- subfigure
#import "@preview/subpar:0.2.2"
//-- pseudo-code
#import "@preview/lovelace:0.3.0": *
//-- siunitx replacement
#import "@preview/unify:0.8.1": num, numrange, qty, qtyrange, unit
//-- index at the end
#import "@preview/in-dexter:0.7.2": *
//-- icons
#import "@preview/heroic:0.1.2": hi
```

#### marginalia
The package marginalia proved to be *great*. 
One can easily decide on the proportion, and since with Typst you can test and marginalia lets you show the frame lines it was rather easy to iterate.

For the figure/table/algorithm captions, I tried to imitate the behaviour of kaobook and for this I had to write several lines of custom commands; those can be seen in `template.typ`.

#### Headers
The chapter headers turned out to be complex, but with the help of a LLM I could iterate rather easily and looked at the results.
My result only works on a A4 page, and everything is hardcoded so changing the page size will most likely result in errors (even to US letter size, sorry for my North American friends...).

I used the package [hydra](https://typst.app/universe/package/hydra) and [headcount](https://typst.app/universe/package/headcount) to help me keep track of the current page and header numbers and to have labels for figures and tables "chapter.number", eg 3.4 or 8.2 for easy navigation. Somehow Typst doesn't make it easy to do out-of-the-box.


#### Clashes in the margins

In LaTeX, there were sometimes clashes between the many margin notes and the figures, and the LaTeX engine did a good job at solving them.
It is essentially the same with Typst, there are only a handful of figures where I had to manually moved them manually up or down (`dy: 100pt` can be seen in some floats).
I enforce figures and widefigures (those using also the margin) to be placed at the top or bottom of a page (`placement: auto` in Typst) but this can create some issues like this one if margin-figures are used. 
Notice that the numbering is not in order in this case...

However, when compiling the book in Typst, one gets a very long warning stating the the optimal placement of figures hasn't converged after 5 attempts. 
I get a warning and I am referred to this page: [https://typst.app/help/state-convergence](https://typst.app/help/state-convergence).
At first I was pretty alarmed at this and thought the results would be really bad, but it turns out that even if the warnings are present, the book always produces a nice PDF and there are not any big errors as far as I can see.
I spent a few hours with a LLM trying to fix those, but I finally gave up. 
I see no logics and those are not triggered, I think, by one weirdly placed figure or margin-note.
If someone knows how to fix/silence those warnings, please make a PR.

#### I love Typst: boxes and icons and fonts were way way easier to implement

Making the different boxes in the book was easy and fun, thanks to Typst. 

I used [showybox](https://typst.app/universe/package/showybox) and it was rather trivial to do.

For the mini-toc at the beginning of each chapter, I used also this showybox, and I had to use the package [suboutline](https://typst.app/universe/package/suboutline) to obtain the table-of-content of a specific chapter.
Pretty easy and straightforward.

Notice that I wouldn't know how difficult these things are to do in LaTeX since I basically just "used" kaobook as is, and I have never really had to implement new functions or modify them.
But I was always fearing doing this, as I see LaTeX as very complex (and when modifying something one has to wait minutes to see the results, which makes me stop after 20min...).
With Typst, it was doable and mostly fun.
