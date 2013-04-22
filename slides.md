=== {"styles": ["notslide", "just_title"], "name":"title", "rotate": 90}
# Impressor

=== {"styles": ["just_title"]}
# [Impressor](http://scommab.github.com/impressor/) is a tool for generating [impress.js](http://github.com/bartaz/impress.js/) presentations 

=== 
# What does Impressor do?
* It generates interesting looking presentations in a snap
* It lets you write your slides in simple markdown
* It gives you slide templates for both slide style and slide placement

=== {"styles": ["just_title"]}
# What do the different slide placement templates look like?

=== {"type": "behind", "styles": ["just_title"]}
# Slides can be behind other slides


=== {"type":"under", "styles": ["just_title"]}
# Slides can be under other slides

=== {"type": "under", "rotate":180, "styles": ["just_title"]}
# Slides can be Rotated

=== {"type": ["reset", "default"], "styles": ["just_title"]}
# And Slides can be reset back to the base line

=== {"styles": ["just_title"]}
# Slides can also be in different colors

=== {"type": "under", "styles": ["just_title", "blue"]}
# Blue

=== {"type": "under", "styles": ["just_title", "red"]}
# Red

=== {"type": "under", "styles": ["just_title", "background_img"]}
# Or with background images

=== {"type": "under", "styles": ["notslide"]}
# Slides can even have no background

=== {"type": ["reset", "default"], "styles": ["just_title", "hidden_slide"]}
# Slides can be hidden until they are selected

=== {"styles": ["just_title"]}
# What do the slide format templates look like

=== {"type":"under", "styles": ["just_title"]}
# This is a slide with large text

=== {"type":"under", "styles": ["subtitles"]}
## Slides with multiple sections 
* These slides work well with lists on them

## And multiple topics
With multiple bits of information


=== {"type": ["reset", "default"]}
# And the default styling

=== {"styles": ["just_title"]}
# All these slide styles and types can be mixed and matched

=== {"styles": ["just_title"]}
# There are also default text styles

=== {"type": "under", "styles": ["subtitles"]}
## Text Stylings 
* <span class="tiny">Tiny Text</span>
* <div class="note">Notes</div>

## Code sections
    This could be some code
    Or anything else you want monospaced

=== {"type": "under", "styles": ["subtitles"]}
## Animated Stylings 
* <b class="positioning">Positioning</b>
* <b class="scaling">Scaling</b>
* Rotating <b class="rotating90">90 degrees</b>

=== {"type":"under", "styles": ["subtitles"]}
## Using Images
![Hey Girl](img/hey-girl.png)

===  {"type":["reset", "default"], "styles": ["just_title"]}
# You can also manually place slides

=== {"z_abs":-10000, "y_abs": 1500, "x": 0}
# Either with absolute distances 

=== {"z": 10000, "y": 1500, "x":0}
# or relative distances

=== {"type": ["reset", "default"], "styles": ["just_title"]}
# And back to normal


=== {"type": ["reset", "default"], "styles": ["just_title"]}
# Now with Graphs

=== {"type":"under"}
# Bar graphs
<div class="bar_chart"
     id="graph1"
     xkey='graphs'
     ykeys='["awesome"]'
     labels='["Awesomeness"]'
     data='[
        {"graphs": 1, "awesome": 2},
        {"graphs": 2, "awesome": 4},
        {"graphs": 3, "awesome": 8}
     ]'
></div>

=== {"type":"under"}
# Line graphs
<div class="line_chart"
     id="graph2"
     xkey='date'
     ykeys='["awesome"]'
     labels='["Awesomeness"]'
     data='[
       {"date": "2010", "awesome": 0},
       {"date": "2011", "awesome": 2},
       {"date": "2012", "awesome": 8}
     ]'
> </div>


=== {"type":"under"}
# Donut graphs
<div class="donut_chart"
     id="graph3"
     data='[
       {"label": "Graph 1", "value": 2},
       {"label": "Graph 2", "value": 4},
       {"label": "Graph 3", "value": 8}
     ]'
></div>


=== {"type": ["reset", "default"], "styles": ["just_title"]}
# Customizable Template Files
* HTML Template - [`templates/template.html`](https://github.com/scommab/impressor/blob/master/templates/template.html)
* Slide templates - [`templates/types.json`](https://github.com/scommab/impressor/blob/master/templates/types.json)
* CSS Styles - [`show/styles.css`](https://github.com/scommab/impressor/blob/master/show/css/styles.css)


===
# Example Slides
    === {"styles": ["notslide", "just_title"]}
    # A simple slide show
    === {"styles": ["just_title"]}
    # A single slide
    === {"type":"under"}
    some interesting content

=== {"styles": ["just_title"]}
# This presentation's source: [`slides.md`](https://github.com/scommab/impressor/blob/master/slides.md)

=== {"name":"overview", "styles": ["notslide", "hidden_slide"], "x_abs":7000, "y_abs":1500, "scale":15}
<br/><br/> <br/><br/> <br/><br/>
<div style="font-size: 30%; padding-top: 100px; text-align: right;">
If you like the presentation try <a href="https://github.com/scommab/impressor">impressor</a>
</div>

