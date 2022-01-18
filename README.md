# Quran Search
A Python Library to access Quran elements and search perform operations

# Sample Usage
```
>>> import quran
>>> q=quran.quran()
>>> q.analyze_ayat(114, 5)
0: ا b'\xd8\xa7'
1: ل b'\xd9\x84'
2: ّ b'\xd9\x91'
3: َ b'\xd9\x8e'
4: ذ b'\xd8\xb0'
5: ِ b'\xd9\x90'
6: ي b'\xd9\x8a'
7:   b' '
8: ي b'\xd9\x8a'
9: ُ b'\xd9\x8f'
10: و b'\xd9\x88'
11: َ b'\xd9\x8e'
12: س b'\xd8\xb3'
13: ْ b'\xd9\x92'
14: و b'\xd9\x88'
15: ِ b'\xd9\x90'
16: س b'\xd8\xb3'
17: ُ b'\xd9\x8f'
18:   b' '
19: ف b'\xd9\x81'
20: ِ b'\xd9\x90'
21: ي b'\xd9\x8a'
22:   b' '
23: ص b'\xd8\xb5'
24: ُ b'\xd9\x8f'
25: د b'\xd8\xaf'
26: ُ b'\xd9\x8f'
27: و b'\xd9\x88'
28: ر b'\xd8\xb1'
29: ِ b'\xd9\x90'
30:   b' '
31: ا b'\xd8\xa7'
32: ل b'\xd9\x84'
33: ن b'\xd9\x86'
34: ّ b'\xd9\x91'
35: َ b'\xd9\x8e'
36: ا b'\xd8\xa7'
37: س b'\xd8\xb3'
38: ِ b'\xd9\x90'

>>> q.analyze_word(114, 5, 1)
0: ا b'\xd8\xa7'
1: ل b'\xd9\x84'
2: ّ b'\xd9\x91'
3: َ b'\xd9\x8e'
4: ذ b'\xd8\xb0'
5: ِ b'\xd9\x90'
6: ي b'\xd9\x8a'
>>> q.analyze_word(114, 5, 2)
0: ي b'\xd9\x8a'
1: ُ b'\xd9\x8f'
2: و b'\xd9\x88'
3: َ b'\xd9\x8e'
4: س b'\xd8\xb3'
5: ْ b'\xd9\x92'
6: و b'\xd9\x88'
7: ِ b'\xd9\x90'
8: س b'\xd8\xb3'
9: ُ b'\xd9\x8f'

>>> q.analyze_word(114, 1, 1)
0: ق b'\xd9\x82'
1: ُ b'\xd9\x8f'
2: ل b'\xd9\x84'
3: ْ b'\xd9\x92'
```
