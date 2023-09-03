# 列表-----list
# list1=["张三","lisi","wangwu","999"]
# --输出列表位置为0的字符
# print(list1[0])

# --输出列表位置为1、2位内容
# print(list1[1:3])

# 反方向输出
# print(list1[::-1])

# 遍历输出列表中的数据
# for s1 in list1:
#     print(s1)

 # 输出列表
# print(len(list1))


# 列表练习
# 把列表中姓张的改为姓李的
# stu=["王张杰","张晓噢","李晓华","张可可","张月敏","like"]
# for i in range(len(stu)):
#     item=stu[i]
#     if item.startswith("张"):
#         new_name="李"+item[1:]
#         print(new_name)
#         stu[i]=new_name
# print(stu)

#列表的排序    sort---升序排列   reverse----翻转
# list1=[525,969,66,652,22,1]
# list1.sort()
# print(list1)
# # 排序后翻转
# list1.sort(reverse=True)
# print(list1)

#列表的循环输出---删除名称中含有李姓的名字
# list1=["李可欣","李月汝","张学记","王悦溪","安可","李克杰"]
# temp= []
# for del1 in list1:
#     if del1.startswith("李"):
#         temp.append(del1)
#
# for del1 in temp:
#     list1.remove(del1)
#
# print(list1)

#元组
# tuple1=("ok","yes","no","hello")
# print(tuple1)
#
# tuple2=("ok")
#
# print("第二个元组值："+tuple2)
#
# tuple3=("ake",)
# print("第san个元组值：")
# print(tuple3 )
#
# for item1 in tuple1:
#     print(item1)

#集合-----set
# set1={'023',52,"keke"}
# print(set1)
#
# set2=set()
# set2.add("wuyu")
# set2.add("akeek")
# set2.add(1230)
# print(set2)
#
# set2.remove(1230)
# print(set2)
#
# set2.remove("wuyu")
# set2.add("xiaoxues")
#
# print(set2)

#利用set去重复数据
# li=["96",99,"okok",99,"plpl","96"]
# print(li)
# print(set(li))
# print(list(set(li)))    ---转义为列表


# 字典
# 定义
# dic1={"ok":"yes","no":"none","my":"mine"}
# dit=dic1["ok"]
# print(dit)

#None判断不存在 提供友好性
# dic2={
#     "wushi":"12",
#     "akesi":"33",
#     "zhangyue":"27"
# }
# name=input("please input your name:")
# na=dic2.get(name)
# if na is None:
#     print("none")
# else:
#     print(na)

# # 循环
# dic1={
#     "001":"anks",
#     "002":"likes",
#     "oo3":"lele"
# }
# # 利用for循环 直接拿到key
# for key in dic1:
#     print("该字典的key值如以下所示：")
#     print(key)
# # 利用key输出value值
# for key in dic1:
#     print(key,dic1[key])
#
# # 把value存到列表中
# print(list(dic1.values()))
#
# # 最简化输出key与value值
# for key,value in dic1.items():
#     print(key,value)


# 嵌套
# tvs={
#     "name1":"扫黑风暴",
#     "tv1" :"东方卫视",
#     "anther":{
#         "name2":"无唧唧哇",
#         "tv2":"湖北卫视"
#     }
#      }
# print(tvs["anther"]["name2"])
# tvs["anther"]["tv2"]="henan"
#
# for key,value in tvs.items():
#     print(key,value)

#循环删除
# dic={"ake":"990","xiaoqiao":"2502","zhouyu":"33"}
# ti=[]
# for key in dic:
#     if key.startswith("a"):
#         ti.append(key)
#
# for t in ti:
#     dic.pop(t)
# print(dic)

