import os
import keyword
import fileinput
"""  recognize python code in an html template
and parse it so the styling can be automated"""
def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Parser(object):

    def __init__(self, filename):
        self.filename = filename
        self.variables = {
            'keyword': keyword.kwlist,
            'built in function': [f for f in dir(__builtins__) if 'Error' not in f and 'Warning' not in f and 'Exception' not in f],
            'exceptions': [f for f in dir(__builtins__) if 'Error' in f or 'Exception' in f or 'Warning' in f],
            'special attribute': dir(type)
        }
        self.dirname = os.path.abspath(os.path.dirname(__file__))
        self.path_to_file = self.find_path()
#find and return path of given filename in the posts directory
    def find_path(self):
        path_to_file = os.path.join(os.path.join(self.dirname, 'posts'), self.filename)
        return path_to_file

    @staticmethod
    def wrap(line, word, id):
        return line.replace(word, "<span id=\"{0}\">{1}</span>".format(id, word))

    def parse_file(self):
        new_file = os.path.join(os.path.join(self.dirname, 'templates'), 'parsed_' + self.filename)
        with open(self.path_to_file, 'r') as file, open(new_file, 'w') as new_file:
            parsed = []
            for line in file.readlines():
                chars = list(line)
                chars.remove('\n')
                line = ''.join(chars).lstrip()
                for word in line.split():
                    if check_int(word):
                        line = Parser.wrap(line, word, 'int')
                    if word == 'tab':
                        line = line.replace(word, '&nbsp;' * 5)
                    elif word in self.variables['keyword']:
                        parsed.append((word, 'keyword'))
                        line = Parser.wrap(line, word, 'keyword')
                    elif word in self.variables['special attribute']:
                        parsed.append((word, 'special attribute'))
                        line = Parser.wrap(line, word, 'special')
                    else:
                        for f in self.variables['built in function']:
                            if f in word:
                                parsed.append((f, 'built in function'))
                                line = Parser.wrap(line, f, 'built_in_function')
                new_file.write(line + '\n')
        return parsed
