my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是{value},取下标元素为-16的元素，值是{value2}")

value = my_str.index("and")
print (f"从字符串{my_str}中查找子字符串\"and\"，首次出现的下标是{value}")

new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}中的子字符串\"it\"替换为\"程序\"，得到新字符串{new_my_str}")

my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}按空格分隔，得到列表{my_str_list}，列表长度是{len(my_str_list)}，类型是{type(my_str_list)}")

my_str = "  itheima and itcast  "
new_my_str = my_str.strip()
print(f"将字符串{my_str}首尾空格去掉，得到新字符串{new_my_str}")

my_str = "12itheima itcast21"
new_my_str = my_str.strip("12")
print(f"将字符串{my_str}首尾的\"12\"去掉，得到新字符串{new_my_str}")

my_str = "itheima and itcast"
count = my_str.count("it")
print(f"在字符串{my_str}中，子字符串\"it\"出现的次数是{count}")

num = len(my_str)
print(f"字符串{my_str}的长度是{num}")

# while循环遍历字符串
my_str = "黑马程序员"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

# for循环遍历字符串
for char in my_str:
    print(char)

for i in my_str:
    print(i)
    