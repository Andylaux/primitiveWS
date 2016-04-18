#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
import pygame.mixer
import csv
from random import randint
#import pyglet
#from pyglet.media import avbin
#import mp3play

from gtts import gTTS
#from subprocess import call


csv_file_name = "/home/poppy/resources/audio/list.csv"
mp3_dir = "/home/poppy/resources/audio/"


def find(reader, sentence):
    for row in reader:
        if row.get("text") == sentence:
            return row.get("file")

    return str(randint(1, 99999))+".mp3"




class Speak(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['sentence_to_speak']
	def __init__(self, robot, text = 'coucou'):
        
			pypot.primitive.Primitive.__init__(self, robot)
                        self._text = text

			print text.decode('utf-8')
                        
	#def start(self, text):
	def start(self):
			pypot.primitive.Primitive.start(self)
			#self._text = text.decode('utf-8', errors='replace')
			


	def run(self):

                
                file = open(csv_file_name, "a+")
                reader = csv.DictReader(file)
                file.seek(0)

                filename_temp = find(reader, self._text)

                filename = mp3_dir + filename_temp

                print filename



                #clip = mp3play.load(os.path.abspath('../utils/Phrase1.mp3'))
                #clip.play()

                #while clip.isplaying() is not False:
                #    time.sleep(0.5)
                try:
                        pygame.mixer.init(16000)
                        pygame.mixer.music.load(os.path.abspath(filename))
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.music.play()
                        
                        print "déjà connu"
                
                except:
                        tts = gTTS(self._text.decode('utf_8'), lang='fr')
                        tts.save(filename)

                        print "nouvelle entrée"
                        new = (self._text, filename_temp)
                        print new
                        w = csv.writer(file)
                        w.writerow(new)

                        pygame.mixer.init(16000)
                        pygame.mixer.music.load(os.path.abspath(filename))
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(0.5)
                
                file.close()

                #pygame.mixer.music.stop()
                #pygame.mixer.quit()
                
                #mp3 = pyglet.media.load(filename)
                #mp3.play()

                # wait until terminated 
                #time.sleep(mp3.duration)
            
	@property
	def sentence_to_speak(self):
			return self._text

	@sentence_to_speak.setter
	def sentence_to_speak(self, text):
            print text
            print text.encode('utf-8')
            self._text = text.encode('utf-8')

        
        
