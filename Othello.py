# Author: Nancy Yang
# GitHub username: NancyyKin
# Date: 06/05/2023
# Description: This program can track a 8x8 board of Othello. Some notable features is it can display a
# list of legal moves, display the current board status, and count up the number of pieces each player has.

class Othello:
    """Represents a round of the game Othello"""
    def __init__(self):
        self._players = {}
        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]
        self._wpieces = 2
        self._bpieces = 2

    def print_board(self):
        """Prints out the current board situation"""
        for each_row in self._board:
            a_row = " "
            for each_item in each_row:
                a_row += " " + each_item
            print(a_row)

    def create_player(self, player_name, color):
        """Takes the player's name and color and adds that player as an object with the Player class
        to the list of players"""
        self._players[color] = Player(player_name, color)

    def return_winner(self):
        """Compares each player's total pieces and returns the winner or if there is a tie"""
        if self._wpieces > self._bpieces:
            return "Winner is white player:" + " " + self._players["white"].get_name()
        elif self._wpieces < self._bpieces:
            return "Winner is black player:" + " " + self._players["black"].get_name()
        else:
            return "It's a tie"

    def return_available_positions(self, color):
        """Takes the color of the player and returns all the currently available positions for that player"""
        if color == "white":
            player = "O"
            opposition = "X"
        else:
            player = "X"
            opposition = "O"
        apositions = []  # available positions

        for lead_num in range(1, 9):
            for sub_num in range(1, 9):
                # checking row left to right
                if self._board[lead_num][sub_num] == ".":
                    if self._board[lead_num][sub_num+1] == opposition:
                        placeholder = sub_num + 1
                        while self._board[lead_num][placeholder] == opposition:
                            placeholder += 1
                        if self._board[lead_num][placeholder] == player:
                            apositions.append((lead_num, sub_num))
                # checking column top to bottom
                if self._board[sub_num][lead_num] == ".":
                    if self._board[sub_num+1][lead_num] == opposition:
                        placeholder = sub_num + 1
                        while self._board[placeholder][lead_num] == opposition:
                            placeholder += 1
                        if self._board[placeholder][lead_num] == player:
                            apositions.append((sub_num, lead_num))
            # checking diagonally down and to the right
            row_index = 1
            lead_holder = lead_num
            while lead_holder != 9 and row_index != 9:
                if self._board[lead_holder][row_index] == ".":
                    if self._board[lead_holder + 1][row_index + 1] == opposition:
                        row_holder = lead_holder + 1
                        col_holder = row_index + 1
                        while self._board[row_holder][col_holder] == opposition:
                            row_holder += 1
                            col_holder += 1
                        if self._board[row_holder][col_holder] == player:
                            apositions.append((lead_holder, row_index))
                lead_holder += 1
                row_index += 1
            # checking diagonally down and to the left
            row_index = 8
            lead_holder = lead_num
            while lead_holder != 0 and row_index != 0:
                if self._board[lead_holder][row_index] == ".":
                    if self._board[lead_holder - 1][row_index - 1] == opposition:
                        row_holder = lead_holder - 1
                        col_holder = row_index - 1
                        while self._board[row_holder][col_holder] == opposition:
                            row_holder -= 1
                            col_holder -= 1
                        if self._board[row_holder][col_holder] == player:
                            apositions.append((lead_holder, row_index))
                lead_holder -= 1
                row_index -= 1

            # checking diagonally down and to the left
            row_index = 8
            lead_holder = lead_num
            while lead_holder != 9 and row_index != 0:
                for next_index in range(row_index, 0, -1):
                    if self._board[lead_holder][next_index] == ".":
                        if self._board[lead_holder + 1][next_index - 1] == opposition:
                            row_holder = lead_holder + 1
                            col_holder = next_index - 1
                            while self._board[row_holder][col_holder] == opposition:
                                row_holder += 1
                                col_holder -= 1
                            if self._board[row_holder][col_holder] == player:
                                apositions.append((lead_holder, next_index))
                lead_holder += 1
                row_index -= 1

        for lead_num in range(8, 0, -1):
            for sub_num in range(8, 0, -1):
                # checking row right to left
                if self._board[lead_num][sub_num] == ".":
                    if self._board[lead_num][sub_num-1] == opposition:
                        placeholder = sub_num - 1
                        while self._board[lead_num][placeholder] == opposition:
                            placeholder -= 1
                        if self._board[lead_num][placeholder] == player:
                            apositions.append((lead_num, sub_num))
                # checking column bottom to top
                if self._board[sub_num][lead_num] == ".":
                    if self._board[sub_num-1][lead_num] == opposition:
                        placeholder = sub_num - 1
                        while self._board[placeholder][lead_num] == opposition:
                            placeholder -= 1
                        if self._board[placeholder][lead_num] == player:
                            apositions.append((sub_num, lead_num))
            # checking diagonal up and right
            row_index = 8
            lead_holder = lead_num
            while lead_holder != 9 and row_index != 0:
                for next_index in range(row_index, 0, -1):
                    if self._board[next_index][lead_holder] == ".":
                        if self._board[next_index - 1][lead_holder + 1] == opposition:
                            row_holder = next_index - 1
                            col_holder = lead_holder + 1
                            while self._board[row_holder][col_holder] == opposition:
                                row_holder -= 1
                                col_holder += 1
                            if self._board[row_holder][col_holder] == player:
                                apositions.append((next_index, lead_holder))
                lead_holder += 1
                row_index -= 1
            # checking diagonal up and left
            row_index = 8
            lead_holder = lead_num
            while lead_holder != 0 and row_index != 0:
                for next_index in range(row_index, 0, -1):
                    if self._board[next_index][lead_holder] == ".":
                        if self._board[next_index - 1][lead_holder - 1] == opposition:
                            row_holder = next_index - 1
                            col_holder = lead_holder - 1
                            while self._board[row_holder][col_holder] == opposition:
                                row_holder -= 1
                                col_holder -= 1
                            if self._board[row_holder][col_holder] == player:
                                apositions.append((next_index, lead_holder))
                lead_holder -= 1
                row_index -= 1
        remove_multiples = set(apositions)  # removes multiples
        apositions = list(remove_multiples)
        apositions.sort()   # sorts the list for easy reading
        return apositions

    def make_move(self, color, piece_position):
        """Takes the color and the new position add adds a that color's piece to that position.
        The board will be updated accordingly to game rules and returns the current board situation"""
        row = piece_position[0]
        col = piece_position[1]
        if color == "white":
            player = "O"
            opposition = "X"
        else:
            player = "X"
            opposition = "O"
        pieces_changed = 1
        self._board[row][col] = player
        # changing going up
        if self._board[row + 1][col] == opposition:
            prow = row
            orow = row + 1
            ocol = col
            while self._board[orow][ocol] == opposition:
                orow += 1
            if self._board[orow][ocol] == player:
                while self._board[prow + 1][ocol] == opposition:
                    self._board[prow + 1][ocol] = player
                    pieces_changed += 1
                    prow += 1
        # changing going down
        if self._board[row - 1][col] == opposition:
            prow = row
            orow = row - 1
            ocol = col
            while self._board[orow][ocol] == opposition:
                orow -= 1
            if self._board[orow][ocol] == player:
                while self._board[prow - 1][ocol] == opposition:
                    self._board[prow - 1][ocol] = player
                    pieces_changed += 1
                    prow -= 1
        # changing going right
        if self._board[row][col - 1] == opposition:
            pcol = col
            orow = row
            ocol = col - 1
            while self._board[orow][ocol] == opposition:
                ocol -= 1
            if self._board[orow][ocol] == player:
                while self._board[orow][pcol - 1] == opposition:
                    self._board[orow][pcol - 1] = player
                    pieces_changed += 1
                    pcol -= 1
        # changing going left
        if self._board[row][col + 1] == opposition:
            pcol = col
            orow = row
            ocol = col + 1
            while self._board[orow][ocol] == opposition:
                ocol += 1
            if self._board[orow][ocol] == player:
                while self._board[orow][pcol + 1] == opposition:
                    self._board[orow][pcol + 1] = player
                    pieces_changed += 1
                    pcol += 1
        # changing going up and left
        if self._board[row - 1][col - 1] == opposition:
            prow = row
            pcol = col
            orow = row - 1
            ocol = col - 1
            while self._board[orow][ocol] == opposition:
                orow -= 1
                ocol -= 1
            if self._board[orow][ocol] == player:
                while self._board[prow - 1][pcol - 1] == opposition:
                    self._board[prow - 1][pcol - 1] = player
                    pieces_changed += 1
                    prow -= 1
                    pcol -= 1
        # changing going down and right
        if self._board[row + 1][col + 1] == opposition:
            prow = row
            pcol = col
            orow = row + 1
            ocol = col + 1
            while self._board[orow][ocol] == opposition:
                orow += 1
                ocol += 1
            if self._board[orow][ocol] == player:
                while self._board[prow + 1][pcol + 1] == opposition:
                    self._board[prow + 1][pcol + 1] = player
                    pieces_changed += 1
                    prow += 1
                    pcol += 1
        # changing going left and up
        if self._board[row - 1][col + 1] == opposition:
            prow = row
            pcol = col
            orow = row - 1
            ocol = col + 1
            while self._board[orow][ocol] == opposition:
                orow -= 1
                ocol += 1
            if self._board[orow][ocol] == player:
                while self._board[prow - 1][pcol + 1] == opposition:
                    self._board[prow - 1][pcol + 1] = player
                    pieces_changed += 1
                    prow -= 1
                    pcol += 1
        # changing going down and right
        if self._board[row + 1][col - 1] == opposition:
            prow = row
            pcol = col
            orow = row + 1
            ocol = col - 1
            while self._board[orow][ocol] == opposition:
                orow += 1
                ocol -= 1
            if self._board[orow][ocol] == player:
                while self._board[prow + 1][pcol - 1] == opposition:
                    self._board[prow + 1][pcol - 1] = player
                    pieces_changed += 1
                    prow += 1
                    pcol -= 1

        if color == "white":
            self._wpieces += pieces_changed
            self._bpieces -= pieces_changed
            self._bpieces += 1
        else:
            self._bpieces += pieces_changed
            self._wpieces -= pieces_changed
            self._wpieces += 1
        return self._board

    def play_game(self, player_color, piece_position):
        """1. Takes the player's color and a new position for its piece and checks if it is valid
        2. If it is invalid, a list of the valid positions will be returned
        3. If it is valid, make_move() will be called and the board will be updated
        4. Checks if the game has reached its limit and returns an ending message counting up the pieces as well
        as calling return_winner()"""
        available_positions = self.return_available_positions(player_color)
        if piece_position in available_positions:
            self.make_move(player_color, piece_position)
            if self.return_available_positions("white") is None:
                if self.return_available_positions("black") is None:
                    self.return_winner()
                    print("Game is ended white piece: ", self._wpieces, " black piece: ", self._bpieces)
        else:
            print("Here are the valid moves:", available_positions)
            return "Invalid move"

 #   def display_apositions(self, color):
 #       the_list = self.return_available_positions(color)
 #       new_board = self._board
 #       for each_position in the_list:
 #           new_board[each_position[0]][each_position[1]] = "!"
 #       for each_row in new_board:
 #           a_row = " "
 #           for each_item in each_row:
 #               a_row += " " + each_item
 #           print(a_row)


class Player:
    """Represents a player for the game Othello"""
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_name(self):
        """Returns the name of the Player"""
        return self._name

    def get_color(self):
        """Returns the color of the player"""
        return self._color
