import random

def get_numbers_ticket(min, max, quantity): 
    if min>0 and max <= 1000 and quantity <= max-min:
        number_list = random.sample(range(min, max), quantity)
        number_list.sort()
        return number_list
    else:
        return []
       