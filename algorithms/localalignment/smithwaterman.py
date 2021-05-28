import algorithms.util.printing as printing


def addToAll(array, v1, v2):
    for item in array:
        item[0] += v1
        item[1] += v2
    return array


def getTraceback(matrix, i, j, seq1, seq2):
    solutions = []
    if matrix[j][i] == 0:
        solutions.append(['', ''])
        return solutions

    if seq1[i-1] == seq2[j-1]:
        branchSolutions = getTraceback(matrix, i-1, j-1, seq1, seq2)
        addToAll(branchSolutions, seq1[i-1], seq1[i-1])
        solutions += branchSolutions
    else:
        maxValue = max(matrix[j-1][i-1], matrix[j-1][i], matrix[j][i-1])
        if matrix[j-1][i-1] == maxValue:
            branchSolutions = getTraceback(matrix, i-1, j-1, seq1, seq2)
            addToAll(branchSolutions, seq1[i-1], seq2[j-1])
            solutions += branchSolutions
        if matrix[j][i-1] == maxValue:
            branchSolutions = getTraceback(matrix, i-1, j, seq1, seq2)
            addToAll(branchSolutions, seq1[i-1], '_')
            solutions += branchSolutions
        if matrix[j-1][i] == maxValue:
            branchSolutions = getTraceback(matrix, i, j-1, seq1, seq2)
            addToAll(branchSolutions, '_', seq2[j-1])
            solutions += branchSolutions

    return solutions


def printMatrix(seq1, seq2, matrix):
    sep = '\t|\t'
    print(*[' ', 'j', *seq1], sep=sep)
    rowStart = ['i', *seq2]
    for i in range(len(matrix)):
        print(rowStart[i], end=sep)
        print(*matrix[i], sep=sep)


def smithwaterman(gapPenalty, match, misMatch, seq1, seq2):
    matrix = [[0] * (len(seq1)+1) for _ in range(len(seq2)+1)]

    maxValue, maxI, MaxJ = 0, 0, 0
    for j in range(1, len(seq1)+1):
        for i in range(1, len(seq2)+1):
            currentValue = max(matrix[i-1][j-1] + (match if seq1[j-1] == seq2[i-1] else misMatch),
                               matrix[i-1][j] +
                               gapPenalty, matrix[i][j-1]+gapPenalty,
                               0)
            if currentValue >= maxValue:
                maxValue = currentValue
                maxI, MaxJ = j, i
            matrix[i][j] = currentValue

    printing.printMatrix(seq1, seq2, matrix)
    print()
    printing.printTraceback(getTraceback(matrix, maxI, MaxJ, seq1, seq2))


if __name__ == "__main__":
    smithwaterman(
        gapPenalty=-6,
        match=5,
        misMatch=-2,
        seq1="TGCTCGTA",
        seq2="TTCATA"
    )
# 0	0	0	0	0	0	0	0	0
# 0	5	0	0	5	0	0	5	0
# 0	5	3	0	5	3	0	5	3
# 0	0	3	8	2	10	4	0	3
# 0	0	0	2	6	4	8	2	5
# 0	5	0	0	7	4	2	13	7
# 0	0	3	0	1	5	2	7	18
#[['TCGTA', 'TCATA']]
