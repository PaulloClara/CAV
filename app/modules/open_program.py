import subprocess


class OpenProgram(object):
    def __init__(self):
        pass

    def run(self, program, parameters):
        output_file = open('./temp/outputs', mode='w+')
        command_line = ''
        if not parameters:
            command_line = f'{program} &'
        else:
            command_line = f'{program} {parameters} &'
        subprocess.run(
            command_line,
            shell=True,
            stdout=output_file,
            stderr=output_file,
            universal_newlines=True
        )

    def find_program(self, user_input, programs_bd):
        possible_program = ''
        for program in programs_bd:
            nickname = program['nickname']
            if nickname in user_input and nickname > possible_program:
                possible_program = program['value']

        return possible_program

    def find_params(self, user_input, parameters_bd):
        parameters = []
        for parameter in parameters_bd:
            if parameter['nickname'] in user_input:
                parameters.append(parameter['value'])

        return ' '.join(parameters)
