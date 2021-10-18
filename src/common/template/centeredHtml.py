from flask import render_template

def render(htmlContent):
  return render_template('centeredContent.html', content=htmlContent)