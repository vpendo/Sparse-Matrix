import sys
import os

class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, matrixFilePath=None):
        self.matrix = {}
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            self.numRows = int(lines[0].split('=')[1].strip())
            self.numCols = int(lines[1].split('=')[1].strip())

            for line in lines[2:]:
                line = line.strip()
                if line:
                    if line[0] != '(' or line[-1] != ')':
                        raise ValueError("Input file has wrong format")

                    parts = line[1:-1].split(',')
                    if len(parts) != 3:
                        raise ValueError("Input file has wrong format")

                    row, col, value = map(int, parts)
                    if value != 0:
                        self.set_element(row, col, value)

    def get_element(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.matrix[(currRow, currCol)] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[(currRow, currCol)]

    def __add__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")

        result = SparseMatrix(self.numRows, self.numCols)
        keys = set(self.matrix.keys()).union(other.matrix.keys())

        for key in keys:
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) + other.get_element(key[0], key[1]))

        return result

    def __sub__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")

        result = SparseMatrix(self.numRows, self.numCols)
        keys = set(self.matrix.keys()).union(other.matrix.keys())

        for key in keys:
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) - other.get_element(key[0], key[1]))

        return result

    def __mul__(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions are not compatible for multiplication")

        result = SparseMatrix(self.numRows, other.numCols)

        for i in range(self.numRows):
            for j in range(other.numCols):
                dot_product = 0
                for k in range(self.numCols):
                    dot_product += self.get_element(i, k) * other.get_element(k, j)
                result.set_element(i, j, dot_product)

        return result

def save_output(matrix, outputFilePath):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)

    with open(outputFilePath, 'w') as file:
        file.write(f"rows={matrix.numRows}\n")
        file.write(f"cols={matrix.numCols}\n")
        for (row, col), value in sorted(matrix.matrix.items()):
            file.write(f"({row}, {col}, {value})\n")

def main():
    if len(sys.argv) < 5:
        print("Usage: sparse_matrix.py <operation> <input_file_1> <input_file_2> <output_file>")
        return

    operation = sys.argv[1]
    input_file_1 = sys.argv[2]
    input_file_2 = sys.argv[3]
    output_file = os.path.join("output", sys.argv[4])

    try:
        matrix1 = SparseMatrix(matrixFilePath=input_file_1)
        matrix2 = SparseMatrix(matrixFilePath=input_file_2)
    except ValueError as e:
        print(e)
        return

    if operation == 'add':
        result = matrix1 + matrix2
    elif operation == 'sub':
        result = matrix1 - matrix2
    elif operation == 'mul':
        result = matrix1 * matrix2
    else:
        print("Invalid operation. Use 'add', 'sub', or 'mul'.")
        return

    save_output(result, output_file)
    print(f"Operation {operation} completed. Result saved to {output_file}")

if __name__ == "__main__":
    main()

