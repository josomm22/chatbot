resto_query = {'start': False, 'amount_people': None,'kashrut':None,'style':None}

restaurant = [{'name': 'Aroma', 'amount_people': 5, 'kashrut': True,  'style': 'salad'},
              {'name': 'Entrecote', 'amount_people': 6, 'kashrut': True, 'style': 'bistro'},
              {'name': 'Yellow', 'amount_people': 8, 'kashrut': True,  'style': 'fast-food'},
              {'name': 'Salateam', 'amount_people': 2, 'kashrut': True,  'style': 'Salad'},
              {'name': 'Brasserie', 'amount_people': 5, 'kashrut': False,  'style': 'Bistro'},
              {'name': 'Giraffe', 'amount_people': 5, 'kashrut': False,  'style': 'fast-food'}]

def is_match(single_data, criteria):
    for attr, value in criteria.items():
        if isinstance(value, (int, float)):
            if single_data[attr] < value:
                return False
        elif isinstance(value, str):
            if single_data[attr] != value:
                return False
    return True
def filter_data(restaurant, criteria):
        answer = []
        for data_dict in restaurant:
            if is_match(data_dict, criteria):
                answer.append(data_dict)
        return answer

def getRestaurant(criteria):
    del criteria['start']
    results = filter_data(restaurant, criteria)
    if len(results) == 0:
        return("There are no matching restaurants")
    else:
        outro = ' Would you like to get news, the weather or do something else now?'
        return('According to your choices ' , *[d.get('name') for d in results] , 'would be a good choice', outro)
