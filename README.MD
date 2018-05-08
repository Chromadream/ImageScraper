# ImageScraper

A simple image scraping script based on urllib2 and BeautifulSoup4.

## How it works

The scraper, given a root URL, will find all links that fulfil the first filter. Each link found from the first scraping process will be scraped for the images link that fulfil the second filter.

The images will then be downloaded, and saved on separate folder based from its page URL.

<code>
Root URL (provided by user) -(first filter)-> Page URL list -(filename filter)-> image URLs -> Downloaded images
</code>

## Possible uses

Here are some possible use case that require two level of URL filtering and scraping:

* Manga site scraping

* Photo blog scraping

* Archiving

## Configuration

`configuration.py`&nbsp;specifies the URL and the filters that will be used in the scraping process.


## Requirements

* Python 3.6

* BeautifulSoup 4

* virtualenv

## TODO

* Proper test suite