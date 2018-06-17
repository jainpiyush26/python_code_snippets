from collections import OrderedDict
from collections import ChainMap
from functools import wraps
from types import MappingProxyType

dict_object = {"name": "test",
               "full_name": "datatype_sample_test",
               "use": "Explain the datatypes"}


def function_name(func_name):
    @wraps(func_name)
    def wrapper(*args):
        print("Calling {0}".format(func_name.__name__))
        func_name(*args)
        return
    return wrapper


@function_name
def order_dict_test():
    # Important note: Use the OrderDict to preserve
    # the order of the keys inserted!
    # this should help with keeping the logic sane!
    order_dict_1 = OrderedDict(one=1, two=2, three=3)
    print(order_dict_1.keys())
    order_dict_1["four"] = 4
    order_dict_1["five"] = 5

    print(order_dict_1.keys())


@function_name
def chainmap_test():
    dict_1 = {'first': 'first_element',
              'second': 'second_element'}
    dict_2 = {'third': 'third_element',
              'fourth': 'fourth_element',
              'fifth': 'fifth_element'}
    chain_map_obj = ChainMap(dict_1, dict_2)

    print(chain_map_obj['fifth'])


@function_name
def immutable_proxy_dicts():
    dict_1 = {x: x for x in range(10)}
    dict_2 = MappingProxyType(dict_1)

    print(dict_1)
    print(dict_2)

    try:
        dict_2[9] = 90
    except TypeError:
        raise TypeError

# order_dict_test()
# chainmap_test()
immutable_proxy_dicts()