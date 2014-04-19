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