#!coding:utf-8#
# 此方法是用来解析json的
import json


#用来获取json里特殊字段的数据
#默认是三层数据接口
#如果是列表数据需要传入jsonkeyobject，返回data数据,如果不是列表，直接返回value值
def getStringFromJson(jsonString, jsonKey,jsonKeyObject=None):
    if (jsonKey in jsonString and type(jsonString) != type({}) and type(jsonString) != type([])):
        data = json.loads(json.dumps({}))
        #使data转换成json对象
        jsonString = json.loads(jsonString)
        keys1 = jsonString.keys()
        for key1 in keys1:
            if (jsonKey in str(jsonString[key1])):
                keys2 = jsonString[key1].keys()
                for key2 in keys2:
                    if (jsonKey in str(jsonString[key1][key2]) ):
                        response = jsonString[key1][key2][jsonKey]
                        # if(jsonKeyObject !=None and jsonKeyObject in str(jsonString[key1][key2])):
                        #     data[jsonString[key1][key2][jsonKeyObject]] = jsonString[key1][key2][jsonKey]
                        keys3 = jsonString[key1][key2]
                        for key3 in keys3:
                            if key3 ==jsonKey:
                                print(jsonString[key1][key2][jsonKey])

    else:
        response = "传入的key在json中没有体现，请检查json数据"
        print("传入的key在json中没有体现，请检查json数据")
    if (jsonKeyObject !=None):
        return data
    else:
        return response


#用来获取json里特殊字段的数据
#默认是三层数据接口
#如果是列表数据需要传入jsonkeyobject，返回data数据,如果不是列表，直接返回value值
# def getStringFromJson12(jsonString, jsonKey,jsonKeyObject=None):
#     if (jsonKey in jsonString and type(jsonString) != type({}) and type(jsonString) != type([])):
#         response = ""
#         jsonString = json.loads(jsonString)

    #根据key从里面获取数据，单独提出来的数据
def getValueFromKey(jsonKey,jsonString):
    if (jsonKey in jsonString and type(jsonString) != type({}) and type(jsonString) != type([])):
        jsonString = json.loads(jsonString)
        if jsonKey in jsonString.keys():
            return jsonString[jsonKey]
        elif jsonKey in jsonString:
            return "True"
        else:
            return "false"



if __name__ == '__main__':
    jsonString = "{\"uuid\":\"369b7c36a99d4f27b48b6d96f01346a5\",\"statusCode\":200,\"message\":\"成功\",\"data\":{\"230567134\":{\"paimaiId\":230567134,\"skuId\":10025909072224,\"currentPrice\":0.0,\"auctionStatus\":2,\"accessNumber\":2,\"startTime\":1609734180000,\"endTime\":1609747380000,\"bidCount\":0,\"title\":\"黑檀+铜艺茶道茶盘摆件90-40-5cm\",\"productImage\":\"jfs/t1/165793/18/209/446260/5fed97a4Eb4d65248/70241121fd02ae45.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1100.0,\"startPrice\":0.0,\"remainTime\":-1,\"discountPrice\":1.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1},{\"id\":1007,\"name\":\"产业带\",\"type\":2,\"showType\":1,\"showOrder\":7,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":593195,\"paimaiResultStatus\":1,\"jdPrice\":1.0,\"currentPriceFormat\":\"0.00\",\"currentPriceWithUnit\":\"0\",\"startPriceWithUnit\":\"0\",\"startPriceFormat\":\"0.00\"},\"230941632\":{\"paimaiId\":230941632,\"skuId\":10023282181385,\"currentPrice\":499.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746118000,\"endTime\":1609747378000,\"bidCount\":0,\"title\":\"【正宝 印度小叶紫檀】拆房老料满金星高密度8mm佛珠手串（附国检鉴定证书）\",\"productImage\":\"jfs/t1/63865/34/13557/321206/5dafd409E255dbbc8/2660830e592226e9.jpg\",\"displayStatus\":1,\"priceLowerOffset\":10.0,\"startPrice\":499.0,\"remainTime\":-1,\"discountPrice\":9.999995E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":765685,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"499.00\",\"currentPriceWithUnit\":\"499\",\"startPriceWithUnit\":\"499\",\"startPriceFormat\":\"499.00\"},\"230961537\":{\"paimaiId\":230961537,\"skuId\":10025744443968,\"currentPrice\":200.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746783000,\"endTime\":1609747383000,\"bidCount\":0,\"title\":\"车丽友 适用于大众cc脚垫全包围汽车专车专用2021款20-10 红色\",\"productImage\":\"jfs/t1/145616/3/19821/543449/5fe318c7E6de6c319/1bde653220fd190a.png\",\"displayStatus\":1,\"priceLowerOffset\":10.0,\"startPrice\":200.0,\"remainTime\":-1,\"discountPrice\":68.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10425730,\"paimaiResultStatus\":1,\"jdPrice\":268.0,\"currentPriceFormat\":\"200.00\",\"currentPriceWithUnit\":\"2E+2\",\"startPriceWithUnit\":\"2E+2\",\"startPriceFormat\":\"200.00\"},\"230870151\":{\"paimaiId\":230870151,\"skuId\":10024947783064,\"currentPrice\":0.0,\"auctionStatus\":2,\"accessNumber\":1,\"startTime\":1609743781000,\"endTime\":1609747381000,\"bidCount\":0,\"title\":\"紫光檀描金工艺中国象棋摆件5.8cm\",\"productImage\":\"jfs/t1/130375/1/18098/321863/5fc5e59dE443308f8/e52317c3a6fd12b9.jpg\",\"displayStatus\":1,\"priceLowerOffset\":800.0,\"startPrice\":0.0,\"remainTime\":-1,\"discountPrice\":1.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1},{\"id\":1007,\"name\":\"产业带\",\"type\":2,\"showType\":1,\"showOrder\":7,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":593195,\"paimaiResultStatus\":1,\"jdPrice\":1.0,\"currentPriceFormat\":\"0.00\",\"currentPriceWithUnit\":\"0\",\"startPriceWithUnit\":\"0\",\"startPriceFormat\":\"0.00\"},\"230936069\":{\"paimaiId\":230936069,\"skuId\":10023282188868,\"currentPrice\":660.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746008000,\"endTime\":1609747448000,\"bidCount\":0,\"title\":\"正宗尼泊尔七瓣姜黄皮爆肉沉水20mm金刚菩提手串9d111-3\",\"productImage\":\"jfs/t1/48403/13/5452/222729/5d329291E6b107a90/1bc8105c62354621.jpg\",\"displayStatus\":1,\"priceLowerOffset\":20.0,\"startPrice\":660.0,\"remainTime\":-1,\"discountPrice\":9.99999339E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":765685,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"660.00\",\"currentPriceWithUnit\":\"6.6E+2\",\"startPriceWithUnit\":\"6.6E+2\",\"startPriceFormat\":\"660.00\"},\"229297805\":{\"paimaiId\":229297805,\"skuId\":10025914909355,\"currentPrice\":2311.0,\"auctionStatus\":2,\"accessNumber\":94,\"startTime\":1609695000000,\"endTime\":1609749686000,\"bidCount\":22,\"title\":\"【全新未拆封 】华为荣耀30 5G青春版6+128G超级新品颜色随机发\",\"productImage\":\"jfs/t1/120906/8/17927/86182/5fa7fd38Eaa608cc0/2947d78e61f261e0.jpg\",\"displayStatus\":1,\"priceLowerOffset\":5.0,\"startPrice\":1.0,\"remainTime\":-1,\"discountPrice\":-2310.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":784645,\"paimaiResultStatus\":6,\"jdPrice\":1.0,\"currentPriceFormat\":\"2311.00\",\"currentPriceWithUnit\":\"2311\",\"startPriceWithUnit\":\"1\",\"startPriceFormat\":\"1.00\"},\"230942756\":{\"paimaiId\":230942756,\"skuId\":10023387710093,\"currentPrice\":136.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746164000,\"endTime\":1609747484000,\"bidCount\":0,\"title\":\"【正宝 印度小叶紫檀 】老料高密度12mm竹节手串9k11\",\"productImage\":\"jfs/t1/149385/28/11623/99625/5f903ba1Ecfbb7394/9b569b351301bd05.jpg\",\"displayStatus\":1,\"priceLowerOffset\":5.0,\"startPrice\":136.0,\"remainTime\":-1,\"discountPrice\":9.99999863E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":0,\"auctionType\":5,\"currentNum\":1,\"vendorId\":765685,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"136.00\",\"currentPriceWithUnit\":\"136\",\"startPriceWithUnit\":\"136\",\"startPriceFormat\":\"136.00\"},\"230926251\":{\"paimaiId\":230926251,\"skuId\":10025820784225,\"currentPrice\":2.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609745642000,\"endTime\":1609747442000,\"bidCount\":0,\"title\":\"威麦驰 狗零食牛肉棒/牛肉粒幼成犬通用型训犬奖励零食 100g 单罐装\",\"productImage\":\"jfs/t1/149017/30/12855/101196/5f9fda18E43155660/ae84a72248410560.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1.0,\"startPrice\":2.0,\"remainTime\":-1,\"discountPrice\":5.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10515510,\"paimaiResultStatus\":1,\"jdPrice\":7.0,\"currentPriceFormat\":\"2.00\",\"currentPriceWithUnit\":\"2\",\"startPriceWithUnit\":\"2\",\"startPriceFormat\":\"2.00\"},\"230926027\":{\"paimaiId\":230926027,\"skuId\":10025997012406,\"currentPrice\":1698.0,\"auctionStatus\":2,\"accessNumber\":2,\"startTime\":1609745640000,\"endTime\":1609747440000,\"bidCount\":0,\"title\":\"【二手9成新】联想Thinkpad X1 Carbon超极本14寸笔记本电脑 超薄商务X1C2018 T440S i7 8G内存 500G机械硬盘\",\"productImage\":\"jfs/t1/7122/1/27/204172/5bc88b07E639fec9b/326a36131a9e9b59.jpg\",\"displayStatus\":1,\"priceLowerOffset\":20.0,\"startPrice\":1698.0,\"remainTime\":-1,\"discountPrice\":401.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":758426,\"paimaiResultStatus\":1,\"jdPrice\":2099.0,\"currentPriceFormat\":\"1698.00\",\"currentPriceWithUnit\":\"1698\",\"startPriceWithUnit\":\"1698\",\"startPriceFormat\":\"1698.00\"},\"230967950\":{\"paimaiId\":230967950,\"skuId\":10025903098684,\"currentPrice\":9.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609747082000,\"endTime\":1609747382000,\"bidCount\":0,\"title\":\"山东利康 碘伏消毒液喷雾剂100ml/瓶消毒液碘酊伤口消毒便携 红色\",\"productImage\":\"jfs/t1/130143/15/5669/157307/5f223373Ee2061cb4/466211d680f64ced.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1.0,\"startPrice\":9.0,\"remainTime\":-1,\"discountPrice\":3.9,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10401805,\"paimaiResultStatus\":1,\"jdPrice\":12.9,\"currentPriceFormat\":\"9.00\",\"currentPriceWithUnit\":\"9\",\"startPriceWithUnit\":\"9\",\"startPriceFormat\":\"9.00\"},\"230946249\":{\"paimaiId\":230946249,\"skuId\":10022980871894,\"currentPrice\":1480.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746302000,\"endTime\":1609747382000,\"bidCount\":0,\"title\":\"连年有余 新疆玉雕工艺师郭磊 和田玉 羊脂玉 连年有余  挂件 重49.556克 璞玉之都\",\"productImage\":\"jfs/t1/114577/31/1941/540122/5e9d2ad0Efe7cace7/512351de7c696cee.jpg\",\"displayStatus\":1,\"priceLowerOffset\":45.0,\"startPrice\":1480.0,\"remainTime\":-1,\"discountPrice\":0.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":735713,\"paimaiResultStatus\":1,\"jdPrice\":1480.0,\"currentPriceFormat\":\"1480.00\",\"currentPriceWithUnit\":\"1.48E+3\",\"startPriceWithUnit\":\"1.48E+3\",\"startPriceFormat\":\"1480.00\"},\"230982410\":{\"paimaiId\":230982410,\"skuId\":10025901686527,\"currentPrice\":4.9,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609747288000,\"endTime\":1609747468000,\"bidCount\":0,\"title\":\"家来纳 垃圾袋 草绿色\",\"productImage\":\"jfs/t1/152834/19/5766/485584/5facc5c9E0cb3226f/bbc780a07d2349e2.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1.0,\"startPrice\":4.9,\"remainTime\":-1,\"discountPrice\":5.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10560621,\"paimaiResultStatus\":1,\"jdPrice\":9.9,\"currentPriceFormat\":\"4.90\",\"currentPriceWithUnit\":\"4.9\",\"startPriceWithUnit\":\"4.9\",\"startPriceFormat\":\"4.90\"},\"230948275\":{\"paimaiId\":230948275,\"skuId\":10024023719160,\"currentPrice\":3680.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746361000,\"endTime\":1609747441000,\"bidCount\":0,\"title\":\"守护大业 省级玉雕大师顾健 和田玉羊脂玉 守护大业 手把件 重182.6836克 璞玉之都\",\"productImage\":\"jfs/t1/149696/14/13209/203843/5fa2c5d7E3b0e623a/aa3859c29d07b968.jpg\",\"displayStatus\":1,\"priceLowerOffset\":88.0,\"startPrice\":3680.0,\"remainTime\":-1,\"discountPrice\":0.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":735713,\"paimaiResultStatus\":1,\"jdPrice\":3680.0,\"currentPriceFormat\":\"3680.00\",\"currentPriceWithUnit\":\"3.68E+3\",\"startPriceWithUnit\":\"3.68E+3\",\"startPriceFormat\":\"3680.00\"},\"230943345\":{\"paimaiId\":230943345,\"skuId\":10024719089039,\"currentPrice\":360.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746185000,\"endTime\":1609747445000,\"bidCount\":0,\"title\":\"正宝橄榄核雕招财貔貅手串21138\",\"productImage\":\"jfs/t1/137318/18/17028/395684/5fbca948Ed25c86e9/29ad01e0c1531029.jpg\",\"displayStatus\":1,\"priceLowerOffset\":10.0,\"startPrice\":360.0,\"remainTime\":-1,\"discountPrice\":9.99999639E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1}],\"publishSource\":5,\"delayedTime\":0,\"auctionType\":5,\"currentNum\":1,\"vendorId\":765685,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"360.00\",\"currentPriceWithUnit\":\"3.6E+2\",\"startPriceWithUnit\":\"3.6E+2\",\"startPriceFormat\":\"360.00\"},\"230962384\":{\"paimaiId\":230962384,\"skuId\":10025941076023,\"currentPrice\":1.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746812000,\"endTime\":1609747412000,\"bidCount\":0,\"title\":\"OLO 玻尿酸避孕套超薄男用安全套水溶免洗无硅油情趣廷时套套夫妻房事性用品 成人用品 红色\",\"productImage\":\"jfs/t1/144241/38/14382/80866/5faf8862E19036156/41f3edd48a8cd5be.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1.0,\"startPrice\":1.0,\"remainTime\":-1,\"discountPrice\":58.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10520232,\"paimaiResultStatus\":1,\"jdPrice\":59.0,\"currentPriceFormat\":\"1.00\",\"currentPriceWithUnit\":\"1\",\"startPriceWithUnit\":\"1\",\"startPriceFormat\":\"1.00\"},\"230981489\":{\"paimaiId\":230981489,\"skuId\":10025964661732,\"currentPrice\":15.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609747259000,\"endTime\":1609747379000,\"bidCount\":0,\"title\":\"【券99-50元】 初醉之家潮汕手打火锅丸子潮汕牛肉丸火锅食材牛筋丸火锅丸料 生鲜 浅紫色\",\"productImage\":\"jfs/t1/110108/1/13985/330572/5ea44482E31ae1b99/6974418492a7aa83.jpg\",\"displayStatus\":1,\"priceLowerOffset\":1.0,\"startPrice\":15.0,\"remainTime\":-1,\"discountPrice\":64.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10345532,\"paimaiResultStatus\":1,\"jdPrice\":79.0,\"currentPriceFormat\":\"15.00\",\"currentPriceWithUnit\":\"15\",\"startPriceWithUnit\":\"15\",\"startPriceFormat\":\"15.00\"},\"230943349\":{\"paimaiId\":230943349,\"skuId\":10024599791412,\"currentPrice\":138.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746185000,\"endTime\":1609747445000,\"bidCount\":0,\"title\":\"正宝海南星月菩提8*10mm多圈手串念珠21107-10\",\"productImage\":\"jfs/t1/123608/13/19621/181694/5fb79570E9cf0b85e/bdf9af73ec83ac50.jpg\",\"displayStatus\":1,\"priceLowerOffset\":5.0,\"startPrice\":138.0,\"remainTime\":-1,\"discountPrice\":9.99999861E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1}],\"publishSource\":5,\"delayedTime\":0,\"auctionType\":5,\"currentNum\":1,\"vendorId\":765685,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"138.00\",\"currentPriceWithUnit\":\"138\",\"startPriceWithUnit\":\"138\",\"startPriceFormat\":\"138.00\"},\"230945461\":{\"paimaiId\":230945461,\"skuId\":10022981148268,\"currentPrice\":8888.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609746261000,\"endTime\":1609747461000,\"bidCount\":0,\"title\":\"泸州老窖国窖1573 52度高度浓香型2.5L白酒曾娜勾调定制收藏酒【巴巴邀久Z】\",\"productImage\":\"jfs/t1/129271/13/15695/202084/5f8f8b40Ecaca00fd/690c294d9bdf42db.jpg\",\"displayStatus\":1,\"priceLowerOffset\":50.0,\"startPrice\":8888.0,\"remainTime\":-1,\"discountPrice\":9.99991111E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1}],\"publishSource\":5,\"delayedTime\":0,\"auctionType\":5,\"currentNum\":1,\"vendorId\":10420408,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"8888.00\",\"currentPriceWithUnit\":\"8888\",\"startPriceWithUnit\":\"8888\",\"startPriceFormat\":\"8888.00\"},\"230886201\":{\"paimaiId\":230886201,\"skuId\":10022979691048,\"currentPrice\":1299.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609744323000,\"endTime\":1609747383000,\"bidCount\":0,\"title\":\"省级玉雕大师闫小波作品 和田玉羊脂玉观音 料细白润 普度众生 45.756克 新疆润钰福祥\",\"productImage\":\"jfs/t1/101586/23/6774/554022/5df738bbE9059ecd0/516ce475360a8aa1.jpg\",\"displayStatus\":1,\"priceLowerOffset\":50.0,\"startPrice\":1299.0,\"remainTime\":-1,\"discountPrice\":0.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1},{\"id\":1007,\"name\":\"产业带\",\"type\":2,\"showType\":1,\"showOrder\":7,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":173765,\"paimaiResultStatus\":1,\"jdPrice\":1299.0,\"currentPriceFormat\":\"1299.00\",\"currentPriceWithUnit\":\"1299\",\"startPriceWithUnit\":\"1299\",\"startPriceFormat\":\"1299.00\"},\"229298004\":{\"paimaiId\":229298004,\"skuId\":10025915012022,\"currentPrice\":1851.0,\"auctionStatus\":2,\"accessNumber\":99,\"startTime\":1609695000000,\"endTime\":1609749568000,\"bidCount\":21,\"title\":\"【全新未拆封】vivo Z6双模5G全网通44W闪充手机6+128G颜色随机发\",\"productImage\":\"jfs/t1/136227/18/14996/587174/5fa65c75E69b08814/bdeb2ad8343606eb.png\",\"displayStatus\":1,\"priceLowerOffset\":5.0,\"startPrice\":1.0,\"remainTime\":-1,\"discountPrice\":-1850.0,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":5,\"auctionType\":5,\"currentNum\":1,\"vendorId\":784645,\"paimaiResultStatus\":6,\"jdPrice\":1.0,\"currentPriceFormat\":\"1851.00\",\"currentPriceWithUnit\":\"1851\",\"startPriceWithUnit\":\"1\",\"startPriceFormat\":\"1.00\"},\"230887836\":{\"paimaiId\":230887836,\"skuId\":10025285185674,\"currentPrice\":5688.0,\"auctionStatus\":2,\"accessNumber\":0,\"startTime\":1609744382000,\"endTime\":1609747382000,\"bidCount\":0,\"title\":\"和田玉 羊脂白玉手镯 73.7570克 内径59.1mm 新疆润钰福祥\",\"productImage\":\"jfs/t1/131201/5/19424/171819/5fd1b079Ed2f06a1b/fec9e384e7789eb6.jpg\",\"displayStatus\":1,\"priceLowerOffset\":88.0,\"startPrice\":5688.0,\"remainTime\":-1,\"discountPrice\":9.99994311E8,\"labelList\":[{\"id\":1011,\"name\":\"京英店铺\",\"type\":3,\"showType\":1,\"showOrder\":5,\"associateType\":1,\"specialType\":2,\"status\":1},{\"id\":1018,\"name\":\"源头好货\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1},{\"id\":1007,\"name\":\"产业带\",\"type\":2,\"showType\":1,\"showOrder\":7,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":0,\"auctionType\":5,\"currentNum\":1,\"vendorId\":173765,\"paimaiResultStatus\":1,\"jdPrice\":9.99999999E8,\"currentPriceFormat\":\"5688.00\",\"currentPriceWithUnit\":\"5688\",\"startPriceWithUnit\":\"5688\",\"startPriceFormat\":\"5688.00\"},\"230970203\":{\"paimaiId\":230970203,\"skuId\":100015940856,\"currentPrice\":119.0,\"auctionStatus\":2,\"accessNumber\":8,\"startTime\":1609747155000,\"endTime\":1609747455000,\"bidCount\":0,\"title\":\"艾美特（Airmate）取暖器/电暖器家用/电暖气 姆明联名同款立卧两用机械款 WP20-X17P-2\",\"productImage\":\"jfs/t1/147665/2/8989/109829/5f69efebEdb5362d3/f8709a9b0b3d4789.jpg\",\"displayStatus\":1,\"priceLowerOffset\":2.0,\"startPrice\":119.0,\"remainTime\":-1,\"discountPrice\":10.0,\"labelList\":[{\"id\":1001,\"name\":\"夺宝捡漏\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1},{\"id\":1020,\"name\":\"自营\",\"type\":1,\"showType\":1,\"showOrder\":6,\"associateType\":1,\"specialType\":1,\"status\":1}],\"publishSource\":5,\"delayedTime\":1,\"auctionType\":5,\"currentNum\":1,\"vendorId\":1000001414,\"paimaiResultStatus\":1,\"jdPrice\":129.0,\"currentPriceFormat\":\"119.00\",\"currentPriceWithUnit\":\"119\",\"startPriceWithUnit\":\"119\",\"startPriceFormat\":\"119.00\"}},\"datas\":[],\"code\":0}"
    str123 = getStringFromJson(jsonString, "title","paimaiId")
    print(str123)
