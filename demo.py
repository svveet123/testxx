'''
print("hello world") #字符串
print(2333)
print(2.3333)
print(True)  #布尔值
print(False)
print(())  #元组
print([])  #数组
print({})  #字典

print("哈哈哈",2333,2.33333)
print("还好"+"喜喜")
print("喜喜"*100)

print(1+2)
print(((1+2)*100-99)/2)
print(2<3)
a = "张三"  #把张三这个值赋值给 变量a
print(a)
'''

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容:",a+b)

# print(type("哈哈"))
# print(type(2333))
# print(type(2.3333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))


# a = str(2333)
# print(type(a))

# a = input("努古you are:")
# b = input("金泰亨:")
# print("字数和",len(a)+len(b))

#元组  下标，从0开始
#a = ()  # 空的元组
# a = ("JIN","SUGA","V","V","V","V","V","J-HOPE","V","V","RM","JIMIN","V","JOOKONK")

#a.index print(a.index("V")) 查找某个值的下标
#a.count print(a.count("V")) 统计某个值的数量

# # b = (a,"V","RM")
# # print(b[0][7])

# # print(a[-1])  #倒着数

#元组一定写好后不能修改，而数组可以修改
# # 切片

# # print(a[0:4])
# # print(a[4:9])
# # print(a[9:])
# print(a)
'''
a = [1,2,3,4,"v","jimin","jk","v","rm","v","jhope","true","false"]
a.append('追加的一个')  #通过append往尾部追加值,添加一个数据
a.append('追加一个1.0')
print(a)
a.insert(4,"insert")  #insert 往数组中指定的位置插入数据，插入在下标为4的数据前面，不能超过原有的下标
print(a)
b = a.pop(0)  #剪切数据
c = a.pop(0)   #第一个取出来的下标0的值是1，第二个取出来的下标0的值是2
print(b+c)
print(a)
print(b)
xx = ["你好","不好"]  
#a.extend(xx) #extend 可以添加数组
print(a+xx)

print(a)
a.remove(4)  #直接删除某个值，数字不代表下标
a.remove("追加的一个")
print(a)


True = 1
False = 0

#下标不要超出范围 = 越界

'''

'''字典的特点
1.字典中的值没有顺序
2.字典的接口必须是 键值对的 结构。key：value
3.字典的取值是靠key来取value值。


a = {"name":"张三",0:"哈哈","age":25}
# 取值,把value值取出来，用key值定位
print(a["name"])
# 新增
a["high"] = "183cm"
print(a)
# 修改
a["name"] = "李四"
print(a)

b = a.get("name")  #取值
print(b)
b = a.pop("name")   #剪切
print(a)
print(b)
a.update(name=1111)   #增加/修改
print(a)
print("------------------")


print(a.get("name"))
#get 如果是不存在的数据，会返回“none”
print(a["name"])
#如果不存在，会报错


#数组和字典的删除
del a["name"]
print(a)

'''

a = input("name:")
b = input("age:")
c = input("sex:")
d = print("个人信息:",a+b+c)
e = {"个人信息":d}
print(e)

