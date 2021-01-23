from flask import Flask, render_template
#from data import Articles

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5c44addc0ba641e5a3d272c06c37d9a7",
                                                           client_secret="f4e81362d2524685b196bca33ed9abe6"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])



"""import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5c44addc0ba641e5a3d272c06c37d9a7'
secret = 'f4e81362d2524685b196bca33ed9abe6'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)"""
"""def spotify_authenticate(spotify_client_id, spotify_client_sectret):
    data = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=data, auth=(spotify_client_id, spotify_client_secret))
    return response.json()['access_token']


@app.route('/backend-search', methods=["GET"])
def search():
    token = spotify_authenticate()
    search_url = 'https://api.spotify.com/v1/search'
    #i know i shouldnt be doing this
    search_txt = request.headers.get('search_text','')
    if search_txt == '':
        search_txt = request.args.get('search_text','')

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }
    params = (
        ('q', '{}*'.format(search_txt)),
        ('type', 'track'),
        ('limit', 10)
    )

    response = requests.get(search_url, headers=headers, params=params).json()
    return json.dumps(response)"""

"""@app.route('/authorize')
def authorize():
  client_id = app.config['5c44addc0ba641e5a3d272c06c37d9a7']
  redirect_uri = app.config['5c44addc0ba641e5a3d272c06c37d9a7']
  scope = app.config['SCOPE']
  state_key = createStateKey(15)
  session['state_key'] = state_key

  authorize_url = 'https://accounts.spotify.com/en/authorize?'
  params = {'response_type': 'code', 'client_id': client_id,
            'redirect_uri': redirect_uri, 'scope': scope, 
            'state': state_key}
  query_params = urlencode(params)
  response = make_response(redirect(authorize_url + query_params))
  return response"""

app = Flask(__name__)


#Articles=Articles()
@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

"""@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)"""

if __name__ == "__main__":
    app.run(debug= True)
    #just run once on terminal and just need to refresh browser