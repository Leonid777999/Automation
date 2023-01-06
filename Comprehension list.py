#COMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSION

# 1.
numbers_list = [1, -2.0, 3, -4.34, 5]
negative_list = [int(x) for x in numbers_list if x<0]

print(negative_list)

# 2.
string_list = ["string", "mediumstring", 'longstring', "hugestring"]
lenght_list = [x for x in string_list if len(x) == 10]

print(lenght_list)

# 3.
thirteen_list = [3, 26, 34, 39, 56]
divisible_list = [x for x in thirteen_list if x % 13 == 0]

print(divisible_list)

# 4.
name_list = ["Jack", "john", "Paul", "sean"]
upper_list = [x for x in name_list if x.islower()==False]
print(upper_list)

# 5.
divnumbers_list = [11, 23, 44, 68, 224, 666, 663, 5555]
division_list = [x for x in divnumbers]                   ###?????????????
print(division_list)







