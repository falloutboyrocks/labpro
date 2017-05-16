from python_speech_features import mfcc
import scipy.io.wavfile as wav
import os

word_path = 'final/word_unit'
chart = dict()
total = 0
for dir in os.listdir(word_path):
    dir_path = word_path + '/' + dir
    for file in os.listdir(dir_path):
	file_path = dir_path + '/' + file
        (rate, sig) = wav.read(file_path)
	mfcc_len = (len(mfcc(sig, rate))) / 10 * 10
	if not mfcc_len in chart:
	    chart[mfcc_len] = 0
	chart[mfcc_len] += 1
	total += 1

accum = 0
for len in sorted(chart):
    accum += chart[len] / float(total)
    print '%s %s' % (len, accum)
        

