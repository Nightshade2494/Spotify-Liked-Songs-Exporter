## **Spotify Liked Songs Exporter**

A Python script that fetches all the songs from your "Liked Songs" playlist on Spotify, including the song name and artist(s), and saves them to a text file. This is useful for backing up your liked songs, sharing your playlist, or keeping a record of your favorite tracks.

---

### **Features**
- Authenticates with Spotify using the **Spotify Web API**.
- Extracts song names and artist information from your "Liked Songs" playlist.
- Saves the exported list to a `.txt` file in a user-specified location.
- Easy-to-use and customizable.

---

### **Requirements**
- **Python 3.7+**
- Spotify Developer App with:
  - `Client ID`
  - `Client Secret`
  - Redirect URI set to `http://localhost:8888/callback`

---

### **Dependencies**
The script uses the following Python libraries:
1. **[Spotipy](https://spotipy.readthedocs.io/)**: A lightweight Python library for the Spotify Web API.
2. **[Python-dotenv](https://pypi.org/project/python-dotenv/)** (Optional): For managing environment variables (if not setting credentials manually).

Install dependencies via pip:
```bash
pip install spotipy python-dotenv
```

---

### **Usage**
1. **Set Up Spotify Developer App**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an app.
   - Copy your **Client ID** and **Client Secret** from the app's settings.

2. **Update the Script**:
   - Replace the placeholders `your_client_id` and `your_client_secret` in the script with your actual credentials.

3. **Run the Script**:
   - Use Python to execute the script:
     ```bash
     python export_songs.py
     ```

4. **Authorize the App**:
   - A browser window will open, prompting you to log in to Spotify and authorize the app.

5. **Check the Output**:
   - The script will save your liked songs in a file (`liked_songs.txt`) at the specified location.

---

### **File Format**
The exported file lists songs in the following format:
```
Song Name - Artist Name
```

---

### **Customization**
- You can change the save location of the exported file by updating the file path in the script:
  ```python
  save_songs_to_file(liked_songs, "desired/path/liked_songs.txt")
  ```

---

### **Future Improvements**
- Add support for exporting other playlists.
- Save the output in other formats like CSV or JSON.
- Create a graphical user interface (GUI) for easier use.
