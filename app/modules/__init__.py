from app.modules.verifications import Verifications
from app.modules.calculator import Calculator
from app.modules.open_program import OpenProgram


class Modules(object):
  def __init__(self):
    self.verifications = Verifications()
    self.calculator = Calculator()
    self.open_program = OpenProgram()
