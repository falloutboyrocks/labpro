# labpro
speech lab

The following commands should be execute under directory lab/  

1. wget LibriSpeech devset & setup directories  
python2 setup.py  
2. Do alignment and split LibriSpeech into word_unit  
(This command will take hours to do alignment & has a lot of dependencies that I forgot :P)  
python2 prepro.py  
3. Extract mfcc of word units and build up training data  
python2 final/extract_mfcc.py  
4. Train a seq2seq model  
python2 final/seq2seq.py  
