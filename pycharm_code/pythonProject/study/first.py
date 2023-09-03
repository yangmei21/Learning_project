# print("nihao! i am ym")
# is a beautiful day

# a=10
# b=20
# print(a+b)

# s='akesi'
# print(s)
# print("hi")
#
# str='''nihao
# wish'''
#
# print(s+str)

# a=input("请输入第一个数字:")
# b=input("请输入第二个数字:")
# print(type(a))  #查看a的类型
# a=int(a)
# b=int(b)
# print(a+b)
#
# money=500
# if money>300:
#     print("你的钱很多!!!")

# money2=input("请输入你的钱：")
# money2=int(money2)
# if money2>200:
#     print("可以买皮肤")
# else :
#     print("不能买呀！")

# money3=input("请输入你的钱：")
# money3=int(money3)
# if money3>300:
#    if money3>500:
#        print("可以买多个荣耀典藏皮肤哦")
#    else :
#        print("买一个传说皮肤")
# else:
#     print("回去吧")

# money4=input("请输入你的钱：")
# money4=int(money4)
# if money4>188:
#     print("荣耀典藏皮肤买！！")
# elif money4>100:
#     print("传说皮肤买呀！！")
# elif money4>30:
#     print("史诗皮肤买！！")
# else:
#     print("六元？？白嫖吧你")

# i=1
# while i<=100:
#     print(i)
#     i=i+1

# 1+2+3+......+100
# sum=0
# i=1
# while i<=100:
#     sum=i+sum
#     i=i+1
# print(sum)


# 1-2+3-4+.......+99-100
# sum1=0
# flag=1
# i=1
# while i<=100:
#     sum1=i*flag+sum1
#     i=i+1
#     flag=flag*(-1)
# print(sum1)

# break
# while True:
#     str=input("录入你的数字吧")
#     if str=="0":
#         break
#     print(str)
#
# print("结束了")

# continue
# i=1
# while i<=10:
#     if i==4:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
#
# ste="amidjfjdjf"
# for s in ste:
#     print(s)
#
# for n in range(0,7,2):
#     print(n)

# name=input("请输入姓名--")
# age=int(input("请输入年龄--"))
# s1="姓名：%s" % (name)
# print(s1)
# s2="年龄：%d" % (age)
# s ="我的姓名为%s,年龄为%d" % (name, age)
# s2="我是{}，年龄是{}".format(name,age)

# s3=f"我是{name},今年{name}l"
# print(s3)

#定义首字母大写-----captialize
# s="wython"
# s1=s.capitalize()
# print(s1)

#定义每个单词首字母大写----title
# s="hello i am yangmei"
# s1=s.title()
# print(s1)

#定义每个字母小写----lower
# s="HELLO WORLD"
# s1=s.lower()
# print(s1)

#定义每个字符都大写----upper
# s="i am from china"
# s1=s.upper()
# print(s1)

# 忽略大小写进行判断--用upper转为大写判断
# verify_code="Aolo"
# user_input=input(f"请输入一下字符串:({verify_code})")
# if verify_code.upper()==user_input.upper():
#     print("pass")
# else:
#     print("fail")

#去掉字符串左右的空格（空格、\n、\t）-----strip
# name=input("登录账号:")
# password=input("密码：")
# if name.strip()=="admin":
#     if password.strip()=="123456":
#         print("登录成功！")
#     else:
#         print("密码错误失败")
# else:
#  print("账号错误失败")

# 替换----replace
# name="killo"
# name1=name.replace("llo","mil")
# print(f"原来的名字是({name}),现在的名字是({name1})")
#
#
# #切割----split
# s="python_java_c_c#"
# lst=s.split("_")
# print(lst)

# 查找与替换
# 查找------find(结果返回字段位置，-1则无该字符)/index（报错无该字符）
# name="王可爱的名字"
# ret=name.find("可爱")
# print(f"名字在{ret}位")
# ret2=name.index("名字")
# print(ret2)

# -----用in/not in 查看是否存在该字符串
# name="张小花"
# print("小花" in name)
# print("张" not in name)

#判断是否以什么开头/结尾----开头（startswith()  结尾(endswith())
# name=input("请输入您的姓：")
# if name.startswith("李"):
#     print("你是姓李的")
# else:
#     print("您不姓李")
#
# name1=input("请输入您的名")
# if name1.endswith("然："):
#     print("你的名字是符合要求的")
# else:
#     print("很遗憾 您不符合我们的要求")

# 字符长度---------------len
# name=input("请输入您的要求：")
# print("您的要求长度为",len(name))
#
#列表中字符连接----------join
# str1=['like','diu','anke']
# str2="".join(str1)
# print(str2)

# 读取文件的信息
# f=open("书单.txt",mode="r",encoding="UTF-8")
# content=f.read()
# print(content)

# 逐行读取
# line=f.readline().strip()
# print(line)
# line=f.readline().strip()
# print(line)

# 列表方式读取？？
# line=f.readlines()
# print(line)

# 循环读取文件
# for fi in f:
#     print(fi.strip())

# 文件中写入内容
# f=open("读书笔记.txt",mode="w",encoding="utf-8")
# f.write("dushubiji")
#
# # 文件中追加写入内容
# f1=open("书单.txt",mode="a",encoding="utf-8")
# f1.write("\nshuji3")
# # f1.close()
# import os
#文件修改---新加入一个文件，将要修改的源文件保存到新的文件中，后对其源文件进行删除，将修改的文件重命名为源文件代替源文件
# with open("书单.txt",mode="r",encoding="utf-8") as f1,\
#      open("书单2.txt",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         line=line.strip()
#         if line.startswith("猪"):
#             line=line.replace("猪","小")
#
#         f2.write(line)
#         f2.write("\n")
# os.remove("书单.txt")
# os.rename("书单2.txt","书单.txt")


# 函数
# def jisuan(a,opt,b):
#     if opt=="+":
#         print(a+b)
#     elif opt=="-":
#         print(a-b)
#     elif opt=="*":
#         print(a*b)
#     elif opt=="/":
#         print(a/b)
#     else:
#         print("无法计算!!!!")
#
# num1=input("请输入第一个数字：")
# num2=input("请输入第二个数字：")
# num1=int(num1)
# num2=int(num2)
# jisuan(num1,"-",num2)

def eat(*food):
    print(food)
eat("meat","vagetable")

def eat2(**food1):
    print(food1)
eat2(eat1="cow",eat001="milk ")