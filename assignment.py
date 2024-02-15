import sys
with open(sys.argv[1], "r") as file:

    matrix= []
    for i in file:
        i = i.replace("\n","").split(" ")
        matrix.append(i)

score = 0

def delete(r, c):

    try:
        global matrix

        h = matrix[r][c]
        matrix[r][c] = " "
    except:
        pass

    try:
        if h == matrix[r][c+1]:
            delete(r,(c+1))
    except:
        pass

    try:
        if h == matrix[r][c-1]:
            delete(r, (c - 1))
    except:
        pass

    try:
        if h == matrix[r+1][c]:
            delete((r+1), c)
    except:
        pass

    try:
        if h == matrix[r - 1][c]:
            delete((r-1), c)
    except:
        pass

    try:
        if h == 'X':
            for j in range(len(matrix[r])):
                matrix[r][j] = " "
            for k in range(len(matrix)):
                matrix[k][c] = " "
    except :
        pass



while True:

    try:
        x = input('please enter a row and column number:')
        xlist=x.split(" ")
        if len(xlist) < 2 or len(xlist) > 2:
            print("Please enter Valid size!")
            continue
        if int(xlist[0]) >= len(matrix) or int(xlist[1]) > len(matrix[int(xlist[0])]):
            print("Please enter Valid size!")
            continue
        r = int(xlist[0])
        c = int(xlist[1])

        if matrix[r][c] == ' ':
            print("Please enter Valid size!")
            continue

        satır = -1
        sütun= -1
        letter = matrix[r][c]
        for i in matrix:
            a = len(i)
        b = len(matrix)
        delete(r,c)

        for i in matrix: #score
            for j in i:
                if j == " ":
                    if letter == "B":
                        score +=  9
                    if letter == "G":
                        score +=  8
                    if letter == "W":
                        score +=  7
                    if letter == "Y":
                        score +=  6
                    if letter == "R":
                        score +=  5
                    if letter == "P":
                        score +=  4
                    if letter == "O":
                        score +=  3
                    if letter == "D":
                        score +=  2
                    if letter == "F":
                        score +=  1
                    if letter == "X":
                        score += 0

        while b >= 0:
            b -= 1

            for i in matrix:
                satır += 1
                if satır >= len(matrix):
                    satır = 0

                for j in i:
                    sütun += 1
                    if sütun >= a:
                        sütun =0

                    if (j == " ") :

                        harf = matrix[satır - 1][sütun]
                        matrix[satır][sütun] = harf
                        matrix[satır - 1][sütun] = ' '

        for i in matrix:
            print(*i)
        print("your score is:", score)

    except:
        print("Please enter Valid size!")




