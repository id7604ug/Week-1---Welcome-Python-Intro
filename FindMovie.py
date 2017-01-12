# This program uses the OMDB api to find a movie by title and display a short description of the plot
import requests
# Link to python requests library help http://docs.python-requests.org/en/master/
r = requests.get('http://www.omdbapi.com/?t=iron+man&y=plot=short&r=json')
print(r.text)
