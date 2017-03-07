import urllib.request
from bs4 import BeautifulSoup

prompt = "\n>"
print ("Enter the start page URL.")
page= input(prompt)
print ("Enter how many pages you'd like to extract.")
endpage = int(input(prompt))
print ("Enter the destination text file name.")
outputfile = input(prompt)


#start loop for scraping pages

for n in range(1,endpage):

#query website and get html to variable page 1

    page1raw = urllib.request.urlopen(page)

#scrape the content

    soup = BeautifulSoup(page1raw, "lxml")
    print (page1raw)
    page1text = soup.find("div", {"class":"post-body entry-content"})

#push cleaned content to output file

    with open(outputfile,"a") as text_file:
        print(page1text.text, file=text_file)
        print(soup.title.string, file=text_file)

#move to next page

    nextpagelink = soup.find('a', href=True, text='Next Page')
    page = nextpagelink['href']
    print (soup.title.string,"    ",n * 100 / endpage,"%","\n")
#close (outputfile)
print ("Completed")
