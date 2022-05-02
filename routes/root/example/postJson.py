from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
  json_req = request.json
  name = json_req['name']
  age = json_req['age']

  return centeredHtml.render(render_template_string("\
    <h4>Hi <b>{{name}}</b>! You're {{age}} years old 😱</h4>\
  ", **locals()))