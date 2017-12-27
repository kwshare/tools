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
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "***REMOVED***",
  "private_key_id": "***REMOVED***",
  "private_key": "-----***REMOVED***-----\n***REMOVED***B8QwhAkCDa3Sl9v9Rx\nCAJ***REMOVED***dG/T\n1v3***REMOVED***pbcK/O1P7gv8CnDOPXd/Ld9VzLW1q***REMOVED***HpF***REMOVED***QC0cuYeriJFzVjm4Zlx+fk4xOW2Foc***REMOVED***lAzZVTT83M4Fo8qKgBfveSFu8R/A\n/K9huGJsexlj5pGVLt9nLXwxktrF***REMOVED***9FdT4Pww1naNXd1c+26JpgxFU3kRCWitJO2om/X7tFVTgSdtmPR\nP8H2poNfzPsfv2eZxgp9uOY5MmIiJYylYKlsQV2lVkf6ahCGORgkbimdL+hMCVY1\n/O226sdKouLch1Uu2/itZoaUJY/TosJpdA9GOjP5QQKBgG***REMOVED***9Z\nk5dWQ4***REMOVED***yNAonptWsYjl\nUUOZYnLC0+TfdPYyL6MjDTbv\n-----END PRIVATE KEY-----\n",
  "client_email": "***REMOVED***@***REMOVED***.iam.gserviceaccount.com",
  "client_id": "***REMOVED***",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/***REMOVED***%40***REMOVED***.iam.gserviceaccount.com"
}
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, language='cmn-Hans-CN',
                                                                            credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
