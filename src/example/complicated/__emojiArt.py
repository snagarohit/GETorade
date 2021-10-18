def __candle():
   return "🕯️"

def __default():
  return "😵"

def render(artName):
  if artName == 'candle':
    return __candle()
  else:
    return __default()