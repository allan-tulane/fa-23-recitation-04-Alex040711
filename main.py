import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    pivot = pivot_fn(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return qsort(less, pivot_fn) + equal + qsort(greater, pivot_fn)
    
def selection_sort(L):
    for i in range(len(L)):
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

def fixed_pivot(a):
    return a[0]

def random_pivot(a):
    return random.choice(a)
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda lst: qsort(lst, fixed_pivot)
    qsort_random_pivot = lambda lst: qsort(lst, random_pivot)
    python_sorted = lambda lst: sorted(lst)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_sort(selection_sort, mylist[:]),
            time_sort(python_sorted, mylist[:])
        ])
    return result
    ###

def compare_sort_random(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    qsort_fixed_pivot = lambda lst: qsort(lst, fixed_pivot)
    qsort_random_pivot = lambda lst: qsort(lst, random_pivot)
    result = []
    for size in sizes:
        mylist = list(range(size))
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist[:]),
            time_search(qsort_random_pivot, mylist[:]),
            time_search(selection_sort, mylist[:]),
            time_search(sorted, mylist[:])
        ])
    return result

def compare_sort_sorted(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    qsort_fixed_pivot = lambda lst: qsort(lst, fixed_pivot)
    qsort_random_pivot = lambda lst: qsort(lst, random_pivot)
    result = []
    for size in sizes:
        mylist = list(range(size))
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(selection_sort, mylist),
            time_search(sorted, mylist)
        ])
    return result

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())
    print_results(compare_sort_random())
    print_results(compare_sort_sorted())

random.seed()
test_print()
