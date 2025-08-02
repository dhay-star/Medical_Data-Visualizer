import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

##1 Import the data 

df1= pd.read_csv("medical_examination.csv")
df1.drop('id', axis=1, inplace=True)

##2 Add an overweight column to the data 

height_m = df1['height'] / 100
#BMI
bmi = df1['weight'] / (height_m ** 2)
#add 'overweight'
df1['overweight'] = (bmi > 25).astype(int)

##3 Normalize data  

df1['cholesterol'] = (df1['cholesterol'] > 1).astype(int)
df1['gluc'] = (df1['gluc'] > 1).astype(int)

##4 Draw the Categorical Plot 

def draw_cat_plot():
    # 5. Create DataFrame for cat plot
    df_cat = pd.melt(df1, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Draw the catplot
    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio').fig

    return fig

##8. Draw Heat Map

def draw_heat_map():
    # 9. Clean the data
    df_heat = df1[
        (df1['ap_lo']  <= df1['ap_hi']) &
        (df1['height'] >= df1['height'].quantile(0.025)) &
        (df1['height'] <= df1['height'].quantile(0.975)) &
        (df1['weight'] >= df1['weight'].quantile(0.025)) &
        (df1['weight'] <= df1['weight'].quantile(0.975))
    ]

    # 10. Calculate the correlation matrix
    corr = df_heat.corr()
  
    # 11. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 13. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

    return fig



