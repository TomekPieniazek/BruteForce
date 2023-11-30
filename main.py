import itertools
def everyPossibility(combination, exchange_list):

    test = itertools.combinations_with_replacement(exchange_list, combination)
    return list(test)

print(everyPossibility(2, [1, 2, 5]))