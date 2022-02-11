# Quran Search
A Python Library to access Quran elements and search perform operations

The text of the Quran is lifted from the following site in xml format and converted to Json:
https://tanzil.net/download/



# Sample Usage
```
>>> import quran
>>> q=quran.quran()
>>> q.get_ayah(114, 5)
'الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ'
>>> q.get_surah(114)
[{'@index': '1', '@text': 'قُلْ أَعُوذُ بِرَبِّ النَّاسِ', '@bismillah': 'بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ'}, {'@index': '2', '@text': 'مَلِكِ النَّاسِ'}, {'@index': '3', '@text': 'إِلَـٰهِ النَّاسِ'}, {'@index': '4', '@text': 'مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ'}, {'@index': '5', '@text': 'الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ'}, {'@index': '6', '@text': 'مِنَ الْجِنَّةِ وَالنَّاسِ'}]
>>> 
>>> q.get_word(114,5,1)
'الَّذِي'
>>> q.get_surah(114)
[{'@index': '1', '@text': 'قُلْ أَعُوذُ بِرَبِّ النَّاسِ', '@bismillah': 'بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ'}, {'@index': '2', '@text': 'مَلِكِ النَّاسِ'}, {'@index': '3', '@text': 'إِلَـٰهِ النَّاسِ'}, {'@index': '4', '@text': 'مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ'}, {'@index': '5', '@text': 'الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ'}, {'@index': '6', '@text': 'مِنَ الْجِنَّةِ وَالنَّاسِ'}]
>>> q.get_ayah(114,5)
'الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ'
>>> q.get_word(114,5,1)
'الَّذِي'
>>> q.analyze_word(114,5,1)
0: ا b'\xd8\xa7'
1: ل b'\xd9\x84'
2: ّ b'\xd9\x91'
3: َ b'\xd9\x8e'
4: ذ b'\xd8\xb0'
5: ِ b'\xd9\x90'
6: ي b'\xd9\x8a'

```
