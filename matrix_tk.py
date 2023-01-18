import tkinter as tk
from tkinter import messagebox
import numpy as np
from numpy import array, linalg


def transpose():
    try:
        matrix = array([[float(entry.get()) for entry in row] for row in entries])
        result = np.transpose(matrix).tolist()
        message = ""
        for row in result:
            message += " ".join(str(x) for x in row) + "\n"
        messagebox.showinfo("Transpose", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def determinant():
    try:
        matrix = array([[float(entry.get()) for entry in row] for row in entries])
        result = np.linalg.det(matrix)
        messagebox.showinfo("Determinant", result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def inverse():
    try:
        matrix = [[float(entry.get()) for entry in row] for row in entries]
        inverse_matrix = np.linalg.inv(matrix)
        message = ""
        for row in inverse_matrix:
            message += " ".join(str(x) for x in row) + "\n"
        messagebox.showinfo("Inverse", message)
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "Matrix is not invertible")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def eigenvalues():
    try:
        matrix = [[float(entry.get()) for entry in row] for row in entries]
        eigenvalues = np.linalg.eigvals(matrix)
        message = "Eigenvalues: " + ", ".join(str(x) for x in eigenvalues)
        messagebox.showinfo("Eigenvalues", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def eigenvectors():
    try:
        matrix = [[float(entry.get()) for entry in row] for row in entries]
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        message = "Eigenvectors:\n"
        for i, eigenvector in enumerate(eigenvectors):
            message += f"for eigenvalue {eigenvalues[i]}: {eigenvector}\n"
        messagebox.showinfo("Eigenvectors", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def spectral_projector():
    try:
        matrix = [[float(entry.get()) for entry in row] for row in entries]
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        projector = np.zeros((len(matrix), len(matrix)))
        for i in range(len(matrix)):
            projector += eigenvalues[i] * np.outer(eigenvectors[:,i], eigenvectors[:,i])
        message = "Spectral projector:\n"
        for row in projector:
            message += " ".join(str(x) for x in row) + "\n"
        messagebox.showinfo("Spectral Projector", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def create_matrix():
    global entries
    matrix_size = size_entry.get().split(",")
    if not all(map(lambda x: x.isnumeric(), matrix_size)):
        messagebox.showerror("Error", "Invalid input")
        return 
    matrix_size = tuple(map(int, matrix_size))
    for i in range(matrix_size[0]):
        row = []
        for j in range(matrix_size[1]):
            entry = tk.Entry(root)
            entry.grid(row=i, column=j)
            row.append(entry)
        entries.append(row)

    transpose_button = tk.Button(root, text="Transpose", command=transpose)
    transpose_button.grid(row=matrix_size[0], column=0)
    determinant_button = tk.Button(root, text="Determinant", command=determinant)
    determinant_button.grid(row=matrix_size[0], column=1)
    inverse_button = tk.Button(root, text="Inverse", command=inverse)
    inverse_button.grid(row=matrix_size[0], column=2)
    eigenvalues_button = tk.Button(root, text="Eigenvalues", command=eigenvalues)
    eigenvalues_button.grid(row=matrix_size[0], column=3)
    eigenvectors_button = tk.Button(root, text="Eigenvectors", command=eigenvectors)
    eigenvectors_button.grid(row=matrix_size[0], column=4)
    spectral_projector_button = tk.Button(root, text="Spectral Projector", command=spectral_projector)
    spectral_projector_button.grid(row=matrix_size[0], column=5)
    size_label.grid_remove()
    size_entry.grid_remove()
    create_matrix_button.grid_remove()

root = tk.Tk()
root.title("Matrix Calculator")

size_label = tk.Label(root, text="Enter the size of the matrix (rows,columns)")
size_label.grid(row=0, column=0)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1)

create_matrix_button = tk.Button(root, text="Create Matrix", command=create_matrix)
create_matrix_button.grid(row=0, column=2)

entries = []

root.mainloop()

