from flask import Flask, render_template
#from data import Articles

import spotipy
"""from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5c44addc0ba641e5a3d272c06c37d9a7",
                                                           client_secret="f4e81362d2524685b196bca33ed9abe6"))
print("...selecting songs")
results = sp.search(q='Lady Gaga', limit=50)
for index, track in enumerate(results['tracks']['items']):
    print(index, track['name'])"""

from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="5c44addc0ba641e5a3d272c06c37d9a7",
                                               client_secret="f4e81362d2524685b196bca33ed9abe6",
                                              redirect_uri="http://localhost:5000/",
                                               scope="user-library-read user-top-read playlist-modify-public"))

print("test!") 

#show my top artists
for sp_range in ['short_term', 'medium_term', 'long_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=50)

    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()

"""def fave_artists(sp):
    print("getting your fave artists...")
    top_art_name=[]
    top_art_uri=[]
    ranges = ['short term', 'medium_term', 'long_term']
    for i in ranges:
        top_art_all_data= sp.current_user_top_artists(limit=50, time_range=r)
        top_art_data= top_art_all_data['items']
        for artist_data in top_art_data:
            if artist_data["name"] not in top_art_name:
                top_art_name.append(artist_data['name'])
                top_art_uri.append(artist_data['uri'])
    
    followed_art_all_data= sp.current_user_followed_artists(limit=50)
    followed_art_data=(followed_art_all_data['artists'])
    for artist_data in followed_art_data["items"]:
        if artist_data["name"] not in top_art_name:
            top_art_uri.append(artist_data['name'])
            top_art_uri.append(artist_data[uri])
    return top_art_uri


def agg_top_tracks(sp, top_art_uri):
    print("getting top tracks")
    top_tracks_uri=[]
    for artist in top_artists_uri:
        top_tracks_all_data= sp.artist_top_tracks(artist)
        top_tracks_data= top_tracks_all_data['tracks']
        for track_data in top_tracks_data:
            top_tracks_uri.append(track_data['uri'])
    return top_tracks_uri"""
"""results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])"""



"""def mood_tracks(sp, results):
    print("getting most upbeat/happiest tracks")
    happy_tracks=[]
    for tracks in list(group(results, 10)):
        tracks_all_data= sp.audio_features(tracks)
        for track_data in tracks_all_data:
            try:
                if mood >= .75:
                    if((mood - 0.15) <= track_data["valence"] <=1 
                    and track_data["danceability"] >= (mood/1.75)
                    and track_data["energy"] >= (mood/1.5)):

                        happy_tracks.append(track_data["uri"])
    return happy_tracks
"""
app = Flask(__name__)


#Articles=Articles()
@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug= True)
    #just run once on terminal and just need to refresh browser