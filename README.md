RssRead
=======

    Version 0.2
     - Refactoring Python Style and more simple API
    Version 0.11
     - Using C implementation of Xml parser
    Version 0.1
     - Initial use of Python class

Repo for RssRead, an experimental rss reader. 
[Python module feedparser is required.]

It's a module you can use with a 

    import RssRead as feed

and then use the News peoperty to get the news

    rss = feed.RssRead() 
    rss.loadNewsRss(NAME)
        for news in rss.News:
            pass
 
In NAME you can use any of the configured* site.
You can, of course, use multiple RssReader on the same program.
Or you can load more news with the same istance (using each time loadNewsRss())
Use the News object bearing in mind that it's already in a Xthml Link format.



*You can add/remove sites you con use the following syntax

    rss + ['sito', 'url']
    rss - 'sito'
    

Enjoy :)
