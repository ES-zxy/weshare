def binary_search(collection, key):
    """Pure implementation of the binary search algorithm in Python.
    :param collection: some mutable ordered collection with heterogeneous
    :param key: the search keyword
    :return: the replace address
    """
    def __binary_search__(collection, start, end, key):
        if start > end:
            return start
        mid = start + (end - start) / 2
        if collection[mid] > key:
            return __binary_search__(collection, start, mid-1, key)
        if collection[mid] < key:
            return __binary_search__(collection, mid+1, end, key)
        return mid+1
    return __binary_search__(collection, 0, len(collection)-1, key)

def binary_insertion_sort(collection):
    """Pure implementation of the binary insertion sort algorithm in Python.
    :param collection: some mutable ordered collection with heterogeneous
    :return: the same collection ordered by ascending

    Examples:
    >>> binary_insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> binary_insertion_sort([])
    []
    >>> binary_insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    for loop_index in range(1, len(collection)):
        insert_point = binary_search(collection[0:loop_index], collection[loop_index])
        if insert_point == loop_index:
            continue
        collection = (collection[0:insert_point]
               + [collection[loop_index]]
               + collection[insert_point:loop_index]
               + collection[loop_index+1:])
    return collection


if __name__ == "__main__":
    print(binary_insertion_sort([0, 5, 3, 2, 2]))
    print(binary_insertion_sort([-2, -5, -45]))
    print(binary_insertion_sort([1,3,2,-1,100,-99,20,9,3,4,7,2]))
