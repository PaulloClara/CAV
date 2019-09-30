class Verifications(object):
    def __init__(self):
        pass

    def checkCorrectFunction(self, user_input, keywords, functions):
        for function in functions:
            function['keywords_found'] = []
        for keyword in keywords:
            if keyword['value'] in user_input:
                index = keyword['id_function'] - 1
                functions[index]['keywords_found'].append(keyword)
        probable_function = functions[0]
        for function in functions:
            function_score = len(function['keywords_found'])
            probable_function_score = len(probable_function['keywords_found'])
            if function_score > probable_function_score:
                probable_function = function
        if not probable_function['keywords_found']:
            return None
        return probable_function
