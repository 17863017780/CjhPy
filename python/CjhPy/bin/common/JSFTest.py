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
        response_str = json.loads(response_str.text)['data']
        return str
    else:
        return "调用jsf服务出错", response_str.status_code, response_str.text


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
    str = jsfInterfaceTest(jsonData)
    str1 = 'eyJjb2RlIjowLCJzdGF0dXMiOjIwMCwibWVzc2FnZSI6IuaIkOWKnyIsImRhdGEiOnsiaWQiOm51bGwsInBpbiI6bnVsbCwib3JkZXJDb3VudCI6bnVsbCwiZGVmYXVsdHNDb3VudCI6bnVsbCwiZGVmYXVsdHNSYXRlIjowLCJib25kQ291bnQiOm51bGwsImdldEF1Y3Rpb25Db3VudCI6bnVsbCwiZ2V0QXVjdGlvblJhdGUiOjAsInJldHVyblJhdGUiOjAsInJldHVybkNvdW50IjpudWxsLCJmaW5pc2hDb3VudCI6bnVsbCwiY3JlYXRlVGltZSI6IkRlYyAyOSwgMjAyMCA1OjQ1OjU2IFBNIiwidXBkYXRlVGltZSI6IkRlYyAyOSwgMjAyMCA1OjQ1OjU2IFBNIiwiaXNEZWxldGUiOjF9fQ=='
    str1 = getStrFromBase64(str1)
    print(str1)

    # abc="1231433515"
    # if(abc.find("4") and True ):
    #     print(True)
    # else:
    #     print(False)
