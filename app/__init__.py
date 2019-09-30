from database import DB
from app.console import Console
from app.modules import Modules


class CAV(object):
    def __init__(self, voice):
        self.db = DB()
        self.modules = Modules()
        self.console = Console(stop=self.stop, voice=voice)
        self.on = True
        self.user_input = ''

    def run(self):
        self.user_input = self.console.get('Em que posso ajudar?').lower()

        probable_function = self.findProbableFunction()

        if not probable_function:
            self.console.show(
                'Desculpe, nao consegui entender...', type_msg='error')
            return

        if probable_function['value'] == 'calculate':
            self.calculate(probable_function['keywords_found'])
        elif probable_function['value'] == 'open_program':
            self.openProgram(probable_function['keywords_found'])
        else:
            self.console.show('Desculpe, ocorreu um erro...', type_msg='error')

    def calculate(self, keywords_found):
        user_input = self.clearUserInput(keywords_found)
        expression = self.modules.calculator.removeUnwantedCharacters(
            user_input)
        result = self.modules.calculator.run(expression)
        self.console.show(f'O resultado é {result}!')

    def openProgram(self, keywords_found):
        user_input = self.clearUserInput(keywords_found)

        columns = ['id', 'nickname', 'value']

        sql_code = self.db.select('programs', columns=columns)
        all_programs = self.db.run(sql_code, columns=columns)
        program = self.modules.open_program.findProgram(
            user_input, all_programs)

        if not program:
            self.console.show(
                'O programa não foi encontrado no banco de dados', type_msg='error')
            return

        user_input = user_input.replace(program, '')

        sql_code = self.db.select('parameters', columns=columns)
        all_parameters = self.db.run(sql_code, columns=columns)
        parameters = self.modules.open_program.findParameters(
            user_input, all_parameters)

        self.modules.open_program.run(program, parameters)

    def findProbableFunction(self):
        columns = ['id', 'value', 'id_function']
        sql_code = self.db.select('keywords', columns=columns)
        keywords = self.db.run(sql_code, columns=columns)

        columns = ['id', 'value']
        sql_code = self.db.select('functions', columns=columns)
        functions = self.db.run(sql_code, columns=columns)

        probable_function = self.modules.verifications.checkCorrectFunction(
            self.user_input,
            keywords,
            functions
        )

        return probable_function

    def clearUserInput(self, keywords_found):
        user_input = self.user_input

        for keyword in keywords_found:
            user_input = user_input.replace(keyword['value'], '')

        return user_input

    def stop(self):
        print('Bye Bye')
        self.on = False
        exit()
