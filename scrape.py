"""
Search through all search requests from a keyword list,
then using the keyword list save to a url array.

"""
from bs4 import BeautifulSoup 
import urllib.request
import pytube
import sqlite3

#Storing key words in an array
urls = []
keywords = ["car collision", "car theft", "emergency response"]

#Declaring functions
#search videos function
def SearchVid(search):
    response = urllib.request.urlopen("https://www.youtube.com/results?search_query="+search)

    soup = BeautifulSoup(response, features = "html.parser")
    divs = soup.find_all("div",{"class": "yt-lockup-content"})

    # Search through divs 
    for i in divs:
        href= i.find('a', href=True)
        urls.append([href.text,"https://www.youtube.com"+href['href']])

#download the searched video function
def Downloader(url):
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    video.download('Videos')

for keyword in keywords:
    #reformat the space in search queries to match input
    SearchVid(keyword.replace(" ", "%20"))

#reformat video information to make inputting into database easier
video_information = []
id_counter = 0
for i in range(len(urls)):
    video_information.append((id_counter, urls[i][0],urls[i][1]))
    id_counter+=1
print(video_information)

#Table Creation to input id, title and url of videos to be downloaded
conn = sqlite3.connect('videos.db')
c = conn.cursor()
c.execute('''CREATE TABLE videos (number integer, title text, url text)''')
for i in range(len(urls)):
    c.executemany("INSERT INTO videos VALUES(?,?,?)",video_information)
conn.commit()
conn.close()

for i in range(len(urls)):
    Downloader(urls[i][1])
    print("Download " + str(i+1) + " completed!")


# User Interface -- instead of keywords can search based on input
#print("Enter Search Query")
#SearchString = input()
#SearchVid(SearchString.replace(" ", "%20"))
#Downloader(urls[0][1])




