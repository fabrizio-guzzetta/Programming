from flask import Flask
from routes.courses import course_blueprint


app = Flask(__name__)
app.secret_key = "fdsfgshfghfjsfhd"


app.register_blueprint(course_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
