import os
from io import StringIO
import datetime


def write_pubs():
  s = StringIO()
  header = "---\nlayout: page\ntitle: publications\npermalink: /pubs/\n---\n\n"
  print (header, file=s)
  update = '<h1>Publications</h1>\n<span class="post-date">(last update: %s)</span>' % (datetime.date.today().isoformat())
  print (update, file=s)
  toc = gettoc()
  warning = getwarning()
  print (warning, file=s)
  print (toc, file=s)
  print ("\n{% raw %}", file=s)

  f = open('pubs.html')
  print (f.read(), file=s)
  print ('{% endraw %}', file=s)
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
      <br><br>
      <i class="fa fa-external-link"></i> <a href='https://orcid.org/0000-0002-1251-8654'> my ORCID page</a>
      <br>
      <i class="fa fa-external-link"></i> <a href='http://www.scopus.com/inward/authorDetails.url?authorID=23988925500&partnerID=MN8TOARS'> my SCOPUS page</a>
      </div>
    """
    return s


def gettoc():    
    s = "\n|"
    for year in reversed(range(2003, 2019)):
        s += ' <a href="#%s">%s</a> |' % (year, year)
    return s

os.chdir("./_pubs/")
os.system("php go.php > pubs.html")
s = write_pubs()
# print s.getvalue()
f = open("../pubs.html", 'w')
f.write(s.getvalue())
f.close()

