## Requirements
First install Python3 (https://www.python.org/downloads)

Before you can run the bot, you will need to install a few Python dependencies.
You can install the three below by doing: `pip3 install -r requirements.txt`

* [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4), for parsing html: `pip3 install BeautifulSoup4`
* [Selenium](http://www.seleniumhq.org/), for browser automation: `pip3 install Selenium`
* lxml for quicker HTML parsing: `pip3 install lxml`

You will also need the appropriate web driver that you would like as specificed in [Selenium](https://selenium-python.readthedocs.io/installation.html):
"Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow."
* Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
	* On MacOS if you have [HomeBrew](https://brew.sh) installed you can use `brew install chromedriver`
* Firefox:	https://github.com/mozilla/geckodriver/releases
	* On MacOS if you have [HomeBrew](https://brew.sh) installed you can use `brew install geckodriver`



You will need to install the [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Google Chrome then put it in the same folder than the bot if you are on Windows, or in the `/usr/bin` folder if you are on OS X.

## Configuration 

Make sure update the path of screenshot folder accorting to your computer in `imageDownloader.py` 


## Run
To run the bot go into the directory where the bot is stored and type `python3 imageDownloader.py`

Make sure you are in the correct folder 

## Output

It will download the 5 pictures in screenshots folder

