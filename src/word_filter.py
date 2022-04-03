from enum import Enum
import numpy as np
from enum import Enum

class Color(Enum):
  BLACK = 'b'
  YELLOW = 'y'
  GREEN = 'g'
  UNKNOWN = '-'

class WordFilter:
  def __init__(self):
    self.permitted = np.ones([26,5]).astype(np.bool)
    self.required = []
    self.known = [-1,-1,-1,-1,-1]

  def handleResult(self, word, colors):
    for i in range(5):
      idx = ord(word[i]) - ord('a')
      color = Color(colors[i])
      if color == Color.BLACK:
        self.permitted[idx,0] = False
        self.permitted[idx,1] = False
        self.permitted[idx,2] = False
        self.permitted[idx,3] = False
        self.permitted[idx,4] = False
      if color == Color.YELLOW:
        self.permitted[idx,i] = False
        self.required += [idx]
      if color == Color.GREEN:
        self.required += [idx]
        self.known[i] = idx

  def filter(self, word):
    hasRequired = np.zeros(len(self.required)).astype(np.bool)
    for i in range(5):
      idx = ord(word[i]) - ord('a')
      if self.known[i] >= 0:
        if self.known[i] != idx:
          return False
      if not self.permitted[idx,i]:
        return False
      for j in range(len(hasRequired)):
        req = self.required[j]
        if idx == req:
          hasRequired[j] = True
    if np.sum(hasRequired) == len(hasRequired):
      return True
    return False
  