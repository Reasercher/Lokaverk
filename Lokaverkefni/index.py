import bottle
from bottle import run,route,redirect,request,post,template,app,response,static_file
from sys import argv
import pymysql
from beaker.middleware import SessionMiddleware
session_opts = {
    'session.type': 'file',

    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

products = [{"pid": 1, "name": "Chips ahoy", "price": 55},
            {"pid": 2, "name": "milky way", "price": 40},
            {"pid": 3, "name": "blue cream cookies", "price": 2000},
            {"pid": 4, "name": "Subway", "price": 61},
            {"pid": 5, "name": "skinny cream cookies", "price": 55},
            {"pid": 6, "name": "Oreos", "price": 7},
            {"pid": 7, "name": "Freshly bar", "price": 1},
            {"pid": 8, "name": "mini chips ahoy", "price": 360},

            ]
@route("/")
def homepage():
    return template("home.tpl")
@route('/nyskra')
def nyr():
    return template('newlogin.tpl')

@route('/donyskra', method='POST')
def nyr():
    user = request.forms.get('user')
    password = request.forms.get('pass')

    response.set_cookie("account", user, secret='some-secret-key')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0511002710', passwd='mypassword', db='Lokaverk' )

    cur = conn.cursor()


    cur.execute("SELECT count(*) FROM user where user=%s",(user))

    result = cur.fetchone()

    print(result)

    if result[0] == 0:
        cur.execute("INSERT INTO user Values(%s,%s)", (user, password))

        conn.commit()
        cur.close()

        conn.close()
        return redirect("/shop")
@route('/innskra')
def inn():
    return template('login.tpl')
@route('/doinnskra', method='POST')
def doinn():
    user = request.forms.get('user')
    password = request.forms.get('pass')
    response.set_cookie("account", user, secret='some-secret-key')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0511002710', passwd='mypassword', db='Lokaverk')
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM user where user=%s and pass=%s",(user,password))
    result = cur.fetchone()
    print(result)
    if result[0] == 1:
        cur.close()
        conn.close()
        return redirect("/shop")
@route("/logout")
def logout():
    response.set_cookie("account", "", expires=0)
    return redirect("/")

@route("/shop")
def shop():
    return template("shop.tpl" ,products=products)

@route("/cart")
def cart():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        session = request.environ.get('beaker.session')

        karfa = []


        if session.get('1'):

            vara1 = session.get('1')
            karfa.append(vara1)

        if session.get('2'):
            vara2 = session.get('2')
            karfa.append(vara2)

        if session.get('3'):
            vara3 = session.get('3')
            karfa.append(vara3)

        if session.get('4'):
            vara4 = session.get('4')
            karfa.append(vara4)

        if session.get('5'):
            vara5 = session.get('5')
            karfa.append(vara5)

        if session.get('6'):
            vara6 = session.get('6')
            karfa.append(vara6)
        if session.get('7'):
            vara7 = session.get('7')
            karfa.append(vara7)

        if session.get('8'):
            vara8 = session.get('8')
            karfa.append(vara8)


        return template("cart.tpl", karfa=karfa)

#hear you add the products in to your cart
@route("/cart/add/<id:int>")
def add_to_cart(id):
    if id == 1:
        session = request.environ.get('beaker.session')
        session["1"] = "Chips ahoy"
        session.save()
        return redirect("/cart")
    if id == 2:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 3:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 4:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 5:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 6:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 7:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 8:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")

    else:
        return redirect("/shop")


@route("/cart/remove")
def remove_from_cart():
    session = request.environ.get('beaker.session')

    session.delete()
    return redirect("/cart")
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')
@route('images/<filename:re:.*\.jpg>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='images', mimetype='images/jpg')
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='images', mimetype='images/png')
#Heroku
#bottle.run(host="0.0.0.0", port=argv[1])
#localhost
bottle.run(host="localhost", port=8080)