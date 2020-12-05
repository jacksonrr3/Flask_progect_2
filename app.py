from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def render_main():
    return 'Здесь будет главная'

@app.route('/all/')
def render_all():
    return 'здесь будут преподы'

@app.route('/goals/<goal>/')
def render_goal(goal):
    return f'сдесь будет цель {goal}'

@app.route('/profiles/<int:id_teacher>/')
def render_teacher(id_teacher):
    return f'здесь будет препод {id_teacher}'

@app.route('/request/')
def render_request():
    return 'здесь будет заявка'

@app.route('/request_done/')
def route_request_done():
    return 'заявка на подбор отправлена'

@app.route('/booking/<int:id_teacher>/<day>/<time>/')
def route_booking_form(id_teacher, day, time):
    return f'сдеаь будет форма бронирования {id_teacher}'

@app.route('/booking_done/')
def route_booking_done():
    return 'заявка отправлена'



app.run('0.0.0.0', 8000)


