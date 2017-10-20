import string
file10=open("book1.txt")
file20=open("book2.txt")
file30=open("book3.txt")

def longest_word():
 book1 = " "
 book2 = " "
 book3 = " "

 for line in file 10:
  for word in line.split():
   if len(word) > len(book1):
    book1 = word
 print('longest word in book1 is :',book1)
 
 for line in file20:
  for word1 on line.split():
   if len(word1) > len(book2):
    book2 = word1
 print('longest word in book 2 is :',book2)

  for line in file30:
   for word2 in line.split():
    if len(word2) > len(book3):
     book3 = word2
 print('longest word in book3 is :',book3)

longest_word()


