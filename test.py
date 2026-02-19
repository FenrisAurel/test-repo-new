my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是{value},取下标元素为-16的元素，值是{value2}")

value = my_str.index("and")
print (f"从字符串{my_str}中查找子字符串\"and\"，首次出现的下标是{value}")
