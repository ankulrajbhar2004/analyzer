# NumPy Analyzer

A beginner-friendly **Python CLI project** built with **NumPy** to perform different array operations, mathematical calculations, array manipulation, searching, sorting, filtering, and statistical analysis.

This project is designed to practice **Python, Object-Oriented Programming (OOP), and NumPy** concepts through a simple menu-driven application.

## 🚀 Features

### 1. Create NumPy Arrays
Create different types of arrays by entering values manually:

- 1D Array
- 2D Array
- 3D Array

The program automatically converts the entered values into NumPy arrays.

### 2. Mathematical Operations

Perform mathematical operations on the created array:

- Addition
- Subtraction
- Multiplication
- Division

The program asks the user to enter another array with the same shape and performs the selected operation.

### 3. Combine & Split Arrays

The project provides options to:

- Combine two arrays using `np.concatenate()`
- Split an array into two parts using `np.array_split()`

### 4. Search, Sort & Filter

You can perform several operations on the array:

#### Search
Check whether a particular value exists in the array.

#### Sort
Sort array elements using:

```python
np.sort()
```

#### Filter
Filter values using Boolean masking:

- Even numbers
- Odd numbers

Example:

```python
mask = self.arr % 2 == 0
filtered_arr = self.arr[mask]
```

### 5. Aggregates & Statistics

Calculate important statistical values:

- Sum
- Mean
- Median
- Standard Deviation
- Variance

The project uses NumPy functions such as:

```python
np.sum()
np.mean()
np.median()
np.std()
np.var()
```

## 🛠️ Technologies Used

- **Python 3**
- **NumPy**
- Object-Oriented Programming
- Python `match-case`
- Command Line Interface (CLI)

## 📂 Project Structure

```text
NumPy-Analyzer/
│
├── main.py
└── README.md
```

> The Python filename can be different depending on how you save the project.

## ⚙️ Installation

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Install NumPy

Open your terminal or command prompt and run:

```bash
pip install numpy
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/numpy-analyzer.git
```

Move into the project directory:

```bash
cd numpy-analyzer
```

Run the program:

```bash
python main.py
```

## 📋 Main Menu

When the program starts, you will see:

```text
====================================
<<-------- WELCOME TO THE NUMPY ANALYZER -------->>
Choose an option

1. Create a Numpy Array.
2. Perform Mathematical Operation.
3. Combine or Split Array.
4. Search, Sort or Filter Array.
5. Compute Aggregates and Statistics
6. Exit...
====================================
```

## 💡 Example

### Creating a 1D Array

```text
Enter your choice: 1

Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array
4. Exit

Enter your choice: 1
Enter the number of elements: 5
Enter 5 elements separated by space: 10 20 30 40 50

[10 20 30 40 50]

1D Array Created Successfully...
```

### Sorting an Array

```text
Original array:
[50 10 40 20 30]

Sorted array:
[10 20 30 40 50]
```

### Filtering Even Numbers

```text
Original array:
[1 2 3 4 5 6]

Even numbers:
[2 4 6]
```

## 🎯 Learning Objectives

This project helped practice:

- Creating NumPy arrays
- Array reshaping
- NumPy arithmetic operations
- Array concatenation
- Array splitting
- Searching array values
- Sorting arrays
- Boolean indexing
- Filtering arrays
- Statistical calculations
- Python classes and objects
- `while` loops
- `match-case`
- User input handling

## 🔮 Future Improvements

Some features that can be added in the future:

- Input validation
- Support for floating-point numbers
- Save arrays to files
- Load arrays from files
- More mathematical operations
- Matrix multiplication
- Maximum and minimum values
- Transpose operation
- Unique values
- Array indexing and slicing
- More advanced statistical functions
- Better error handling
- Graphical User Interface (GUI)

## 👨‍💻 Author

**Ankul Udaybhan Rajbhar**

BCA Graduate | Python & Web Development Learner

## ⭐ Support

If you find this project useful for learning NumPy and Python, consider giving the repository a ⭐ on GitHub.

---

### 📌 Note

This project is created primarily for **learning and practicing NumPy and Python programming concepts**. It is a command-line based application and does not require a graphical interface.
