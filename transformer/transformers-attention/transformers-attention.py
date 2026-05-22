import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    raw_att = torch.matmul(Q, K.transpose(-2,-1)) #transpose last 2 dim of k
    k_dim = K.shape[-1]
    score = raw_att / math.sqrt(k_dim)
    soft = F.softmax(score, dim=-1)
    return torch.matmul(soft, V)
    pass