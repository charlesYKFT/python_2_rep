# I decided to write a code that generates data filtering object from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


# I decided to leave out your wrong choices because I want you to clearly see the difference."

# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
positive_even = Filter(
    [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
# positive_even.apply(range(100)) should return only even numbers from 0 to 99
positive_even.apply(range(100))


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    # keywards = ['name':'polly', 'type':'bird']
    for key, value in keywords.items():
        def keyword_filter_func(item):
            return item[key] == value
        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list
make_filter(name='polly', type='bird').apply(sample_data)

# There are multiple bugs in this code. Find them all and write tests for faulty cases.

"""A list of bugs I found here:
1. A syntax error in line 19. Instead of 'lamba a' you should write 'lambda a'.
2. A syntax error in line 19, extra right parenthesis at the end.
3. An error in writing isinstance function in line 19. This function should be written in this format: isinstance(object, classinfo). To fix this, we change 'isinstance(int, a)' to isinstance(a, int)
4. One syntax in 19 line. All lambda functions must be in list, because class Filter takes only one argument functions.
5. A Wrong argument in keyword_filter_func (32 lines) - var 'value' must have another name, for example a name 'item'.
"""
