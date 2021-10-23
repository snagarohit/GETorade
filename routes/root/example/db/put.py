import src.common.db.aws as db
from flask import request, render_template_string
from src.common.template import centeredHtml

app = db.App("DBExample", "Content")
database = db.SimpleDatabase(app)

def main():
  data = request.args.get('data')
  database['data'] = data

  return centeredHtml.render(render_template_string("\
    <h4>Putting this in the database:</h4><br/><br/><h2>{{data}}</h2>\
  ", data=data))