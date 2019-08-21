import subprocess


class OpenProgram(object):
  def __init__(self):
    pass

  def run(self, program, parameters):
    output_file = open('./temp/outputs', 'w+')
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

  def findProgram(self, user_input, all_programs):
    possible_program = ''
    for program in all_programs:
      nickname = program['nickname']
      if nickname in user_input and nickname > possible_program:
        possible_program = program['value']

    return possible_program

  def findParameters(self, user_input, all_parameters):
    parameters = []
    for parameter in all_parameters:
      if parameter['nickname'] in user_input:
        parameters.append(parameter['value'])

    return ' '.join(parameters)
