# find gossiping article title and author
import requests 
from bs4 import BeautifulSoup 
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

cookies = {
    'over18' : '1'
}
resp = requests.get(url, cookies = cookies) 
soup = BeautifulSoup(resp.text, 'html5lib')
arts = soup.find_all('div', class_='r-ent')

for art in arts:
    title = art.find('div', class_='title').getText().strip()
    link = 'https://www.ptt.cc' + \
        art.find('div', class_='title').a['href'].strip()
    author = art.find('div', class_='author').getText().strip()
    print(f'title: {title}\nlink: {link}\nauthor: {author}')

'''
title: Re: [問卦] 有紋身的人瘦下來圖案會有變化嗎?
link: https://www.ptt.cc/bbs/Gossiping/M.1710574056.A.550.html
author: Phoenix723
title: [問卦] 35歲男不婚不生放假只能在家打手槍正常嗎?
link: https://www.ptt.cc/bbs/Gossiping/M.1710574269.A.D4A.html
author: zrct5566
title: [問卦] 台塑集團企業轉型改賣牛排有搞頭嗎       
link: https://www.ptt.cc/bbs/Gossiping/M.1710574303.A.3B4.html
author: BlueBird5566
title: Re: [問卦] 台灣是進入價值觀重整了嗎？
link: https://www.ptt.cc/bbs/Gossiping/M.1710574315.A.3F0.html
author: ilw4e
title: [新聞] 雪碧脫口「網美吸麻不是沒原因」！ 抗壓  
link: https://www.ptt.cc/bbs/Gossiping/M.1710574588.A.547.html
author: Marle
title: Re: [問卦] 35歲男不婚不生放假只能在家打手槍正 常嗎?
link: https://www.ptt.cc/bbs/Gossiping/M.1710574680.A.21C.html
author: b122771
title: [問卦] 臉書被砲幾天會想關閉
link: https://www.ptt.cc/bbs/Gossiping/M.1710574747.A.974.html
author: CenaC
title: Re: [問卦] 碳權到底是什麼
link: https://www.ptt.cc/bbs/Gossiping/M.1710574803.A.30E.html
author: pauljet
title: [公告] 八卦板板規(2023.11.11)
link: https://www.ptt.cc/bbs/Gossiping/M.1699632792.A.2CB.html
author: lwt501cx
title: [公告]～（＠ｏ＠）～三月置底閒聊區
link: https://www.ptt.cc/bbs/Gossiping/M.1709979240.A.A3A.html
author: ubcs
title: [協尋] 2024/2/28 17:00台南新市大洲1-35號      
link: https://www.ptt.cc/bbs/Gossiping/M.1709296467.A.866.html
author: jokersosmart
'''
