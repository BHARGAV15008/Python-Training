# # 1. Creating list using lambda function
# lstCreate = lambda x: [i for i in range(1, x)]

# cr_list  = lstCreate(11)
# print(cr_list)

# # 2. anagram program
# inp = input("Enter your String here : \n")
# inp1 = input("Enter your second String here: \n")

# sort_str = sorted(inp)
# sort_str1 = sorted(inp1)

# if sort_str == sort_str1:
# 	print("your strings is anagram...\n")
# else:
# 	print("sorry... its not anagram.\n")

# # 3. create numpy array using inbuilt function
# import numpy as np

# arr_num = np.arange(10)
# print(arr_num)

# 	np.random.shuffle(arr_num)
# print(arr_num)


# 4. Given a list of dictionaries,  write a function that will sort the list of dictionaries based on the value of one of the keys, and return only the values of another key for the dictionaries in the sorted list. 

# For example, given the following list of dictionaries: 

# [{'name': 'John', 'age': 30, 'score': 90},    {'name': 'Jane', 'age': 25, 'score': 95},    {'name': 'Jim', 'age': 35, 'score': 80}] 

# If we sort the list of dictionaries based on the 'age' key in ascending order, and return the values of the 'name' key for the dictionaries in the sorted list, the output should be: 

# ['Jane', 'John', 'Jim']

# lst_dict = [{'name': 'John', 'age': 30, 'score': 90}, {'name': 'Jane', 'age': 25, 'score': 95}, {'name': 'Jim', 'age': 35, 'score': 80}]

# sorted_list = sorted(lst_dict, key=lambda x: x['age'])


# print(sorted_list)


# # 5. python program to rolled dice 10 times and print in dictionary
# import numpy as np

# num_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# print(type(num_dict))
# # print(num_dict[1]+1)

# # lst = [1, 2, 3, 4, 5, 6]

# for i in range(10):
# 	num = np.random.randint(1,6)
# 	# print(num_dict[num] + 1)
# 	num_dict[num] = num_dict[num] + 1

# print(num_dict)


# # 6. write program to check string is palimdrone 
# str1 = input("Enter your string here: \n")
# print(str1)

# str2 = str1[::-1]
# print(str2)

# if str1 == str2:
# 	print("Your string is Palimdrone...\n")
# else:
# 	print("Your string is not Palimdrone...\n")


