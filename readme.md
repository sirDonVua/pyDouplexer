# pyDouplexer
Bring Double face printing into an unsupported old printer (or a cheap one).

## Features
This app is made using the kivy framework in python.
The backend of this app uses pymupdf.
This app is not vibe coded ! all the mistakes are made by a human !!

the app have 3 main features:

- LTR 2UP: make every face have a 2 horizintal pages (eg: |1|2| )
- RTL 2UP: same as above but for RTL languages like arabic (eg: |2|1| )
- Split: it's the main way to bring Double face printing into an old printer.
    by deviding the pdf into two files {even,odd} then you print the even file, flip the printed
    pages then print the odd file.

### Coming soon (I hope so)
- [ ] Booklet like pages arrangment
- [ ] UI enhancment
- [ ] adding Themes to the app (maybe i could switch to kivymd)
- [ ] adding more languages (i will probably use ai or goolge translator for this)
- [ ] adding a feature to specify theb name of the output file

## Why ?
I made this app for 2 main reasons, the first is for learning, the second reason is 
because i couldn't find any site online that had an RTL 2up so i decided to make my own. 

## Notes:
1. I Recommend doing some tests first by using a small pdf file.
    DO NOT use this on a big pdf file for you first Time because you will likely
    screw it up.
2. This app currently in beta, so it will probably suck and may not work
    like intended.
