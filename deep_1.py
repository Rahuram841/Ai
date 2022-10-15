import numpy as np
import typing
from typing import Callable
from typing import List
import matplotlib.pyplot as plt
class Exp:
    def __call__(self,X):
        return np.power(X,2)

print("Python list operations")
a=[1,2,3]
b=[4,5,6]
print("a+b:",a+b)
try:
    print(a*b)
except TypeError:
    print("a*b has no meaning for Python")
print()
print("Numpy array operations:")
C=np.array([[1,2,3],[2,5,6]])
D=np.array([[2,3,4],[7,9,3],[3,5,4]])
B=np.array([4,5,6])
A=np.array([1,2,3])
print("a+b:",A+B)
print("a*b",A*B)
Array_function=Callable[[np.ndarray],np.ndarray]
Chain=List[Array_function]
def square(x):
    return np.power(x,2)
def matmul_forward(X,W):
    
    #assert X.shape[1]== W.shape[0]
    N=np.dot(X,W)
    return N


def sigmoid(x):
    return 1/(1+np.exp(-x))
def leaky_relu(x):
    return np.maximum(0.2*x,x)
def deriv(func:Callable[[np.ndarray],np.ndarray],X:np.ndarray,delta:float=0.001)->np.ndarray:
    return (func(X+delta)-func(X-delta))/(2*delta)
def fun(bar:Callable[[int],int],a:int):
    return bar(a)
def chain_length_2(chain:Chain,x:np.ndarray)->np.ndarray:
    assert len(chain)==2
    f1=chain[0]
    f2=chain[1]
    return f2(f1(x))
def chain_deriv_2(chain:Chain,input_range:np.ndarray)->np.ndarray:
    assert len(chain)==2
    assert input_range.ndim==1
    f1=chain[0]
    f2=chain[1]
    f1_of_x=f1(input_range)
    df1dx =deriv(f1,input_range)
    df2du= deriv(f2,f1(input_range))
    return df1dx*df2du
def chain_deriv_3(chain:Chain,input_range:np.ndarray)->np.ndarray:
    assert len(chain)==3
    f1 = chain[0]
    f2 = chain[1]
    f3 = chain[2]
    f1_of_x = f1(input_range)
    f2_of_x = f2(f1_of_x)
    df3du = deriv(f3,f2_of_x)
    df2du = deriv(f2,f1_of_x)
    df1dx = deriv(f1,input_range)
    return df1dx*df2du*df3du
def multiple_inputs_add(x:np.ndarray,y:np.ndarray,sigma:Array_function):
    assert x.shape == y.shape
    a= x+y
    return sigma(a)
def multiple_inputs_add_backward(x:np.ndarray,y:np.ndarray,sigma:Array_function)->float:
    a=x+y
    dsda=deriv(sigma,a)
    dadx,dady=1,1
    return dsda*dadx,dsda*dady
    
def matmul_backward_first(X:np.ndarray,W:np.ndarray)->np.ndarray:
    dNdX = np.transpose(W,(1,0))
    return dNdX
def matrix_forward_extra(X:np.ndarray,W:np.ndarray,sigma:Array_function)->np.ndarray:
    assert X.shape[1]==W.shape[0]
    N = np.dot(X,W)
    S = sigma(N)
    return S
def matrix_function_backward_1(X:np.ndarray,W:np.ndarray,sigma:Array_function)->np.ndarray:
    assert X.shape[1]== W.shape[0]
    N = np.dot(X,W)
    S = sigma(N)
    dSdN = deriv(sigma,N)
    dNdX=np.transpose(W,(1,0))
    return np.dot(dSdN,dNdX)
def matrix_function_forward_sum(X:np.ndarray,W:np.ndarray,sigma:Array_function)->float:
    assert X.shape[1]==W.shape[0]
    N=np.dot(X,W)
    S =sigma(N)
    L=np.sum(S)
    return L
def matrix_function_backward_sum_1(X:np.ndarray,W:np.ndarray,sigma:Array_function)->np.ndarray:
    assert X.shape[1] == W.shape[0]
    N = np.dot(X,W)
    S = sigma(N)
    L= np.sum(S)
    dLdS = np.ones_like(S)
    dSdN= deriv(sigma,N)
    dLdN = dLdS*dSdN
    dNdX = np.transpose(W,(1,0))
    dLdX = np.dot(dSdN,dNdX)
    return dLdX

print(sigmoid(C))
print(matmul_forward(C,D))
print(square(B))
print("First derivative:",deriv(sigmoid,A))
chain_1 = [square, sigmoid]
print(chain_length_2(chain_1,A))
np.random.seed(190204)
X = np.random.randn(3, 3)
W = np.random.randn(3, 2)
print("X:")
print(X)
print("L:")
print(round(matrix_function_forward_sum(X, W, sigmoid), 4))
print()
print("dLdX:")
print(matrix_function_backward_sum_1(X, W , sigmoid))

