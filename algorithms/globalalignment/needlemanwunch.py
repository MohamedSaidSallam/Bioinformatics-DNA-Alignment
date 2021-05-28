import algorithms.util.printing as printing


def addToAll(array, v1, v2):
    for item in array:
        item[0] += v1
        item[1] += v2
    return array


def getTraceback(matrix, i, j, seq1, seq2):
    solutions = []
    if not(i > 0 and j > 0):
        solutions.append([])
        if i > 0:
            solutions[0].append(seq1[:i])
            solutions[0].append('_' * len(seq1[:i]))
        elif j > 0:
            solutions[0].append('_' * len(seq2[:j]))
            solutions[0].append(seq2[:j])
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


def initMatrix(seq1Length, seq2Length, gapPenalty):
    matrix = [[]]
    for i in range(seq1Length+1):
        matrix[0].append(i * gapPenalty)
    for i in range(1, seq2Length+1):
        matrix.append([i * gapPenalty] + [0 for i in range(seq1Length)])
    return matrix


def needlemanWunch(gapPenalty, match, misMatch, seq1, seq2):
    matrix = initMatrix(len(seq1), len(seq2), gapPenalty)

    for j in range(1, len(seq1)+1):
        for i in range(1, len(seq2)+1):
            matrix[i][j] = max(matrix[i-1][j-1] + (match if seq1[j-1] == seq2[i-1] else misMatch),
                               matrix[i-1][j]+gapPenalty, matrix[i][j-1]+gapPenalty)

    printing.printMatrix(seq1, seq2, matrix)
    print()
    printing.printTraceback(getTraceback(
        matrix, len(seq1), len(seq2), seq1, seq2))


if __name__ == "__main__":
    needlemanWunch(
        gapPenalty=-1,
        match=2,
        misMatch=-1,
        seq1="ACGCTG",
        seq2="CATGT"
    )
    # 0       -1      -2      -3      -4      -5      -6
    # -1      -1      1       0       -1      -2      -3
    # -2      1       0       0       -1      -2      -3
    # -3      0       0       -1      -1      1       0
    # -4      -1      -1      2       1       0       3
    # -5      -2      -2      1       1       3       2
    # [['_ACGCTG', 'CATG_T_'], ['ACGCTG_', '_C_ATGT'], ['ACGCTG_', '_CA_TGT']]
