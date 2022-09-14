from turtle import update


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# z[0].update({'x':15})
# # print(z[0])
# students[0].update({'last_name':'Bryant'})
# print(students[0])
# sports_directory['soccer'][0]='Andres'
# # print(sports_directory['soccer'][0])
# z[0].update({'y':30})
# print(z[0])


# def iterateDictionary(students) :
#     for x in students:
#         print('\n')
#         for i, j in x.items():
#             print(i,':',j,)

# iterateDictionary(students)


# def iterateDictionary2(key_name, some_list):
#     stringReturn = ''
#     for val in some_list:
#         stringReturn += f"{val[key_name]} \n"
#     return stringReturn
# print(iterateDictionary2('last_name',students))

# dojo = {
# 'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
# 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printDictonaryInfo(my_dictonary):
#     for key in my_dictonary:
#         print(f"{len(my_dictonary[key])} {key.upper()}")
#         for val in my_dictonary[key]:
#             print(val)
#         print("")
# printDictonaryInfo(dojo)