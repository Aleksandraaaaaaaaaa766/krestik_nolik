import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")

        self.reset_game()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.reset_button = tk.Button(self.root, text='Сбросить игру', command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)

    def on_button_click(self, i, j):
        if self.board[i][j] == '' and self.current_player:
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} победил!")
                self.disable_buttons()
            elif all(cell != '' for row in self.board for cell in row):
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Проверка строк, столбцов и диагоналей на победу
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
