from app.modules.verifications import Verifications
from app.modules.calculator import Calculator


class Modules(object):
  def __init__(self):
    self.verifications = Verifications()
    self.calculator = Calculator()
