import random
import unittest
from linear_search import linear_search
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort

class TestSorts(unittest.TestCase):
    sorts = [
            insertion_sort,
            selection_sort,
            merge_sort,
            ]

    def test_sorts(self):
        #test_arrays = generate_test_arrays()
        for i in range(random.randint(50,100)):
            #TODO: better randomization
            a = list(range(20))
            random.shuffle(a)
            for sort in self.sorts:
                #for a in test_arrays:
                a_sorted = a.copy()
                a_sorted.sort()
                a_test_sort = sort(a)
                self.assertEqual(a_sorted, a_test_sort)


if __name__ == '__main__':
    unittest.main()

