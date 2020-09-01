import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
df = pd.read_csv("audio_features.csv", parse_dates=['Date Added'], index_col=['Date Added'])

# bar plot
plt.title("Energy")
sns.distplot(a=df["Energy"], kde=False)

# scatterplot
#plt.title("Energy and Valence")
#sns.scatterplot(x=df.index.values, y=df['Energy'])

# jointplot
#sns.jointplot(x="Valence", y="Energy", data=df, kind="kde")
plt.show()