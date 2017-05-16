import os

os.system('wget http://www.openslr.org/resources/12/test-clean.tar.gz')
os.system('tar zxvf test-clean.tar.gz')
os.system('rm test-clean.tar.gz')
os.system('mv LibriSpeech a')
os.system('mv a/test-clean .')
os.system('rm -rf a')
os.system('mv test-clean LibriSpeech')
os.system('mkdir final/word_unit')
