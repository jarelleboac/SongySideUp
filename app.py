from flask import Flask, render_template
#from data import Articles
import sys
import spotipy
import spotify #this is the name of the module declared in other file
import random

"""from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5c44addc0ba641e5a3d272c06c37d9a7",
                                                           client_secret="f4e81362d2524685b196bca33ed9abe6"))
print("...selecting songs")
results = sp.search(q='Lady Gaga', limit=50)
for index, track in enumerate(results['tracks']['items']):
    print(index, track['name'])"""

from spotipy.oauth2 import SpotifyOAuth
if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="5c44addc0ba641e5a3d272c06c37d9a7",
                                               client_secret="f4e81362d2524685b196bca33ed9abe6",
                                              redirect_uri="http://localhost:5000/",
                                               scope="user-library-read user-top-read playlist-modify-public"))

app = Flask(__name__)


#Articles=Articles()

#handles requests when go to /url
@app.route("/")
def hello():
    #return render_template('home.html')
    return render_template('home.html', track_dict=spotify.top_tracks())

@app.route("/information")
def info():
    #return render_template('home.html')
    return render_template('information.html')

@app.route('/about')
def about():
    return render_template('about.html')
#creating a url

#http://127.0.0.1:5000/top-tracks
@app.route('/top-tracks')
def toptracks():
    #whatever return is what is rendered to browser
    #return str(spotify.top_tracks())
    return render_template('home.html', members=str(spotify.top_tracks()))

if __name__ == "__main__":
    app.run(debug= True)
    #just run once on terminal and just need to refresh browser