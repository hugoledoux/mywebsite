import os
import datetime


def write_pubs():
  s = ""
  header = "---\nlayout: page\ntitle: publications\npermalink: /pubs/\n---\n\n"
  s += header
  update = '<h1>Publications</h1>\n<span class="post-date">(last update: %s)</span>' % (datetime.date.today().isoformat())
  s += update
  toc = gettoc()
  warning = getwarning()
  s += warning
  s += toc
  s += "\n{% raw %}"
  f = open('pubs.html')
  s += f.read()
  s += '{% endraw %}'
  os.remove('pubs.html')
  return s 


def getwarning():    
    s = """<div class="message">
      I provide here the author's version of most of my papers. 
      These are for <em>personal use only</em>, and not for redistribution or commercial use. 
      Please use the official published version ( <a><i class="fa fa-bookmark"></i></a> ) if you have access to it.
      <br><br>
      <a><i class="ai ai-open-access-square"></i></a> = open access
      <br><br>
      <a><i class="fa fa-github"></i></a> = the "reproducibility repository", where the code and/or the data needed to reproduce the results of the paper, is given.
      <hr>
      <a><i class="ai ai-orcid"></i></a> <a href='https://orcid.org/0000-0002-1251-8654'> my ORCID page</a>
      <br>
      <a><i class="fa fa-archive"></i></a> <a href='http://www.scopus.com/inward/authorDetails.url?authorID=23988925500&partnerID=MN8TOARS'> my SCOPUS page</a>
      <br>
      <a><i class="ai ai-google-scholar"></i></a> <a href='https://scholar.google.com/citations?user=NWmgjlMAAAAJ&hl=en'> my Google Scholar page</a>
      </div>
    """
    return s


def gettoc():    
    s = "\n|"
    for year in reversed(range(2003, 2023)):
        s += ' <a href="#%s">%s</a> |' % (year, year)
    return s

os.chdir("./_pubs/")
os.system("php go.php > pubs.html")
s = write_pubs()
f = open("../pubs.html", 'w')
f.write(s)
f.close()

