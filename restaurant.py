resto_query = {'start': False, 'amount_people': None,'kashrut':None,'style':None}

restaurant = [{'name': 'Aroma', 'people': 30, 'kosher': True, 'lemehadrin': False, 'style': 'salad', 'sindex': 'A'},
              {'name': 'Entrecote', 'people': 10, 'kosher': True, 'lemehadrin': True, 'style': 'bistro', 'sindex': 'B'},
              {'name': 'Yellow', 'people': 30, 'kosher': True, 'lemehadrin': False, 'style': 'fast-food', 'sindex': 'C'},
              {'name': 'Salateam', 'people': 10, 'kosher': True, 'lemehadrin': False, 'style': 'Salad', 'sindex': 'A'},
              {'name': 'Brasserie', 'people': 20, 'kosher': False, 'lemehadrin': False, 'style': 'Bistro', 'sindex': 'B'},
              {'name': 'Giraffe', 'people': 20, 'kosher': False, 'lemehadrin': False, 'style': 'fast-food', 'sindex': 'C'}]

def is_match(single_data, criteria):
    for attr, value in criteria.items():
        if isinstance(value, (int, float)):
            if single_data[attr] < value:
                return False
        elif isinstance(value, str):
            if single_data[attr] != value:
                return False
    return True

def getRestaurant(criteria):
    answer = []
    for data_dict in restaurant:
        if is_match(data_dict, criteria):
            answer.append(data_dict)
    return answer
    def filter_data(restaurant, criteria):
        answer = []
        for data_dict in restaurant:
            if is_match(data_dict, criteria):
                answer.append(data_dict)
        return answer
    results = filter_data(restaurant, criteria)
    if len(results) == 0:
        return("There are no matching restaurants")
    else:
        return('These are your dining options:', *[d.get('name') for d in results])



# def crit():
#     try:
#         crit.amount_people = int(input('How many people will you be dining with?'))
#     except ValueError:
#         print('This is not a whole number.')
#         exit()
#     crit.kashrut = input(str('do you keep kosher? y / n'))
#     if crit.kashrut.lower() == 'y':
#         crit.kashrut = True
#         crit.lamehadrin = input(str('Should it be Kosher lamehadrin y / n'))
#         if crit.lamehadrin.lower() == 'y':
#             crit.lamehadrin = True
#         elif crit.lamehadrin.lower() == 'n':
#             crit.lamehadrin = False
#         else:
#             print('please enter either y or n')
#             exit()
#     elif crit.kashrut.lower() == 'n':
#         crit.kashrut = False
#         crit.lamehadrin = False
#     else:
#         print('please enter either y or n')
#         exit()
#     print('what style of food do you like?')
#     print('A - salad')
#     print('B - Bistro')
#     print('C - fast-food')

#     crit.rstyle = input(str('enter your choice from A to C'))
#     crit.rstyle = crit.rstyle.upper()
#     if crit.rstyle == 'A':
#         print('You chose salad')
#     elif crit.rstyle == 'B':
#         print('You chose Bistro')
#     elif crit.rstyle == 'C':
#         print('You chose fast-food')
#     else:
#         print('you did not make a valid choice')
#         exit()
#     return crit.kashrut
#     return crit.amount_people
#     return crit.lamehadrin
#     return crit.rstyle

# criteria = {'people': crit.amount_people, 'kosher': crit.kashrut, 'lemehadrin': crit.lamehadrin, 'sindex': crit.rstyle}

# print('These are your search criteria:', criteria)
# def is_match(single_data, criteria):
#     for attr, value in criteria.items():
#         if isinstance(value, (int, float)):
#             if single_data[attr] < value:
#                 return False
#         elif isinstance(value, str):
#             if single_data[attr] != value:
#                 return False
#     return True

# def filter_data(restaurant, criteria):
#     answer = []
#     for data_dict in restaurant:
#         if is_match(data_dict, criteria):
#             answer.append(data_dict)
#     return answer
# #print(filter_data(restaurant, criteria))
# results = filter_data(restaurant, criteria)
# #print(results[1])
# if len(results) == 0:
#     print("There are no matching restaurants")
#     exit()
# else:
#     print('These are your dining options:', *[d.get('name') for d in results], sep="\n")
#     exit()
