#7.9

tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
print('주어진 튜플:', tup)
같은_tup = tuple(set(tup))
print('중복 제거 튜플:', 같은_tup)
