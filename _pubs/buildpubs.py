import os
import StringIO
import datetime

def write_pubs():
  s = StringIO.StringIO()
  header = "---\nlayout: page\ntitle: publications\n---\n\n"
  print >>s, header
  update = '<h1>Publications</h1>\n<span class="post-date">(last update: %s)</span>' % (datetime.date.today().isoformat())
  print >>s, update
  toc = gettoc()
  print >>s, toc
  print >>s, "\n{% raw %}"

  f = open('pubs.html')
  print >>s, f.read()
  print >>s, '{% endraw %}'
  return s 


def gettoc():    
    s = "\n|"
    for year in reversed(range(2003, 2016)):
        s += ' <a href="#%s">%s</a> |' % (year, year)
    return s



os.system("php go.php > pubs.html")
s = write_pubs()
# print s.getvalue()
f = open("../pubs.html", 'w')
f.write(s.getvalue())
f.close()

