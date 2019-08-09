from app.modules.utils import mathematicalCharacters


class Calculator(object):
  def __init__(self):
    self.mathematical_characters = mathematicalCharacters()

  def run(self, expression):
    result = eval(expression)
    return result

  def removeUnwantedCharacters(self, expression):
    treated_expression = ''
    for character in expression:
      treated_expression += character
    return treated_expression
