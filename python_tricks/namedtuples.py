from collections import namedtuple

"""
syntax is to pass the object name and then the key names as a list of space
separated string,
I would prefer passing them explicitly as a list!
They are still tuples but can be used to store initial value of an object or
something like that
"""
test_obj = namedtuple('test_obj', ['obj_name', 'obj_fullname', 'obj_uid'])

test_obj_1 = test_obj('first', 'first_object', 1)
test_obj_2 = test_obj('second', 'second_object', 23)

print(test_obj_1)

print(test_obj_2)

print(test_obj._fields)
named_tuple_ordered_dict = test_obj_1._asdict()
for key, values in named_tuple_ordered_dict.items():
    print(key, values)
