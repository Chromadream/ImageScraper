from get_links import get_links
from downloader import downloader
from configuration import *

def main(ROOT_URL,FIRST_FILTER,FILENAME_FILTER):
    links = get_links(ROOT_URL,FIRST_FILTER)
    all_image_array = []
    for link in links:
        images = get_links(link,FILENAME_FILTER)
        images = [link]+images[:]
        all_image_array.append(images)
    for url_array in all_image_array:
        downloader(url_array)
    print("Download complete!")


if __name__=="__main__":
    main(ROOT_URL,FIRST_FILTER,FILENAME_FILTER)