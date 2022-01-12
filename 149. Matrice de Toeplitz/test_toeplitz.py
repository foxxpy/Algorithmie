from toeplitz import is_toeplitz

def print_matrix(matrix):
    for row in matrix:
        print(row)
        
print("------------------------")
matrix = [[1,2,3],
          [3,1,2],
          [4,3,1]
          ]
print_matrix(matrix)
print(is_toeplitz(matrix))

print("------------------------")
matrix = [[1,2],
          [3,1],
          [16,3],
          [8,16],
          [7,8]
          ]
print_matrix(matrix)
print(is_toeplitz(matrix))

print("------------------------")
matrix = [[1,2,3,4,5,6,7,8,9],
          [10,1,2,3,4,5,6,7,8]
          ]
print_matrix(matrix)
print(is_toeplitz(matrix))

print("------------------------")
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]
print_matrix(matrix)
print(is_toeplitz(matrix))
