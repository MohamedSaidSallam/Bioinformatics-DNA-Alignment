def printMatrix(seq1, seq2, matrix):
    sep = '\t|\t'
    print(*[' ', 'j', *seq1], sep=sep)
    rowStart = ['i', *seq2]
    for i in range(len(matrix)):
        print(rowStart[i], end=sep)
        print(*matrix[i], sep=sep)

def printTraceback(tracebback):
    print('Traceback:')
    for i, sol in enumerate(tracebback):
        print(f'\t#{i+1}')
        print(f'\t\tSequence 1: {sol[0]}')
        print(f'\t\tSequence 2: {sol[1]}')