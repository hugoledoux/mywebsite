---
layout: post
title: biblatex
author: Hugo Ledoux
category: blog
tags: latex
comments: true
---

With natbib and plainnat for instance you easily get nicely formatted references

```tex
%-- biblatex
\usepackage[backend=biber,
            natbib=true,
            dashed=false,
            maxcitenames=3,
            maxbibnames=10,
            firstinits=true,
            isbn=false,
            doi=false,
            url=false,
            defernumbers=true,
            abbreviate=false,
            style=authoryear-icomp]{biblatex} 

%-- formatting hell for biblatex
%-- remove "In:"
\renewbibmacro{in:}{}
%-- no "quotes" around titles of chapters/article titles
\DeclareFieldFormat[article, inbook, incollection, inproceedings, misc, thesis, unpublished]
{title}{#1}
%-- no punctuation after volume
\DeclareFieldFormat[article]
{volume}{{#1}} 
%-- puts number/issue between brackets
\DeclareFieldFormat[article, inbook, incollection, inproceedings, misc, thesis, unpublished]
{number}{\mkbibparens{#1}} 
%-- and then for articles directly the pages w/o any "pages" or "pp." 
\DeclareFieldFormat[article]
{pages}{#1}
%-- for some types replace "pages" by "p."
\DeclareFieldFormat[inproceedings, incollection, inbook]
{pages}{p. #1}
%-- format 16(4):224--225 for articles
\renewbibmacro*{volume+number+eid}{
  \printfield{volume}
  \printfield{number}
  \printunit{\addcolon}
}
%-- citations with square brackets (== \usepackage[square]{natbib})
\makeatletter
\newrobustcmd*{\parentexttrack}[1]{
  \begingroup
  \blx@blxinit%
  \blx@setsfcodes%
  \blx@bibopenparen#1\blx@bibcloseparen%
  \endgroup}
\AtEveryCite{
  \let\parentext=\parentexttrack%
  \let\bibopenparen=\bibopenbracket%
  \let\bibcloseparen=\bibclosebracket}
\makeatother


\addbibresource{hugomyown.bib}
```



