from app.ui.cli import CLI
from app.ui.gui import GUI


class UI(object):
  def __init__(self, stop, ui='cli', speech=False):
    self.cli = CLI()
    self.gui = GUI()
    self.stop = stop
    self.ui_selected = ui
    self.speech_activated = speech

  def show(self, msg='', type_msg=''):
    if self.ui_selected == 'cli':
      self.cli.show(msg, type_msg=type_msg)
    else:
      self.gui.show(msg)

  def get(self, msg='', type_input='str'):
    user_input = ''
    if self.ui_selected == 'cli':
      user_input = self.cli.get(msg)
    else:
      user_input = self.gui.get(msg)
    self.checkStopRequest(user_input)
    if type_input == 'int':
      user_input = self.convertInt(user_input, msg)
    return user_input

  def checkStopRequest(self, value):
    if value.lower() in ['sair', 'exit', 'off']:
      self.stop()

  def convertInt(self, value, msg=''):
    try:
      value = int(value)
    except ValueError:
      self.show('Valor Invalido!', type_msg='error')
      value = self.get(msg, type_input='int')
    return value
