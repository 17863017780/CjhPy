# -*- coding: utf-8 -*
import requests


def requestAPI(url, data=None, json=None, cookies=None, referer=None, method="get", ip=None, host=None):
    verify = True
    # 构造headers
    if not ip is None:
        url = url.replace(host, ip, 1)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': cookies,
            'referer': referer,
            'host': host
            # 如果需要其他，在接口中自定义，估计的话也不会需要其他东西
        }
        # 判断请求是get还是post
        if method == "get":
            result = requests.get(url, data=data, json=json, headers=headers, verify=False)
        elif method == "post":
            result = requests.post(url, data=data, json=json, headers=headers, verify=False)
    else:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': cookies,
            'referer': referer
            # 如果需要其他，在接口中自定义，估计的话也不会需要其他东西
        }
        # 判断请求是get还是post
        if method == "get":
            result = requests.get(url, data=data, json=json, headers=headers)
        elif method == "post":
            result = requests.post(url, data=data, json=json, headers=headers, verify=False)
    if result.status_code == 200:
        return result.text
    else:
        return str(result.status_code)
    # return requests.get(url).text





if __name__ == '__main__':
    url = "https://beta-api.m.jd.com/api?appid=paimai&functionId=getCurrentDaySeckillAccessNumberForApi&body={}"
    str = requestAPI(url)
    print(str)
    # print(add(1,2))
    url = "http://beta-api.m.jd.com/api?appid=mipaimai-h5&functionId=paimai_getUserStatus&&loginType=3"
    cookie = '__jdv=137720036|direct|-|none|-|1608022034833; __jdu=1608022034832953704053; areaId=1; ipLoc-djd=1-2809-0-0; shshshfpa=ced41d50-b64f-6783-1255-22908eabfa19-1608186651; shshshfpb=r09AC4AeKQLvKFCoCLIfEIA%3D%3D; _base_=YKH2KDFHMOZBLCUV7NSRBWQUJPBI7JIMU5R3EFJ5UDHJ5LCU7R2NILKK5UJ6GLA2RGYT464UKXAI5KK7PNC5B5UHJ2HVQ4ENFP57OC7ZLDSIJBQHQ7UCZUW6LAMIZO3ATCNE6YVKRXISUUNC5YBH6PXX4YQRRXDZZB4QAMKSG4SOQWCP5WPWO6EFS7HEHMRWVKBRVHB33TFD5FMC4VEQIPFBO5LYZS4KXUMIMAEF75DKQPQEAQ4ASED5W3W7QZNILZSK5G2CDQCRTDPTQJDPOQN4BF2ZQTTGGT3YU737XOOZK63H6SQO6IEKMHDAXG7EQXYY37XB4RWTL3VFV3633UYZCM; sso.jd.com=BJ.3fcc7cd369a2477db718d25ff288755b; PCSYCityID=CN_110000_110100_110112; TrackID=1EN_1FNT1VSgU61H_cUmkyrY0Lj3wllPlB4HyTzJZkQLVKzz8REZaWonDktcjOLUg6pgDiOPMo8SE7sBUm2tgRD00yWACqSeIkFvF5591GUG41x6yQMr0ITbbMuwKEwKz; pinId=16bv2iaWDDBa3YoQ5JcJ9rV9-x-f3wj7; pin=jd_5c01c795994d9; unick=as%E6%84%A4%E6%80%92%E7%9A%84%E8%8C%84%E5%AD%90; ceshi3.com=000; _tp=pTQ9wn1r6qJtyFhs4Ug%2FToYbklNeTkqSfvYzZXcNwyo%3D; _pst=jd_5c01c795994d9; shshshfp=f724ab06728ad48d0e594ed1846c8864; shshshsID=0b9fefebef3317914befba4a3d9b7edd_1_1608726865500; user-key=7f40f5c3-76ff-4fe2-8de2-febebe68e322; cn=4; __jda=122270672.1608022034832953704053.1608022035.1608703335.1608724872.20; __jdb=122270672.23.1608022034832953704053|20.1608724872; __jdc=122270672; thor=4E57F02F2C5D3D391D9E8E789E276C9827EA8A23F1D7829982D97B95169F7D6DEC9588CA2CFC16D1308B0EAD323E41DFE682095A36EE9D5F645840971496370925D47F23F504D7218F6111DA0481A43FE03A8287D16032C19FC371A3679B5E64AC3186CEF4B696EF707744479298708D9D9E8F8AA3EE5B5147EC4569EDD15AF81BADBE839486D649AF6535067601ECE26D7E0A24C38724EB0021C188E7D2DA86; 3AB9D23F7A4B3C9B=MFHACFRONJ2VZ6MLYZGSN6KXP4IEYMGFNMOJIHCDVKG66CU6ABKIYFZDNKMT6IFIGXJDFO6VFALXMANQO2CO6DIXKQ'
    print(requestAPI(url, cookies=cookie))
