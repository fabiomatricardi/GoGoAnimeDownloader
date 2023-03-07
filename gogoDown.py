import requests
import os
from tqdm import tqdm
"""
Download entire Anime serie, quality  360p, from gogoanime.
accept aas imput the id of the serie.
exapmle ANIME = BENRIYA SAITOU-SAN, ISEKAI NI IKU
gogoanime page = https://www1.gogoanime.bid/category/benriya-saitou-san-isekai-ni-iku
myidx = benriya-saitou-san-isekai-ni-iku
"""
myidx = input('Take it from GoGoAnime url: ')


# Using the example query "demon", and looking at the 2nd page of results.
url = f"https://api.consumet.org/anime/gogoanime/{myidx}"
response = requests.get(url, params={"page": 1})
search = response.json()
#print(search) #only for testing purposes

# Fetching all the informations about the selected anime.
url = f"https://api.consumet.org/anime/gogoanime/info/{myidx}"
response = requests.get(url)
info = response.json()
title =info['title']
eps = info['totalEpisodes']
idname = info['id']
print(info['title'])
print("---------------")
print(info['description'])
print("Total Num of Episodes: "+str(info['totalEpisodes']))
title = title.replace(' ','_')

#Download silent
print("Start downloading all episodes...")
"""
Using the example episode ID taken from info[id],
explicitly defining default server for demostrative purposes.
"""
for ep in tqdm(range(1,eps+1)):
    url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{ep}"
    response = requests.get(url, params={"server": "vidstreaming"})
    data = response.json()
    link = data['sources'][0]['url']
    filename=f"{title}_ep_{ep}.mp4"
    s = 'downloadm3u8 -o '+filename + ' '+link+' &> /dev/null'
    with os.popen(s):
        pass
print("completed")