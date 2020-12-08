import json

from flask import Flask, render_template, request

from data import goals, days, times

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/all/')
def render_all():
    return render_template('all.html')


@app.route('/goals/<goal>/')
def render_goal(goal):
    return render_template('goal.html')


@app.route('/profiles/<int:teacher_id>/')
def render_teacher(teacher_id):
    try:
        with open('data_base.json', 'r') as jf:
            teachers = json.load(jf)
            teacher = teachers[teacher_id]
        return render_template('profile.html',
                               teacher_id=teacher_id,
                               teacher=teacher,
                               goals=goals,
                               days=days,
                               times=times)
    except IOError:
        print("An IOError has occurred!")


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def route_request_done():
    return render_template('request_done,html')


@app.route('/booking/<int:teacher_id>/<day>/<time>/')
def route_booking(teacher_id, day, time):
    with open('data_base.json', 'r') as jf:
        teachers = json.load(jf)
        teacher = teachers[teacher_id]
        return render_template('booking.html',

    )


@app.route('/booking_done/')
def route_booking_done():
    return render_template('booking_done.html')


app.run('0.0.0.0', 8000)


