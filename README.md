# GoGoAnimeDownloader
Python code to download entire Anime serie episodes.
In the GUI versiont (gui-anime-download.py) you can select the destination folder,
and a single episode to be downloaded

### Usage
0. Paste the ID of the anime from GoGoAnime
1. Click on Get Info
2. Click on Destination Folder selection
3. Optional: if you want to download a single episode click on button 3.Select episode
4. Use button **Download Anime** (for all episode), or **Download episode** (for the selected episode)
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

## Required Libraries for GUI
```python
import tkinter as tk
from tkinter import filedialog, simpledialog
import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import io
from PIL import Image, ImageTk
import requests
import os
from io import BytesIO
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
- [x] Create a better GUI (DONE with gui-anime-download.py )

### Additional Notes:
The Google Colab file contains also commands for moving downloaded files into 

a personal directory in Google Drive. It is for test purposes only
