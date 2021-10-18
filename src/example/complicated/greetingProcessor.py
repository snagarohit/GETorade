from flask import render_template_string

# Note that below we're using fully qualified module path, i.e.,
# "src.example.complicated._emojiArt" and not simply "_emojiArt" because
# the execution context is "/main.py" (see https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x)
from src.example.complicated.__emojiArt import render

def renderBirthdayMessage(name, age):
  candleArt = render('candle') * age
  return render_template_string("\
  <b>Happy birthday, {{name}}!</b><br/><b>Here's {{age}} candles for you:</b><br/>{{candleArt}} \
  ", **locals())