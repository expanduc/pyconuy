#! /usr/bin/python
import os
import wave
import requests
from os.path import (abspath, dirname)
import ipdb

#ipdb.set_trace()
path = dirname(abspath(__file__))

DATA_DIR = "%s/%s" % (path, 'data')

# Relative audio path to data dir
AUDIO_FILE = 'F-audio-sample.wav'

AUDIO_FILE_PATH = "%s/%s" % (DATA_DIR, AUDIO_FILE)

URL = 'http://voiceapi.expand.com.uy/recognize/gender'

frames_chunk = 10000

wav = wave.open(AUDIO_FILE_PATH, "r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.\
                                                                    getparams()
bitdepth = sampwidth * 8

frames = wav.readframes(frames_chunk * nchannels)

wav.close()

data = {'audio_sequence': 1,
        'audio_samplerate': framerate,
        'audio_bitdepth': bitdepth,
        'audio_channels': nchannels,
        'audio_sent_frames': frames_chunk}

files_audiodata = {'file': ('file', frames)}

r = requests.post(URL, data=data, files=files_audiodata)

print("Service replied with status code [%s]" % (r.status_code))
print("Response body:\n%s" % (r.text))
