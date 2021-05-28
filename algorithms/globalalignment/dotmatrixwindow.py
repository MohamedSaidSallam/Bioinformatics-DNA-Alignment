
def getSimilarity(seg1, seg2):
    count = 0
    for i in range(len(seg1)):
        count += int(seg1[i] == seg2[i])
    return count


def DotMatrixWindowScoring(windowSize, step, threshold, seq1, seq2):
    output = [[' '] * len(seq1) for _ in range(len(seq2))]
    for j in range(0, len(seq2) - windowSize+1, step):
        for i in range(0, len(seq1) - windowSize+1, step):
            if getSimilarity(seq1[i: i+windowSize], seq2[j: j+windowSize]) >= threshold:
                output[j + (windowSize//2)][i + (windowSize//2)] = 'x'
    print(*[' ', *seq1], sep='|')
    for i in range(len(output)):
        print(seq2[i] + '|', end='')
        print(*output[i], sep='|')


if __name__ == "__main__":
    DotMatrixWindowScoring(windowSize=9,
                           step=3,
                           threshold=4,
                           seq1="ACCTTGTCCTCTTTGCCC",
                           seq2="ACGTTGACCTGTAACCTC"
                           )
#  |A|C|C|T|T|G|T|C|C|T|C|T|T|T|G|C|C|C
# A| | | | | | | | | | | | | | | | | |
# C| | | | | | | | | | | | | | | | | |
# G| | | | | | | | | | | | | | | | | |
# T| | | | | | | | | | | | | | | | | |
# T| | | | |x| | | | | | | | |x| | | |
# G| | | | | | | | | | | | | | | | | |
# A| | | | | | | | | | | | | | | | | |
# C| | | | | | | |x| | | | | | | | | |
# C| | | | | | | | | | | | | | | | | |
# T| | | | | | | | | | | | | | | | | |
# G| | | | |x| | | | | |x| | | | | | |
# T| | | | | | | | | | | | | | | | | |
# A| | | | | | | | | | | | | | | | | |
# A| | | | | | | | | | | | | |x| | | |
# C| | | | | | | | | | | | | | | | | |
# C| | | | | | | | | | | | | | | | | |
# T| | | | | | | | | | | | | | | | | |
# C| | | | | | | | | | | | | | | | | |
