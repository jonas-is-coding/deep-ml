import numpy as np

def cross_product(a, b):
    # Your code here
    res = []
    for i in range(3):
        j = i + 1
        if j > 2:
            j = 0
        k = j + 1
        if k > 2:
            k = 0
        
        res.append(a[j] * b[k] - a[k] * b[j])

    return res