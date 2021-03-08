# # -*- coding: utf-8 -*
# import InterfaceRequests
# import JSFTest
# import jsonData
# import json
# import time
# import random
#
#
# def testWeiGuan(http_url):
#     # 为了增加围观数，刷的接口，方便使用，实际没有啥效果
#     a = int(random.random() * 1000) + int(random.random() * 100) + int(random.random() * 10)
#     # a=100
#     print(" start !", a, ",url:" + http_url)
#     for i in range(0, 3):
#         InterfaceRequests.requestAPI(http_url)
#     print("this is ok !," + http_url)
#
#
# def testJSF():
#     parameterJson = "[{\"pin\": \"Gtyrant\"}]"
#     interfaceName = "com.jd.auction.gateway.color.IPaimaiStatisticsColorService"
#     alias = "ipaimai-common"
#     methodName = "getStatisticsInfo"
#     argsClass = "java.util.Map"
#     JSFTest.jsfInterface()
#
#
# def deletequery():
#     for i in range(1, 3):
#         print(i)
#         time.sleep(1)
#         httpUrl = "https://api.m.jd.com/api?functionId=seckill_querySaunter&appid=paimai&body=%7B%22categoryId%22:-1,%22page%22:" + str(
#             i) + ",%22excludeCategoryIds%22:%22%22%7D"
#         print(httpUrl)
#         response = InterfaceRequests.requestAPI(httpUrl)
#         data = json.loads(response)
#         # print(data['datas'])
#         list = data["datas"]
#         print(list)
#         strlList = ""
#         for p in list:
#             # data = lisz
#             strlList += str(p['data']['id']) + ","
#             print(str(p['data']['id']))
#         print(strlList)
#     # print(str)
#
#
# if __name__ == '__main__':
#     file = open("/Applications/jd/工作文件/测试/刷围观.txt")
#     # a = int(random.random() * 1000)+400
#     # print(a)
#     while 1:
#         line = file.readline()
#         if not line:
#             break
#         else:
#             testWeiGuan(line)
#             time.sleep(5)
#             # print(line)
#         pass  # do something
#     file.close()
#     print("Everything is ok !!!")
#     # testWeiGuan("https://paimai.jd.com/254607670")
