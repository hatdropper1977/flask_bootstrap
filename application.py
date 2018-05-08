#!/usr/bin/env python
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from models import QuizForm

class Config(object):
    SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

application = Flask(__name__)
application.config.from_object(Config)

Bootstrap(application)

@application.route('/', methods=['GET', 'POST'])
def take_test():
    form = QuizForm(request.form)
    if not form.validate_on_submit():
        return render_template('take_quiz_template.html', form=form)
    if request.method == 'POST':
        return 'Submitted!'

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
