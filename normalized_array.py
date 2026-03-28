import numpy as np

def normalize_array(data):
    min_val = np.min(data)
    max_val = np.max(data)
    
    diff = max_val - min_val
    
    if diff == 0:
        return np.zeros_like(data, dtype=float)
    
    return (data - min_val) / diff
