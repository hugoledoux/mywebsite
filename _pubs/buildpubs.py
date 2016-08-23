import os
import StringIO
import datetime


def write_pubs():
  s = StringIO.StringIO()
  header = "---\nlayout: page\ntitle: publications\npermalink: /pubs/\n---\n\n"
  print >>s, header
  update = '<h1>Publications</h1>\n<span class="post-date">(last update: %s)</span>' % (datetime.date.today().isoformat())
  print >>s, update
  toc = gettoc()
  warning = getwarning()
  print >>s, warning
  print >>s, toc
  print >>s, "\n{% raw %}"

  f = open('pubs.html')
  print >>s, f.read()
  print >>s, '{% endraw %}'
  os.remove('pubs.html')
  return s 


def getwarning():    
    s = """<div class="message">
      I provide here the author's version of most of my papers. 
      These are for <em>personal use only</em>, and not for redistribution or commercial use. 
      Please use the official published version ( <i class="fa fa-bookmark"></i> ) if you have access to it.
      <br><br>
      Where applicable, a link to the "reproducibility repository" ( <i class="fa fa-github"></i> ), where the code and/or the data needed to reproduce the results of the paper, is given.
      </div>
    """
    return s


def gettoc():    
    s = "\n|"
    for year in reversed(range(2003, 2018)):
        s += ' <a href="#%s">%s</a> |' % (year, year)
    return s

os.chdir("./_pubs/")
os.system("php go.php > pubs.html")
s = write_pubs()
# print s.getvalue()
f = open("../pubs.html", 'w')
f.write(s.getvalue())
f.close()

