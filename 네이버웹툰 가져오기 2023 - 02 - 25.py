import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}



url = 'https://comic.naver.com/webtoon/list?titleId=790713&weekday=fri'
site = requests.get(url, headers=headers)
source1_data = site.text

count = source1_data.count('" width="71"')

for i in range(count):

      pos1 = source1_data.find('<em class="ico_store2')+ len('<em class="ico_store2')
      source1_data = source1_data[pos1:]

      pos2 = source1_data.find('<a href="')+ len('<a href="')
      source1_data = source1_data[pos2:]

      pos3 = source1_data.find('" onclick="nclk_v2(event,')
      a_data = source1_data[: pos3]
            
      pos4 = source1_data.find('" alt="')+ len('" alt="')
      source1_data = source1_data[pos4:]

      pos5 = source1_data.find('" width="71"')
      b_data = source1_data[: pos5]

      for date in range(104, 94, -1):
            url = 'https://comic.naver.com/webtoon/detail?titleId=790713&no={0}&weekday=tue'.format(date)
            site = requests.get(url, headers=headers)
            source2_data = site.text

            count = source2_data.count('" title="" alt="comic content" id')

            for i in range(count):

                  pos6 = source2_data.find('alt="comic content" onerror=')+ len('alt="comic content" onerror=')
                  source2_data = source2_data[pos6:]
                  
                  pos7 = source2_data.find('<img src="')+ len('<img src="')
                  source2_data = source2_data[pos7:]

                  pos8 = source2_data.find('" title="" alt="comic content" id')
                  c_data = source2_data[: pos8]

                  source2_data = source2_data[pos8+1:]
                  print(i+1, a_data, b_data, c_data)
