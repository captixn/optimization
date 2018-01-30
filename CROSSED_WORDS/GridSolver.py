import numpy as np 
import string 

alphabet = list(string.ascii_lowercase)

class GridSolver:

  def __init__(self, grid, words):
    self.file = grid
    self.matrix = []
    self.content = ''
    self.sol = []
    self.m = 0 
    self.n = 0
    self.words = {} 
    self.parseWords(words)
    self.parse(grid)

  def solve(self):
    var = {}
    i = 0
    for k in range(0, self.m):
        for l in range(0,self.n):
            var[str(k)+','+str(l)] = i
            i += 1
    # attention : chaque variable doit avoir son propre domaine
    #             ne pas utiliser le même objet ensemble pour plusieurs variables
    domains = [set(alphabet) for _ in range(len(var))]
    print(var)

  def parse(self, file):
    f = open(file,'r')
    self.content = f.read()
    lines = self.content.splitlines()
    i = 0
    self.m = len(lines)
    self.n = len(lines[0])
    self.matrix = np.zeros((self.m,self.n))
    for line in lines:
      j = 0
      for char in line: 
        if char == '#':
          self.matrix[i][j] = 0
        else:
          self.matrix[i][j] = 1
        j += 1
      i += 1

  def parseWords(self, file):
    f = open(file,'r')
    lines = f.read().splitlines()
    for line in lines:
      length = len(line)
      if length in self.words.keys():
        self.words[length].append(line)
      else: 
        self.words[length] = [line]
    
  def genConstraints(self):
    self.sol = self.matrix 
    # horizontally 
    for i in range(0, self.m):
      start_i = i 
      start_j = -1
      end_j = -1 
      for j in range(0, self.n):
        if self.matrix[i][j] == 1 and start_j == -1 : 
          # find until what case it is 1 to find out what word with how many chars must be placced 
          start_j = j
          end_j = j
        elif start_j > -1 and self.matrix[i][j] == 0 :
          end_j = j-1 
      if end_j - start_j >= 2 :
        # generer contrainte mot entre (i, start_j) et (i, end_j)
        print('New word found :')
        print('From...')
        print((i, start_j))  
        print('To...')
        print((i, end_j))
    # vertically
    for j in range(0, self.n):
      start_j = j 
      start_i = -1
      end_i = -1
      for i in range(0, self.m):
        if self.matrix[i][j] == 1 and start_i == -1 : 
          # find until what case it is 1 to find out what word with how many chars must be placced 
          start_i = i
          end_i = i
        elif start_i > -1 and self.matrix[i][j] == 0 :
          end_i = i-1 
      if end_i - start_i >= 2 :
        print('New word found :')
        print('From...')
        print((start_i, j))  
        print('To...')
        print((end_i, j))

def main():
  grid = 'crossword1.txt'
  words = 'words1.txt'
  gp = GridSolver(grid, words)
  gp.genConstraints()
  gp.solve()
  #print(gp.words)
  #print(gp.matrix)

main()