import numpy as np
from typing import Dict,Tuple
def forward_linear_regression(X_batch:np.ndarray,Y_batch:np.ndarray,weights:Dict[str,np.ndarray])->Tuple[float,Dict[str,np.ndarray]]:
    assert X_batch.shape[0]==Y_batch.shape[0]
    assert X_batch.shape[1]==weights['W'].shape[0]
    assert weights['B'].shape[0]==weights['B'].shape[1]==1

    N=np.dot(X_batch,weights['W'])
    P=N+weights['B']
    loss =np.mean(np.power(Y_batch-P,2))

    forward_info:Dict[str,np.ndarray]={}
    forward_info['X']=X_batch
    forward_info['N']=N
    forward_info['P']=P
    forward_info['Y']=Y_batch

    return loss,forward_info
def loss_gradients(forward_info:Dict[str,np.ndarray],weights:Dict[str,np.ndarray])->Dict[str,np.ndarray]:
    batch_size = forward_info['X'].shape[0]
    dLdP = -2*(forward_info['Y']-forward_info['P'])
    
