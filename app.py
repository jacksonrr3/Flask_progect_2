from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login/')
def render_login():

    form = """
      <form class="search-form" action="/search/" method="post">
        <input type="text" name="username">
        <input type="submit" value="найти">
      </form>
      """
    return form

@app.route('/search/', methods=['POST'])
def render_search():
    username = request.form['username']
    password = request.form.get('password')

    return f'Login - {username}, pass - {password}'


app.run('0.0.0.0', 8000)


