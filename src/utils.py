from pickle import FALSE, TRUE
import numpy as np

def get_freqs(words):
  counts = np.zeros([26,5]).astype(np.int)
  for word in words:
    idx0 = ord(word[0]) - ord('a')
    idx1 = ord(word[1]) - ord('a')
    idx2 = ord(word[2]) - ord('a')
    idx3 = ord(word[3]) - ord('a')
    idx4 = ord(word[4]) - ord('a')
    
    counts[idx0,0] += 1
    counts[idx1,1] += 1
    counts[idx2,2] += 1
    counts[idx3,3] += 1
    counts[idx4,4] += 1
  return counts / len(words)

def score_words(words, freqs):
  scores = np.zeros(len(words))
  for i in range(len(words)):
    word = words[i]
    idx0 = ord(word[0]) - ord('a')
    idx1 = ord(word[1]) - ord('a')
    idx2 = ord(word[2]) - ord('a')
    idx3 = ord(word[3]) - ord('a')
    idx4 = ord(word[4]) - ord('a')
    scores[i] = (np.log(freqs[idx0, 0])
               + np.log(freqs[idx1, 1])
               + np.log(freqs[idx2, 2])
               + np.log(freqs[idx3, 3])
               + np.log(freqs[idx4, 4]))
  return scores

def wordHasDouble(word):
  for i in range(5):
    for j in range(i+1,5):
      if (word[i] == word[j]):
        return True
  return False

def get_best_word(words, scores):
  idxs = np.argsort(-scores)
  sorted = words[idxs]
  for word in sorted:
    hasdouble = wordHasDouble(word)
    if not hasdouble:
      return word
  return sorted[0]

if __name__ == "__main__":
  dictionary = open('dictionary.txt','r')
  words = np.array(dictionary.readlines())
  freqs = get_freqs(words)
  scores = score_words(words, freqs)
  best = get_best_word(words, scores)
  print("best word: {}".format(best.strip()))
