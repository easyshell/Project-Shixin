# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class shixinItem(Item):
    # define the fields for your item here like:
    id = Field()
    iname = Field()
    caseCode = Field()
    age = Field()
    sexy = Field()
    cardNum = Field()
    courtName = Field()
    areaName = Field()
    partyTypeName = Field()
    gistId = Field()
    regDate = Field()
    gistUnit = Field()
    duty = Field()
    performance = Field()
    performedPart = Field()
    unperformPart = Field()
    disruptTypeName = Field()
    publishDate = Field()

