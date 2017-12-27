#!/usr/bin/python
# coding:utf-8

# tools - speech.py
# 2017/12/21 22:32
# speech recognition

__author__ = 'Benny <benny@bennythink.com>'

# !/usr/bin/env python3

import speech_recognition as sr

from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "1.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='cmn-Hans-CN'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""Your Credentials
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, language='cmn-Hans-CN',
                                                                            credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
