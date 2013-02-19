import markdown2
import json
import sys

types = {}
with open("templates/types.json") as types_file:
  types = json.loads(types_file.read())

class Slide:
  def __init__(self, style, last_slide=None):
    self.style = style
    self.content = []
    self.last_slide = last_slide
    self.slide_num = 1
    self.total_slide_num = ""
    if self.last_slide:
      self.slide_num = self.last_slide.slide_num + 1
    self.types = []
    details = {}
    if " " in style:
      d_json = style[style.index(" ")+1:]
      details = json.loads(d_json)
    if "type" in details:
      t = details["type"]
      if isinstance(t, list):
        self.types = t
      else:
        self.types = [t]
    else:
      self.types = ["default"]
    self.details = {}
    for t in self.types:
      self.details.update(types.get(t, {}))
    self.details.update(details)
    #if "x" not in self.details:
    #  self.details["x"] = 1000
    self.x = self.calcPos("x")
    self.y = self.calcPos("y")
    self.z = self.calcPos("z")

  def addLine(self, l):
    self.content.append(l.rstrip())

  def calcPos(self, pos):
    if hasattr(self, pos):
      return getattr(self, pos)
    abs_pos = self.details.get(pos+"_abs", None)
    if abs_pos is not None:
      return abs_pos
    offset = self.details.get(pos, 0)
    if not self.last_slide:
      return offset
    p = self.last_slide.calcPos(pos) + offset
    return p

  def getStyles(self):
    styles = ["step"]
    s = self.details.get("styles", [])
    if isinstance(s, list):
      styles.extend(s)
    elif s:
      #it's not a list, it's just a string so just append it
      styles.append(s)
    if "notslide" not in styles:
      styles.append("slide")
    return styles

  def toHtml(self):
    r = self.details.get("rotate", 0)
    s = self.details.get("scale", 1)
    name = self.details.get("name", "")
    body = markdown2.markdown("\n".join(self.content))
    body += "<div class='slide_number'>%d<span class='total_slide_number'>/%s</span></div>" % (self.slide_num, self.total_slide_num)
    pos = ("data-x='%d' data-y='%d' data-z='%d' " + 
           "data-rotate='%d' data-scale='%d'") % \
          (self.x, self.y, self.z, r, s)
    html = "<div id='%s' class='%s' %s>%s</div>" % \
           (name, " ".join(self.getStyles()), pos, body)
    return html

def load_slides(f):
  slides = []
  content = None
  with open(f) as slides_file:
    for l in slides_file:
      if l.startswith("==="):
        if content:
          slides.append(content)
        content = Slide(l.strip(), content)
        continue
      if content:
        content.addLine(l.rstrip())
  slides.append(content)
  for s in slides:
    s.total_slide_num = len(slides)
  return slides

if len(sys.argv) <= 1:
  print """
Usage:
       make_slides.py <slides file> > output.html
"""
  sys.exit(-1)

slides_file_name = sys.argv[1]

slides = load_slides(slides_file_name)
slides_html = []
for s in slides:
  slides_html.append(s.toHtml())

with open("templates/template.html") as template_file:
  print template_file.read() % "".join(slides_html)
