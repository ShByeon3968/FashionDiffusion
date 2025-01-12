import operation as op
from base import Variable
import numpy as np

x = Variable(np.array(0.5))
y = op.square(op.exp(op.square(x)))
y.backward()
print(x.grad)