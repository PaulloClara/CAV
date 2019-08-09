from app.ui import UI
from app.modules import Modules
from database import DB


class CAV(object):
  def __init__(self):
    self.on = True
    self.user_input = ''
    self.ui = UI(stop=self.stop)
    self.modules = Modules()
    self.db = DB()

  def run(self):
    while self.on:
      self.user_input = self.ui.get('Em que posso ajudar?').lower()
      probable_function = self.findProbableFunction()
      if not probable_function:
        self.ui.show('Desculpe, nao consegui entender...', type_msg='error')
        self.run()
      if probable_function['value'] == 'calculate':
        self.calculate(probable_function['keywords_found'])
      elif probable_function['value'] == 'open_program':
        self.openProgram()
      else:
        self.ui.show('Desculpe, ocorreu um erro...', type_msg='error')

  def calculate(self, keywords_found):
    user_input = self.clearUserEntries(keywords_found)
    expression = self.modules.calculator.removeUnwantedCharacters(user_input)
    result = self.modules.calculator.run(expression)
    self.ui.show(f'O é resultado é {result}!')

  def openProgram(self):
    pass

  def findProbableFunction(self):
    # Buscando keywords e functions no BD
    columns = ['id', 'value', 'id_function']
    sql_code = self.db.select('keywords', columns=columns)
    keywords = self.db.run(sql_code, columns=columns)
    columns = ['id', 'value']
    sql_code = self.db.select('functions', columns=columns)
    functions = self.db.run(sql_code, columns=columns)
    # Verificando qual funcao tem maior chance de estar carreta
    probable_function = self.modules.verifications.checkCorrectFunction(
      self.user_input,
      keywords,
      functions
    )
    return probable_function

  def clearUserEntries(self, keywords_found):
    user_input = self.user_input
    for keyword in keywords_found:
      user_input = user_input.replace(keyword['value'], '')
    return user_input

  def stop(self):
    self.on = False
    self.ui.show('Bye Bye')
    exit()
