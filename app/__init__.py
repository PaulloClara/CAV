from database import DB
from app.console import Console
from app.modules import Modules


class CAV(object):
    """
    class master

    control of the entire program flow

    Attrs:
        db (object): database manager
        modules (object): resource module
        console (object): handle input and output
        on (bool): running -- true
        user_input (str): user input in the round
    """

    def __init__(self, voice):
        """
        init class

        create database, modules (submodules) and console (in/out) object

        Args:
            voice (bool): enable or desable speech -- true (enable)
        """

        self._db = DB()
        self._modules = Modules()
        self._console = Console(stop=self.stop, voice=voice)

        self._on = True
        self._user_input = ''
        self._functionality = {}

    def run(self):
        """
        execution flow

        - get user input
        - find functionality
        - run functionality
        """

        self._user_input = self._console.get('How can I help you?').lower()
        self._functionality = self.find_functionality()

        if not self._functionality:
            self._console.show(
                'Sorry I do not understand',
                type_msg='error'
            )
            return

        for keyword in self._functionality['keywords_found']:
            self._user_input = self._user_input.replace(keyword['value'], '')

        if self._functionality['value'] == 'calculate':
            self.calculate()
        elif self._functionality['value'] == 'open_program':
            self.open_program()
        else:
            self._console.show(
                'Sorry, something went wrong...',
                type_msg='error'
            )

    def calculate(self):
        """
        calculate skill

        - clear user input
        - run calculator
        - show result
        """

        expression = self._modules.calculator.remove_unwanted_characters(
            self._user_input
        )

        result = self._modules.calculator.run(expression)

        self._console.show(f'The result is {result}!')

    def open_program(self):
        """
        open program skill

        - get all programs in database
        - find correct program
        - remove program from user input
        - get all parameters
        - run program with params
        """

        columns = ['id', 'nickname', 'value']

        sql_code = self._db.select('programs', columns=columns)
        all_programs = self._db.run(sql_code, columns=columns)

        program = self._modules.open_program.find_program(
            self._user_input,
            programs_bd=all_programs
        )

        if not program:
            self._console.show('Program not found', type_msg='error')
            return

        self._user_input = self._user_input.replace(program, '')

        sql_code = self._db.select('parameters', columns=columns)
        all_parameters = self._db.run(sql_code, columns=columns)

        parameters = self._modules.open_program.find_params(
            self._user_input,
            parameters_bd=all_parameters
        )

        self._modules.open_program.run(program, parameters)

    def find_functionality(self):
        columns = ['id', 'value', 'id_function']
        sql_code = self._db.select('keywords', columns=columns)
        keywords = self._db.run(sql_code, columns=columns)

        columns = ['id', 'value']
        sql_code = self._db.select('functions', columns=columns)
        functionalities = self._db.run(sql_code, columns=columns)

        functionality = self._modules.check.correct_functionality(
            self._user_input,
            keywords=keywords,
            functionalities=functionalities
        )

        return functionality

    def stop(self):
        print('Bye Bye')
        self._on = False
        exit()
