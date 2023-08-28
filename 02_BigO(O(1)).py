"""Big O(1) also know as constant time. This means that no matter the number of inputs, the number of 
operationsis still constant."""
import numpy as np
box = np.arange(50)
print(box)

def compressFirstBox(boxes):
    print("Compressing first box...",boxes[0]) # this has a big O notation of O(1). because only one task is performed
    print("Compressing second box...",boxes[1])# this has a big O notation of O(1). because only one task is performed
    """So overall, the Big O notation will be O(2)"""

compressFirstBox(box)