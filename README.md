scrapy-painting
===============

Example of simple web crawler using [scrapy.org](http://scrapy.org)

Website to crawle: [art-on-line.com.ua](http://art-on-line.com.ua)
the goal was to extract painting info like price, author, size, rating etc.

Cli command to run crawler:
scrapy crawl paint -o items.json -t json

Conversion from json to csv was done using simple open source code:
[JSON2CSV](https://github.com/danmandle/JSON2CSV)

