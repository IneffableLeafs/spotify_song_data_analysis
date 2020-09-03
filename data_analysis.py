from sklearn.metrics import mean_absolute_error

class DataAnalysis(object):

	# this function will turn our list of lists into a csv file, that we can use with pandas for data analysis
	def dataframe_conversion(pd, data_list):
		df = pd.DataFrame(data_list).transpose()
		df.columns = ["Danceability", "Energy", "Valence", "Tempo", "Song ID", "Date Added"]
		df.to_csv("audio_features.csv")
		print(df)
		return df

	# creates a csv file for our recently listened to songs
	def recent_dataframe_conversion(pd, data_list):
		df = pd.DataFrame(data_list).transpose()
		df.columns = ["Danceability", "Energy", "Valence", "Tempo", "In Liked Songs"]
		df.to_csv("recent_audio_features.csv")
		print(df)
		return df

	# define a function that we can pass a model into, that prints the mean absolute error:
	def score_model(model, train_X, val_X, train_y, val_y):
		model.fit(train_X, train_y)
		prediction = model.predict(val_X)
		print(mean_absolute_error(val_y, prediction))
		
	# this function will take in the csv of our liked songs and using our features narrow it down
	# to a list of "ideal songs" to be used with the recommendations() spotipy method
	def ideal_song(pd, csv_name, max_energy, max_valence, max_tempo, min_energy, min_valence, min_tempo):
		df = pd.read_csv(csv_name)
		df = df[(df["Energy"]>=min_energy) & (df["Energy"]<=max_energy)]
		print(df)
		df = df[(df["Valence"]>=min_valence) & (df["Valence"]<=max_valence)]
		print(df)
		df = df[(df["Tempo"]>=min_tempo) & (df["Tempo"]<=max_tempo)]
		print(df)

		# get the Song IDS of the remaining songs after applying features
		recommendation_list = df["Song ID"].to_list()
		return recommendation_list
