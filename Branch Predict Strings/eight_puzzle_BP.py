import copy
import bp as BP

SIZE = 3
SIZESQ = 9

class Puzzle:

  def __init__(self, v):
    flags = [False for x in range(SIZESQ)]
    for i in range(SIZESQ):
      assert(v[i] >= 0 and v[i] <= SIZESQ-1)
      assert(flags[v[i]] == False)
      flags[v[i]] = True
    assert(len(v) == SIZESQ)
    self.v = v
    self.hash = 0
    self.recompute_hash()

  #---------------------------

  def __str__(self):
    s = ''
    for i in range(SIZESQ):
      if self.v[i] == 0:
        s = s + ' '
      else:
        s = s + str(self.v[i])
      if (i+1) % SIZE == 0:
        s = s + '\n'
    return(s)

  #---------------------------

  def g(self):
    sum = 0
#BP for i in range(SIZESQ):
    i = 0
    while True:
      BP.bp_info.check(i==SIZESQ)
      if i == SIZESQ:
        break

      BP.bp_info.check(self.v[i] != 0)
      if self.v[i] != 0:
        BP.bp_info.check(self.v[i] != i+1)
        if self.v[i] != i+1:
          sum = sum + 1

      i = i + 1 # for BP

    return sum

  #---------------------------

  def recompute_hash(self):
    mult = 1
    sum = 0
#BP for i in range(SIZESQ):
    i = 0
    while True:
      BP.bp_info.check(i == SIZESQ)
      if i == SIZESQ:
        break
      sum = sum + self.v[i] * mult
      mult = mult * (SIZESQ+1)

      i = i + 1 # for BP
    self.hash = sum

  #---------------------------

  def __lt__(self, other):
    return self.hash < other.hash

  #---------------------------

  def __eq__(self, other):
    return self.hash == other.hash

  #---------------------------

  def swap(self, i, j):
    v2 = copy.deepcopy(self.v)
    v2[i] = self.v[j]
    v2[j] = self.v[i]
    return v2

  #---------------------------

  def generate_child_nodes2(self):
    rtnval = []
    BP.bp_info.check(self.v[0] == 0)
    if self.v[0] == 0:
      v2 = self.swap(0, 1)
      rtnval.append(Puzzle(v2))
      v2 = self.swap(0, 3)
      rtnval.append(Puzzle(v2))

    else:
      BP.bp_info.check(self.v[1] == 0)
      if self.v[1] == 0:
        v2 = self.swap(1, 0)
        rtnval.append(Puzzle(v2))
        v2 = self.swap(1, 2)
        rtnval.append(Puzzle(v2))
        v2 = self.swap(1, 4)
        rtnval.append(Puzzle(v2))

      else:
        BP.bp_info.check(self.v[2] == 0)
        if self.v[2] == 0:
          v2 = self.swap(2, 1)
          rtnval.append(Puzzle(v2))
          v2 = self.swap(2, 5)
          rtnval.append(Puzzle(v2))

        else:
          BP.bp_info.check(self.v[3] == 0)
          if self.v[3] == 0:
            v2 = self.swap(3, 0)
            rtnval.append(Puzzle(v2))
            v2 = self.swap(3, 4)
            rtnval.append(Puzzle(v2))
            v2 = self.swap(3, 6)
            rtnval.append(Puzzle(v2))

          else:
            BP.bp_info.check(self.v[4] == 0)
            if self.v[4] == 0:
              v2 = self.swap(4, 1)
              rtnval.append(Puzzle(v2))
              v2 = self.swap(4, 3)
              rtnval.append(Puzzle(v2))
              v2 = self.swap(4, 5)
              rtnval.append(Puzzle(v2))
              v2 = self.swap(4, 7)
              rtnval.append(Puzzle(v2))

            else:
              BP.bp_info.check(self.v[5] == 0)
              if self.v[5] == 0:
                v2 = self.swap(5, 4)
                rtnval.append(Puzzle(v2))
                v2 = self.swap(5, 2)
                rtnval.append(Puzzle(v2))
                v2 = self.swap(5, 8)
                rtnval.append(Puzzle(v2))

              else:
                BP.bp_info.check(self.v[6] == 0)
                if self.v[6] == 0:
                  v2 = self.swap(6, 3)
                  rtnval.append(Puzzle(v2))
                  v2 = self.swap(6, 7)
                  rtnval.append(Puzzle(v2))

                else:
                  BP.bp_info.check(self.v[7] == 0)
                  if self.v[7] == 0:
                    v2 = self.swap(7, 6)
                    rtnval.append(Puzzle(v2))
                    v2 = self.swap(7, 4)
                    rtnval.append(Puzzle(v2))
                    v2 = self.swap(7, 8)
                    rtnval.append(Puzzle(v2))

                  else:
                    assert(self.v[8] == 0)
                    v2 = self.swap(8, 5)
                    rtnval.append(Puzzle(v2))
                    v2 = self.swap(8, 7)
                    rtnval.append(Puzzle(v2))

    return rtnval

#===================================

def test():
  p = Puzzle([4, 0, 3, 6, 7, 1, 2, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 0, 6, 7, 1, 2, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 0, 7, 1, 2, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 7, 0, 1, 2, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 7, 1, 0, 2, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 7, 1, 2, 0, 8, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 7, 1, 2, 8, 0, 5])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

  p = Puzzle([4, 3, 6, 7, 1, 2, 8, 5, 0])
  print(p, end='')
  print('hash is ' + str(p.hash))
  rtnval = p.generate_child_nodes2()
  for r in rtnval:
    print(r)
  print('')

#===================================

def test2():
  p = Puzzle([4, 7, 3, 6, 5, 0, 1, 8, 2])
  print(p)
  print('g = ' + str(p.g()))

#===================================

#test2()

