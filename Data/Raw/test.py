import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights_data.csv')
df['delay'] = df['arr_delay'] > 0
df.groupby('carrier')['delay'].mean().plot(kind='bar')
plt.title('Average delay by airline')
plt.show()
