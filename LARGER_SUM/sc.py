def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst2) > sum(lst1):
    return lst2
  else:
    return lst1

# Test your code
print(larger_sum([1, 9, 5], [2, 3, 7]))
