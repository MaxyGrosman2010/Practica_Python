###Sixth Class###

#Regex
import re
my_string = "This is the sixth class: Regex"
other_string = "This isn't the fifth class: File handler"
#Looks matches from the beginning of the string
print(re.match('This is the sixth', my_string))
print(re.match('This is the sixth', other_string))
print(re.match('Regex', my_string))

match = re.match('This is the sixth', my_string)
print(match)
print(match.span())
start, end = match.span()
print(my_string[start:end])
#How to handle the expression
match = re.match('This is the sixth', other_string)
if  match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])
else: print("It wasn't a match")
#Search
search = re.search('class', my_string)
print(search)
start, end = search.span()
print(my_string[start:end])

#Findall
my_string = "This is the sixth class: Regex"
findall = re.findall('class', my_string)
print(findall)
my_string = "This is the sixth class: Regex Class"
findall = re.findall('class', my_string)
print(findall)
my_string = "This is the sixth class: Regex class"
findall = re.findall('class', my_string)
print(findall)
my_string = "This is the sixth class: Regex Class"
findall = re.findall('class', my_string, re.I)#Re.i ignores the differences
print(findall)
my_string = "This is the sixth class: Regex"

#Split
split = re.split(":", my_string)
print(split)

#Sub
print(re.sub('Regex', 'regex', my_string))
print(re.sub('class', 'CLASS', my_string, re.I))
my_string = "This is the sixth class: Regex Class"
print(re.sub('class|Class', 'CLASS', my_string))
print(re.sub('[c|C]lass', 'CLASS', my_string))

#Patterns
patterns = r"[c|C]lass"
print(re.findall(patterns, my_string))
patterns = r"[c|C]lass|Regex"
print(re.findall(patterns, my_string))
patterns = r"[0-9]"
print(re.findall(patterns, my_string))
patterns = r"[0-5]"
print(re.findall(patterns, my_string))
patterns = r"[a-z]"
print(re.findall(patterns, my_string))