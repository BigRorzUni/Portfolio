from flask import Blueprint, render_template
from .projects import projects

base = Blueprint('home', __name__)

@base.route("/")
def index():
    return render_template("index.html", projects=projects)