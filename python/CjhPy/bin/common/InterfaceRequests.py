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
            'referer': referer,
            # 'User-Agent':'dapp;android;9.3.3;10;123-456;network/wifi;model/VOG-AL00;addressid/2562016888;aid/7837585c71e1922a;oaid/b9fffd73-df5f-e219-eff7-9fe9d37eeb2d;osVer/29;appBuild/86090;psn/864674045234769-b8c38518d6da|757;psq/28;uid/864674045234769-b8c38518d6da;adk/;ads/;pap/JA2015_311210|9.3.3|ANDROID 10;osv/10;pv/687.34;jdv/0|kong|t_1000170135|tuiguang|notset|1608998092416|1608998092;ref/https%3A%2F%2Fzpsy.jd.com%2F%3FcollectionId%3D16%26lng%3D116.391248%26lat%3D39.126053%26un_area%3D5_274_49708_49882;partner/huawei;apprpd/RNAuction_MyAuction;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36'
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




#
# if __name__ == '__main__':
#     url = "https://beta-api.m.jd.com/api?appid=paimai&functionId=getCurrentDaySeckillAccessNumberForApi&body={}"
#     str = requestAPI(url)
#     print(str)
#     # print(add(1,2))
#     url = "http://beta-api.m.jd.com/api?appid=mipaimai-h5&functionId=paimai_getUserStatus&&loginType=3"
#     cookie = '__jdv=137720036|direct|-|none|-|1608022034833; __jdu=1608022034832953704053; areaId=1; ipLoc-djd=1-2809-0-0; shshshfpa=ced41d50-b64f-6783-1255-22908eabfa19-1608186651; shshshfpb=r09AC4AeKQLvKFCoCLIfEIA%3D%3D; _base_=YKH2KDFHMOZBLCUV7NSRBWQUJPBI7JIMU5R3EFJ5UDHJ5LCU7R2NILKK5UJ6GLA2RGYT464UKXAI5KK7PNC5B5UHJ2HVQ4ENFP57OC7ZLDSIJBQHQ7UCZUW6LAMIZO3ATCNE6YVKRXISUUNC5YBH6PXX4YQRRXDZZB4QAMKSG4SOQWCP5WPWO6EFS7HEHMRWVKBRVHB33TFD5FMC4VEQIPFBO5LYZS4KXUMIMAEF75DKQPQEAQ4ASED5W3W7QZNILZSK5G2CDQCRTDPTQJDPOQN4BF2ZQTTGGT3YU737XOOZK63H6SQO6IEKMHDAXG7EQXYY37XB4RWTL3VFV3633UYZCM; sso.jd.com=BJ.3fcc7cd369a2477db718d25ff288755b; PCSYCityID=CN_110000_110100_110112; TrackID=1EN_1FNT1VSgU61H_cUmkyrY0Lj3wllPlB4HyTzJZkQLVKzz8REZaWonDktcjOLUg6pgDiOPMo8SE7sBUm2tgRD00yWACqSeIkFvF5591GUG41x6yQMr0ITbbMuwKEwKz; pinId=16bv2iaWDDBa3YoQ5JcJ9rV9-x-f3wj7; pin=jd_5c01c795994d9; unick=as%E6%84%A4%E6%80%92%E7%9A%84%E8%8C%84%E5%AD%90; ceshi3.com=000; _tp=pTQ9wn1r6qJtyFhs4Ug%2FToYbklNeTkqSfvYzZXcNwyo%3D; _pst=jd_5c01c795994d9; shshshfp=f724ab06728ad48d0e594ed1846c8864; shshshsID=0b9fefebef3317914befba4a3d9b7edd_1_1608726865500; user-key=7f40f5c3-76ff-4fe2-8de2-febebe68e322; cn=4; __jda=122270672.1608022034832953704053.1608022035.1608703335.1608724872.20; __jdb=122270672.23.1608022034832953704053|20.1608724872; __jdc=122270672; thor=4E57F02F2C5D3D391D9E8E789E276C9827EA8A23F1D7829982D97B95169F7D6DEC9588CA2CFC16D1308B0EAD323E41DFE682095A36EE9D5F645840971496370925D47F23F504D7218F6111DA0481A43FE03A8287D16032C19FC371A3679B5E64AC3186CEF4B696EF707744479298708D9D9E8F8AA3EE5B5147EC4569EDD15AF81BADBE839486D649AF6535067601ECE26D7E0A24C38724EB0021C188E7D2DA86; 3AB9D23F7A4B3C9B=MFHACFRONJ2VZ6MLYZGSN6KXP4IEYMGFNMOJIHCDVKG66CU6ABKIYFZDNKMT6IFIGXJDFO6VFALXMANQO2CO6DIXKQ'
#     print(requestAPI(url, cookies=cookie))

if __name__ == '__main__':
    json=[{
	    "pimaiId": 147317709,
	    "bindType": 2,
        "operation": 0
    }]
    cookie="JSESSIONID=7EB56DC2953F7D92EF22DC172C8F9D3C.s1; jd.erp.lang=zh_CN; __jdu=161406672088490306157; areaId=1; mba_muid=161406672088490306157; wxa_level=1; shshshfpb=djREJ4P9MY1n%20A%20Q%20QIFkug%3D%3D; shshshfpa=6e4ea78b-1ca2-4978-22cd-7bfca7da9269-1614051038; TrackerID=_Sk4VduSifSFKAqFn69hnUdfzfVPEAtzFL2JdJu9UM8uHLA2aRMJb1owqSs1_YmEnsN5BjuTI5P1mnTveM4j1YVdxjCiwUt5FQ3E9TcF4yfWQ73JSlfR7-KEA4qZsBIr5fIFohhWuwazxI6BqBSu2A; pt_key=AAJgNLT4ADDcvbXY4egaLF3AhanKmzLVLoagJov0B257XDlyQqrtfvLDdZs85gswVWh_zwR2kqg; pt_pin=jd_5c01c795994d9; pt_token=9rapkhit; pwdt_id=jd_5c01c795994d9; sfstoken=tk01m8ce61be7a8sM3gxcDFBb3BFH7F69kQgPFlujJTPtq8NkXLLHAFNMlJ53odKdaVqvmwEO8RXpJmVe8LfooZ7PfVM; ipLoc-djd=1-2809-51231-0; TrackID=1FEGK3re3CkN8SwWFy5o-y7nPItjV8a1t7pqilRqF8cdeZ7S6Hgj7yLSabZ_o7crYGOtra0w6ZczeXT3he0UjRV0tIGQg-JGgd2uqIgnp8EDR2NsOpSpiOUF0YCIzOKnQ; pinId=16bv2iaWDDBa3YoQ5JcJ9rV9-x-f3wj7; pin=jd_5c01c795994d9; unick=as%E6%84%A4%E6%80%92%E7%9A%84%E8%8C%84%E5%AD%90; ceshi3.com=000; _tp=pTQ9wn1r6qJtyFhs4Ug%2FToYbklNeTkqSfvYzZXcNwyo%3D; _pst=jd_5c01c795994d9; ll-sso=e16885ea1be05ff323c0bcd9e697cf7b%3A0604cb2fd32ede904acbe0812ba1ed379c46b47d73f6fb3fa00b893a8873be4a242a7c1f110312b9b2e9484948d7d92e; __jdv=122270672%7Ciosapp%7Ct_335139774%7Cappshare%7CWxfriends%3Fback%3D1%7C1614149156155; qd_uid=KLJ37Y4M-SGQ0JT1C7GQZQYOB29FE; qd_fs=1614149977979; user-key=84d9b542-c0ab-41b5-88c9-6ba35823d528; cn=7; retina=1; cid=9; webp=1; visitkey=6980185597570246; PPRD_P=UUID.161406672088490306157; sc_width=375; __wga=1614153035746.1614152919877.1614152919877.1614152919877.6.1; wlfstk_smdl=thurp21wkgo4m2ywdg4im84rwymmc456; jdd69fo72b8lfeoe=MFHACFRONJ2VZ6MLYZGSN6KXP4IEYMGFNMOJIHCDVKG66CU6ABKIYFZDNKMT6IFIGXJDFO6VFALXMANQO2CO6DIXKQ; erp1.jd.com=7C4E1E07870492AB718CE153E3BDD6F2EBB160042108705ED1B82F1AB73995B0205119C47ACB3C5D4B3D647CA4A925DCD73CAA7116176073D93A8F0679FE3A1EAFEDD20C5F0E05FF6F7E3FA52C61C33F; sso.jd.com=BJ.154816d6bc5c4f7b873bb994b1d0070a; jdc_art=1614234584959-TEjQjcSo5NZvWrOf-mwCm3KuSCYZfbKt; jdc_art.sig=fCmvTvsGkmiOPR0UDoN-bu7AMgQ; RT=\"sl=0&ss=klki1wf7&tt=0&z=1&dm=jd.com&si=yh1t5106pwk&r=0b28881ee77b4d3b40f6870317b84a8b&ul=33d9e&hd=33djr\"; qd_ad=jdpaycert.jd.com%7C-%7Cjd%7C-%7C0; 3AB9D23F7A4B3C9B=MFHACFRONJ2VZ6MLYZGSN6KXP4IEYMGFNMOJIHCDVKG66CU6ABKIYFZDNKMT6IFIGXJDFO6VFALXMANQO2CO6DIXKQ; qd_ls=1614246154345; qd_ts=1614248367007; qd_sq=4; __jda=50436146.161406672088490306157.1614066721.1614240552.1614253998.17; __jdc=50436146; shshshfp=511d7e17f4880072f30b19b07197b2a7; __jdb=50436146.18.161406672088490306157|17.1614253998; mba_sid=16142544542202156052043574550.14; __jd_ref_cls=MAuction_Product_Contact; shshshsID=27b89fe84c73dde5d64176c144ca6bb8_9_1614257273055; JSESSIONID=7EB56DC2953F7D92EF22DC172C8F9D3C.s1"
    a=requestAPI("https://box.man.jd.com/assistAgency/delete.action",json=json
               ,cookies=cookie,method="post")
    print(a)