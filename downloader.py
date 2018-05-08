from urllib.request import urlretrieve
import os

def create_directory(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def downloader(urlarray):
    foldername = urlarray[0].split('/')[-1]
    urlarray.pop(0)
    create_directory(foldername)
    download_directory = foldername+"/"
    count = 0
    for link in urlarray:
        filename = download_directory+str(count)+".jpg"
        urlretrieve(link,filename)
        print("{} is successfully downloaded".format(link))
        count+=1