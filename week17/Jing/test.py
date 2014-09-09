def exist(board, word):
    if not board:
        return True if not word else False
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited = []
            if search(word, visited, board, i, j):
                return True
    return False
def search(word, visited, board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    print(visited)
    if (i,j) not in visited and word[0] == board[i][j]:
        if len(word) == 1:
            return True
        visited.append((i,j))
        return search(word[1:], visited, board, i-1, j) or search(word[1:], visited, board, i+1, j) or search(word[1:], visited, board, i, j-1) or search(word[1:], visited, board, i, j+1)
    return False

print(exist(["ABCE","SFES","ADEE"], "ABCESEEEFS"))
