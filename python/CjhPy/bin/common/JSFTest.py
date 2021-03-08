#!coding:utf-8#
import requests
import json
import base64

smartTestUrl = "http://smarttest.jd.com/open/api/jsf/invokeHttp"

def jsfInterfaceTest(parameterJson):
    httpUrl = smartTestUrl
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'erp': 'ccjh1',
        'token': '385ca9d'
        # erp和token 是找测试平台要的，实际上就是通过测试平台去请求接口
    }
    response_str = requests.post(url=httpUrl, headers=headers, json=parameterJson)
    if (response_str.status_code == 200 and response_str.text.find("\"status\":0")):
        return response_str.text
    else:
        return "调用jsf服务出错", response_str.status_code, response_str.text



# parameterJson 接口入参
# interfaceName 接口name
# alias 别名
# methodName 方法名称
# argsClass 方法入参类型，例如map等
def jsfInterface(parameterJson,interfaceName,alias,methodName,argsClass):
    parameJson = {
        "parameterJson": parameterJson,
        "interfaceName": interfaceName,
        "alias": alias,
        "methodName": methodName,
        "argsClass": [argsClass]
    }
    return jsfInterfaceTest(parameJson)



# 此方法就是用来base64解码的
def getStrFromBase64(str1):
    missing_padding = 4 - len(str1) % 4
    if missing_padding:
        str1 += '=' * missing_padding
    return base64.b64decode(str1).decode('utf-8')


if __name__ == '__main__':
    jsonData = {
        "parameterJson": "[{\"pin\": \"Gtyrant\"}]",
        "interfaceName": "com.jd.auction.gateway.color.IPaimaiStatisticsColorService",
        "alias":  "ipaimai-common",
        "methodName": "getStatisticsInfo",
        "argsClass": [
            "java.util.Map"
        ]
    }
    parameterJson= "[{\"pin\": \"Gtyrant\"}]"
    interfaceName ="com.jd.auction.gateway.color.IPaimaiStatisticsColorService"
    alias = "ipaimai-common"
    methodName = "getStatisticsInfo"
    argsClass="java.util.Map"
    jsondata2={
        "parameterJson": parameterJson,
        "interfaceName": interfaceName,
        "alias":  alias,
        "methodName": methodName,
        "argsClass": [argsClass]
    }
    print(getStrFromBase64(jsfInterfaceTest(jsonData)))
    print(getStrFromBase64(jsfInterface(parameterJson,interfaceName,alias,methodName,argsClass)))