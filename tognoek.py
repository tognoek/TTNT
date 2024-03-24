import numpy as np
a = np.array([[2, 3],
              [4, 1],
              [4, 3],
              [5, 7]])

print(np.mean(a, axis=0))
print(a[0, :])