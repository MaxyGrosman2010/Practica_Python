#Material
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises 1
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies = it_companies.union({'Sony', 'Monolith Soft', 'Nintendo'})
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
it_companies.discard('Facebook')
print(it_companies)

#Exercises 2
a_b = A.union(B)
print(a_b)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A, B

#Exercises 3
age_set = set(age)
print(len(age))
print(len(age_set))
#String: A collection of chars with a max length of 255 which
#List: A collection of objects which can be modify, it can be organized
#Tuple: A collection of objects that can't be modify any way
#Set: A collection of objects which doesn't accept duplicates, you can't extract element from it
string = "I am a teacher and I love to inspire and teach people"
list = string.split(' ')
set = set(list)
print(set)