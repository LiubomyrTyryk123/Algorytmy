import numpy as np

tab = np.array([[5, 1, 3], [1, 0, 2], [4, 6, 7]])
min_values = np.min(tab, axis=1)
min_indices = np.argmin(tab, axis=1)

i = 0
while i < len(tab):
    tab[i, 0],tab[i, min_indices[i]] = tab[i, min_indices[i]],tab[i, 0]
    i += 1
print(tab)