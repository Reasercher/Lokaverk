from bottle import *
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)
@bottle.route("/")
def index():
    return bottle.template("index.tpl")
def session_test():
    s = bottle.request.environ.get('beaker.session')
    s['text'] ='vara'
    s.save()
    bottle.redirect('/output')


@bottle.route('/output')
def session_output():
    s = bottle.request.environ.get('beaker.session')
    return s['text']

@bottle.route("/add/<item>")
def addtocart(item):
    print(item)
    return bottle.redirect("/cart")
@bottle.route("/cart")
def cart():
    return

bottle.run(app=app, host='localhost', port=5000, debug=True, reloader=True)
