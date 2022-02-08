try:
    import requests
    import time
    import json
    import traceback
    import random
    from notify import send
except Exception as e:
    print('import model exception：{}'.format(e))


# try:
#     send('WSKEY转换', 'te_xt')
# except:
#     logger.info("通知发送失败")

def sendMsg(title,description):
    # msgurl=f'http://tangzhiyong.picp.io:8017/qywxyysendmessage?agentid=1000003&title={title}&toall=0&msgtype=textcard'
    # data ={'description':description}
    # requests.post(msgurl,data=data)
    send(description, description)

def queryNewQuan(payload={},headers={}):
    url = "http://tytapp.quntitong.cn/sportinterNew/androidnorder/queryNewQuan.do"
    files=[

    ]
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(1)
    response = json.dumps(response.text)
    print(2)
    response = json.loads(response)
    print(3)
    response = json.loads(response)
    print(4)

    quanlist = response[0]['data']
    totalRecord = response[0]['totalRecord']
    print(5,quanlist)

    if quanlist:
        quanlist = json.loads(quanlist)
    else:
        quanlist=[]

    quans=f'优惠券信息({totalRecord}张):'
    for index,q in enumerate(quanlist):
        order = index +1
        quan = ''
        name = q['name']
        fullMoney = q['fullMoney']
        availableTime = q['availableTime']
        logtime = q['logtime']
        quan=f'\r\n{order}.《{name},满{fullMoney}可用,可用时间:{availableTime},过期时间:{logtime}》'
        quans=quans+quan

    return quans


def getScore(payload={},headers={},qiandaoresult='',queryNewQuanResult=''):
    currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    url = "http://tytapp.quntitong.cn/sportinterNew/androidaccount/userAll.do"
    files=[]
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = json.loads(response.text)

    score = response[0]['score']
    mobilePhone = response[0]['mobilePhone']
    print(response)

    description=f'电话:{mobilePhone};\r\n积分:{score};\r\n签到结果:{qiandaoresult}{queryNewQuanResult}'
    title=f'群体通积分余额.{mobilePhone}.({currenttime})'
    sendMsg(title,description)

def qiandao(payload={},headers={}):
    url = "http://tytapp.quntitong.cn/sportinterNew/androidsignscore/saveSignDate.do"
    files=[

    ]
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    result = response.text
    print(f'签到结果：{result}')
    return result

#===============15218828238 👇=========================
#randI = random.randint(10,360)
#randI=1
#time.sleep(randI)

time_stamp = time.time()
time_stamp=int(time_stamp)
print(f'time_stamp:{time_stamp}')
#=========================
qiandao_payload_15218828238={'authstring': '99a47ac8cf726d1c6fccca8c6858aa75',
    'authstring2': 'ff2b38c88c65849e8bb766f354d71ce0',
    'cityName': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'citys': '440100',
    'deviceid': '09946D00-DC9B-42EC-B82C-6843A39A74EC',
    'imsi': 'DF7C23699FC0460EBE109607E880BB7D',
    'mobilephone': '15218828237',
    'os': 'ios',
    'service': 'hn',
    'timestamp': time_stamp,
    'userId': '8a42f4917afbb358017b67735cba1b00',
    'version': '4.0.3'}
newquan_payload_15218828238={'authstring': '99a47ac8cf726d1c6fccca8c6858aa75',
    'authstring2': 'ff2b38c88c65849e8bb766f354d71ce0',
    'cityName': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'citys': '440100',
    'deviceid': '09946D00-DC9B-42EC-B82C-6843A39A74EC',
    'imsi': 'DF7C23699FC0460EBE109607E880BB7D',
    'mobilephone': '15218828237',
    'os': 'ios',
    'pageIndex': '1',
    'pageSize': '20',
    'service': 'hn',
    'status': '1',
    'timestamp': time_stamp,
    'userid': '8a42f4917afbb358017b67735cba1b00',
    'version': '4.0.3'}
headers_15218828238 = {
    'Cookie': '__surprise_lottery_app_user__={%22id%22:%8a42f4917afbb358017b67735cba1b00%22%2C%22phone%22:%2215218828237%22}',
    'User-Agent': 'GZSportsWaiter/4.0.3 (iPhone; iOS 14.5.1; Scale/2.00)'
    }

sendmsg_payload_15218828238={'authstring': '99a47ac8cf726d1c6fccca8c6858aa75',
    'authstring2': 'ff2b38c88c65849e8bb766f354d71ce0',
    'cityName': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'citys': '440100',
    'deviceToken': 'b3020293cad99b5300fe21745b77ef2934dee7fa9f9784be7875140972c7f70a',
    'deviceid': '09946D00-DC9B-42EC-B82C-6843A39A74EC',
    'imsi': 'DF7C23699FC0460EBE109607E880BB7D',
    'loginId': '15218828237',
    'loginType': 'ios',
    'mobilephone': '15218828237',
    'os': 'ios',
    'password': 'FD157E40A4E5FB2359EF08686E4B6A4D',
    'service': 'hn',
    'timestamp': time_stamp,
    'version': '4.0.3'}
# ############## 15218828237 👇#######################
try:
    qiandaoresult_152 = qiandao(qiandao_payload_15218828238,headers_15218828238)
    queryNewQuanResult_152 = queryNewQuan(newquan_payload_15218828238,headers_15218828238)
    getScore(sendmsg_payload_15218828238,headers_15218828238,qiandaoresult_152,queryNewQuanResult_152)
except BaseException as e:
    traceback.print_exc()




#===============13925418991 👇=========================
#randI = random.randint(10,360)
# randI=1
#time.sleep(randI)

time_stamp = time.time()
time_stamp=int(time_stamp)
print(f'time_stamp:{time_stamp}')
#=========================
qiandao_payload_13925418991={'authstring': '1aa3e6e5abda97a485bc53e6464fafea',
    'authstring2': '45cbe64ef0be7b5ea97597c254388756',
    'cityName': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'citys': '440100',
    'deviceid': '7E6B5288-301F-4B9C-BAC9-127E522FBCB5',
    'imsi': '29025EE24AF444F29080E17016AE3AFE',
    'mobilephone': '13925418991',
    'os': 'ios',
    'service': 'hn',
    'timestamp': time_stamp,
    'userId': '8a42f4917bc9b8c2017bd868c1c91a13',
    'version': '4.0.3'}
newquan_payload_13925418991={'authstring': '1aa3e6e5abda97a485bc53e6464fafea',
    'authstring2': '45cbe64ef0be7b5ea97597c254388756',
    'cityName': r'%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'citys': '440100',
    'deviceid': '7E6B5288-301F-4B9C-BAC9-127E522FBCB5',
    'imsi': '29025EE24AF444F29080E17016AE3AFE',
    'mobilephone': '13925418991',
    'os': 'ios',
    'pageIndex': '1',
    'pageSize': '10',
    'service': 'hn',
    'status': '1',
    'timestamp': time_stamp,
    'userid': '8a42f4917bc9b8c2017bd868c1c91a13',
    'version': '4.0.3'}
headers_13925418991 = {
    'Cookie': r'__surprise_lottery_app_user__={%22id%22:%228a42f4917bc9b8c2017bd868c1c91a13%22%2C%22phone%22:%2213925418991%22}',
    'User-Agent': 'GZSportsWaiter/4.0.3 (iPhone; iOS 14.7.1; Scale/3.00)'
    }
sendmsg_payload_userall_13925418991={'authstring':'1aa3e6e5abda97a485bc53e6464fafea',
'authstring2':'45cbe64ef0be7b5ea97597c254388756',
'cityName':'%E5%B9%BF%E5%B7%9E%E5%B8%82',
'citys':'440100',
'deviceToken':'f772a0184914a1e8805146f159cb4b1619ee96c8daf16ec9b876899933ee24a7',
'deviceid':'7E6B5288-301F-4B9C-BAC9-127E522FBCB5',
'imsi':'29025EE24AF444F29080E17016AE3AFE',
'loginId':'13925418991',
'loginType':'ios',
'mobilephone':'13925418991',
'os':'ios',
'password':'FD157E40A4E5FB2359EF08686E4B6A4D',
'service':'hn',
'timestamp':time_stamp,
'version':'4.0.3'}

# ##############13925418991 👇#######################
try:
    qiandaoresult_13925 = qiandao(qiandao_payload_13925418991,headers_13925418991)
    queryNewQuanResult_13925 = queryNewQuan(newquan_payload_13925418991,headers_13925418991)
    getScore(sendmsg_payload_userall_13925418991,headers_13925418991,qiandaoresult_13925,queryNewQuanResult_13925)
except BaseException as e:
    traceback.print_exc()
