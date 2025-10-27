from flask import Blueprint, render_template

course_index_blueprint = Blueprint('course_index', __name__)

@course_index_blueprint.route('/')
def index():
    return render_template('courses.html')
