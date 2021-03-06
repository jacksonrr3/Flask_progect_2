import json
import operator
import random

from flask import Flask, render_template, abort, request

from data import goals, days


app = Flask(__name__)


def read_data_from_json_file(path):
    """ reading data from data_base json file, return dict """
    try:
        with open(path, 'r') as jf:
            return json.load(jf)
    except IOError:
        print("An IOError has occurred!")


def write_data_to_json_file(path, data):
    """ writing data to data_base json file"""
    try:
        with open(path, 'w') as jf:
            json.dump(data, jf)
    except IOError:
        print("An IOError has occurred!")


@app.route('/')
def render_index():
    teachers = read_data_from_json_file('data_base.json')
    ch_teachers = random.sample(teachers, 6)
    return render_template('index.html',
                           teachers=ch_teachers,
                           goals=goals)


@app.route('/all/', methods=['POST', 'GET'])
def render_all():
    teachers = read_data_from_json_file('data_base.json')
    selected_value = request.args.get('selected')
    if selected_value == '1':
        random.shuffle(teachers)
    elif selected_value == '2':
        teachers.sort(key=operator.itemgetter("rating"), reverse=True)
    elif selected_value == '3':
        teachers.sort(key=operator.itemgetter("price"), reverse=True)
    elif selected_value == '4':
        teachers.sort(key=operator.itemgetter("price"))
    else:
        random.shuffle(teachers)
    return render_template('all.html',
                           teachers=teachers,
                           goals=goals)


@app.route('/goals/<goal>/')
def render_goal(goal):
    teachers = read_data_from_json_file('data_base.json')
    teachers.sort(key=operator.itemgetter("rating"), reverse=True)
    return render_template('goal.html',
                           goal=goal,
                           goals=goals,
                           teachers=teachers)


@app.route('/profiles/<int:teacher_id>/')
def render_teacher(teacher_id):
    teachers = read_data_from_json_file('data_base.json')
    if teacher_id >= len(teachers):
        abort(404)
    teacher = teachers[teacher_id]
    return render_template('profile.html',
                           teacher=teacher,
                           goals=goals,
                           days=days)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def route_request_done():
    goal = request.form.get("goal")
    time = request.form.get("time")
    name = request.form.get("name")
    phone = request.form.get("phone")
    req = {'goal': goal, 'time': time, 'name': name, 'phone': phone}
    requests = read_data_from_json_file('request.json')
    requests.append(req)
    write_data_to_json_file('request.json', requests)
    return render_template('request_done.html',
                           goal=goal,
                           time=time,
                           name=name,
                           phone=phone)


@app.route('/booking/<int:teacher_id>/<day>/<time>/')
def route_booking(teacher_id, day, time):
    time = time + ':00'
    teachers = read_data_from_json_file('data_base.json')
    if teacher_id >= len(teachers) or day not in days:
        abort(404)
    teacher = teachers[teacher_id]
    return render_template('booking.html',
                           teacher=teacher,
                           days=days,
                           day=day,
                           time=time)


@app.route('/booking_done/', methods=['POST'])
def route_booking_done():
    teachers = read_data_from_json_file('data_base.json')
    client_weekday = request.form.get("clientWeekday")
    client_time = request.form.get("clientTime")
    client_teacher = request.form.get("clientTeacher")
    client_name = request.form.get("clientName")
    client_phone = request.form.get("clientPhone")
    teachers[int(client_teacher)]["free"][client_weekday][client_time] = False
    write_data_to_json_file('data_base.json', teachers)

    bookings = read_data_from_json_file('booking.json')
    bookings.append((client_name, client_phone, client_weekday, client_time))
    write_data_to_json_file('booking.json', bookings)

    client_weekday = days[client_weekday]
    return render_template('booking_done.html',
                           day=client_weekday,
                           time=client_time,
                           client_name=client_name,
                           client_phone=client_phone)


if __name__ == '__main__':
    app.run()


