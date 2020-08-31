import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
df = pd.read_csv("audio_features.csv")

# plots
plt.title("Tempo")
sns.distplot(a=df["Tempo"], kde=False)

plt.show()