from flask import Flask, send_from_directory
import importlib

app = Flask(__name__,template_folder='src/common/template/static')

@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>', methods=['POST', 'GET'])
def router(path):
  # route requests to "foo/bar/si" to
  # `si.py` in `bar` directory, which is in `foo` directory,
  # which is inside `root` directory of `roots`
  
  if path == '':
    return router('index')

  moduleObjectToRouteTo = None
  modulePathToRouteTo = path

  if '/' in modulePathToRouteTo:
    modulePathToRouteTo = modulePathToRouteTo.replace('/', '.')

  try:
    moduleObjectToRouteTo = importlib.import_module('routes.root.'+modulePathToRouteTo)
  except ModuleNotFoundError:
    #try if it's a static file
    return send_from_directory('static', path)

  return moduleObjectToRouteTo.main()

@app.errorhandler(404)
def fourOhFour(e):
  return router('404')

from waitress import serve
serve(app, host='0.0.0.0', port=80)