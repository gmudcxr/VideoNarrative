"""
Author: Liuchuan Yu; lyu20@gmu.edu
"""

import os
import shutil
import sys
from tts import TextToSpeech, Voices

### Voice Settings
rate = 125
volume = 1.0
voice = Voices.Male  # Voices.Female
###

in_file = 'input.txt'

if not os.path.exists(in_file):
    print(f'{in_file} was not found.')
    sys.exit(1)

output_folder = './output'
if os.path.exists(output_folder):
    # remove first
    shutil.rmtree(output_folder)
os.mkdir(output_folder)

out_sentence_file = 'Sentences.txt'
wav_prefix = 'Sentence_'

text = None

with open(in_file, 'r') as f:
    text = f.read()

if text is None:
    print(f'Failed to read content in {in_file}.')
    sys.exit(1)

tts = TextToSpeech(rate=rate, volume=volume, voice=voice)

lines = list(filter(lambda x: len(x), text.split('\n')))

out_sentence_file = os.path.join(output_folder, out_sentence_file)
with open(f'{out_sentence_file}', 'w', encoding='utf-8') as f:
    for idx, text in enumerate(lines, start=1):
        f.write(f'{idx}\t{text}\n')
        filename = os.path.join(output_folder, f'{wav_prefix}{idx}.wav')
        tts.save_file(text, filename)
