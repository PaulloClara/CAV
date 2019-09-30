from app.modules.utils import mathematical_characters


class Calculator(object):
    def __init__(self):
        self.mathematical_characters = mathematical_characters()

    def run(self, expression):
        result = eval(expression)
        return result

    def remove_unwanted_characters(self, expression):
        treated_expression = ''
        for character in expression:
            if character in self.mathematical_characters:
                treated_expression += character
        return treated_expression
