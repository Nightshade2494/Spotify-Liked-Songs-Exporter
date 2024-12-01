import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials (Set manually)
SPOTIFY_CLIENT_ID = "your_client_id"  # Replace with your actual Client ID
SPOTIFY_CLIENT_SECRET = "your_client_secret"  # Replace with your actual Client Secret
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"  # Keep this as is

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read"
))

# Function to fetch liked songs
def get_liked_songs():
    songs = []
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        for item in results['items']:
            track = item['track']
            song_name = track['name']
            artist_name = ', '.join(artist['name'] for artist in track['artists'])
            songs.append(f"{song_name} - {artist_name}")
        results = sp.next(results) if results['next'] else None
    return songs

# Function to write songs to a file
def save_songs_to_file(songs, file_name="liked_songs.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')

# Main execution
if __name__ == "__main__":
    print("Fetching your liked songs from Spotify...")
    liked_songs = get_liked_songs()
    save_songs_to_file(liked_songs, "C:/Users/YourName/Documents/liked_songs.txt")  # Update file path as needed
    print(f"Saved {len(liked_songs)} songs to C:/Users/YourName/Documents/liked_songs.txt")
