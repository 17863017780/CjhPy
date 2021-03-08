


import bin.common.JSFTest
import time
import bin.common.InterfaceRequests
import bin.common.jsonData
import json
import bin.paimai.skuConfig



#创建平台化活动所需的方法
#sku，开始结束时间，循环时间
def createPlatform(sku,startTime, endTime, cycleTime):
    print("createPlatform",sku,startTime, endTime, cycleTime)
    nowTime = time.time()
    startTime = nowTime + startTime * 60
    endTime = nowTime + endTime * 60
    interfaceName = "com.jd.pop.auction.center.api.platform.service.write.PlatformSkuDetailWriteService"
    parameterJson = [{
        "supplierCode": "10255942",
        "bail": 0,
        "businessCode": "cycleIncr",
        "auctionForm": 1,
        "stockNum": 200,
        "startTime": startTime,
        "auctionType": 1,
        "id": 0,
        "skuId": sku,
        "creator": "test_jed001shop",
        "dealActivity": "False",
        "tailOrderPaymode": 0,
        "initialPrice": 1,
        "auditor": "",
        "bindSku": 0,
        "skuType": 0,
        "cycleType": 2,
        "createSource": 2,
        "updateSource": 2,
        "bindSpu": 0,
        "updator": "test_jed001shop",
        "jdPrice": 1,
        "spuId": 0,
        "endTime": endTime,
        "delayPeriod": 1,
        "properties": [
            {
                "property": "priceLowerOffset",
                "dataValue": "20"
            }, {
                "property": "slogan",
                "dataValue": "好货正在捡漏中，快来抢拍"
            }, {
                "property": "duration",
                "dataValue": cycleTime * 60
            }
        ],
        "reservedPrice": 0
    },
        {
            "pin": "ccjh1",
            "sourceIp": "127.0.0.1",
            "sourceType": 1
        }
    ]
    alias = "platform-center"
    methodName = "addPlatformSkuDetail"
    argsClass = "com.jd.pop.auction.center.api.platform.dto.ware.PlatformSkuDetailSaveParamDTO,com.jd.pop.auction.center.api.platform.dto.ClientSourceDTO"
    response = bin.common.JSFTest.jsfInterface(interfaceName=interfaceName,
                                               parameterJson=parameterJson,
                                               alias=alias,
                                               methodName=methodName,
                                               argsClass=argsClass)
    print("createPlatform,response",response)
    if response.find("true")>=0:
        response = json.loads(response)
        return response["data"]
    else:
        return "创建不成功，请检查网络是否正常"


# 这个方法是发布商品所用的方法
def publish(skudetailId,venderId,pin):
    interfaceName = "com.jd.pop.auction.center.api.platform.service.write.PlatformSkuDetailWriteService"
    parameterJson = [skudetailId,venderId,pin]
    alias = "platform-center"
    methodName = "publish"
    argsClass = "java.lang.Long,java.lang.String,java.lang.String"
    response = bin.common.JSFTest.jsfInterface(interfaceName=interfaceName,
                                               parameterJson=parameterJson,
                                               alias=alias,
                                               methodName=methodName,
                                               argsClass=argsClass)
    print("createPlatform,response", response)
    if response.find("true")>=0:
        return "发布成功"
    else:
        return "发布不成功，请检查网络是否正常"



# 用来判断该商品正处于哪种状态
def judgePaimaiStatus(skuId):
    #todo 这里需要问一下客户端信息应该给我们哪一个
    print("judgePaimaiStatus",skuId)
    url = "http://api.m.jd.com/api?appid=paimai&functionId=getPaimaiCurrentInfoByIdsForApi&body={%22ids%22:[" + str(skuId) + "],%22idType%22:1,%22clientInfo%22:{%22businessId%22:1005}}"
    response = bin.common.InterfaceRequests.requestAPI(url)
    print("judgePaimaiStatus",response)
    if response.find("\"auctionStatus\":1")>=0 or response.find("\"auctionStatus\":0")>=0:
        return False
    else:
        return True

# 商品下架
def good_off_shelves(skuId):
    interfaceName = "com.jd.pop.auction.center.api.platform.service.write.PlatformSkuWriteService"
    parameterJson = [skuId,"ccjh1_terminationAuction"]
    alias = "auction_platform_center_jsf_yf"
    methodName = "terminationAuction"
    argsClass = "java.lang.Long,java.lang.String"
    response = bin.common.JSFTest.jsfInterface(interfaceName=interfaceName,
                                               parameterJson=json.dumps(parameterJson),
                                               alias=alias,
                                               methodName=methodName,
                                               argsClass=argsClass)
    # 因为得让商品结束掉，所以在重新上拍之前得下架
    print(json.dumps(parameterJson))
    print("good_off_shelves",str(response))
    if str(response).find("\"data\": true") >= 0:
        return True
    else:
        return False


def createPOPSku(startTime,endTime,cycleTime):
    #1、首先根据sku查询一下商品状态
    print("createPOPSku",startTime,endTime,cycleTime)
    sku_length = bin.paimai.skuConfig.pop_Sku.__len__()
    temp = 0
    for sku in  bin.paimai.skuConfig.pop_Sku :
        print("createPOPSku,第一个sku",sku)
        if judgePaimaiStatus(sku):
            print("createPOPSku,judgePaimaiStatus", sku)
            temp = temp + 1
        else:
            print("createPOPSku,judgePaimaiStatus23", sku)
            response =createPlatform(sku,startTime,endTime,cycleTime)
    if temp == sku_length:
        if good_off_shelves(bin.paimai.skuConfig.pop_Sku[0]):
            response = createPlatform(bin.paimai.skuConfig.pop_Sku[0],startTime,endTime,cycleTime)
        else:
            return "商品都在用，下架也没成功~你自己想办法吧"
    if not publish(response, "10255942", "cjh_test_jed02").find("不成功") >= 0:
        return bin.paimai.skuConfig.pop_Sku[0]
    else:
        return "发布不成功，你自己看着办吧"



if __name__ == '__main__':
    print("main方法开始创建")
    # print(createPOPSku(6,11,3))
    print(good_off_shelves(10027226249970))