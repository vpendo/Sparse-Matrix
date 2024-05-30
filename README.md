# Sparse Matrix Operations

This project implements a sparse matrix class in Python, enabling efficient storage and operations on sparse matrices. The supported operations are addition, subtraction, and multiplication of sparse matrices. The matrices can be loaded from files, manipulated, and the results can be saved back to a file.

## Features

- Efficient storage of sparse matrices
- Addition, subtraction, and multiplication of sparse matrices
- Load matrices from text files
- Save result matrices to text files

## Project Structure

- `sparse_matrix.py`: Main script containing the `SparseMatrix` class and the `main` function to execute the operations.
- `sample_input/`: Directory for input files.
- `output/`: Directory where the result files will be saved.

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:

```sh
    git clone https://github.com/vpendo/   Sparse-Matrix.git
```
cd Sparse-Matrix

2. Run the script:

    python sparse_matrix.py <input_file_1> <input_file_2> <output_file>


3. The script will prompt you to select an operation:

       Please choose an operation ``(add, sub, mul):``

Enter `add`, `sub`, or `mul `to perform the desired operation.

4. Saving the Result

The result will be saved in the specified `result.txt` output file `in the `output/ directory`. 

### Example of how to run the script

- `python sparse_matrix.py sample_input/easy_sample_02_3.txt sample_input/easy_sample_02_3.txt .\result.txt`

## Author
- Vestine Pendo

- GitHub: vpendo

- Email: v.pendo@alustudent.com

## License
This project is licensed under the MIT License - see the LICENSE file for details.



