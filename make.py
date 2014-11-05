# -*- coding: utf-8 -*-
import os
import sys
import string
import StringIO
import markdown2
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
      <br>
      <br>
      <br>
      <br>
      <div class="row">
        <img class="img-circle" src="assets/img/hugo.jpg" width="200" height="200" alt="">
        <h1>Hugo Ledoux</h1>
        <h3>I am an assistant-professor in the 3D geoinformation group at the Delft University of Technology</h3>
        <a href="http://www.tudelft.nl"><img src="assets/img/tudwhite.png" width="150" alt=""></a>
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
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-53152577-1', 'auto');
    ga('send', 'pageview');
  </script>
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
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>  

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
      <i class="fa fa-times menu-close"></i>
      <a href="#home" class="smoothScroll">home</a>
      <a href="#about" class="smoothScroll">about</a>
      <a href="#projects" class="smoothScroll">projects</a>
      <a href="#pubs" class="smoothScroll">publications</a>
      <a href="#students" class="smoothScroll">students</a>
      <a href="#phdthesis" class="smoothScroll">PhD thesis</a>
      <a href="#contact" class="smoothScroll">contact</a>
      <a href="https://github.com/hugoledoux"><i class="fa fa-github fa-lg"></i></a>
      <a href="https://twitter.com/hugoledoux"><i class="fa fa-twitter fa-lg"></i></a>
    </div>
    <!-- Menu button -->
    <div id="menuToggle"><i class="fa fa-bars"></i></div>
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
        <div class="col-lg-10 col-lg-offset-1">
  """
  print >>s, s1
  f = codecs.open('students.md', mode='r', encoding="utf-8")
  html = markdown2.markdown(f.read(), extras=["smarty-pants"])
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
        <div class="col-lg-10 col-lg-offset-1">
  """
  print >>s, s1
  f = codecs.open('about.md', mode='r', encoding="utf-8")
  html = markdown2.markdown(f.read(), extras=["smarty-pants"])
  print >>s, html
  print >>s, '</div></div></div>'
  return s   


def write_code():
  return """
  <!-- ========== PROJECTS ========== -->
  <section id="projects"></section>
    <div class="container">
      <div class="row">
        <h2>projects I'm currently working on</h2>
        <div class="col-lg-10 col-lg-offset-1">
        <div class="col-lg-4">
          <a href="https://github.com/tudelft-gist/prepair" class="thumbnail">
            <img src="img/prepair_logo.png" alt="">
          </a>
          <h3>prepair</h3>
          Automatic repair of invalid polygons acc. to the international standard ISO19107
       </div>
        <div class="col-lg-4">
          <a href="https://github.com/tudelft-gist/pprepair" class="thumbnail">
            <img src="img/pprepair_logo2.png" alt=""></a>
          <h3>pprepair</h3>
          Automatic repair of GIS planar partitions
        </div>
        <div class="col-lg-4">
          <a href="http://geovalidation.bk.tudelft.nl/val3dity" class="thumbnail">
            <img src="img/val3dity_logo.png" alt="">
          </a>
          <h3>val3dity</h3>
          Validation of solids acc. to the international standard ISO19107
        </div>
        <div class="col-lg-4">
          <a href="http://3dsm.bk.tudelft.nl" class="thumbnail">
            <img src="img/3dsm.png" alt="">
          </a>
          <h3>3DSM</h3>
          Smart simplification of LiDAR datasets
        </div>
        <div class="col-lg-4">
          <a href="http://3dsm.bk.tudelft.nl/matahn" class="thumbnail">
            <img src="img/matahn.png" alt="">
          </a>
          <h3>MATAHN</h3>
          A user-friendly way to download parts of the <a href="http://www.ahn.nl">AHN2 datasets</a>
        </div>
        <div class="col-lg-4">
          <a href="http://www.geo5d.nl" class="thumbnail">
            <img src="img/geo5d.png" alt="">
          </a>
          <h3>geo5D</h3>
          Higher-dimensional modelling of geographical information (ie 4D+)
        </div>

      </div>
      </div>
    </div>
  """

if __name__ == "__main__":
    main()  
