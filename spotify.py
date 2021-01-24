import sys
import spotipy

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




#print("test!") 

#show my top tracks
def top_tracks():
    """all_top_tracks= []
    track_name_artists=[]"""
    track_dict = {}

    for sp_range in ['medium_term']:
        #print("retrieving top songs")
        results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
        for i, item in enumerate(results['items']):
            #print(i, item['name'], '//', item['artists'][0]['name'])
            #name of the song, artist
            """all_top_tracks.append((item['name']))
            track_name_artists.append((item['artists']))"""
            track_dict[item['name']]= item['artists'][0]['name']
            #dictionary inside a list of one item
        #print()
    return track_dict


#show my top artists
def top_artists():
    """all_top_artists=[]
    for sp_range in ['medium_term']:
    #print("range:", sp_range)

        results_top_artists = sp.current_user_top_artists(time_range=sp_range, limit=50)

        for i, item in enumerate(results_top_artists['items']):
            print(i, item['name'])
        print()
        for i, item in enumerate(results_top_artists['items'])"""
    top_artists_name = []
    top_artists_uri = []

    ranges = ['short_term', 'medium_term', 'long_term']
    for r in ranges:
        top_artists_all_data = sp.current_user_top_artists(limit=50, time_range= r)
        top_artists_data = top_artists_all_data['items']
        for artist_data in top_artists_data:
            if artist_data["name"] not in top_artists_name:		
                top_artists_name.append(artist_data['name'])
                top_artists_uri.append(artist_data['uri'])

    followed_artists_all_data = sp.current_user_followed_artists(limit=50)
    followed_artists_data = (followed_artists_all_data['artists'])
    for artist_data in followed_artists_data["items"]:
        if artist_data["name"] not in top_artists_name:
            top_artists_name.append(artist_data['name'])
            top_artists_uri.append(artist_data['uri'])

    return top_artists_uri
    
