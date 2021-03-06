import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from skimage import transform, data
import csv
from os import listdir
import re

np.set_printoptions(threshold = 5000)


def write_into_csv(file_name, spectrogram, label):
    S = transform.resize(spectrogram, (32,32))
    S = S.reshape(-1)
    #print(S)
    S = str(S)
    #print(S)
    #print('------')
    #S = re.sub(']' ,'' ,S)
    #S = re.sub('[', '0', S)
    S = ''.join( c for c in S if c not in '[]')
    #print(S)
    with open(file_name, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow([label, S])
    

save_data = 'data/data_128_val.csv'
feq = 44100
window_size = 128
mode = 'magnitude'
with open(save_data, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['label', 'feature'])

# label 0 : Tettigonioidea1
path = 'val/Tettigonioidea1'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal,fs=feq, nperseg = window_size, window = 'hamming', mode = mode)

    write_into_csv(save_data,S,0)

# label 1 : Tettigonioidea2 
path = 'val/Tettigonioidea2'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal,fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,1)

# label 2 : drums_Snare 
path = 'val/drums_Snare'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,2)

# label 3 : Grylloidea1 
path = 'val/Grylloidea1'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,3)

# label 4 : drums_MidTom
path = 'val/drums_MidTom'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,4)

# label 5 : drums_HiHat 
path = 'val/drums_HiHat'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,5)

# label 6 : drums_Kick 
path = 'val/drums_Kick'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,6)


# label 7 : drums_SmallTom 
path = 'val/drums_SmallTom'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,7)


# label 8 : guitar_chord2 
path = 'val/guitar_chord2'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,8)


# label 9 : Frog1
path = 'val/Frog1'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,9)


# label 10 : Frog2 
path = 'val/Frog2'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,10)


# label 11 : drums_FloorTom 
path = 'val/drums_FloorTom'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,11)


# label 12 : guitar_7th_fret 
path = 'val/guitar_7th_fret'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,12)


# label 13 : drums_Rim 
path = 'val/drums_Rim'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,13)


# label 14 : Grylloidea2 
path = 'val/Grylloidea2'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,14)


# label 15 : guitar_3rd_fret 
path = 'val/guitar_3rd_fret'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,15)


# label 16 : drums_Ride
path = 'val/drums_Ride'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,16)


# label 17 : guitar_chord1 
path = 'val/guitar_chord1'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,17)


# label 18 : guitar_9th_fret 
path = 'val/guitar_9th_fret'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,18)


# label 19 : Frog3 
path = 'val/Frog3'

files = listdir(path)
#print(files)
for i in files:
    signal = np.load(path + '/' + i)
    F, T, S = scipy.signal.spectrogram(signal, fs=feq, nperseg = window_size, window = 'hamming', mode = mode)
    write_into_csv(save_data,S,19)


