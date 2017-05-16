import tensorflow as tf
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import os

word_path = 'final/word_unit'
num_of_mfcc = 100
mfcc_dim = 13

def pad(mfcc_seq):
    pad_num = num_of_mfcc - len(mfcc_seq)
    pad_arr = np.zeros((pad_num, mfcc_dim))
    return np.append(mfcc_seq, pad_arr, axis = 0)

# preprocessing 
mfcc_data = []
for dir in os.listdir(word_path):
    dir_path = word_path + '/' + dir
    for file in os.listdir(dir_path):
	file_path = dir_path + '/' + file
	(rate, sig) = wav.read(file_path)
	mfcc_seq = mfcc(sig, rate)
	if len(mfcc_seq) < num_of_mfcc:
	    mfcc_data.append(pad(mfcc_seq))
	else:	# truncate if too long
	    cutoff = len(mfcc_seq) - num_of_mfcc
	    front = cutoff / 2
	    back = cutoff - front
	    mfcc_data.append(mfcc_seq[front:-back])
mfcc_mat = np.stack(mfcc_data, axis=0)
np.save('final/mfcc_mat', mfcc_mat)




