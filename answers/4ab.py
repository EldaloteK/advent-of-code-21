#!/usr/bin/env python3

with open("../input/4ab.txt", "r") as report:
    bingo_content = [r.strip() for r in report.readlines()]

    # Part A
    bingo_nums_completed = False
    bingo_boards = []
    temp_arr = []

    for line in bingo_content:
        if (not bingo_nums_completed):
            if not line:
                bingo_nums_completed = True
                continue
            else:
                bingo_numbers = (line.strip().split(","))
                continue

        if (bingo_nums_completed):
            if not line:
                bingo_boards.append(temp_arr)
                temp_arr = []
                continue
            else:
                temp_arr.append(line.strip().split())
                continue

    bingo_boards.append(temp_arr)

    won = False
    board_sums = 0
    final_num = 0

    for bingo_num in bingo_numbers:
        if (won):
            break

        for board in bingo_boards:
            for board_line in board:
                if (bingo_num in board_line):
                    board_line[board_line.index(bingo_num)] = '-1'

                if (not(won)):
                    for k in board_line:
                        if (all(x == '-1' for x in [row[board_line.index(k)] for row in board]) or (all(y == '-1' for y in board_line))):
                            final_num = bingo_num
                            for z in board:
                                board_sums += (sum(int(i) for i in z if i != '-1'))

                            print('Part A score:', int(final_num) * int(board_sums))

                            won = True
                            break
                        else:
                            continue


    # Part B
    boards_won = []
    for bingo_num in bingo_numbers:
        if (len(boards_won) == len(bingo_boards)):
            break

        for board in bingo_boards:
            if (bingo_boards.index(board) in boards_won):
                continue
            won = False
            board_sums = 0
            final_num = 0

            for board_line in board:
                if (bingo_num in board_line):
                    board_line[board_line.index(bingo_num)] = '-1'
                rowsize = len(board_line) 
                for k in range(0, rowsize):
                    if won:
                        break

                    if (all(row[k] == '-1' for row in board) or (all(y == '-1' for y in board_line))):
                        final_num = bingo_num
                        for z in board:
                            board_sums += (sum(int(i) for i in z if i != '-1'))

                        won = True
                        boards_won.append(bingo_boards.index(board))
                        break
                    else:
                        continue
                if won:
                    break
            if (won and len(boards_won) == len(bingo_boards)):
                print('Last board to win: ')
                print(board)
                print('Part B Score:', int(final_num) * int(board_sums))
                continue
