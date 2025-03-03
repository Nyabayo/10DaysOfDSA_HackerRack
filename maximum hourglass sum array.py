def hourglassSum(arr):
    max_sum = -float('inf')  # Start with the smallest possible number

    # Loop through all possible hourglass starting points
    for i in range(4):  # Rows (0 to 3)
        for j in range(4):  # Columns (0 to 3)
            # Extract the hourglass sum
            hg_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            # Update max_sum if the new hourglass sum is larger
            max_sum = max(max_sum, hg_sum)

    return max_sum  # Return after all hourglasses are checked

# Sample Input
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# Output the result
print(hourglassSum(arr))  
