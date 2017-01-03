---
layout: post
title: Fiddling with biblatex
author: Hugo Ledoux
category: blog
tags: latex
comments: true
---

[Biblatex](https://www.ctan.org/pkg/biblatex?lang=en), used with [Biber](https://www.ctan.org/pkg/biber) as the backend, is in theory a major improvement over bibtex.
One can for instance: 

  - easily have different reference sections in one document, and have different styles and sorting options for each section;
  - easily decide if fields such as DOI, URL should be in the references (without having to create a new style);
  - control how many authors are listed in the citation and the reference.
  - have references with UTF-8 characters

I used it recently for the first time for a grant proposal where 3 different reference sections were asked: 

  1. main text with numerical style, sorted by authors; 
  1. my own publications in author-year, sorted by descending years; 
  1. my top 5 publications, sorted descending by year. 

Doing this with bibtex would be a nightmare I thought, so I gave biblatex a try.
The results? In theory biblatex is great, but in practice it's not there yet, at least in my experience.
There are *several* bugs and things that annoyed me, and I spent way too much time trying to fix these.

Here's a summary of things I learned.


## The biber cache often gets corrupted

If you run biber and get a weird error pointing to a temporary folder, this usually solves the problem:

```
$ rm -rf `biber --cache`
```

## Citations with square brackets are not easy

I prefer to have a citation such as Smith [2001], instead of Smith (2001). 
With natbib, it's simple:

```
\usepackage[square]{natbib}
```

With biblatex, you have to put this in your preambule:

```
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
```


## The formatting of the references is dreadful

I'm used to natbib's styles such as *plainnat* and *abbrvnat*, with these you get for example:

> B. N. Delaunay. Sur la sphère vide. *Izvestia Akademia Nauk SSSR, Otdelenie Matematicheskii i Estestvennyka Nauk*, 7:793–800, 1934.

> D. H. Douglas and T. K. Peucker. Algorithms for the reduction of the number of points re- quired to represent a digitized line or its caricature. *The Canadian Cartographer*, 10(2):112– 123, 1973.

If biblatex is used "out-of-the-box", with the style *authoryear-icomp*, this is what is obtained:

> Delaunay, Boris N. (1934). "Sur la sphère vide". In: *Izvestia Akademia Nauk SSSR, Otdelenie Matem- aticheskii i Estestvennyka Nauk* 7, pp. 793–800.

> Douglas, D. H. and T. K. Peucker (1973). "Algorithms for the reduction of the number of points required to represent a digitized line or its caricature". In: *The Canadian Cartographer* 10.2, pp. 112–123.

Several things are annoying and these can be fixed as follows:

### the 'In:' for the journal title

```tex
\renewbibmacro{in:}{}
```

### the quotes around the title of the paper

```tex

\DeclareFieldFormat[article, inbook, incollection, inproceedings, misc, thesis, unpublished]{title}{#1}

```

### the volume and the issue are separated by a dot

To obtain what natbib *plainnat* has (ie volume(issue):pp--pp) and to shorten 'pages' to 'p.':

```tex
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
```

## The full preambule is thus as follows

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

\addbibresource{myreferences.bib}
```

which gives:

> Delaunay, B. N. (1934). Sur la sphère vide. *Izvestia Akademia Nauk SSSR, Otdelenie Matematicheskii i Estestvennyka Nauk* 7:793–800.

> Douglas, D. H. and T. K. Peucker (1973). Algorithms for the reduction of the number of points required to represent a digitized line or its caricature. *The Canadian Cartographer* 10 (2):112– 123.

My advice? Stick to bibtex for the time being, unless you *really* need the benefits of biblatex.

