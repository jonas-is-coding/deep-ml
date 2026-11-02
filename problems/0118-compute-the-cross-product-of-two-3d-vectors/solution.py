import numpy as np

def cross_product(a, b):
    # Your code here
    res = []

    for i in range(3):
        j = (i + 1) % 3
        k = (i + 2) % 3

        res.append(a[j] * b[k] - a[k] * b[j])

    return res