'''
为了代码复用
# def 固定
# sum:方法名
# g,h 在调用方法时要传的数据
# return 返回值

def sum(g,h,i):
    he = g+h+i
    return he
a = 1 
b = 2
c = 3
s1 = sum(a,b,c)
s2 = sum(b,c,c)
print(s1)
print(s2)
'''

'''
def test1():
    print("用户")
    print(123)
    print(2.333)
    print([1,2,3])
    print((23,43,21))
test1()
'''

'''
参数的数据类型可以是任何形式的

def test2(l):
    print(l)
test2(1)
test2(2.333)
test2("姓名")
test2([1,2.3,4])
test2({"username":"hu","key":"value"})
'''
'''
def test3(l):
    return(l)

a = test3(1)
b = test3("用户")
c = test3([1,2.3,4,5])
d = test3({"用户":"金泰亨","age":"25"})
print(a)
print(b)
print(c)
print(d)
'''


#from dbtools import chaxun

# # 模拟管理员登录，输入账号和密码，查询输入的账号和密码，如果数据库中有该账号密码，则能查询到结果；
# # 如果账号密码不正确，则查询结果为空
# username = input("请输入账号：")
# password = input("请输入密码：")
# sql = 'select * from t_admin where username="{}" and password="{}"'.format(username,password)
# res = chaxun(sql)
# if len(res) != 0:
#     print("管理员登录成功")
# else:
#     print("管理员登录失败")

#---------------------------------注册-------------------------------------
from dbtools import commit
username = input("请输入账号：")
password = input("请输入密码：")
sql = 'INSERT into t_admin values(NULL, "{}", "{}", NULL, NULL, "管理员2", "好好学习啊", "headimg.jpg", NULL, "女", 0, NULL, NULL, NULL)'.format(username,password)
res = commit(sql)
if res ==True:
    print("账号注册成功")
else:
    print("账号注册失败")

