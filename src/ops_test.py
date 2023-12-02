import unittest
from . import ops


class OpsTest(unittest.TestCase):
    """
    Test case for the ops module.
    """

    def test_sum(self):
        self.assertEqual(ops.sum(1, 2), 7)
