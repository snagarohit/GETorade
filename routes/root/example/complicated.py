from flask import request
from src.common.template import centeredHtml
from src.example.complicated.greetingProcessor import renderBirthdayMessage

def main():
  #birthday greetings
  name = request.args.get('name')
  age = int(request.args.get('age'))

  return centeredHtml.render(renderBirthdayMessage(name, age))