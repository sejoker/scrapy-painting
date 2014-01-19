scrapy-painting
===============

Example of simple web crawler using [scrapy.org](http://scrapy.org)
website to crawle: [art-on-line.com.ua](http://art-on-line.com.ua)
the goal was to extract painting info like price, author, size, rating etc.

cli command to run crawler:
scrapy crawl paint -o items.json -t json

conversion from json to csv was done using simple open source code:
[JSON2CSV](https://github.com/danmandle/JSON2CSV)

