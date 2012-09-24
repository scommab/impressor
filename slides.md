=== {"styles": ["notslide", "just_title"], "name":"title", "rotate": 90}
# Impressor

=== {"styles": ["just_title"]}
# Impressor is a tool for generating <a href="http://bartaz.github.com/impress.js/">impress.js</a> presentations 

=== 
# What does Impressor do?
* It generates interesting looking presentations in a snap
* It lets you write your slides in markdown
* It lets you use simple slide templates (for slide style and slide placement)

=== {"styles": ["just_title"]}
# What do the different slide placement templates look like?

=== {"type": "behind", "styles": ["just_title"]}
# Slides can be behind other slides


=== {"type":"under", "styles": ["just_title"]}
# Slides can be under other slides

=== {"type": "under", "rotate":180, "styles": ["just_title"]}
# Slides can be Rotate

=== {"type": ["reset", "default"], "styles": ["just_title"]}
# And Slides can be reset back to the base line

=== {"styles": ["just_title"]}
# What do the different slide effect templates look like?

=== {"type": "under", "styles": ["hidden_slide", "just_title"]}
# Slides can be hidden until they are selected

=== {"type": "under", "styles": ["notslide"]}
# Slides can have no background

=== {"type": ["reset", "default"], "styles": ["just_title"]}
# What do the slide format templates look like

=== {"type":"under", "styles": ["just_title"]}
# Slides with just titles

=== {"type":"under", "styles": ["subtitles"]}
## Slides with multiple sections 
* These slides work well with lists on them

## And mutliple topics
With mutliple bits of information


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

===  {"type":["reset", "default"], "styles": ["just_title"]}
# You can also manually place slides

=== {"z_abs":-10000, "y_abs": 1500, "x": 0}
# Either with absolute distances 

=== {"z": 10000, "y": 1500, "x":0}
# or relative distances

=== {"type": ["reset", "default"], "styles": ["just_title"]}
# And back to normal

=== {"styles": ["just_title"]}
# All templates are defined in `types.json`

=== {"styles": ["just_title"]}
# All styles are defined in `impressor.css`

=== {"styles": ["just_title"]}
# The text of your slides go in to `slides.md`

=== {"styles": ["just_title"]}
# If you wish to edit the html template used to generate the slides it's in `template.html`

===
# Example Slide
    === {"type":"under", "styles": ["just_title"]}
    # Slides with just titles
=== {"name":"overview", "styles": ["notslide"], "x_abs":7000, "y_abs":1500, "scale":15}

