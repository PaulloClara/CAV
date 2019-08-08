class Verifications(object):
  def __init__(self):
    pass

  def checkCorrectFunction(self, user_input, key_expressions, functions):
    for function in functions:
      function['possibility'] = 0
    for key_expression in key_expressions:
      if key_expression['value'] in user_input:
        index = key_expression['id_function'] - 1
        functions[index]['possibility'] += 1
    probable_function = functions[0]
    for function in functions:
      if function['possibility'] > probable_function['possibility']:
        probable_function = function
    if not probable_function['possibility']:
      return None
    return probable_function['value']
