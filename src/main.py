import word_filter
import utils

from word_filter import WordFilter

import numpy as np

# def f(x):
#   if x[0] == 'a':
#     return True
#   return False

def step(words, wfilter):
  freqs = utils.get_freqs(words)
  scores = utils.score_words(words, freqs)
  best = utils.get_best_word(words, scores)
  print("best word: {}".format(best.strip()))
  print("type the word guessed followed by the result string seperated by a dash, no spaces (ex:cares-bbbyg):")
  result = input()
  result = result.split('-')
  wfilter.handleResult(result[0], result[1])

  def f(x):
    return wfilter.filter(x)

  # filtered = np.array(list(filter(wfilter.filter, words)))
  filtered = np.array(list(filter(f, words)))
  return filtered

if __name__ == "__main__":
  dictionary = open('dictionary.txt','r')
  words = np.array(dictionary.readlines())
  wfilter = WordFilter()
  print("There are {} words in the dictionary".format(len(words)))

  for i in range(6):
    words = step(words, wfilter)
    for word in words:
      print(word.strip())
    print("There are {} words left in dictionary".format(len(words)))
