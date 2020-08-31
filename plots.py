import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
df = pd.read_csv("audio_features.csv", parse_dates=['Date Added'], index_col=['Date Added'])

# plots
#plt.title("Energy")
#sns.distplot(a=df["Energy"], kde=False)

#plt.show()

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 7))

# Add x-axis and y-axis
ax.scatter(df.index.values,
        df['Valence'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Valence",
       title="Valence over Time")
# scatterplot
#plt.title("Energy and Valence")
#sns.scatterplot(x=df.index.values, y=df['Energy'])

# jointplot
#sns.jointplot(x="Valence", y="Energy", data=df, kind="kde")
plt.show()