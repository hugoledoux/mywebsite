---
layout: post
title: The Rules for happily collaborating on a LaTeX document
category: blog
tags: latex
comments: true
---

When it comes to writing my [papers](/pubs/), I must admit that I prefer [LaTeX](http://latex-project.org/intro.html) over [that-other-ubiquitous-software-that-I'd-rather-not-mention](http://www.wordperfect.com/rw/). 
*Prefer* is an understatement here: I would probably do *anything* to avoid writing a paper with the other software, eg spending hours harrasing the editor of the journal/conference so that she accepts LaTeX, spending one full day fighting with one of the many [converters](http://peterwittek.com/2013/11/comparing-latex-conversion-tools/) even if I know they don't really work[^1], or asking one of my [students](/proteges/) to do it for me.

So when I can choose, I always impose LaTeX on my co-authors. 
Since some of them are users of the other software, that often creates friction and someone ends up fixing manually all the "mistakes" and inconsistencies in the file. 

So I propose here *The Rules for happily collaborating on a LaTeX document*©, a set of 10 rules that: (1) novices can easily apply; (2) will make your co-authors happy. 

Please add new Rules in the comments below.


### 1. You shall use only one sentence per line

And use one empty line to start a new paragraph.
It'll then be easier to track changes in a versioning system such as SVN or Git since these are line-based.

{% highlight tex %}
I like to create buffers in ArcGIS.
But it is not always possible as it often crashes.

Also, ...
{% endhighlight %} 


### 2. You shall use natbib for citations

and the commands `\citet{}` (cite in the text as a noun) `\citep{}` (cite between parentheses). 

{% highlight tex %}
\usepackage[round]{natbib}
...
\citet{Smith00} succeeded in creating a buffer.
However, it has been shown that it is not an easy task~\citep{Brown90}.
{% endhighlight %} 


### 3. You shall prevent breaking lines with "~" when referencing and citing

{% highlight tex %}
In Section~\ref{sec:intro}, we can observe that the buffer was a success~\citep{Smith99}.
{% endhighlight %} 


### 4. You shall use one `-` for an hyphen, two `--` for a range between numbers, and three `---` for a punctuation in a sentence

{% highlight tex %}
I like---unlike my father---to build multi-dimensional models, 
especially those made in 1990--1995.
{% endhighlight %} 


### 5. You shall give meaningful labels
A figure's label should start with `fig:` and a section's label with `sec:`

{% highlight tex %}
\section{Introduction}  
\label{sec:intro}

In recent years, buffers have been rather complex to implement because ...
{% endhighlight %} 


### 6. You shall put a short space after e.g. and i.e. with the use of a backslash

The following two commands shall thus be used:

{% highlight tex %}
\newcommand{\ie}{i.e.}
\newcommand{\eg}{e.g.}
...
Buffers can be generated on different geometries, \eg\ points, polylines and polygons.
{% endhighlight %}


### 7. You shall put all figures/graphs in a single subfolder (`figs/`)

And you shall put the source file (eg [IPE](http://ipe7.sourceforge.net), OmniGraffle, Illustrator, etc.) there as well for future use.


### 8. In your BibTeX file, you shall use curly brackets for words/letters you want to have capitalised in the title

The other fields are not affected by this. LaTeX does this to uniformise the capitalisation in all citations.

{% highlight tex %}
@article{Smith00,
  Author = {Smith, John},
  Journal = {The GIS Journal},
  Title = {The {3D} {CityGML} building was constructed with the {Delaunay} triangulation},
  Year = {2001},
  ...
}
{% endhighlight %} 


### 9. You shall not add any commands to change the format until the the paper is finished

`\vspace` and `\newpage` are thus forbidden.


### 10. You shall declare all sizes relative to `\linewidth`.

So that the paper can be switched to a 2-column one without (too much) pain.

{% highlight tex %}
\includegraphics[width=0.95\linewidth]{figs/potato.pdf}
{% endhighlight %} 

[^1]: in all fairness, they work great if your paper has no figures and no mathematical equations
