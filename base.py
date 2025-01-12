import numpy as np
from util import as_array

class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError(f'{type(data)}는 지원하지 않습니다.')
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop() # 함수 가져오기
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)
            if x.creator is not None:
                funcs.append(x.creator)

class Function:
    def __call__(self, input: Variable):
        x = input.data
        y = self.forward(x)
        output = Variable(as_array(y)) # 변수가 ndarray가 되도록 
        output.set_creator(self) # 출력 변수에 창조자를 자기 자신으로 설정
        self.input = input
        self.output = output
        return output
    
    def forward(self,x):
        raise NotImplementedError()
    
    def backward(self,gy):
        raise NotImplementedError()

# 제곱 연산
class Square(Function):
    def forward(self,x):
        return x ** 2

    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx
    
# Napier's Constant
class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
