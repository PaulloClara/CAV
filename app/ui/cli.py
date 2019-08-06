class CLI(object):
  def __init__(self):
    self.__layout_show = ('\n\t=> \033[1;32m{}\033[0;0m')
    self.__layout_show_error = ('\n\n\t==> \033[1;33m{}\033[0;0m\n\n')
    self.__layout_get = ('\n\t=> \033[1;34m{}\033[0;0m\n> ')

  def show(self, msg, type_msg=''):
    if type_msg == 'error':
      print(self.__layout_show_error.format(msg))
    else:
      print(self.__layout_show.format(msg))

  def get(self, msg):
    return input(self.__layout_get.format(msg))
