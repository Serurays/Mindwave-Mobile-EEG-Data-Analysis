import numpy as np
import pandas as pd
import sys
import json
import time
from telnetlib import Telnet

attention_values = []
meditation_values = []
delta_values = []
theta_values = []
lowAlpha_values = []
highAlpha_values = []
lowBeta_values = []
highBeta_values = []
lowGamma_values = []
highGamma_values = []
blinkStrength_values = []
time_array = []

tn = Telnet('localhost', 13854)

start = time.perf_counter()

i = 0
tn.write(b'{"enableRawOutput": true, "format": "Json"}')

outfile = "null"
if len(sys.argv) > 1:
    outfile = sys.argv[-1]
    outfptr = open(outfile, 'w')

eSenseDict = {'attention': 0, 'meditation': 0}
waveDict = {'lowGamma': 0, 'highGamma': 0, 'highAlpha': 0, 'delta': 0, 'highBeta': 0, 'lowAlpha': 0, 'lowBeta': 0, 'theta': 0}
signalLevel = 0

while time.perf_counter() - start < 30:
    blinkStrength = 0
    line = tn.read_until(b'\r').decode('utf-8')
    if len(line) > 20:
        timediff = time.perf_counter() - start
        data_dict = json.loads(line)
        if "poorSignalLevel" in data_dict:
            signalLevel = data_dict['poorSignalLevel']
        if "blinkStrength" in data_dict:
            blinkStrength = data_dict['blinkStrength']
        if "eegPower" in data_dict:
            waveDict = data_dict['eegPower']
            eSenseDict = data_dict['eSense']
        outputstr = f"{timediff}, {signalLevel}, {blinkStrength}, {eSenseDict['attention']}, {eSenseDict['meditation']}, {waveDict['lowGamma']}, {waveDict['highGamma']}, {waveDict['highAlpha']}, {waveDict['delta']}, {waveDict['highBeta']}, {waveDict['lowAlpha']}, {waveDict['lowBeta']}, {waveDict['theta']}"
        time_array.append(timediff)
        blinkStrength_values.append(blinkStrength)
        lowGamma_values.append(waveDict['lowGamma'])
        highGamma_values.append(waveDict['highGamma'])
        highAlpha_values.append(waveDict['highAlpha'])
        delta_values.append(waveDict['delta'])
        lowBeta_values.append(waveDict['lowBeta'])
        highBeta_values.append(waveDict['highBeta'])
        theta_values.append(waveDict['theta'])
        lowAlpha_values.append(waveDict['lowAlpha'])
        attention_values.append(eSenseDict['attention'])
        meditation_values.append(eSenseDict['meditation'])
        print(outputstr)
        if outfile != "null":
            outfptr.write(outputstr + "\n")

data_row = pd.DataFrame({'attention': attention_values, 'meditation': meditation_values,
                         'delta': delta_values, 'theta': theta_values, 'lowAlpha': lowAlpha_values,
                         'highAlpha': highAlpha_values, 'lowBeta': lowBeta_values, 'highBeta': highBeta_values,
                         'lowGamma': lowGamma_values, 'highGamma': highGamma_values,
                         'blinkStrength': blinkStrength_values, 'time': time_array})

data_row.to_csv('data_eeg.csv', index=False)

tn.close()
if outfile != "null":
    outfptr.close()