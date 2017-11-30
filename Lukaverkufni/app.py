import bottle
from beaker.middleware import SessionMiddleware
from sys import argv

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

bottle.run(host='0.0.0.0', port=argv[1])

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@bottle.route('/test')
def test():
  s = bottle.request.environ.get('beaker.session')
  s['test'] = s.get('test',0) + 1
  s.save()
  return 'Test counter: %d' % s['test']

bottle.run(app=app)

bottle.run(host='0.0.0.0', port=argv[1])
