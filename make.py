# -*- coding: utf-8 -*-
import os
import sys
import string
import StringIO
import markdown
import codecs

def main():
  fOut = codecs.open("site/index.html", "w", encoding="utf-8", errors="xmlcharrefreplace")
  
  fOut.write(write_header())
  fOut.write(write_navbar())
  fOut.write(write_home())

  s = write_about()
  fOut.write(s.getvalue())

  fOut.write(write_code())

  os.system("php go.php > pubs.html")
  s = write_pubs()
  fOut.write(s.getvalue())

  s = write_students()
  fOut.write(s.getvalue())

  f = open('phdthesis.html')
  fOut.write(f.read())

  f = open('contact.html')
  fOut.write(f.read())

  fOut.write(write_footer())

  print "done."

def write_pubs():
  s = StringIO.StringIO()
  s1 = """
  <!-- ========== PUBLICATIONS ========== -->
  <section id="pubs"></section>
    <div class="container">
      <div class="row">
        <h2>publications</h2>
        <p class="centered"><i class="icon-ellipsis-horizontal icon-large"></i></p>
        <div class="col-lg-10 col-lg-offset-1">
  """
  print >>s, s1
  f = open('pubs.html')
  print >>s, f.read()
  print >>s, '</div></div></div>'
  return s   


def write_home():
  return """
  <!-- ========== HOME SECTION ========== -->
  <section id="home"></section>
  <div id="headerwrap">
    <div class="container">
      <div class="logo">
        <a href="http://www.tudelft.nl"><img src="assets/img/tudblack.png" width="150" alt=""></a>
      </div>
      <br>
      <div class="row">
        <img class="img-circle" src="assets/img/hugo.jpg" width="200" height="200" alt="">
        <h1>Hugo Ledoux</h1>
        <!-- <br> -->
        <h3>I am an assistant-professor in the <a href="http://www.gdmc.nl">GIS technology group</a><br>of the <a href="http://www.tudelft.nl">Delft University of Technology</a>.</h3>
        <br>
        <br>
        <div class="col-lg-6 col-lg-offset-3">
        </div>
      </div>
    </div><!-- /container -->
  </div><!-- /headerwrap -->
  """


def write_footer():
  return """
  </div>
  <!-- Bootstrap core JavaScript
  ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="assets/js/classie.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/smoothscroll.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
  """

def write_header():
  return """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="assets/ico/favicon.png">

    <title>Hugo Ledoux</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/main.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/font-awesome.min.css">
    <!-- <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet"> -->


    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/modernizr.custom.js"></script>
  

    <link href='http://fonts.googleapis.com/css?family=Ubuntu' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Ubuntu+Condensed' rel='stylesheet' type='text/css'>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="assets/js/html5shiv.js"></script>
      <script src="assets/js/respond.min.js"></script>
    <![endif]-->
  </head>
  <body data-spy="scroll" data-offset="0" data-target="#theMenu">
  """

 
def write_navbar():
  return """
  <!-- Menu -->
  <nav class="menu" id="theMenu">
    <div class="menu-wrap">
      <h1 class="logo"><a href="index.html#home"></a></h1>
      <i class="icon-remove menu-close"></i>
      <!-- <i class="icon-github menu-close"></i> -->
      <!-- <i class="fa fa-times menu-close"></i> -->
      <a href="#home" class="smoothScroll">home</a>
      <a href="#about" class="smoothScroll">about</a>
      <a href="#code" class="smoothScroll">code</a>
      <a href="#pubs" class="smoothScroll">publications</a>
      <a href="#students" class="smoothScroll">students</a>
      <a href="#phdthesis" class="smoothScroll">PhD thesis</a>
      <a href="#contact" class="smoothScroll">contact</a>
      <a href="https://github.com/hugoledoux"><i class="icon-github icon-4X"></i></a>
      <a href="https://twitter.com/hugoledoux"><i class="icon-twitter icon-4x"></i></a>
      <!-- <a href="https://github.com/hugoledoux"><i class="fa fa-home"></i></a> -->
      <!-- <a href="https://twitter.com/hugoledoux"><i class="fa fa-home fa-4x"></i></a> -->
    </div>
    
    <!-- Menu button -->
    <div id="menuToggle"><i class="icon-reorder"></i></div>
    <!-- <div id="menuToggle"><i class="fa fa-bars"></i></div> -->
  </nav>
  """

def write_students():
  s = StringIO.StringIO()
  s1 = """
  <div id="f">
  <!-- ========== STUDENTS SECTION ========== -->
  <section id="students"></section>
    <div class="container">
      <div class="row">
        <h2>supervised students</h2>
        <p class="centered"><i class="icon-ellipsis-horizontal icon-large"></i></p>
        <div class="col-lg-10 col-lg-offset-1">
  """
  print >>s, s1
  f = codecs.open('students.md', mode='r', encoding="utf-8")
  html = markdown.markdown(f.read(), extensions=['smartypants(entities=named)'])
  print >>s, html
  print >>s, '</div></div></div>'
  return s  

def write_about():
  s = StringIO.StringIO()
  s1 = """
  <div id="f">
  <!-- ========== ABOUT SECTION ========== -->
  <section id="about"></section>
    <div class="container">
      <div class="row">
        <h2>about</h2>
        <p class="centered"><i class="icon-ellipsis-horizontal icon-large"></i></p>
        <div class="col-lg-10 col-lg-offset-1">
  """
  print >>s, s1
  f = codecs.open('about.md', mode='r', encoding="utf-8")
  html = markdown.markdown(f.read(), extensions=['smartypants(entities=named)'])
  print >>s, html
  print >>s, '</div></div></div>'
  return s   


def write_code():
  return """
  <!-- ========== CODE ========== -->
  <section id="code"></section>
    <div class="container">
      <div class="row">
        <h2>open-source code</h2>
        <p class="centered"><i class="icon-ellipsis-horizontal icon-large"></i></p>       
        <div class="col-lg-10 col-lg-offset-1">
        <div class="col-lg-4">
          <a href="https://github.com/tudelft-gist/pprepair" class="thumbnail">
            <img src="img/pprepair_logo2.png" alt=""></a>
          <h3>pprepair</h3>
          Automatic repair of "broken" GIS planar partitions stored in <em>shapefiles</em>
        </div>
        <div class="col-lg-4">
          <a href="https://github.com/tudelft-gist/prepair" class="thumbnail">
            <img src="img/prepair_logo.png" alt="">
          </a>
          <h3>prepair</h3>
          Automatic repair of invalid polygons according to the standards ISO 19107
       </div>
        <div class="col-lg-4">
          <a href="https://github.com/tudelft-gist/val3dity" class="thumbnail">
            <img src="img/val3dity_logo.png" alt="">
          </a>
          <h3>val3dity</h3>
          Validation of solids according to the international standard ISO 19107
        </div>
      </div>
      </div>
    </div>
  """

if __name__ == "__main__":
    main()  
