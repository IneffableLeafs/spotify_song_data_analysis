class DataAnalysis(object):

	# this function will turn our list of lists into a csv file, that we can use with pandas for data analysis
	def dataframe_conversion(pd, data_list):
		df = pd.DataFrame(data_list).transpose()
		df.columns = ["Danceability", "Energy", "Acousticness", "Valence", "Tempo"]
		df.to_csv("audio_features.csv")
		print(df)
		return df