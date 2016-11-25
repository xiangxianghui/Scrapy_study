# Scrapy settings for dmoz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dmoz'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dmoz.spiders']
NEWSPIDER_MODULE = 'dmoz.spiders'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ROBORSTXT_OBEY =True
ITEM_PIPELIES={'dmoz.dmoz.pipelines.HeartsongPipeline':300,}

