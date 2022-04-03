words_f = open('words.txt', 'r')
filtered_words = open('dictionary.txt','w')

word = words_f.readline()
while word:
  if (len(word) == 6):
    filtered_words.write(word)
  word = words_f.readline()

words_f.close()
filtered_words.close()