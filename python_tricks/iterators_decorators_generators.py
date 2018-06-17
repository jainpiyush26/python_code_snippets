from functools import wraps
import time
from uuid import uuid4
from error_handler import *


def functiondetails(function_name):
    '''
    Decorator
    '''
    @wraps(function_name)
    def wrapper(*args, **kwargs):
        print("Running the function '{0}'".format(function_name.__name__))
        start_time = time.time()
        function_name(*args, **kwargs)
        print("{0} function took {1} seconds".format(
            function_name.__name__, time.time()-start_time))
        return
    return wrapper


def setuuid(*expected_args):
    def decorator_function(function_name):
        @wraps(function_name)
        def wrapper(*args, **kwargs):
            print("uuid for the function is '{0}'".format(expected_args[0]))
            return function_name(*args, **kwargs)
        return wrapper
    return decorator_function


# Iterators
class custom_iterator:
    def __init__(self, key_list, value_list):
        self.key_list = key_list
        self.value_list = value_list
        self.key_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = (self.key_list[self.key_index],
                      self.value_list[self.key_index])
        except IndexError:
            raise StopIteration
        self.key_index += 1
        return result

    def next(self):
        return self.__next__()

    def prev(self):
        try:
            result = (self.key_list[self.key_index],
                      self.value_list[self.key_index])
        except IndexError:
            raise StopIteration
        self.key_index -= 1
        return result


def custom_generators(key_list, value_list):
    '''
    Generator
    '''
    key_index = 0
    while key_index < len(key_list):
        yield (key_list[key_index], value_list[key_index])
        key_index += 1


@functiondetails
@setuuid(uuid4())
def iterator_calling():
    data = custom_iterator(key_list=["first_name", "last_name"],
                           value_list=["Piyush", "Jain"])
    for items in data:
        print(items)


@functiondetails
@setuuid(uuid4())
def generator_calling():
    data = custom_generators(["first_name", "last_name", "method_name"],
                             ["Piyush", "Jain", "iterator calling"])
    while True:
        try:
            print(data.__next__())
        except StopIteration:
            break


@setuuid(uuid4)
class test_dunderfunction(object):
    def __init__(self, *args):
        self.argument_data = args

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__,
                                 ",".join(self.argument_data))


def check_error_functions(name_value=""):
    '''
    This is to play around with the custom error classes
    '''
    if isinstance(name_value, int):
        raise NotStrError(name_value)
    elif not name_value:
        raise UnknownError(name_value)
    elif len(name_value) > 8:
        raise StringTooLongError(name_value)
    else:
        print("BOOYEAH")


def main():
    # iterator_calling()
    # generator_calling()
    # class_obj = test_dunderfunction("name", "surname", "data")
    # print(class_obj)
    # check_error_functions(1)
    # check_error_functions()
    # check_error_functions("PiyushJain")
    # check_error_functions("piyush")


if __name__ == "__main__":
    main()
