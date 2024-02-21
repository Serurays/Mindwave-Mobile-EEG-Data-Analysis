import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data_eeg.csv')

fig_all_waves = px.line(df, x='time', y=df.columns[2:10], title='EEG Waves Over Time')
fig_all_waves.update_xaxes(title_text='Time (Seconds)')
fig_all_waves.add_trace(
    go.Scatter(x=df['time'], y=df[df.columns[10]],
               mode='markers',
               marker=dict(size=df[df.columns[10]] // 5, color='red', symbol='circle'),
               name='Blink Strength'
              )
)

fig_attention_meditation = px.line(df, x='time', y=['attention', 'meditation'],
                                   title='Attention and Meditation over Time')
fig_attention_meditation.update_xaxes(title_text='Time (Seconds)')

fig_attention_meditation.add_trace(
    go.Scatter(x=df['time'], y=df[df.columns[10]],
               mode='markers',
               marker=dict(size=df[df.columns[10]] // 5, color='red', symbol='circle'),
               name='Blink Strength'
              )
)

fig_all_waves.show()
fig_attention_meditation.show()