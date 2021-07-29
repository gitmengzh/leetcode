"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
    数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：
    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。

示例 1：
输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

示例 2：
输入：board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

提示：
    board.length == 9
    board[i].length == 9
    board[i][j] 是一位数字或者 '.'

链接：https://leetcode-cn.com/problems/valid-sudokus
"""


def isValidSudoku(board):
    # hashmap=dict()
    # for r in range(9):
    #     for c in range(9):
    #         val = board[r][c]
    #         if val != '.':
    #             if not val in hashmap: hashmap[val]=[[r, c, r//3, c//3]] # 没有收录就收录它
    #             else:
    #                 for old_r, old_c, zone_r, zone_c in hashmap[val]: # 收录了就比较它
    #                     if r//3 == zone_r and c//3 == zone_c: return False # 在同一区域
    #                     if r==old_r or c==old_c: return False # 在同一行或者列
    #                 hashmap[val].append([r, c, r//3, c//3]) # 更新哈希表
    # return True

    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3  #  将九宫格分为9个区域

                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1          # dict.get(key, default=None) key -- 字典中要查找的键。
                                                                #  default -- 如果指定键的值不存在时，返回该默认值。
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True



def isValidSudoku2(board):

    temp_cell = [[] for i in range(9)]
    for i in range(9):
        temp_row = []
        temp_col = []
        for j in range(9):
            num_row = board[i][j]
            num_col = board[j][i]
            cell_row = (i//3)*3 + j // 3
            # cell_col = (j//3)*3 + i // 3
            if num_row != '.' and num_row not in temp_row:
                temp_row.append(num_row)
            else:
                if num_row != '.':
                    return False
            if num_col != '.' and num_col not in temp_col:
                temp_col.append(num_col)
            else:
                if num_col != '.':
                    return False
            if num_row != '.' and num_row not in temp_cell[cell_row]:
                temp_cell[cell_row].append(num_row)
            else:
                if num_row != '.':
                    return False

    return True







if __name__ == "__main__":
    board =[["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]



    print(isValidSudoku2(board1))