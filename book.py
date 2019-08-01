#!/usr/bin/env python3
import random
import sys

def init_combo(n, k): #------------------------------------------------#
    """ The tricky stuff here is the presence of a Sentinel """
    c = list(range(k)) #                                               #
    c.append(n) #                                             Sentinel #
    return c #---------------------------------------------------------#

def next_combo(c, k): #````````````````````````````````````````````````#
    for j in reversed(range(k)): #                                     #
        if c[j] + 1 != c[j + 1]: #                                     #
            break; #                                             thatz #
    else: #                                                 ve ar don? #
        return False #                                            Yez! #
    c[j] += 1 #                                              increment #
    for i in range(j, k - 1): # init next ones to the lowest order seq #
        c[i + 1] = c[i] + 1 #                                          #
    return True #``````````````````````````````````````````````````````#

def Combo(n, k): #==================================== combo generator #
    c = init_combo(n, k) #                                             #
    while True: #                                                      #
        yield c[:-1] #                              dodge the Sentinel #
        if not next_combo(c, k): #                                     #
            raise StopIteration #========================== ve ar don! #

def init_partition(n, s): #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    """ s - number of subgroups,
        here we are in a reversed order, becoz when cking for enemies
        it's better to start with the largest subgroup """
    s -= 1 #                                                           #
    return [n - s] + [1] * s #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
# _ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_ `_
def next_partition(p, s): #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#
    """ p - partition
        s - number of subgroups """
    dest = 0 #                                                         #
    for i in range(s - 1): #                                           #
        for j in range(i + 1, s): #                                    #
            if p[i] - p[j] > 1: #                                      #
                orig, dest = i, j #                                    #
                break #                                                #
    if dest == 0: return False #                                       #
    p[orig] -= 1 #                                                     #
    p[dest] += 1 #                                                     #
    return True #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#

def Partition(n, s): #'''''''''''''''''''''''''''''''''''''''''''''''''#
    p = init_partition(n, s) #                                         #
    while True: #                                                      #
        yield p #                                                      #
        if not next_partition(p, s): #                                 #
            raise StopIteration #''''''''''''''''''''''''''''''''''''''#

class group(list): #____________________________________________________
    """ group of indexes """                                  
    def __str__(self): #_______________________________________________
        return '[' + ', '.join(list(map(getnom, self))) + ']' #________

    def enemyck(self): #``````````````````````````````````` enemy check
        """ enemy ck among the colleagues discussing the book """
        for j in self: #                                               `
            n_enemy = sum(c in enemy[j] for c in self) #  #j's enemies `
            if n_enemy > p: #                                          `
                return False #__ _  _   _    _     _      _     eNOuPe `
        return True # OKAY ````````````````````````````````````````````
    
class node: #, , , , , , , , , , , , , , , , , , , , , , , , , , , , , #
    def __init__(self, subg, othr): #...................................
        self.subg = group(subg) #                            sub group .
        self.othr = group(othr) #   other persons not yet in any group .
        self.level = 0 #                                    tree level .
        self.parent = None #.............................. parent node .

    def fork(self, c): #,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,
        """ split a subgroup indexed by c from self.othr """
        nd = node([], self.othr) #                                     ,
        for j in c: #                                                  ,
            nd.subg.append(self.othr[j]) #                             ,
            nd.othr.remove(self.othr[j]) #                             ,
        if not nd.subg.enemyck(): #                                    ,
            return None #            too many enemies for a discussion ,
        nd.level = self.level + 1 #                                    ,
        nd.parent = self #                                             ,
        return nd #_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,

stk = [] #st a  c    k        *                .                       *

def walk(root, k): #~|~\~|~|~/~|~|~|~|~\~/~|~|~|~/~|~\~|~|~|~\~|~/~\~|~
    """ by walking the root tree in preorder, gather all possible
        combinations of subgroubs, such that, each member of a subgroup
        has no more than p enemies, for a given partition k """
    for c in Combo(len(root.othr), k[root.level]): #                   ~
        nd = root.fork(c) #                                            ~
        if nd is None: #                                               ~
            continue #                                                 ~
        if not nd.othr: #                                              ~
            stk.append(nd) #                                           ~
            return #                                                   ~
        walk(nd, k) #|~|~\~\~|~|~|~/~|~/~|~\~|~|~|~\~|~|~|~\~/~/~|~|~|~

from collections import deque #.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.`.

deq = deque() #.........................................................
        
def get_leaf_str(nd): #ZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZN
    while nd.parent: #                                                 N
        deq.appendleft(nd) #                                           Z
        nd = nd.parent #                                               N
    s = '\n'.join(map(lambda x: str(x.subg), deq)) #                   Z
    deq.clear() #                                                      N
    return s #ZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZNZ

def sample(mn, mx): #* * * * * * * * * * * * * * * * * * * * * * * * * #
    """ build random enemies and buddies """
    def sample_funk(x): # ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` *    #
        """ Yeah, my first nested function """                         
        y = g[:] # , , , , , , , , , , , , , , Copy Ninja Kakashi *    #
        y.remove(x) #_____________________________________________*    #
        y = group(random.sample(y, random.randint(mn, mx))) #     *    #
        y.sort() #                                                *    #
        return y #~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ *    #
    return group(map(sample_funk, g)) #................................#

if sys.argv[1:]: #-----------------------------------------------------+
    n, s, k, p, b = map(int, sys.argv[1:]) #          make no mistake! |
    g = group(range(n)) #                                              |
    buddy = sample(n//2 + 1, n - 1) #                                  |
    enemy = sample(0, k) #                                             |
else: #----------------------------------------------------------------+
    n = 8 #----------------------------------------- number of persons |
    s = 3 #_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ number of subgroups |
    k = 4 #................................ maximum enemies per person |
    p = 0 #""""""""""""""""""""""""""""" maximum enemies in a subgroup |
    g = group(range(n)) #,,,,,,,,,,,,,,,,,,,,,,,, the group of persons |
    b = 1 #:::::::::::::::::::::::::::::::::::::::::::::::: book owner |
    buddy = [group([1, 3, 4, 5, 7]), #-----------  ----   ------ ------+
             group([0, 4, 5, 6, 7]), #            -                    |
             group([0, 1, 3, 6, 7]), #                                 |
             group([0, 1, 4, 5, 6, 7]), #        -                     |
             group([0, 1, 2, 3, 6, 7]), #                -             |
             group([0, 2, 3, 4, 7]), #                 -               |
             group([0, 1, 2, 3, 4, 5, 7]), #            -              |
             group([0, 1, 3, 4, 5])] #                          -      |
    enemy = [group([1, 5, 6]), #---------------------------------------+
             group([5]), #                                e7àTe noBe4e |
             group([0, 6]), #                                          |
             group([5, 6]), #                                          |
             group([]), #                                              |
             group([4]), #                                             |
             group([1, 2, 4, 7]), #                                    |
             group([0])] #---------------------------------------------+

def getnom(j): #.... .  .    .        .                o               o
    if j < len(nom): #                                                 o
        return nom[j] #                                                o
    else: #                                                            o
        return "Dwarf" + str(j) #.... .  .    .        .               .

nom = ["Anton", #======================================================_
       "Bobby", #                                                      _
       "Todor", #                                                      _
       "Han Solo", #                                                   _
       "Dart Vader", #                                                 _
       "Rand", #                                                       _
       "D'Artagnan", #                                                 _
       "Legolas", #                                                    _
       "qq", #                                                         _
       "Harry (the H-Pawn)"] #=========================================_

def dump(colleagues): #:::::::::::::::::::::::::::::::::::::::::::::::::
    for i, j in enumerate(colleagues): #                              ::
        print(getnom(i).ljust(18, '_'), j) #::::::::::::::::::::::::::::

def discussion_time(): #::..::..::..::..::..::..::..::..::..::..::..::..
    print("Discussion Time:") #                                       ..
    dump(enemy) #                                                     ..
    root = node([], g) #                                              ..
    for k in Partition(n, s): #                                       ..
        print(k) #                                                    ..
        walk(root, k) #                                               ..
        if stk: #                                                     ..
            print(get_leaf_str(stk[0])) #                             ..
        else: #                                                       ..
            print("No Solution") #                                    ..
        stk.clear() #:..::..::..::..::..::..::..::..::..::..::..::..::..

f = buddy #                                                   shortcut `

def ck(i, j): #`````````````````````````````````````````````````````````
    """ ck if buddy[i][j] has already read the book """
    return next((True for rec in stk if f[i][j] == rec[2]), False) #````

def book_cycle(): #`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`
    for ls in f: ls.append(n) #                           add Sentinel `
    i = b #                     person passing the book to his friends `
    j = 0 #                                     receiver index in f[i] `
    levl = 0 #                           tree level (number of passes) `
    stk.append((0, 0, b)) #                                            `
    while True: #                                                      `
        if not ck(i, j): #              ck if f[i][j] has had the book `
            levl += 1 #                                             OK `
            stk.append((i, j, f[i][j])) #                              `
            i = f[i][j] #                                 switch roles `
            j = 0 #      set receiver to the first friend in f[i] list `
            continue #                                                 `
        if f[i][j] == b and levl == n - 1: #                ar ve don? `
            stk.append((i, j, f[i][j])) #                              `
            return #                                               yp! `
        while True: #                                                  `
            j += 1 #                                    ck next friend `
            if f[i][j] != n: #                                         `
                break #                                                `
            rec = stk.pop() #                         no solution here `
            i, j = rec[:-1] #                 try with i's next friend `
            levl -= 1 #`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`, update level `
    
def reading_time(): #'''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Reading Time:") #                                           '
    dump(buddy) #                                                      '
    book_cycle() #                                                     '
    for rec in stk[1:]: #                                              '
        print(getnom(rec[0]), #                                        '
              getnom(buddy[rec[0]][rec[1]])) #                         '
    stk.clear() #'''''''''''''''''''''''''''''''''''''''''''''''''''''''

def suntory_time(): #---------------------------------------------------
    print("For relaxing times, make it Suntory Time!") #----------------

reading_time()
discussion_time()
suntory_time()
