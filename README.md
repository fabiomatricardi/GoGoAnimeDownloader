# GoGoAnimeDownloader
Python code to download entire Anime serie episodes.
## References
**GitHub Repo**
> https://github.com/riimuru/gogoanime-api#how-to-get-started

**API documentation**
> https://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-linkshttps://docs.consumet.org/rest-api/Anime/gogoanime/get-anime-episode-streaming-links
---
## Required Libraries
```python
import requests
import os
from tqdm import tqdm
```

## Usage
Download entire Anime serie, quality  360p, from gogoanime.

Accept as imput the id of the serie.

```
exapmle ANIME = BENRIYA SAITOU-SAN, ISEKAI NI IKU
gogoanime page = https://www1.gogoanime.bid/category/benriya-saitou-san-isekai-ni-iku
myidx = benriya-saitou-san-isekai-ni-iku
```

When requested paste  *`benriya-saitou-san-isekai-ni-iku`*

<br>

## Next steps
Create a better GUI

### Additional Notes:
The Google Colab file contains also commands for moving downloaded files into 

a personal directory in Google Drive. It is for test purposes only
