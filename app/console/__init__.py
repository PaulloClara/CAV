class Console(object):
    def __init__(self, stop, voice):
        self._stop = stop
        self._speech_activated = voice
        self.__layout_show = ('\n\t=> \033[1;32m{}\033[0;0m')
        self.__layout_show_error = ('\n\n\t==> \033[1;33m{}\033[0;0m\n\n')
        self.__layout_get = ('\n\t=> \033[1;34m{}\033[0;0m\n> ')

    def show(self, msg, type_msg=''):
        if type_msg == 'error':
            print(self.__layout_show_error.format(msg))
        else:
            print(self.__layout_show.format(msg))

    def get(self, msg='', type_input='str'):
        user_input = input(self.__layout_get.format(msg))

        self.check_stop_request(user_input)

        if type_input in ['int', 'float']:
            user_input = self.convert(user_input, msg, type_input)

        return user_input

    def check_stop_request(self, value):
        if value.lower() in ['exit', 'leave', 'get out']:
            self._stop()

    def convert(self, value, msg='', type_input='int'):
        try:
            if type_input == 'int':
                value = int(value)
            else:
                value = float(value)
        except ValueError:
            self.show('Invalid value!', type_msg='error')

            value = self.get(msg, type_input=type_input)

        return value
