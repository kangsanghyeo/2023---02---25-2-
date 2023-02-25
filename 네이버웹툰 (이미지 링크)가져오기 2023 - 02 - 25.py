import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


for date in range(104, 94, -1):
      url = 'https://comic.naver.com/webtoon/detail?titleId=790713&no={0}&weekday=tue'.format(date)
      site = requests.get(url, headers=headers)
      source_data = site.text

      count = source_data.count('" title="" alt="comic content" id')

      for i in range(count):

            pos1 = source_data.find('alt="comic content" onerror=')+ len('alt="comic content" onerror=')
            source_data = source_data[pos1:]
            
            pos2 = source_data.find('<img src="')+ len('<img src="')
            source_data = source_data[pos2:]

            pos3 = source_data.find('" title="" alt="comic content" id')
            extract_data = source_data[: pos3]

            source_data = source_data[pos3+1:]
            print(i+1, extract_data)
