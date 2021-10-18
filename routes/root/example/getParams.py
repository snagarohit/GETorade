from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
  name = request.args.get('name')
  age = request.args.get('age')

  return centeredHtml.render(render_template_string("\
    <h4>Hi <b>{{name}}</b>! You're {{age}} years old 😱</h4>\
  ", **locals()))