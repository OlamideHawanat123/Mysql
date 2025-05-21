
import unittest
import QuickTask

class MyTestCase(unittest.TestCase):

    def test_that_stack_is_empty(self):
        self.assertEqual([4, 16, 64], QuickTask.filter_out([1, 2, 3, 4, 16, 64, 125], 4))


