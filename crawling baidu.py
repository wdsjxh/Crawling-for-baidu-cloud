import urllib
import urllib.request
import webbrowser  
import re
def yunpan_search(key):
    keyword = key
    keyword = keyword.encode('utf-8')
    keyword = urllib.request.quote(keyword)
    url = "http://www.wangpansou.cn/s.php?q="+keyword+"&wp=0&start=0"
    #webbrowser.open(url) 
    req = urllib.request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
    opener = urllib.request.urlopen(req)
    html = opener.read()
    html = html.decode('utf-8')
    rex = r'https?://pan.baidu.com.*\?uk=[0-9]{10}.*[\d+?]"'
    m = re.findall(rex,html)
    f = open('d:/1213.txt','w')
    for i in m:
        f.write(i)
        f.write('\n\n')
    f.close();
    print("success!")
     
 
if __name__=='__main__':
    print('crawling for baidu cloud')
    key = input('what do you want to search:')
    yunpan_search(key)
