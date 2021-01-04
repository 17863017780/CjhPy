# -*- coding: utf-8 -*
import InterfaceRequests

if __name__ == '__main__':
    #为了增加围观数，刷的接口，方便使用，实际没有啥效果
    for i in range(0, 10):
        InterfaceRequests.requestAPI("https://mpaimai.jd.com/203248113")
        print(" start !" ,i)
    print("this is ok !")
