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

# binary search without using loops
def binary_search_no_loop(target, items):
    
    max = len(items) - 1
    min = 0
    mid =(max - min) / 2
    mid_item = items[mid]
    print items
    print target, mid_item, items[min], items[max]
    
    if target == mid_item:
        print -1
        print target, mid_item
        return mid_item
    else:
        if target > mid_item:
            min = mid_item
            new_list = items[mid:]
            print 0
            return binary_search_no_loop(target, new_list)
        elif target < mid_item:
            max = mid_item
            new_list = items[:-mid]
            print 1
            return binary_search_no_loop(target, new_list)

print binary_search_no_loop(4, test_a)