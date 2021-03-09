# Scraping the news site La Republica
![enter image description here](https://miro.medium.com/max/658/1*kfOsUxggG5wDbDcxgC0Uwg.png)
Hello, this project consists of having a history of news in .txt files, grouped by folders, depending on the day the script is executed.
obtaining the following information:

 - the title
 - the summary 
 - the date
 - the author

[La Republica](https://www.larepublica.co/) is one of the biggest news media in Colombia.
I will use Xpath expressions to search the texts within the page.
In this project we used these libraries:

    import requests
    import lxml.html
    import so
    import datetime
