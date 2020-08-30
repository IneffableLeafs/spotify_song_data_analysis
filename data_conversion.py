class DataAnalysis(object):

	# this function will turn a list into a csv files, that we can use with pandas for data analysis
	def csv_conversion(data_list):
		df = pd.DataFrame(data_list)
		print(df)
		return df

		