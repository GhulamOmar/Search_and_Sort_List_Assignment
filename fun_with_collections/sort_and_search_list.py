"""
Program: sort_and_search_list.py
Author: Ghulam Omar
Last date modified: 10/07/2019
This program is an example of search and sort a list.
"""

list = [9, 7, 6, 3, 8, 9, 2, 3]


def sort_list(list):
    """ Sorting the list"""

    list.sort()
    print("Sorted list", list)
    return [list]


def search_list(index):
    """Searching and  return the index of the object in the list"""

    print("The index is", list[5])
    index = list.index(6)
    return index


if __name__ == '__main__':
    sort_list(list)
    search_list(list)
