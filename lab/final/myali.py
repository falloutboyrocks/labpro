# output a aligment file of json format
import os
import sys
from pydub import AudioSegment

corp_path = 'LibriSpeech'
transcriber = 'p2fa/text_to_transcript.py'
aligner = 'p2fa/align.py'

dir_dict = dict()
for dir in os.listdir(corp_path):
    dir_dict[dir] = []
    for file in os.listdir(corp_path + '/' + dir + '/'):
            dir_dict[dir].append(corp_path + '/' + dir + '/' + file)

# flac to wav
for dir in dir_dict:
    for file in dir_dict[dir]:
	if '.flac' in file:
	    flac_file = AudioSegment.from_file(file, 'flac')
	    flac_file.export(file[:-4] + 'wav', format='wav')
	    os.system('chmod 777 ' + file)
	    os.system('rm ' + file)

# align the transcription
for dir in dir_dict:
    for file in dir_dict[dir]:
	if '.lab' in file:
	    name = file[:-4]
	    labf = name + '.lab'
	    wavf = name + '.wav'
	    json = name + '.json'
            os.system('python2 ' + transcriber + ' --output-file temp ' + labf)
            os.system('python2 ' + aligner + ' ' + wavf + ' temp ' + json)
	    os.remove('temp')




	    
	    

