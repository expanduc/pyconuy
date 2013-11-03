#! /usr/bin/python
import os
import wave
import requests
import time
from os.path import (abspath, dirname, join)

path = dirname(abspath(__file__))

DATA_DIR = "%s/%s" % (path, 'data')

# Relative audio path to data dir
AUDIO_FILE = 'F-audio-sample.wav'

AUDIO_FILE_PATH = join(DATA_DIR, AUDIO_FILE)

RECOGNITION_URL = 'http://voiceapi.expand.com.uy/recognize/gender'
RESULT_URL = 'http://voiceapi.expand.com.uy/recognize/gender/result'

frames_chunk = 80000

wav = wave.open(AUDIO_FILE_PATH, "r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = \
    wav.getparams()

# sampwidth holds bytes, let's get the bit count
bitdepth = sampwidth * 8

frames = wav.readframes(frames_chunk * nchannels)

wav.close()

data = {'audio_sequence': 1,
        'audio_samplerate': framerate,
        'audio_bitdepth': bitdepth,
        'audio_channels': nchannels,
        'audio_sent_frames': frames_chunk}

files_audiodata = {'file': ('audiodata', frames)}

print("Feeding audio to WS")
audio_req = requests.post(RECOGNITION_URL, data=data, files=files_audiodata)
print("Service replied with status code [%s]" % (audio_req.status_code))
response = audio_req.json()
result_in = response['new_result_in']
task_id = response['task_id']
print("Waiting %s secs for response" % (result_in))
time.sleep(result_in)
result = requests.post(RESULT_URL, data={'task_id': task_id})
print("Service replied with status code [%s]" % (result.status_code))
print("Response body:\n%s" % (result.text))
