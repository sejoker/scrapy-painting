from scrapy.item import Item, Field

class PaintItem(Item):
	paintType = Field()
	title = Field()
   	material = Field()
    	width = Field()
    	height = Field()
    	author = Field()
    	price = Field()
    	status = Field()
    	description = Field()
    	rating = Field()
    	url = Field()
