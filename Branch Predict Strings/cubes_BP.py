import queue
import copy
import bp as BP

# red - 1
# white - 2
# green - 3
# blue - 4

#  ------
# /     /|
# ------ |
# |    | /
# |    |/      side facing out is 2; to the left is 1; to the right is 3
# ------       side not seen is 4; side on bottom is 6; side on top is 5

#==============================================================

RED = 1
WHITE = 2
GREEN = 3
BLUE = 4

#==============================================================
# position 1 - face to the left of front
# position 2 - face on the front
# position 3 - face to the right of front
# position 4 - face in back
# position 5 - face on top
# position 6 - face on bottom

class Cube:
  def __init__(self, faces):
    self.faces = [0, 0, 0, 0, 0, 0, 0] # use faces[1] to faces[6]
    assert(len(faces) == 6)

    for i in range(6):
      assert(faces[i] >=1 and faces[i] <= 4)
      self.faces[i+1] = faces[i]

    # for orientiation/identification
    self.face_one = 1 # meaning original faces[1] is in position 1
    self.face_two = 2 # meaning original faces[2] is in position 2

  #------------------------------------------------------------

  def rotate_left(self):
    tmp = self.faces[1]
    self.faces[1] = self.faces[2]
    self.faces[2] = self.faces[3]
    self.faces[3] = self.faces[4]
    self.faces[4] = tmp

    # orientation/identification
    BP.bp_info.check(self.face_one == 1)
    if self.face_one == 1:
      self.face_one = 4
    else:
      if self.face_one == 2:
        self.face_one = 1
      else:
        if self.face_one == 3:
          self.face_one = 2
        else:
          if self.face_one == 4:
            self.face_one = 3

    if self.face_two == 1:
      self.face_two = 4
    else:
      if self.face_two == 2:
        self.face_two = 1
      else:
        if self.face_two == 3:
          self.face_two = 2
        else:
          if self.face_two == 4:
            self.face_two = 3

  #------------------------------------------------------------

  def rotate_right(self):
    tmp = self.faces[4]
    self.faces[4] = self.faces[3]
    self.faces[3] = self.faces[2]
    self.faces[2] = self.faces[1]
    self.faces[1] = tmp

    # orientation/identification
    if self.face_one == 1:
      self.face_one = 2
    else:
      if self.face_one == 2:
        self.face_one = 3
      else:
        if self.face_one == 3:
          self.face_one = 4
        else:
          if self.face_one == 4:
            self.face_one = 1

    if self.face_two == 1:
      self.face_two = 2
    else:
      if self.face_two == 2:
        self.face_two = 3
      else:
        if self.face_two == 3:
          self.face_two = 4
        else:
          if self.face_two == 4:
            self.face_two = 1

  #------------------------------------------------------------

  def rotate_up(self):
    # bottom -> face #2
    # face #4 -> bottom
    # top -> face #4
    # face #2 -> top
    tmp = self.faces[2]
    self.faces[2] = self.faces[6]
    self.faces[6] = self.faces[4]
    self.faces[4] = self.faces[5]
    self.faces[5] = tmp

    # orientation/identification
    if self.face_one == 2:
      self.face_one = 5 # front -> top
    else:
      if self.face_one == 5:
        self.face_one = 4 # top -> back
      else:
        if self.face_one == 4:
          self.face_one = 6 # back -> bottom
        else:
          if self.face_one == 6:
            self.face_one = 2 # bottom -> front

    if self.face_two == 2:
      self.face_two = 5 # front -> top
    else:
      if self.face_two == 5:
        self.face_two = 4 # top -> back
      else:
        if self.face_two == 4:
          self.face_two = 6 # back -> bottom
        else:
          if self.face_two == 6:
            self.face_two = 2 # bottom -> front

  #------------------------------------------------------------

  def rotate_down(self):
    # top -> face #2
    # face #4 -> top
    # bottom -> face #4
    # face #2 -> bottom
    tmp = self.faces[2]
    self.faces[2] = self.faces[5]
    self.faces[5] = self.faces[4]
    self.faces[4] = self.faces[6]
    self.faces[6] = tmp

    # orientation/identification
    if self.face_one == 2:
      self.face_one = 6 # front -> bottom
    else:
      if self.face_one == 6:
        self.face_one = 4 # bottom -> back
      else:
        if self.face_one == 4:
          self.face_one = 5 # back -> top
        else:
          if self.face_one == 5:
            self.face_one = 2 # top -> front

    if self.face_two == 2:
      self.face_two = 6 # front -> bottom
    else:
      if self.face_two == 6:
        self.face_two = 4 # bottom -> back
      else:
        if self.face_two == 4:
          self.face_two = 5 # back -> top
        else:
          if self.face_two == 5:
            self.face_two = 2 # top -> front

  #------------------------------------------------------------

  def __str__(self):
    s = ''

    for i in range(1,7):
      if i == 5:
        s = s + ' top '
      else:
        if i == 6:
          s = s + ' bot '
      if self.faces[i] == RED:
        s = s + 'R '
      else:
        if self.faces[i] == WHITE:
          s = s + 'W '
        else:
          if self.faces[i] == GREEN:
            s = s + 'G '
          else:
            s = s + 'B '

    return s

#==============================================================

class Tower:
  def __init__(self, cubes):
    assert(len(cubes) == 4)
    self.cubes = cubes
    self.recompute_hash()

  #------------------------------------------------------------

  def recompute_hash(self):
    hash = 0
    index = 1
#BP for i in range(4):
    i = 0
    while True:
      BP.bp_info.check(i<4)
      if i == 4:
        break
      hash = hash + index*self.cubes[i].face_one
      index = index*10
      hash = hash + index*self.cubes[i].face_two
      index = index*10

      i = i + 1 # for BP

    self.hash = hash

  #------------------------------------------------------------

  def __str__(self):
    s = ''
    for i in range(3,-1,-1):
      s = s + self.cubes[i].__str__()
      s = s + '\n'
    return s

  #------------------------------------------------------------

  def g(self):
    total = 0
#BP for i in range(1,5):
    i = 1
    while True:
      BP.bp_info.check(i < 5)
      if i == 5:
        break;

      found_red = False
      found_green = False
      found_blue = False
      found_white = False
#BP   for j in range(4):
      j = 0
      while True:
        BP.bp_info.check(j<4)
        if j == 4:
          break

        BP.bp_info.check(self.cubes[j].faces[i] == RED)
        if self.cubes[j].faces[i] == RED:
          found_red = True
        else:
          BP.bp_info.check(self.cubes[j].faces[i] == GREEN)
          if self.cubes[j].faces[i] == GREEN:
            found_green = True
          else:
            BP.bp_info.check(self.cubes[j].faces[i] == BLUE)
            if self.cubes[j].faces[i] == BLUE:
              found_blue = True
            else:
              found_white = True

        j = j + 1 # for BP

      BP.bp_info.check(found_red)
      if found_red:
        total = total + 1
      BP.bp_info.check(found_green)
      if found_green:
        total = total + 1
      BP.bp_info.check(found_blue)
      if found_blue:
        total = total + 1
      BP.bp_info.check(found_white)
      if found_white:
        total = total + 1

      i = i + 1 # for BP

    return 16 - total

  #------------------------------------------------------------

  def __lt__(self, other):
    return self.hash < other.hash

  #------------------------------------------------------------

  def generate_child_nodes(self, pqueue, closed_list, h):

#BP for i in range(4):
    i = 0
    while True:
      BP.bp_info.check(i<4)
      if i == 4:
        break;

      # rotate cube i left
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_left()
      towcopy.recompute_hash()

      BP.bp_info.check(towcopy.hash not in closed_list)

      if towcopy.hash not in closed_list:
#J      node = Node(towcopy, h+1)
        closed_list.append(towcopy.hash)
        g = towcopy.g()
        f = h + 1 + g
        pqueue.put((f, (towcopy, h+1)))
        print(str(i+1) + ' L: put ' + str(towcopy.hash) + ' in the closed list, h = ' + str(h+1) + ' g = ' + str(g))

      # rotate cube i right
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_right()
      towcopy.recompute_hash()

      BP.bp_info.check(towcopy.hash not in closed_list)
      if towcopy.hash not in closed_list:
#J      node = Node(towcopy, h+1)
        closed_list.append(towcopy.hash)
        g = towcopy.g()
        f = h + 1 + g
        pqueue.put((f, (towcopy, h+1)))
        print(str(i+1) + ' R: put ' + str(towcopy.hash) + ' in the closed list, h = ' + str(h+1) + ' g = ' + str(g))

      # rotate cube i up
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_up()
      towcopy.recompute_hash()
      BP.bp_info.check(towcopy.hash not in closed_list)
      if towcopy.hash not in closed_list:
#J      node = Node(towcopy, h+1)
        closed_list.append(towcopy.hash)
        g = towcopy.g()
        f = h + 1 + g
        pqueue.put((f, (towcopy, h+1)))
        print(str(i+1) + ' U: put ' + str(towcopy.hash) + ' in the closed list, h = ' + str(h+1) + ' g = ' + str(g))

      # rotate cube i down
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_down()
      towcopy.recompute_hash()
      BP.bp_info.check(towcopy.hash not in closed_list)
      if towcopy.hash not in closed_list:
#J      node = Node(towcopy, h+1)
        closed_list.append(towcopy.hash)
        g = towcopy.g()
        f = h + 1 + g
        pqueue.put((f, (towcopy, h+1)))
        print(str(i+1) + ' D: put ' + str(towcopy.hash) + ' in the closed list, h = ' + str(h+1) + ' g = ' + str(g))

      i = i + 1 # for BP

#TO HERE

  #------------------------------------------------------------

  def generate_child_nodes2(self):
    rtnval = []

#BP for i in range(4):
    i = 0
    while True:
      BP.bp_info.check(i<4)
      if i == 4:
        break
 
      # rotate cube i left
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_left()
      towcopy.recompute_hash()
      rtnval.append(towcopy)

      # rotate cube i right
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_right()
      towcopy.recompute_hash()
      rtnval.append(towcopy)

      # rotate cube i up
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_up()
      towcopy.recompute_hash()
      rtnval.append(towcopy)

      # rotate cube i down
      towcopy = copy.deepcopy(self)
      towcopy.cubes[i].rotate_down()
      towcopy.recompute_hash()
      rtnval.append(towcopy)

      i = i + 1 # for BP
    return rtnval
