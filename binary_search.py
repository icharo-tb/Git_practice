url = 'https://www.freecodecamp.org/news/binary-search-in-python-with-examples/'

# SEARCH ALGORITHM:
    # A search algorithm will help us retrieve data from any data structure
        # LINEAR SEARCH:
            # Simplest one
            # Operates in sequence
            # Searchs one element after another until it finds the correct key and value
        # DIJKSTRA SEARCH:
            # Used for advanced searches
            # It maps the shortest distance between 2 nodes (Often, this nodes are route networks)
            # EX: Useful when searching routes in maps, finding the shortest path possible
        # BINARY SEARCH:
            # Half interval search
            # They return the position of a value on a sorted list
            # Uses 'Divide and Conquer' technique to make an efficient work
            # Also a simple search algorithm
            # It doesn´t loop over the indexes to get a key and value
            # How it works:
                # Binary search splits the list into 2 parts in order to get the middle element (left, right and middle side)
                # Left side contains smaller values than the middle element and right side contains higher values
                # It uses sorted lists that have its elements in a particular order
                # Lists should be arranged correctly to make the algorithm work properly
                # On the contrary, the list will need to be sorted first by another algorithm
        # SORTING ALGORITHMS
            # Accpets unsorted lists as an input
            # They will return a  sorted list arranged in a particular order (mostly ascending order)
            # Types: insertion sort, quick sort, bubble sort and merge sort

# BINARY SEARCH IN DEPTH:
    # The algorithm will split the list in 2: left and right separated by the middle element
    # It will create a variable to store the value of the item that is being searched
    # It will pick the middle element and comapres it with the item we are looking for
    # If the comparison is correct then the process ends
    # If not, the middle element is either greater or smalller than the item you are looking for
        # If item is greater: splits the list and searches on the left side 
        # If item is smaller: splits the list and searches on the right side
    # This process can either be implemented using recursion or iteration
    # Case of use:
        # Searching a word on a dictionary
        # Searching for a literature book on a literature section on a library
        # Searching for an element in a sorted list
        # Searching for students taller than 1,79m in a line of students arranged according to their heights

# LET´S GET INTO IT:

# sorted_list = [4, 12, 23, 27, 32, 36]
# We create a sorted list, otherwise we need to sort the list we have avaliable

# value_search = 23
# We create the variable that will store our search value

# Condition 1:
# if middle_element == value_search:
    # return position of middle_element
# Code-ends

# Condition 2:
    # middle_element = 23
    # value_search = 4
    # if 23 > 4
        # index(23) = 2
        # new_position = index(23) - 2 | 2 -1   = 1
        # Search will end at index 1

# BINARY SEARCH: ITERATION
def binary_iter_search(sorted_list, value_search):
    first_index = 0
    size = len(sorted_list)
    last_index = size -1
    mid_index = (first_index + last_index) // 2 # // = integer division
    # print(mid_index)
    mid_element = sorted_list[mid_index]
    # print(mid_element)

    is_found = True
    # We start our iterative loop here
    while is_found:
        if first_index == last_index:
            if mid_element != value_search:
                is_found = False
                return 'Does not appear in the list'
            # Condition 1:
            elif mid_element == value_search:
                return(f'{mid_element} is in position {mid_index}')
            # Condition 2_Case 1:
            elif mid_element > value_search:
                new_position = mid_index - 1
                last_index = new_position
                mid_index = (first_index + last_index) // 2
                mid_element = sorted_list[mid_index]
                if mid_element == value_search:
                    return f'{mid_element} is in postion {mid_index}'
            #Condition 2_Case 2:
            elif mid_element < value_search:
                new_position = mid_index + 1
                first_index = new_position
                last_index = size -1
                mid_index = (first_index + last_index) // 2
                mid_element = sorted_list[mid_index]
                if mid_element == value_search:
                    return f'{mid_element} is in postion {mid_index}'

# TRY THE CODE:
num_list_iter = [8, 9, 12, 16, 57, 65, 89, 90]

print(binary_iter_search(num_list_iter, 57))
print(binary_iter_search(num_list_iter, 10))

# =================================================================================================

# BINARY SEARCH: RECURSION
def binary_recur_search(sorted_list, first_index, last_index, value_search):
    if last_index >= first_index:
        mid_index = (first_index + last_index) // 2
        mid_element = sorted_list[mid_index]

        if mid_element == value_search:
            return f'{mid_element} is on position {mid_index}'
        elif mid_element > value_search:
            new_position = mid_index -1
            # new last_index is the new_position
            return binary_recur_search(sorted_list, first_index, new_position, value_search)
        elif mid_element < value_search:
            new_position = mid_index + 1
            # new first_index is the new_position
            return binary_recur_search(sorted_list, new_position, last_index, value_search)
        else:
            return 'Does not appear in the list'

# TRY THE CODE:
num_list_recur = [1, 3, 10, 15, 34, 42, 76, 90]
search = 15
first = 0
last = len(num_list_recur) - 1

print(binary_recur_search(num_list_recur, first, last, search))

# IMPORTANT!!
# Binary search is a method that can take quite a long time even if recursion might be a bit faster than iteration
# It should work just fine on long lists, while in short ones it will surely works slower than expected

#---------------------------------------------------EXTRA----------------------------------------------------------

# LINEAR SEARCH:
    # Simplest one
    # Operates in sequence
    # Searchs one element after another until it finds the correct key and value

# LINEAR SEARCH: ITERATION
def linear_search_iter(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return f'The value {x} is in index postion {i}'
    return 'Not found in the array'

# TRY THE CODE:
list_iter = ['A','B','C','D','E','F','G','H','I','J','K']
x = 'D'

print(linear_search_iter(list_iter, x))

# LINEAR SEARCH: RECURSION
def linear_search_recur(arr, curr_index, key):
    if curr_index == -1:
        return 'Not found in the array'
    elif arr[curr_index] == key:
        return f'The value {key} is in position {curr_index}'
    return linear_search_recur(arr, curr_index -1, key)

# TRY THE CODE:
list_recur = ['A','B','C','D','E','F','G','H','I','J','K']
curr_index = len(list_recur) -1
key = 'H'

print(linear_search_recur(list_recur, curr_index, key))

# Extra: Binary Search

def binary_search(arr:list,low,high,value:int,time=0):

    mid = (low+high)//2
    time += 1

    if high >= low:
        if arr[mid] == value:
            return f"Value is at index {mid} and needed {time} rounds"
        elif value < arr[mid]:
            return binary_search(arr,low,mid-1,value)
        else:
            return binary_search(arr,mid+1,high,value)
    else:
        return False

lst = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(lst,0,len(lst)-1,9))