"""
Author: Liuchuan Yu; lyu20@gmu.edu
"""

import os
from enum import Enum

import pyttsx3
import soundfile as sf

"""
About sound file size:
For the same data and same sample_rate,
wav file is 79KB, while ogg is only 9KB. 

See example/how_are_you.ogg and example/how_are_you.wav.
"""


class Voices(Enum):
    Male = 0
    Female = 1


class TextToSpeech(object):

    def __init__(self, rate=125, volume=1.0, voice=Voices.Male):
        self.engine = None
        self.rate = rate
        self.volume = volume  # (min=0 and max=1)
        self.voice = voice

        self.init_engine()

    def init_engine(self):
        self.engine = pyttsx3.init()
        # set rate
        self.engine.setProperty('rate', self.rate)
        # set volume
        self.engine.setProperty('volume', self.volume)
        # set voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.voice.value].id)

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def save_file(self, sentence, filename):
        # this file should be wav format
        # On linux make sure that 'espeak' and 'ffmpeg' are installed
        self.engine.save_to_file(sentence, filename)
        self.engine.runAndWait()

    @staticmethod
    def run(sentence, filename, rate=125, volume=1.0, voice=Voices.Male):
        ts = TextToSpeech(rate=rate, volume=volume, voice=voice)
        ts.save_file(sentence, filename)

    @staticmethod
    def to_ogg_file(filename, keep_original_file=True):
        folder = os.path.dirname(filename)
        basename = os.path.basename(filename)
        data, sample_rate = sf.read(filename)
        ogg_file = os.path.splitext(basename)[0] + ".ogg"
        ogg_file = os.path.join(folder, ogg_file)
        sf.write(ogg_file, data, sample_rate)
        if not keep_original_file:
            os.remove(filename)
        return ogg_file


if __name__ == '__main__':
    ts = TextToSpeech()
    ts.save_file('How are you?', 'test.wav')
    ts.to_ogg_file('test.wav')
