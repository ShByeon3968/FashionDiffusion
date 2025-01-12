import operation as op
from base import Variable
import numpy as np
import unittest

class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = op.square(x)
        expected = np.array(4.0)
        self.assertEqual(y.data, expected)