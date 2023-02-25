import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}



url = 'https://comic.naver.com/webtoon/list?titleId=790713&weekday=fri'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('" width="71"')

for i in range(count):

      pos1 = source_data.find('<em class="ico_store2')+ len('<em class="ico_store2')
      source_data = source_data[pos1:]

      pos1 = source_data.find('<a href="')+ len('<a href="')
      source_data = source_data[pos1:]

      pos2 = source_data.find('" onclick="nclk_v2(event,')
      a_data = source_data[: pos2]
            
      pos3 = source_data.find('" alt="')+ len('" alt="')
      source_data = source_data[pos3:]

      pos4 = source_data.find('" width="71"')
      b_data = source_data[: pos4]

      source_data = source_data[pos4+1:]
      print(i+1, a_data, b_data)
