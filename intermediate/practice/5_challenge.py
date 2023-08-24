### Fifth Challenge ###

"""
Invert String
Invert a string without using functions of the programming language you are using
"""

def invert_str(string):
    result = ""
    for i in range(0, len(string)):
        result += string[len(string) - 1 - i]
    return result
print(invert_str("Hello World"))