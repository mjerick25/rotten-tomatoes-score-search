import re
import urllib2
from bs4 import BeautifulSoup

def find_media():
    media_type = raw_input('Are you asking about a movie or tv show? ')
    if (media_type.upper() == MOVIE):
        url_type = '/m/'
    elif (media_type.upper() == TV SHOW or media_type.upper() == TV):
        url_type = '/tv/
    else:
        print("I dont undertand, can you say that again?")
        find_media()
#this creates a variable that will help create the url
 
media = raw_input('Enter the movie/tv show: ') #retrieves the media name from the user
media = str(media).replace(' ', '_') #puts media in format so it_looks_like_this
url = 'http://rottentomatoes.com' + url_type + media #creates url for media
 
try:
    urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print('uh oh! try again!')
except urllib2.URLError, e:
    print('uh oh! try again!')
 
#checks if url is valid
page = urllib2.urlopen(url)
page_html = BeautifulSoup(page, 'html.parser')
#creates html info for page
 
score_box = page_html.find(attrs={'class': 'meter-value superPageFontColor'})
#finds the part of the html with the score
 
score = re.sub('[^0-9]', '', str(score_box))
#gets rid of all the non-score parts
 
print score
#prints the score for the user
