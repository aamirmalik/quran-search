#!/usr/bin/env python3
import json

FILENAME='quran-simple.json'

class quran():

    def __init__(self):
        fh=open(FILENAME, 'r')
        self.quran = json.load(fh)

    def get_surah(self, surah_num):
        surah=self.quran[surah_num-1]['aya']
        s=[]
        for i,ayah in enumerate(surah):
            s.append(ayah['@text'])
        return s

    def get_num_surahs(self):
        return(len(self.quran))

    def get_ayah(self, surah_num, ayat_num):
        surah=self.get_surah(surah_num)
        return(surah[ayat_num-1])

    def get_num_ayat(self, surah_num):
        surah=self.get_surah(surah_num)
        return(len(surah))

    def get_word(self, surah_num, ayat_num, word_num):
        ayat=self.get_ayah(surah_num, ayat_num)
        words=ayat.split(' ')
        return (words[word_num-1])

    def get_num_words(self, surah_num, ayat_num, word_num):
        ayat=self.get_ayah(surah_num, ayat_num)
        words=ayat.split(' ')
        return (len(words))

    def analyze_ayat(self, surah_num, ayat_num):
        print(f"Analyzing {self.get_ayah(surah_num, ayat_num)}")
        a=self.get_ayah(surah_num, ayat_num)
        for i,ch in enumerate(a):
            print(f"{i}: {ch} {ch.encode('utf-8')}")

    def analyze_word(self, surah_num, ayat_num, word_num):
        print(f"Analyzing Surah:{surah_num} Ayah:{ayat_num} Word:{word_num} {self.get_word(surah_num, ayat_num, word_num)}")
        w=self.get_word(surah_num, ayat_num, word_num)
        for i,ch in enumerate(w):
            print(f"{i}: {ch} {ch.encode('utf-8')}")


