import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# first we will do a simple decision tree model:

read_data = "recent_audio_features.csv"
data = pd.read_csv(read_data)
data.describe()

data.columns

# prediction target:
y = data['In Liked Songs']

# features
features = ['Danceability', 'Energy', 'Valence', 'Tempo']
X = data[features]

X.head()

# split the data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=2)
song_liked_model = DecisionTreeRegressor(random_state=2) # adding rndst optional
song_liked_model.fit(train_X, train_y)

val_predictions = song_liked_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))