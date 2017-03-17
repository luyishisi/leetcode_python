import requests

url = "http://xzqh.mca.gov.cn/fuzzySearch"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"fs\"\r\n\r\n%C9%BD%B6%AB\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "15",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cookie': "JSESSIONID=18FE58311DA45394282E0D4E3014B6D9",
    'host': "xzqh.mca.gov.cn",
    'origin': "http://xzqh.mca.gov.cn",
    'pragma': "no-cache",
    'referer': "http://xzqh.mca.gov.cn/fuzzySearch",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    'postman-token': "3c17a0fa-bf33-7001-f044-3955ded357ca"
    }

response = requests.request("POST", url, data=payload, headers=headers,timeout=10)
print 'begin'
print(response.text)
print 'end'
