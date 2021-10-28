#google search

from googlesearch import GoogleSearch as

google_query = str(input("concepto de ciencia"))

for i in search(google_query, start=0, pause=2):
    print (i)