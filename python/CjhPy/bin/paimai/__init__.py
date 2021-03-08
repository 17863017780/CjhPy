
# import bin.common.InterfaceRequests
#
# url="https://api.m.jd.com/api?appid=paimai&functionId=getSearchProducts&body={%22apiType%22:10,%22keyword%22:%22%E8%8B%A5%E9%A6%A8%22,%22sortField%22:12,%22paimaiStatus%22:%22%22,%22currentPriceRangeStart%22:%22%22,%22currentPriceRangeEnd%22:%22%22,%22pageSize%22:40,%22page%22:1,%22upSkuId%22:%22%22,%22attributeList%22:%22%22}"
#
# for i in range(0,3):
#     url = "https://api.m.jd.com/api?appid=paimai&functionId=getSearchProducts&body={%22apiType%22:10,%22keyword%22:%22%E8%8B%A5%E9%A6%A8%22,%22sortField%22:12,%22paimaiStatus%22:%22%22,%22currentPriceRangeStart%22:%22%22,%22currentPriceRangeEnd%22:%22%22,%22pageSize%22:40,%22page%22:"+ str(i) +",%22upSkuId%22:%22%22,%22attributeList%22:%22%22}"
#     response = bin.common.InterfaceRequests.requestAPI(url)
#     print(response)
#     if "10023073662566" in response :
#         print(i)