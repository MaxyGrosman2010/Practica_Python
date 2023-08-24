### Fifth Challenge ###

"""
Invert String
Invert a string without using functions of the programming language you are using
"""

def invert_str(string):
    str_as_list = list(string)
    result = []
    for i in reversed(str_as_list):
        result.append(i)
    return ''.join(result)
print(invert_str("Hello World"))