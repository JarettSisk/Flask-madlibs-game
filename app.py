from flask import Flask, request, render_template
app = Flask(__name__)
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'

toolbar = DebugToolbarExtension(app)

# Create a new story
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# route to handle use input
@app.route("/form")
def form_route():
    return render_template("form.html", questions=story.prompts)

# Route to generate and show the story
@app.route("/story")
def story_route():
    # Generate story given the users input
    story_text = story.generate(request.args)
    return render_template("story.html", new_story=story_text)


