test_list = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)] 
print("The original list is : " + str(test_list)) 
N =1
test_list.sort(key = lambda x: x[N]) 
print("List after sorting tuple by Nth index sort : " + str(test_list))
