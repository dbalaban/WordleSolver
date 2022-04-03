import word_filter
import utils

from word_filter import WordFilter

import numpy as np

def get_response(word, guess):
  response = ""
  for i in range(5):
    if word[i] == guess[i]:
      response += 'g'
      continue
    found = False
    for j in range(5):
      if guess[i] == word[j]:
        response += 'y'
        found = True
        break
    if not found:
      response += 'b'
  return response  

def guess(word, dictionary, wfilter):
  freqs = utils.get_freqs(dictionary)
  scores = utils.score_words(dictionary, freqs)
  best = utils.get_best_word(dictionary, scores)
  result = get_response(word, best)
  if result == 'ggggg':
    return [result]
  wfilter.handleResult(best, result)

  def f(x):
    return wfilter.filter(x)
  
  filtered = np.array(list(filter(f, dictionary)))
  return filtered

def solve(word, words):
  wfilter = WordFilter()
  for i in range(6):
    words = guess(word, words, wfilter)
    if words[0] == 'ggggg':
      break
  return i
  
def collect_stats(dictionary):
  words = np.array(dictionary.readlines())
  words_cpy = np.copy(words)
  counts = np.zeros(7).astype(np.int)
  for word in words:
    print("testing {}".format(word.strip()))
    steps = solve(word, words_cpy)
    counts[steps] += 1
  return counts

if __name__ == "__main__":
  dictionary = open('dictionary.txt','r')
  stats = collect_stats(dictionary)
  print(stats)
  print(100.0 * stats / np.sum(stats))