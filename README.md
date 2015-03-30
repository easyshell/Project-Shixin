# A Crawler based on the scrapy framework
This spider was modified by jpshuimu in order to get the dishonesty information from "http://shixin.court.gov.cn/"

As the website use javascripe to hide the real url, but the logic was quite simple. 

I use selector to choose the id from start_url and process it to yield Request.

Build a csvPipeLine to output a csv type result.

In order to speed up the download and avoid the potential ban policy, I use random user-agents.
