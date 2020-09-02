import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from data_analysis import DataAnalysis

# read in our data/csv file
read_data = "recent_audio_features.csv"
data = pd.read_csv(read_data)

# prediction target
y = data['In Liked Songs']

# features
features = ['Danceability', 'Energy', 'Valence', 'Tempo']
X = data[features]

# split the data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=2)

# our models
decision_tree_model = DecisionTreeRegressor(random_state=2)
forest_1 = RandomForestRegressor(n_estimators=50, random_state=0)
forest_2 = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
forest_3 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
forest_4 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

# fit the model and run predictions:
DataAnalysis.score_model(decision_tree_model, train_X, val_X, train_y, val_y)




