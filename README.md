# learning-web-scrapping


### HTML PAGE

* Simplist method for basic pages
* Request to get page
* BeautifulSoup to parse the HTML data
* View Source
* HTML Tables
* Pagination by changing URLs

### Dealing with Logins

* Useful for business systems
* Inspect element -> Network tab
* Login manually look to where the login data is being sent.
* Replicate with Requests in Python.
* Use Session () to remain logged in

### Rendering JavaScript
* Modern websites use JS to dynamically load data.
* Scripts must be loaded by a browser
* Requests-html and Render() runs Chromium in the background to exec scripts
* Has a HTML parser we can use to collect data.

### API Endpoints
* Requires more investigation
* Skip out rendering the page data and get it from the source. 
* Network tab -> XHR find JSON data 
* Replicate and change in API program like Postman or Insomnia 
* Download with requests and JSON module

### Selenium, Browser Automation and Helium
* Use selenium control the browser. 
* Not ideal solution, slow and resource heavy. 
* Can be used to click buttons and write in text boxes. 
* Get data from Elements or download rendered html source. 
* scroll and load dynamic Elements

### Legality and Other Notes
* Can be a grey area. 
* Scrape only publically available data. 
* Check your countries laws. 
* Obey robots.txt 
* Anti bot measures 
* Don't spam requests to other peoples servers 
* Use APIs where available

## Web Scraping Tips 1

**INVESTIGATE**

* N : - **The Network Tab**: This shows all the network activity from the server to the browser and often contains the API endpoint for easy access
* I :- **Inspect Element**: The DOM and Inspect Element tools show what the browser is interpreting and is very useful for finding the elements that contain the data we want.
* S :- **View Source**: Check what your http request is actually seeing, this will give you a good idea of how you need to proceed.
* H :- **HTML**: Plan HTML still exists a lot even on the modern web, check it out it might be the best option for data extraction.

## Web Scraping Tips 2

**PARSE LOCALLY**

Saving a copy of the HTML or JSON data you are working on to you local hard drive with help you speed up parsing and data extraction without sending multiple requests to the server.

## Web Scraping Tips 3

**WRITE A PLAN**

Using pseudocode or writing out a plan/scope for your project will help you keep on track with what you are trying to achieve, and not let you get carried away spending time on things that aren’t core to the project.

## Web Scraping Tips 4

**KEEP IT SIMPLE**

Keep feature to a minimum for now. Organize you files and keep the scraper doing just that, scrapping data. Save the analysis for another PY file. Write clear and concise functions and classes where necessary.

## Web Scrapping Tips 5
**THE RIGHT TOOL**

Rendering the page or using Selenium should be the last resort! There is almost always a better way - if you did tip 1, investigate the site properly you may have found the API endpoint, or JSON in the HTML somewhere.

**Web-Scrapping using Beautiful Soup and Requests**

### Example:-

1. [Bookstoscrape](/script/Books%20Scrape.ipynb)
2. [Premier League Table](/script/Premier%20League%20Table.ipynb)
3. [Bypass Login Page](/script/Bypass%20Login%20Page.ipynb)
4. [Airbnb](/script/Airbnb.ipynb)
5. [Youtube](/script/youtube.py)
6. [Yell](/script/Yell.ipynb)
7. [Yahoo Finance](/script/Yahoo%20Finance.ipynb)
8. [Wander Lust Wine](/script/Wander%20Lust%20Wine.ipynb)
9. [Bare Foot Buttons](/script/Bare%20Foot%20Buttons.ipynb)
10. [Beerwulf](/script/Beerwulf.ipynb)
11. [Steam Using API](/script/Steam%20Using%20API.ipynb)
12. [Steam](/script/Steam.ipynb)
13. [FastestLaps](/script/FastestLaps.ipynb)
14. [Flipkart](/script/Flipkart.ipynb)
15. [Google News](/script/Google%20News.ipynb)
16. [Hockey](/script/Hockey.ipynb)
17. [Mozilla Blog](/script/Mozilla%20Blog.ipynb)
18. [Rei](/script/Rei.ipynb)
19. [Roting Proxies](script/Roting%20Proxies.ipynb)
20. [Stackoverflow](/script/Stackoverflow.ipynb)
