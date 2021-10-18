from flask import Flask, send_from_directory
import importlib

app = Flask(__name__,template_folder='template/static')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def master_route(path):
  module = None

  if path == '':
    path = 'index'

  try:
    module = importlib.import_module('routes.root.'+path)
  except ModuleNotFoundError:
    module = None

  if module == None:
    #try if it's a static file
    return send_from_directory('static', path)
  else:
    return module.main()

@app.errorhandler(404)
def fourOhFour(e):
  return master_route('404')
  


# @app.route('/')
# def index():
#   return template.centeredHtml.render('<img src="https://i.pinimg.com/originals/3a/7e/43/3a7e434cc7cde1b176234cc12b3a5bc8.gif"/>')

@app.route('/ping')
def ping():
  return {'ping':'pong'}
  
@app.route('/verify-ownership')
def verify_ownership():

  return 'verified'


from waitress import serve
serve(app, host='0.0.0.0', port=80)