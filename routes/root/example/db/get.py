import src.common.db.aws as db
from flask import render_template_string
from src.common.template import centeredHtml

app = db.App("DBExample", "Content")
database = db.SimpleDatabase(app)

def main():
  data = database['data']

  return centeredHtml.render(render_template_string("\
    <h4>Fetched this from the database:</h4><br/><br/><h2>{{data}}</h2>\
  ", data=data))