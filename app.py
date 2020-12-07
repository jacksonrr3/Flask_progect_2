import json

from flask import Flask, render_template, request

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
    with open('data_base.json', 'r') as jf:
        db = json.load(jf)
        teacher = db['teachers'][teacher_id]
        goals = db['goals']
        return render_template('profile.html', teacher=teacher, goals=goals)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def route_request_done():
    return render_template('request_done,html')


@app.route('/booking/<int:teacher_id>/<day>/<time>/')
def route_booking(teacher_id, day, time):
    return render_template('booking.html')


@app.route('/booking_done/')
def route_booking_done():
    return render_template('booking_done.html')


app.run('0.0.0.0', 8000)


