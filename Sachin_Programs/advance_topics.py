# create an iterator object from that iterable
my_list = [4, 7, 0, 3]
iter_obj = iter(my_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        print(element)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break