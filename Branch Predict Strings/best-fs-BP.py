import queue
import copy
#import board
import cubes_BP as cubes
#import eight_puzzle

import bp as BP

num_examined = 0

#============================================================

def best_fs(pqueue, closed_list):
  global num_examined

  found = False
# while not found and not pqueue.empty():
  while True:
    BP.bp_info.check(not_found)
    BP.bp_info.check(pqueue.empty())
    if found or pqueue.empty():
      break
    item = pqueue.get() # this is a tuple: first is the value; 2nd is the data
    node = item[1] # this is a tuple; 1st thing is the data; 2nd is the hval
    print('popped a node, h is ' + str(node[1]) + ' g is ' + str(node[0].g()))
    print(node[0])
    num_examined = num_examined + 1
    BP.bp_info.check(node[0].g() == 0)
    if node[0].g() == 0:
      found = True
    else:
      node[0].generate_child_nodes(pqueue, closed_list, node[1])

#   if pqueue.qsize() > 100:
#     print('pqueue too big')
#     return None

  BP.bp_info.check(found)
  if found:
    print('I looked at ' + str(num_examined) + ' nodes')
    return node[0]
  else:
    return None

#============================================================

def best_fs2(pqueue, closed_list):
  global num_examined

  found = False
# while not found and not pqueue.empty():
  while True:
    BP.bp_info.check(not found)
    BP.bp_info.check(not pqueue.empty())
    if found or pqueue.empty():
      break;
    item = pqueue.get() # this is a tuple: first is the value; 2nd is the data
    node = item[1] # this is a tuple; 1st thing is the data; 2nd is the hval
    print(' popped a node, h is ' + str(node[1]) + ' g is ' + str(node[0].g()))
    print(node[0])
    num_examined = num_examined + 1
    BP.bp_info.check(node[0].g() == 0)
    if node[0].g() == 0:
      found = True
    else:
      board = node[0]
      h = node[1]
      children = board.generate_child_nodes2()
      assert(children is not None)

#BP   for child in children:
      numch = len(children)
      jj = 0
      while True:
        BP.bp_info.check(jj < numch)
        if jj == numch:
          break;
        child = children[jj]

        BP.bp_info.check(child.hash not in closed_list) 
        if child.hash not in closed_list:
          closed_list.append(child.hash)
          g = child.g()
          f = h+1 + g
          pqueue.put((f, (child, h+1)))
          print('put ' + str(child.hash) + ' in the closed list, h = ' + str(h+1) + ' g = ' + str(g))
#         print('child')
          print(child)

        jj = jj + 1 # for BP

#   if pqueue.qsize() > 100:
#     print('pqueue too big')
#     return None

  BP.bp_info.check(found)
  if found:
    print('I looked at ' + str(num_examined) + ' nodes')
    return node[0]
  else:
    return None

#============================================================

def n_queens():
  # testing a specific config
# b0 = Board([1, 1, 3, 2])
# print(b0)
# np = b0.num_pairs()
# print('np = ' + str(np));
# return

# b1 = Board([2, 1, 3, 2])
  b1 = board.Board([2, 1, 3, 2])
  print(b1)
  np = b1.g()
  print('np = ' + str(np))
  print('')
  print('hash is ' + str(b1.hash))
  print('pow is ' + str(b1.pow))

# b2 = copy.deepcopy(b1)
# b2.vals[1] = 3
# print(b2)
# print(b1)

  pqueue = queue.PriorityQueue(50000)
  closed_list = []

  # g = h + f, where h is depth and f is #interacting pairs of queens
  g = 0 + b1.g();
  pqueue.put((g, (b1, 0)))

  rtnval = best_fs2(pqueue, closed_list)
  if rtnval is not None:
    print('found!')
    print(rtnval)
  else:
    print('did not find a solution')

#==========================================================

def color_cubes():
  cube_1 = cubes.Cube([cubes.RED, cubes.WHITE, cubes.GREEN, cubes.BLUE, cubes.GREEN, cubes.WHITE])
  cube_2 = cubes.Cube([cubes.GREEN, cubes.BLUE, cubes.GREEN, cubes.WHITE, cubes.RED, cubes.BLUE])
  cube_3 = cubes.Cube([cubes.GREEN, cubes.RED, cubes.WHITE, cubes.WHITE, cubes.BLUE, cubes.RED])
  cube_4 = cubes.Cube([cubes.WHITE, cubes.RED, cubes.BLUE, cubes.GREEN, cubes.RED, cubes.RED])
  tower = cubes.Tower([cube_1, cube_2, cube_3, cube_4])
  print(tower)
  g = tower.g()

  print('g = ' + str(tower.g()) + ' hash = ' + str(tower.hash))

  closed_list = []
  pqueue = queue.PriorityQueue(10000)
  pqueue.put((g, (tower, 0)))

  rtnval = best_fs2(pqueue, closed_list)

  BP.bp_info.check(rtnval is None)

  if rtnval is not None:
    print('found!')
    print(rtnval)
  else:
    print('did not find a solution')

#==========================================================

def puzzle8():
# puzzle = eight_puzzle.Puzzle([4, 5, 7, 6, 3, 2, 0, 1, 8])
# puzzle = eight_puzzle.Puzzle([1, 2, 3, 4, 5, 6, 7, 0, 8])
  puzzle = eight_puzzle.Puzzle([7, 3, 5, 2, 0, 1, 8, 4, 6])
  g = puzzle.g()

  closed_list = []
  pqueue = queue.PriorityQueue(20000)
  pqueue.put((g, (puzzle, 0)))
  rtnval = best_fs2(pqueue, closed_list)
  if rtnval is not None:
    print('found!')
    print(rtnval)
  else:
    print('did not find a solution')

#==========================================================
#n_queens()

color_cubes()

BP.bp_info.print_summary()

#puzzle8()
