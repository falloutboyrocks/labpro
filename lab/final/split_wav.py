from pydub import AudioSegment
import os
import json

corp_path = 'LibriSpeech'
output_path = 'final/word_unit'

def parse_wav(wavf, jsonf):
    with open(jsonf) as data_file:
        data = json.load(data_file)
    audio = AudioSegment.from_wav(wavf)
    for word in data['words']:
	if not os.path.exists(output_path + '/' + word['alignedWord']):
	    os.mkdir(output_path + '/' + word['alignedWord'])
	start = word['start'] * 1000
	end = word['end'] * 1000
	newAudio = audio[start:end]
	newAudio.export(output_path + '/' + word['alignedWord'] + '/' + wavf[-8:-4] + str(start) + '.wav', \
	                format='wav')


##########################

for dir in os.listdir(corp_path):
    for file in os.listdir(corp_path + '/' + dir + '/'):
	if '.wav' in file:
	    name = corp_path + '/' + dir + '/' + file[:-4]
	    wavf = name + '.wav'
	    jsonf = name + '.json'
	    if not os.path.exists(jsonf):
		continue
	    else:
	        parse_wav(wavf, jsonf)
