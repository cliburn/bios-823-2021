import torch

def train_test_split(x, y, test_frac=0.2):
    n = x.shape[0]
    k = int(test_frac*n)
    
    idx = torch.randperm(n)
    train_idx = idx[k:]
    val_idx = idx[:k]
    
    return x[train_idx], y[train_idx], x[val_idx], y[val_idx]
