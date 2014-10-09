"""
dynamic programming for sequence alignment prolem
"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    build the scoring matrix
    """
    alphabet.add('-')
    scoring_matrix = {key: {} for key in alphabet}
    for char in alphabet:
        for second_char in alphabet:
            if '-' in (char, second_char):
                scoring_matrix[char][second_char] = dash_score
            elif char == second_char:
                scoring_matrix[char][second_char] = diag_score
            elif char != second_char:
                scoring_matrix[char][second_char] = off_diag_score
    return scoring_matrix

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    compute alignment_matrix
    """
    len_x = len(seq_x)
    len_y = len(seq_y)
    align_matrix = [[0]*(len_y+1) for _ in range(len_x+1)]
    align_matrix[0][0] = 0
    for row in range(1, len_x+1):
        align_matrix[row][0] = align_matrix[row-1][0]+scoring_matrix[seq_x[row-1]]['-']
        if not global_flag and align_matrix[row][0] < 0:
            align_matrix[row][0] = 0
    for col in range(1, len_y+1):
        align_matrix[0][col] = align_matrix[0][col-1]+scoring_matrix['-'][seq_y[col-1]]
        if align_matrix[0][col] < 0 and not global_flag:
            align_matrix[0][col] = 0
    for row in range(1, len_x+1):
        for col in range(1, len_y+1):
            align_matrix[row][col] = max(align_matrix[row-1][col-1]+scoring_matrix[seq_x[row-1]][seq_y[col-1]],
                    align_matrix[row-1][col]+scoring_matrix[seq_x[row-1]]['-'],
                    align_matrix[row][col-1]+scoring_matrix['-'][seq_y[col-1]])
            if align_matrix[row][col] < 0 and not global_flag:
                align_matrix[row][col] = 0
    return align_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    compute global alignment
    """
    row = len(seq_x)
    col = len(seq_y)
    align_x = align_y = ""
    score = alignment_matrix[row][col]
    while row != 0 and col != 0:
        if alignment_matrix[row][col] == alignment_matrix[row-1][col-1] + scoring_matrix[seq_x[row-1]][seq_y[col-1]]:
            align_x = seq_x[row-1]+align_x
            align_y = seq_y[col-1]+align_y
            row -= 1
            col -= 1
        elif alignment_matrix[row][col] == alignment_matrix[row-1][col] + scoring_matrix[seq_x[row-1]]['-']:
            align_x = seq_x[row-1] + align_x
            align_y = '-' + align_y
            row -= 1
        else:
            align_y = seq_y[col-1]+align_y
            align_x = '-' + align_x
            col -= 1
    while row != 0:
        align_x = seq_x[row-1]+align_x
        align_y = '-' + align_y
        row -= 1
    while col != 0:
        align_y = seq_y[col-1]+align_y
        align_x = '-' + align_x
        col -= 1
    return (score, align_x, align_y)



def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    compute local alignment
    """
    score = l_row = l_col  = 0
    for row in range(len(alignment_matrix)):
        for col in range(len(alignment_matrix[0])):
            if alignment_matrix[row][col] > score:
                score = alignment_matrix[row][col]
                l_row = row
                l_col = col

    align_x = align_y = ""
    while alignment_matrix[l_row][l_col] != 0 and l_row != 0 and l_col != 0:
        if alignment_matrix[l_row][l_col] == alignment_matrix[l_row-1][l_col-1] + scoring_matrix[seq_x[l_row-1]][seq_y[l_col-1]]:
            align_x = seq_x[l_row-1]+align_x
            align_y = seq_y[l_col-1]+align_y
            l_row -= 1
            l_col -= 1
        elif alignment_matrix[l_row][l_col] == alignment_matrix[l_row-1][l_col] + scoring_matrix[seq_x[l_row-1]]['-']:
            align_x = seq_x[l_row-1] + align_x
            align_y = '-' + align_y
            l_row -= 1
        else:
            align_y = seq_y[l_col-1]+align_y
            align_x = '-' + align_x
            l_col -= 1
    while alignment_matrix[l_row][l_col] != 0 and l_row != 0:
        align_x = seq_x[l_row-1]+align_x
        align_y = '-' + align_y
        l_row -= 1
    while alignment_matrix[l_row][l_col] != 0 and l_col != 0:
        align_y = seq_y[l_col-1]+align_y
        align_x = '-' + align_x
        l_col -= 1
    return (score, align_x, align_y)

scoring_matrix = build_scoring_matrix(set('ACTG'), 10, 4, 10)
seq_x = 'AAC'
seq_y = 'TAAT'
alignment_matrix_local =  compute_alignment_matrix(seq_x, seq_y, scoring_matrix, 0)
alignment_matrix_global =  compute_alignment_matrix(seq_x, seq_y, scoring_matrix, 1)
print 'global', alignment_matrix_global
print 'local ', alignment_matrix_local
print alignment_matrix_global[2][2]
print alignment_matrix_local[2][2]
