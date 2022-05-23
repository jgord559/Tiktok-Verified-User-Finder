import requests 
import json
import random
import string

r = requests.session

def veri():
    while True:
        keyword = random.choice(string.ascii_letters)
        veriurl = f"https://api31-normal-useast1a.tiktokv.com/aweme/v1/discover/search/?count=30&cursor=0&keyword={keyword}&search_source=report_user&type=1&device_id=7100986933613987334&aid=1233"
        verihed = {
            'Host': 'api31-normal-useast1a.tiktokv.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip',
            'Cookie': 'store-idc=maliva; store-country-code=gb; install_id=7100986988781913861; ttreq=1$ce89e6d9a5add643681688dd655eb995ccee6a72; odin_tt=6033ac7df43163a318dcab32b0825d5aae93cc8f1284992068f7d640238170118a24c398358cc77a70567dc712204d3c169f416eb509091c4ac6ac2d57fb9beb9ed77febd6be1d847d1a1848f01a3076; msToken=Pvu7YImaOu3ZVFtChCYy-uhgesCf8BzYiJFOZSmuEvvgfcEYyh7hJdS54Cf4Spgd-ZRGqsCMzHJ_DJqiEWt7OSmK-4yS95GatprDruv5WtQ=',
            'Passport-Sdk-Version': '19',
            'Sdk-Version': '2',
            'User-Agent': 'com.zhiliaoapp.musically/2022405010 (Linux; U; Android 7.1.2; en; ASUS_Z01QD; Build/N2G48H;tt-ok/3.12.13.1)',
            'X-Argus': 'sJizTNGmwRp+tE8syrDcdlNCuVfmFLCXwm82BWxIS2yLprtBx8lyW8/Np+xd+nmD+wCKHGn08n/4meh9KmyclCowazyGStwN9K5oZz2TRU0x1EgnEOVmWxYUye9n0T5toAdwmvC8UbnKu9dwOHlYqpCxfKkNk2gi6fZNSwcWckfOT+e6D4QTKAWl3ruJBnU8ZbmDjR9SRqZNToWRpymWhlsknz3l4C/gGxsb3z54N7S+WGgvZEQZZJFLSOX3NQitY9E7DbHyRiaFn0BTmVB71VpwiCUZ4XFAES+S8GlkvlZQew==',
            'X-Gorgon': '0404e05f0000b0e2a26679721b10c7f1c61106a776e2841e0cb2',
            'X-Khronos': '1653327444',
            'X-Ladon': 'C5hxWz/3yjuEQKra079Z70IZizzpFq3qzJbhadux6SvCsADH',
            'X-Ss-Req-Ticket': '1653327444979',
            'X-Tt-Dm-Status': 'login=0;ct=1;rt=6',
            'X-Tt-Store-Region': 'gb',
            'X-Tt-Store-Region-Src': 'did',
            'X-Vc-Bdturing-Sdk-Version': '2.2.1.i18n'}
        verireq = requests.get(veriurl, headers=verihed)
        verijson = dict(json.loads(verireq.text))
        #print(verijson)
        total = len(verijson['user_list'])
        for i in range(total):
            verijsonlist = (verijson['user_list'][i]['user_info'])
            verilist = (verijsonlist['unique_id'])
            print(verilist)


veri()

