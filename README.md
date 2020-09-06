# Spotify Song Data Analysis
This is my Spotify song analysis project!

# Start by going to [Spotify's developer website](https://developer.spotify.com/dashboard/login):
1. You'll want to create a Spotify account if you don't have one already.
2. Then, click "Create an App", and enter in an "App name" and "App description".
3. Record down the "Client ID" and "Client Secret", located in the dashboard.
4. Click on the "Edit Settings" button and type: "http://localhost:8888/callback" into the Redirect URIs field, click add and save.

# Next, go to the spotipy_connection.py file:
- Type the client_id, client_secret, and your spotify username into the variables.

# Now go to get.py:
The purpose of this file is to GET songs. It will get:
1. All the songs in your "liked songs".
2. The energy, valence, and tempo (also known as [audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)) of your songs.
3. Your 50 most recently played songs.
4. The audio features from step 2 for your recent 50 songs.
It will also CREATE files, namely: 
1. **audio_features.csv**: contains the audio features, song ID, and date added of all your liked songs.
2. **recent_audio_features.csv**: contains the audio features of your recently listened to songs. If that song is in your liked songs, it will have a "1", otherwise it will have a "0".
**Run get.py**
You should have these two new files in the same directory as the program itself.

# Next, move to machine_learning_models.py:
The purpose of this file is to run machine learning algorithms on your csv files, to see how well they can predict whether you will like a song based on its audio features.
Five models are provided. One is a decision tree regression, and the other four are random forest regressions.
1. On line 30 of the file, replace you can replace "decision_tree_model" with "forest_1", "forest_2", etc. to try other models.
2. Running this file will show you the percent error. So if you get 0.1, the algorithm predicts wrong 10% of the time.
3. This will give you an idea of how wide your music taste is. The lower your score, the more focused your music taste is.

# Now, move to plots.py:
Here, you can play around with the data you have. In this case, line 17 has a bivariable plot, that compares two variables.
- You'll want to compare all three audio features against each other, so for x and y, make sure you try:
1. x=Valence, y=Energy
2. x=Valence, y=Tempo
3. x=Energy, y=Tempo
- Notice the darkest portion of the graph. Record the approximate ranges of these numbers.
- For example, the darkest region of the graph is around 100-120 tempo, when comparing tempo to both valence and energy.
- These numbers will help the app find song recommendations for you.

# Finally, go to add.py:
The purpose of this file is to ADD songs. It will:
1. Generate ideal songs for you (songs in your library that fit in the bounds you specified).
2. Generate recommended songs based on your bounded audio features and the ideal songs.
3. Create a playlist in your Spotify.
4. Add these recommendations to that playlist (the default name is DataPlaylist).
In the **add.py** file:
1. You'll want to enter your recorded numbers here, replacing the values of max_energy to min_tempo (lines 7-12) with your own bounds.
2. Run it!

**data_analysis.py** and **spotify_client** contain all the helper functions used.
With that, check your Spotify for your new playlist, and enjoy music that matches your taste!


