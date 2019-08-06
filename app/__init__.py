from app.ui import UI


class CAV(object):
  def __init__(self):
    self.on = True
    self.ui = UI(stop=self.stop)

  def run(self):
    while self.on:
      self.ui.show(self.ui.get('Qual seu nome?'))
      self.ui.show(self.ui.get(f'Quantos anos vc tem?', type_input='int'))

  def stop(self):
    self.on = False
    self.ui.show('Bye Bye')
    exit()
