import heapq
#import board
#import cubes
import eight_puzzle_BP as eight_puzzle
import bp as BP

ALPHA = 1
BETA = 2
MAX_DEPTH = 50

#===================================================

class Node:
  def __init__(self, parent, item, depth, f, g, h):
    self.parent = parent
    self.item = item
    self.depth = depth
    self.f = f
    self.g = g
    self.h = h

  #-------------------------------------------------

  def __str__(self):
    s = ''
    s = s + 'depth=' + str(self.depth) + \
        ' f=' + str(self.f) + ' g=' + str(self.g) + ' h=' + str(self.h)
    return s

  def __lt__(self, other):
    return self.f < other.f

  def __eq__(self, other):
    return self.item.hash == other.item.hash

#===================================================

def a_star(open_list, closed_list):
#BP while len(open_list) > 0:
  while True:
      len_ol = len(open_list)
      BP.bp_info.check(len_ol > 0)
      if len_ol == 0:
        break;

    # get the current best node in the open list
      parent_node = heapq.heappop(open_list)
      print('examine this board (', end='')
      print(parent_node, end=')\n')
      print(parent_node.item)

      BP.bp_info.check(parent_node.h == 0)
      if parent_node.h == 0:
        return parent_node

      closed_list.append(parent_node.item)
      print('put ' + str(parent_node.item.hash) + ' in the closed_list')

      # heuristic: don't go too deep
      BP.bp_info.check(parent_node.depth <= MAX_DEPTH)
      if parent_node.depth <= MAX_DEPTH:
        # enumerate adjacent states
        children = parent_node.item.generate_child_nodes2()
        print('generated ' + str(len(children)) + ' children')
#BP     for child in children:
        l_c = len(children)
        ii = 0
        while True:
          BP.bp_info.check(ii < l_c)
          if ii == l_c:
            break;
          child = children[ii]

          BP.bp_info.check(not child in closed_list)
          if not child in closed_list:
            g = parent_node.depth+1
            h = child.g()
            f = ALPHA*g + BETA*h
            child_node = Node(parent_node, child, parent_node.depth+1, f, g, h)
            # is the child in the open list?

            BP.bp_info.check(child_node in open_list)
            if child_node in open_list:
              idx = open_list.index(child_node)
              node_in_list = open_list[idx]
              BP.bp_info.check(node_in_list.g <= child_node.g)
              if node_in_list.g <= child_node.g:
                # here, the node in the list has a better g value,
                # so do nothing
                pass
              else:
                # child board has been seen, but child's value is better
                # than the value that's in the list:
                # hook it to the parent (and place it in the open list)
                print('node is in list, but current node is better: ' + str(child_node.g) + ' <= ' + str(node_in_list.g))
                print(child_node.item)
                del open_list[idx]
                heapq.heappush(open_list, child_node)
            else:
              heapq.heappush(open_list, child_node)
              print('push board ' + str(child_node))
              print(child)

          else:
            print('have already seen child')
            print(child)

          ii = ii + 1 # for BP
  return None

#=======================================================

def n_queens():
  closed_list = []
  open_list = []

  b1 = board.Board([2, 1, 3, 2, 3, 4])
  print(b1)
  g = 0
  h = b1.g()
  f = ALPHA*g + BETA*h
  node = Node(None, b1, 0, f, g, h)

  heapq.heappush(open_list, node)

  rtnval = a_star(open_list, closed_list)
  if rtnval is not None:
    print('solved:')
    print(rtnval)
    print(rtnval.item)
    parent = rtnval.parent
    idx = 0
    while parent is not None and idx < 5:
      print(parent.item)
      parent = parent.parent
      idx = idx + 1

#=======================================================

def color_cubes():
  closed_list = []
  open_list = []

  cube_1 = cubes.Cube([cubes.RED, cubes.WHITE, cubes.GREEN, cubes.BLUE, cubes.GREEN, cubes.WHITE])
  cube_2 = cubes.Cube([cubes.GREEN, cubes.BLUE, cubes.GREEN, cubes.WHITE, cubes.RED, cubes.BLUE])
  cube_3 = cubes.Cube([cubes.GREEN, cubes.RED, cubes.WHITE, cubes.WHITE, cubes.BLUE, cubes.RED])
  cube_4 = cubes.Cube([cubes.WHITE, cubes.RED, cubes.BLUE, cubes.GREEN, cubes.RED, cubes.RED])
  tower = cubes.Tower([cube_1, cube_2, cube_3, cube_4])
  print(tower)

  g = 0
  h = tower.g()
  f = ALPHA*g + BETA*h
  node = Node(None, tower, 0, f, g, h)

  heapq.heappush(open_list, node)

  rtnval = a_star(open_list, closed_list)
  if rtnval is not None:
    print('solved:')
    print(rtnval)
    print(rtnval.item)
    parent = rtnval.parent
    idx = 0
    while parent is not None and idx < 5:
      print(parent.item)
      parent = parent.parent
      idx = idx + 1

#=======================================================

def puzzle():
  closed_list = []
  open_list = []

  puzzle = eight_puzzle.Puzzle([7, 3, 5, 2, 0, 1, 8, 4, 6])
  g = 0
  h = puzzle.g()
  f = ALPHA*g + BETA*h
  node = Node(None, puzzle, 0, f, g, h)

  heapq.heappush(open_list, node)

  rtnval = a_star(open_list, closed_list)
  if rtnval is not None:
    print('solved:')
    print(rtnval)
    print(rtnval.item)
    parent = rtnval.parent
    while parent is not None:
      print(parent.item)
      parent = parent.parent
  else:
    print('not solved')

#=======================================================

#n_queens()

#color_cubes()

puzzle()

BP.bp_info.print_summary()

