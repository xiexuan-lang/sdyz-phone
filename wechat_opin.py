import wechat # 导入模块文件
import json
import xuan_DATABASE as xuan

# 增加表------------------------------------------------------------------------------------
'''
print(WeChat.add(WeChat.access_token(),'diary','谢轩','高一八班','true'))

WeChat.access_token()----调用函数获取acces_token
'diary'------------------增加的集合的名称（在这个集合内增加表）
'谢轩'-------------------增加的表的属性之一：名字
'高一八班'---------------增加的表的属性之一：班级
'true'------------------增加的表的属性之一：手机是否取出（取出：true，存入：false）

调用该函数会返回调用错误信息（成功返回ok）
'''
# 更新表------------------------------------------------------------------------------------
'''
print(WeChat.update(WeChat.access_token(),'student_list','name:"陆永佳"','right:false'))

WeChat.access_token()----调用函数获取acces_token
'student_list'-----------更新的集合的名称（更新这个集合内的表）
'name:"陆永佳"'----------更新的表的特征：名字（只更改属性name等于"陆永佳"的表，注意嵌套双引号）
'right:false'-----------更新的表的属性：是否有权限取出手机
'true'------------------增加的表的属性之一：是否取出（取出操作：true，存入操作：false）

调用该函数会返回调用错误信息（成功返回ok）
'''
# 获取表------------------------------------------------------------------------------------
'''
print(WeChat.get(WeChat.access_token(),'student_list'))

WeChat.access_token()----调用函数获取acces_token
'student_list'-----------查询的集合的名称（更新这个集合内的表）

调用该函数会返回一个对象组[{字典},{字典},{字典}]，将字典分离出来见下
'''
def Db_sync():
    student_list = wechat.get(wechat.access_token(),'student_list')
    #l = 1
    for i in student_list:
        dic = json.loads(i)
        #print(dic)
        ISORNOT="'"+str(wechat.getisornot(dic))+"'"
        NAME = "'"+dic['name']+"'"
        #print(ISORNOT)
        ID = "'"+dic['_id']+"'"
        xuan.del_data1('test','CLASS',NAME)
        xuan.add_data1('test','CLASS',ID,NAME,str(ISORNOT))


def Db_isornotupdata(Name,State):
    wechat.update(wechat.access_token(),'student_list','name:"{name}"','state:{state}'.format(name = Name,state = State))
#Db_sync()
#xuan.get_all_data('test','CLASS')
#xuan.del_f('test','class')
#xuan.del_data('test','CLASS',"'林家浚'")
#Db_isornotupdata('陆永佳','True')