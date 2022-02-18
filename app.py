from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config["SECRET_KEY"] = "w57h63ff"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def compile_story():
    compiled_story = story.generate(request.args)
    return render_template("story.html", compiled_story=compiled_story)
