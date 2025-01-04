#Write your function here
def odd_indices(my_list):
  my_lst = []
  for i in range(len(my_list)):
    if i % 2 != 0 :
      my_lst.append(my_list[i])
  return my_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
