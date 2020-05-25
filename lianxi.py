#练习：现在有10个学生的成绩，需要录入到系统中 ，这十个人分别是 索张三 李四 王麻子 浪晋 流云 喜喜 小亮 二狗 陈平安 珠珠 亚
#并且名字和成绩需要对应上
#而且大于60的和小于60的需要分开放

#字典 分开存放到数组/字典  input

# highchengji = {}#  定义了一个空字典 存储信息
# lowchengji = {}
# studentlist = ["张三","李四","王麻子","浪晋", "流云","喜喜","小亮","二狗","陈平安","亚索"]
# a = 0  #定义了一个变量 用来控制数组的下标的变化
# while a<len(studentlist):#因为所有的人的信息的录入，都是要用input，所有写了循环，len判断了数组的长度，总长度-1就是最大的下标
#     chengji=int(input("请输入"+studentlist[a]+"的成绩"))#录入信息 为了方便 转换了格式
#     if chengji>=60:
#         highchengji[studentlist[a]] = chengji#存到字典中
#     else:
#         lowchengji[studentlist[a]] = chengji 
#     a = a + 1 #控制下标变化 每一次循环都+1
# print("大于60的:",highchengji)
# print("小于60的：",lowchengji)



# highchengji = {}#  定义了一个空字典 存储信息
# lowchengji = {}
# studentlist = ["张三","李四","王麻子","浪晋", "流云","喜喜","小亮","二狗","陈平安","亚索"]
# for i in studentlist:
#     chengji=int(input("请输入"+i+"的成绩"))#录入信息 为了方便 转换了格式
#     if chengji>=60:
#          highchengji[i] = chengji#存到字典中
#     else:
#          lowchengji[i] = chengji 
# print("大于60的:",highchengji)
# print("小于60的：",lowchengji)



#练习  实现一个九九乘法表

# for i in range(1,10):#因为是从 1开始的
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end=" ")
#     print()#起换行的作用

#练习1
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次
#练习2
使用代码实现一个注册的功能。用户输入账号和密码，要求账号长度是5-8位 密码 6-12位，并且这个账号必须小写字母开头。
储存到字典中{username：password}