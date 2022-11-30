# 库调用
import requests
import json
import time

# 基本数据
AppID = 'wxeffacf63b1136f83'  # 微信小程序AppID
AppSecret = '3e62fb5f9dcfd061e22f9618906ee90f'  # 微信小程序APPSecret
ENV = 'cloud1-7guabcq68d8fc85f' # 微信小程序环境ID

# 函数
# 获取access_token
def access_token():
    AppID = 'wxeffacf63b1136f83'  # 微信小程序AppID
    AppSecret = '3e62fb5f9dcfd061e22f9618906ee90f'  # 微信小程序APPSecret
    
    WeChat_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + str(AppID) + '&secret=' + str(AppSecret) # 路径

    response = requests.get(WeChat_url)
    result = response.json()
    return result["access_token"]

# 查询对象组
def get(access_token,collection_name):
    ENV = 'cloud1-7guabcq68d8fc85f' # 微信小程序环境ID
    
    WeChat_url = 'https://api.weixin.qq.com/tcb/databasequery?access_token=' + str(access_token) # 路径
    data = {
        "env": ENV, # 微信小程序环境ID
        "query": "db.collection(\""+str(collection_name)+"\").limit(100).get()" # 对象组名称
    }
    data = json.dumps(data) # 数据预处理

    response = requests.post(WeChat_url,data)
    result = response.json()
    return result['data']

# 更新对象
def update(access_token,collection_name,limit,content):
    ENV = 'cloud1-7guabcq68d8fc85f' # 微信小程序环境ID
    
    WeChat_url = 'https://api.weixin.qq.com/tcb/databaseupdate?access_token=' + str(access_token) # 路径
    data = {
        "env": ENV, # 微信小程序环境ID
        "query": "db.collection(\""+str(collection_name)+"\").where({"+str(limit)+"}).update({data:{"+str(content)+"}})" # 对象组名称 限制条件 更改的内容
    }
    data = json.dumps(data) # 数据预处理
    response = requests.post(WeChat_url,data)
    result = response.json()
    return result['errmsg']

# 增加对象
def add(access_token,collection_name,name,class_name,operation):
    ENV = 'cloud1-7guabcq68d8fc85f' # 微信小程序环境ID
    
    WeChat_url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token=' + str(access_token) # 路径
    t = time.time() # 时间戳
    date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t)) # 格式化日期
    query = 'db.collection("'+str(collection_name)+'").add({\ndata:{\nname:"'+str(name)+'",\nclass_name:"'+str(class_name)+'",\noperation:'+str(operation)+',\ndate:"'+str(date)+'"\n}\n})' #对象组名称 姓名 班级 操作
    data={
        "env": ENV, # 微信小程序环境ID
        "query": query 
    }
    data = json.dumps(data) # 数据预处理
    
    response = requests.post(WeChat_url,data)
    result = response.json()
    return result['errmsg']


# 删除对象
def delete(access_token,collection_name,limit):
    ENV = 'cloud1-7guabcq68d8fc85f' # 微信小程序环境ID
    
    WeChat_url = 'https://api.weixin.qq.com/tcb/databasedelete?access_token=' + str(access_token) # 路径
    data = {
        "env": ENV, # 微信小程序环境ID
        "query": 'db.collection(\"'+str(collection_name)+'\").where({'+str(limit)+'}).remove()' # 对象组名称
    }
    data = json.dumps(data) # 数据预处理
    
    response = requests.post(WeChat_url,data)
    result = response.json()
    return result['errmsg']


def getisornot(dic):
    ISORNOT = ''
    if dic['state']:
        ISORNOT = '1'
    else:
        ISORNOT = '0'
    if dic['right']:
        ISORNOT = ISORNOT + '1'
    else:
        ISORNOT = ISORNOT +'0'
    return ISORNOT

