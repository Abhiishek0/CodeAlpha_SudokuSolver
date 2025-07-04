import tkinter as tk
from tkinter import messagebox

# === Window Setup ===
root = tk.Tk()
root.title("🧩 Sudoku Solver – CodeAlpha")
cells = [[None for _ in range(9)] for _ in range(9)]

#  Backtracking Solver
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# === GUI Logic ===
def get_input():
    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            val = cells[row][col].get()
            current_row.append(int(val) if val.isdigit() else 0)
        board.append(current_row)
    return board

def display_solution(board):
    for row in range(9):
        for col in range(9):
            cells[row][col].delete(0, tk.END)
            cells[row][col].insert(0, str(board[row][col]))

def solve():
    board = get_input()
    if solve_sudoku(board):
        display_solution(board)
    else:
        messagebox.showerror("Error", "❌ No solution exists!")

def clear_grid():
    for row in range(9):
        for col in range(9):
            cells[row][col].delete(0, tk.END)

# === Create Sudoku Grid ===
for i in range(9):
    for j in range(9):
        e = tk.Entry(root, width=2, font=('Arial', 20), justify='center')
        e.grid(row=i, column=j, padx=5, pady=5)
        cells[i][j] = e

# === Buttons ===
solve_btn = tk.Button(root, text="✅ Solve", command=solve, bg='green', fg='white', font=('Arial', 14))
solve_btn.grid(row=9, column=3, columnspan=2, pady=10)

clear_btn = tk.Button(root, text="🧹 Clear", command=clear_grid, bg='red', fg='white', font=('Arial', 14))
clear_btn.grid(row=9, column=5, columnspan=2, pady=10)

# === Run App ===
root.mainloop()
