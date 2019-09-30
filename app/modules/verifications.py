class Verifications(object):
    def __init__(self):
        pass

    def correct_functionality(self, user_input, keywords, functionalities):
        for functionality in functionalities:
            functionality['keywords_found'] = []

        for keyword in keywords:
            if keyword['value'] in user_input:
                index = keyword['id_function'] - 1
                functionalities[index]['keywords_found'].append(keyword)

        probable_function = functionalities[0]

        for functionality in functionalities:
            function_score = len(functionality['keywords_found'])
            probable_function_score = len(probable_function['keywords_found'])
            if function_score > probable_function_score:
                probable_function = functionality

        if not probable_function['keywords_found']:
            return None

        return probable_function
