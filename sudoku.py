# Sudoku validator.
# Function checksudoku takes a list, p, comprising nine lists with nine elements each.
# It then checks if each 3x3 square contains numbers 1-9, then checks each row, then each column.

test = [[5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]

test2 = [[0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,6,0,7,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,2,0,3,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,8,0,0,0,5,0],
         [0,0,0,0,0,0,0,0,0]]        

ideallist = [1,2,3,4,5,6,7,8,9]

def issudoku(p):
    if type(p) is not list:
        return False
    if len(p) != 9:
        return False
    if len(max(p)) != 9 or len(min(p)) != 9:
        return False
    return True        

def checkboxes(p):
    for i in xrange(3):
        mult = i * 3
        box1 = p[mult][:3] + p[mult+1][:3] + p[mult+2][:3]
        box1.sort()
        if box1 != ideallist:
            return False
        box2 = p[mult][3:6] + p[mult+1][3:6] + p[mult+2][3:6]
        box2.sort()
        if box2 != ideallist:
            return False
        box3 = p[mult][6:] + p[mult+1][6:] + p[mult+2][6:]
        box3.sort()
        if box3 != ideallist:
            return False
    return True

def checkrows(p):
    for i in p:
        q = []
        q.extend(i)
        q.sort()
        if q != ideallist:
            return False
    return True

def checkcolumns(p):
    for x in xrange(9):
        q = []
        for i in xrange(9):
            q.append(p[i][x])
        q.sort()
        if q != ideallist:
            return False
    return True
    
def checksudoku(p):
    if issudoku(p) == False:
        print "Input must be a list of 9 lists with 9 numbers."
        return False
    if checkboxes(p) == False:
        return False
    if checkrows(p) == False:
        return False
    if checkcolumns(p) == False:
        return False
    return True    

# Function checkinput takes a list of lists (p), places inputnum in p[whichlist][whichelement],
# and checks whether it violates any rules.  As-yet-unknown entries are designated as zeroes.

test2 = [[0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,6,0,7,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,2,0,3,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,8,0,0,0,5,0],
         [0,0,0,0,0,0,0,0,0]]

def checkinput(p, inputnum, whichlist, whichelement):
    if issudoku(p) == False:
        print "You need a sudoku square to check against."
        return False
    # Should I check if p[whichlist][whichelement] is already used by another number?
    if inputnum in p[whichlist]:
        print "Whoops!  Check the row you're putting it in."
        return False
    for i in p:
        if i[whichelement] == inputnum:
            print "Check the column you're putting it in."
            return False
    wl = whichlist / 3
    we = whichelement / 3
    q = []
    q.extend(p[wl*3][(we*3):(we*3)+3])
    q.extend(p[wl*3+1][(we*3):(we*3)+3])
    q.extend(p[wl*3+2][(we*3):(we*3)+3])
    if inputnum in q:
        print "Check the 9-number area around where you're putting in the number."
        return False
    p[whichlist][whichelement] = inputnum
    print "No problems putting it here!"
    return p

# Function suggestnums takes a sudoku square (p) and coordinates (via whichlist and whichelement)
# and determines which numbers can possibly be put into that cell.
    
def suggestnums(p, whichlist, whichelement):
    if p[whichlist][whichelement] != 0:
        print "This cell is already full."
        return None
    usable = [1,2,3,4,5,6,7,8,9]
    for i in p[whichlist]:
        if i in usable:
            usable.remove(i)
    for i in p:
        if i[whichelement] in usable:
            usable.remove(i[whichelement])
    wl = whichlist / 3
    we = whichelement / 3
    q = []
    q.extend(p[wl*3][(we*3):(we*3)+3])
    q.extend(p[wl*3+1][(we*3):(we*3)+3])
    q.extend(p[wl*3+2][(we*3):(we*3)+3])
    for i in q:
        if i in usable:
            usable.remove(i)
    print usable
    return usable