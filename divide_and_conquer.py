#################################################################
# DIVIDE AND CONQUER
#################################################################
# a series of algorithms that use the divide and conquer approach

test_a = [4, 5, 10, 12, 8, 3, 24]


# sum all values of a list without using a loop
def no_loop_sum(items):

    if len(items) == 1:
        return items[0]
    else:
        return items[-1] + no_loop_sum(items[:-1])


print no_loop_sum(test_a)


# count the number of items in a list without using a loop
def count_no_loop(items):

    if len(items) == 1:
        return 1
    else:
        return 1 + count_no_loop(items[:-1])


print count_no_loop(test_a)


# find the greatest number in a list without using a loop
def find_max_no_loop(items):

    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        if items[0] > items[1]:
            return items[0]
        else:
            return items[1]
    else:
        new_list = []
        if items[0] > items[1]:
            new_list.append(items[0])
        else:
            new_list.append(items[1])
        new_list.extend(items[2:])
        #print new_list
        return find_max_no_loop(new_list)


print find_max_no_loop(test_a)


def binary_search(target, items, currentiter=0):
    """Binary search implementation to look for a target item
    inside a list. The list must be sortable.
    The element must implement the <, == and > operators
    in order for the search to work properly.

    Args:
        target (obj): The target element to search.
        items (list): Containing all of the elements. Each element must be of the same type as the supplied target.
        currentiter (int, optional): Represents the current iteration

    Returns:
        (obj): The found item, otherwise None if the item is not present in the list
    """

    # Remove duplicates and sort the list
    current_list = sorted(set(items))
    print current_list

    # Split the list in 2, and check if the target is lesser o greater than then the center of the list
    mid_index = len(current_list) // 2

    first_item = current_list[0]
    mid_item = current_list[mid_index]
    last_item = current_list[-1]

    print 'first: {}, mid: {}, last: {}'.format(first_item, mid_item, last_item)

    if currentiter == 0:

        # Exit condition 1.a, the first matches the target
        if current_list[0] == target:
            print 'item found in {} iterations --> {}'.format(
                currentiter, current_list[0])
            return current_list[0]

        # Exit condition 1.b, the last matches the target
        elif current_list[-1] == target:
            print 'item found in {} iterations --> {}'.format(
                currentiter, current_list[-1])
            return current_list[-1]

    # Exit condition 2, mid matches the target
    if mid_item == target:
        print 'item found in {} iterations --> {}'.format(currentiter, mid_item)
        return mid_item

    # Exit condition 3, there are two items in the list and none of them matches the target
    elif len(current_list) <= 2:
        print 'item {} is not present inside given list'.format(target)
        return

    else:
        current_iter = currentiter + 1

        if target > mid_item:
            new_list = current_list[mid_index:]
            binary_search(target, new_list, current_iter)

        elif target < mid_item:
            new_list = current_list[:mid_index]
            binary_search(target, new_list, current_iter)


print binary_search(4, test_a)