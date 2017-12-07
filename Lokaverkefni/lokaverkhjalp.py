from bottle import run, template, route, request, response, post, redirect

@route('/')
def index():
    return template("index.tpl")

@route('/logout')
def index2():
    response.set_cookie("account", "", expires=0)
    return redirect("/")


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    name = "admin"
    pword = "admin"

    if (username == name and password == pword):
        response.set_cookie("account", username, secret='some-secret-key')
        return redirect("/restricted")
    else:
        return "<p>Login failed.</p>"

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title></title>
        </head>
        <body>
            <p>Welcome! You are now logged in.</p>"
            <a href="/logout">Log out</a>
        </body>
        </html>
        """""""""
    else:
        return "You are not logged in. Access denied."

run(host="localhost",port=8080,reloader=True)