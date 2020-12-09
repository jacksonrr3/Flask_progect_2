import json

from flask import Flask, render_template, abort, request

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
            if teacher_id >= len(teachers):
                abort(404)
            teacher = teachers[teacher_id]
        return render_template('profile.html',
                               teacher=teacher,
                               goals=goals,
                               days=days)
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
    try:
        time = time + ':00'
        with open('data_base.json', 'r') as jf:
            teachers = json.load(jf)
            if teacher_id >= len(teachers) \
                    or day not in days \
                    or time not in times:
                abort(404)
            teacher = teachers[teacher_id]

        return render_template('booking.html',
                                   teacher=teacher,
                                   days=days,
                                   day=day,
                                   time=time)
    except IOError:
        print("An IOError has occurred!")


@app.route('/booking_done/', methods=['POST'])
def route_booking_done():
    try:
        with open('data_base.json', 'r') as jf:
            teachers = json.load(jf)

        client_weekday = request.form.get("clientWeekday")
        client_time = request.form.get("clientTime")
        client_teacher = request.form.get("clientTeacher")
        client_name = request.form.get("clientName")
        client_phone = request.form.get("clientPhone")

        teachers[int(client_teacher)]["free"][client_weekday][client_time] = False

        with open('data_base.json', 'w') as jf:
            json.dump(teachers, jf)
        client_weekday = days[client_weekday]
        return render_template('booking_done.html',
                               day=client_weekday,
                               time=client_time,
                               client_name=client_name,
                               client_phone=client_phone
                               )
    except IOError:
        print("An IOError has occurred!")


app.run('0.0.0.0', 8000)


