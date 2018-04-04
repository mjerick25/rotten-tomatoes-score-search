import re
import urllib2
from bs4 import BeautifulSoup
 
movie = raw_input('Enter the movie: ') #retrieves the movie from the user
movie = str(movie).replace(' ', '_') #puts movie in format so it_looks_like_this
url = 'http://rottentomatoes.com/m/' + movie #creates url for movie
 
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
