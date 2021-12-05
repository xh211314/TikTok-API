#Created by FrogCode

#Credits
#https://www.codenong.com/cs109390694/
#https://github.com/szdc/tiktok-api

import hashlib
import time
import requests
from urllib.parse import urlparse
import json
from bs4 import BeautifulSoup

class TTAPI:
    def __init__(self):
        #Default device parameters
        self.deviceParams = {'os_api': '25', 'device_type': 'ONEPLUS+A3010', 'app_name': 'trill', 'version_name': '17.8.4', 'channel': 'apkpure', 'device_platform': 'android', 'iid': '7032045377013942018', 'version_code': '170804', 'device_id': '7031670777339250182', 'os_version': '7.1.1', 'aid': '1180'}
        
    #Parameter Generation======================================================================================================================================================
    def genXGorgon(self, url, cookies="", stub=""):

        byteTable1 = "D6 28 3B 71 70 76 BE 1B A4 FE 19 57 5E 6C BC 21 B2 14 37 7D 8C A2 FA 67 55 6A 95 E3 FA 67 78 ED 8E 55 33 89 A8 CE 36 B3 5C D6 B2 6F 96 C4 34 B9 6A EC 34 95 C4 FA 72 FF B8 42 8D FB EC 70 F0 85 46 D8 B2 A1 E0 CE AE 4B 7D AE A4 87 CE E3 AC 51 55 C4 36 AD FC C4 EA 97 70 6A 85 37 6A C8 68 FA FE B0 33 B9 67 7E CE E3 CC 86 D6 9F 76 74 89 E9 DA 9C 78 C5 95 AA B0 34 B3 F2 7D B2 A2 ED E0 B5 B6 88 95 D1 51 D6 9E 7D D1 C8 F9 B7 70 CC 9C B6 92 C5 FA DD 9F 28 DA C7 E0 CA 95 B2 DA 34 97 CE 74 FA 37 E9 7D C4 A2 37 FB FA F1 CF AA 89 7D 55 AE 87 BC F5 E9 6A C4 68 C7 FA 76 85 14 D0 D0 E5 CE FF 19 D6 E5 D6 CC F1 F4 6C E9 E7 89 B2 B7 AE 28 89 BE 5E DC 87 6C F7 51 F2 67 78 AE B3 4B A2 B3 21 3B 55 F8 B3 76 B2 CF B3 B3 FF B3 5E 71 7D FA FC FF A8 7D FE D8 9C 1B C4 6A F9 88 B5 E5"

        def getXGon(url, stub, cookies):
            NULL_MD5_STRING = "00000000000000000000000000000000"
            sb = ""
            if len(url) < 1:
                sb = NULL_MD5_STRING
            else:
                sb = encryption(url)
            if len(stub) < 1:
                sb += NULL_MD5_STRING
            else:
                sb += stub
            if len(cookies) < 1:
                sb += NULL_MD5_STRING
            else:
                sb += encryption(cookies)
            try:
                index = cookies.index("sessionid=")
            except:
                index = -1
            if index == -1:
                sb += NULL_MD5_STRING
            else:
                sessionid = cookies[index + 10:]
                if sessionid.__contains__(';'):
                    endIndex = sessionid.index(';')
                    sessionid = sessionid[:endIndex]
                sb += encryption(sessionid)
            return sb

        def encryption(url):
            obj = hashlib.md5()
            obj.update(url.encode("UTF-8"))
            secret = obj.hexdigest()
            return secret.lower()

        def initialize(data):
            myhex = 0
            byteTable2 = byteTable1.split(" ")
            for i in range(len(data)):
                hex1 = 0
                if i == 0:
                    hex1 = int(byteTable2[int(byteTable2[0], 16) - 1], 16)
                    byteTable2[i] = hex(hex1)
                elif i == 1:
                    temp = int("D6", 16) + int("28", 16)
                    if temp > 256:
                        temp -= 256
                    hex1 = int(byteTable2[temp - 1], 16)
                    myhex = temp
                    byteTable2[i] = hex(hex1)
                else:
                    temp = myhex + int(byteTable2[i], 16)
                    if temp > 256:
                        temp -= 256
                    hex1 = int(byteTable2[temp - 1], 16)
                    myhex = temp
                    byteTable2[i] = hex(hex1)
                if hex1 * 2 > 256:
                    hex1 = hex1 * 2 - 256
                else:
                    hex1 = hex1 * 2
                hex2 = byteTable2[hex1 - 1]
                result = int(hex2, 16) ^ int(data[i], 16)
                data[i] = hex(result)
            for i in range(len(data)):
                data[i] = data[i].replace("0x", "")
            return data

        def handle(data):
            for i in range(len(data)):
                byte1 = data[i]
                if len(byte1) < 2:
                    byte1 += '0'
                else:
                    byte1 = data[i][1] + data[i][0]
                if i < len(data) - 1:
                    byte1 = hex(int(byte1, 16) ^ int(data[i + 1], 16)).replace("0x", "")
                else:
                    byte1 = hex(int(byte1, 16) ^ int(data[0], 16)).replace("0x", "")
                byte1 = byte1.replace("0x", "")
                a = (int(byte1, 16) & int("AA", 16)) / 2
                a = int(abs(a))
                byte2 = ((int(byte1, 16) & int("55", 16)) * 2) | a
                byte2 = ((byte2 & int("33", 16)) * 4) | (int)((byte2 & int("cc", 16)) / 4)
                byte3 = hex(byte2).replace("0x", "")
                if len(byte3) > 1:
                    byte3 = byte3[1] + byte3[0]
                else:
                    byte3 += "0"
                byte4 = int(byte3, 16) ^ int("FF", 16);
                byte4 = byte4 ^ int("14", 16)
                data[i] = hex(byte4).replace("0x", "")
            return data

        def xGorgon(timeMillis, inputBytes):
            data1 = []
            data1.append("3")
            data1.append("61")
            data1.append("41")
            data1.append("10")
            data1.append("80")
            data1.append("0")
            data2 = input(timeMillis, inputBytes)
            data2 = initialize(data2)
            data2 = handle(data2)
            for i in range(len(data2)):
                data1.append(data2[i])

            xGorgonStr = ""
            for i in range(len(data1)):
                temp = data1[i] + ""
                if len(temp) > 1:
                    xGorgonStr += temp
                else:
                    xGorgonStr += "0"
                    xGorgonStr += temp
            return xGorgonStr

        def input(timeMillis, inputBytes):
            result = []
            for i in range(4):
                if inputBytes[i] < 0:
                    temp = hex(inputBytes[i]) + ''
                    temp = temp[6:]
                    result.append(temp)
                else:
                    temp = hex(inputBytes[i]) + ''
                    result.append(temp)
            for i in range(4):
                result.append("0")
            for i in range(4):
                if inputBytes[i + 32] < 0:
                    result.append(hex(inputBytes[i + 32]) + '')[6:]
                else:
                    result.append(hex(inputBytes[i + 32]) + '')
            for i in range(4):
                result.append("0")
            tempByte = hex(int(timeMillis)) + ""
            tempByte = tempByte.replace("0x", "")
            for i in range(4):
                a = tempByte[i * 2:2 * i + 2]
                result.append(tempByte[i * 2:2 * i + 2])
            for i in range(len(result)):
                result[i] = result[i].replace("0x", "")
            return result

        def strToByte(str):
            length = len(str)
            str2 = str
            bArr = []
            i = 0
            while i < length:
                a = str2[i]
                b = str2[1 + i]
                c = ((str2hex(a) << 4) + str2hex(b))
                bArr.append(c)
                i += 2
            return bArr

        def str2hex(s):
            odata = 0;
            su = s.upper()
            for c in su:
                tmp = ord(c)
                if tmp <= ord('9'):
                    odata = odata << 4
                    odata += tmp - ord('0')
                elif ord('A') <= tmp <= ord('F'):
                    odata = odata << 4
                    odata += tmp - ord('A') + 10
            return odata

        params = url[url.index('?') + 1:]
        s = getXGon(params, stub, cookies)
        ts = str(time.time()).split(".")[0]
        gorgon = xGorgon(ts, strToByte(s))
        return gorgon

    def genXKhronos(self):
        ts = str(time.time()).split(".")[0]
        return ts

    def genXSSReqTicket(self):
        _rticket = str(time.time() * 1000).split(".")[0]
        return _rticket
    
    #TikTok API sign + request======================================================================================================================================================
    def dict2Query(self, dict):
        query = ""
        for param in dict:
            query += ("&"+param+"="+dict[param])
        query = query[1:]
        return query
    
    def signUrl(self, url, deviceParams):
        #Create query of device parameters
        paramQuery = self.dict2Query(deviceParams)

        #Create full url
        parsedUrl = urlparse(url)
        
        if parsedUrl.scheme == "":
            parsedUrl = urlparse("https://"+url)
        
        if parsedUrl.query == "":
            fullUrl = url+"?"+paramQuery+"&_rticket="+self.genXSSReqTicket()
        else:
            fullUrl = url+"&"+paramQuery+"&_rticket="+self.genXSSReqTicket()
    
        #Generate XGorgon + XKhronos
        XGorgon = self.genXGorgon(fullUrl)
        XKhronos = self.genXKhronos()
        
        #Generate headers
        headers = {
        "x-gorgon": XGorgon,
        "method": "GET",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.10.0.1",
        "x-khronos": XKhronos
        }
        
        #Return signed url + headers
        signed = {'url':fullUrl, 'headers':headers}
        
        return signed
        
    def TTAPIRequest(self, path, queryDict, deviceParams):
        url = "https://api-h2.tiktokv.com"+path+"?"+self.dict2Query(queryDict)
        #Sign
        signed = self.signUrl(url, deviceParams)
        #Request
        request = requests.get(signed['url'], headers=signed['headers'])
        try:
            response = request.json()
            return response
        except:
            return {} #Error

    def TTNEXTDATA(self, url):
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            }
            html = requests.get(url, headers=headers).text
            htmlParsed = BeautifulSoup(html, "html.parser")
            script = htmlParsed.find("script", id="__NEXT_DATA__")
            NEXT_DATA = script.contents[0]
            return json.loads(NEXT_DATA)
        except:
            return {} #Error
    
    #Device parameters======================================================================================================================================================
    def getDeviceParams(self, paramUrl):
        queryList = urlparse(paramUrl).query.split('&')
        
        fullParams = {}
        for queryObj in queryList:
            fullParams[queryObj.split("=")[0]]=queryObj.split("=")[1]
            
        requiredParams = ["os_api","device_type","app_name","version_name","channel","device_platform","iid","version_code","device_id","os_version","aid"]
        
        #Check if all needed parameters are available
        if (False in [param in list(fullParams.keys()) for param in requiredParams]):
            return {}
        else:
            params = {}
            for param in requiredParams:
                params[param]=fullParams[param]
                
            return params
            
    def setDeviceParams(self, deviceParams):
        self.deviceParams = deviceParams
    
    #TikTok API Methods======================================================================================================================================================
    def getPost(self, id): #Gets a post.
        return self.TTAPIRequest("/aweme/v1/aweme/detail/",{'aweme_id':id},self.deviceParams)

    def listComments(self, id, amount): #Lists comments for a post.
        return self.TTAPIRequest("/aweme/v1/comment/list/",{'aweme_id':id,"count":amount},self.deviceParams)
    
    def getUser(self, id): #Gets a user's profile.
        return self.TTAPIRequest("/aweme/v1/user/",{'user_id':id},self.deviceParams)

    def listPosts(self, id): #Lists a user's posts.
        return self.TTAPIRequest("/aweme/v1/aweme/post/",{'user_id':id},self.deviceParams)

    def listFollowers(self, id): #Lists the users that follow the specified user.
        return self.TTAPIRequest("/aweme/v1/user/follower/list/",{'user_id':id},self.deviceParams)

    def listFollowing(self, id): #Lists the users that the specified user follows.
        return self.TTAPIRequest("/aweme/v1/user/following/list/",{'user_id':id},self.deviceParams)

    #ID finder======================================================================================================================================================
    def getPostId(self, url):
        #Sample url's:
        #https://vm.tiktok.com/abcde
        #https://vt.tiktok.com/abcde
        #https://m.tiktok.com/v/12345
        #https://tiktok.com/@user/video/12345
        
        try:
            data = self.TTNEXTDATA(url)
            return data["props"]["pageProps"]["itemInfo"]["itemStruct"]["id"]
        except:
            return "" #Error
        
    def getUserId(self, url):
        try:
            data = self.TTNEXTDATA(url)
            return data["props"]["pageProps"]["itemInfo"]["itemStruct"]["author"]["id"]
        except:
            return "" #Error
