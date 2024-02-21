import pandas as pd
import plotly.express as px

df = pd.read_csv('data_eeg.csv')

fig_all_waves = px.line(df, x='time', y=df.columns[2:10], title='EEG Waves Over Time')
fig_all_waves.update_xaxes(title_text='Time (Seconds)') 

blinks_column = df.columns[10]
blink_times = df[df[blinks_column] != 0]['time'].tolist()

for blink_time in blink_times:
    fig_all_waves.add_shape(
        type='line',
        x0=blink_time,
        x1=blink_time,
        y0=0,
        y1=1,
        yref='paper',
        line=dict(color='red', width=1)
    )

fig_attention_meditation = px.line(df, x='time', y=['attention', 'meditation'],
                                   title='Attention and Meditation over Time')
fig_attention_meditation.update_xaxes(title_text='Time (Seconds)')

for blink_time in blink_times:
    fig_attention_meditation.add_shape(
        type='line',
        x0=blink_time,
        x1=blink_time,
        y0=0,
        y1=1,
        yref='paper', 
        line=dict(color='red', width=1)
    )

fig_all_waves.show()
fig_attention_meditation.show()