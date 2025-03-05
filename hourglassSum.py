def hourglassSum(arr):

    #Intitialize the maximum sum to a very low value (negative infinity)
    max_sum = -float('inf')

    #Loop through each possible starting point of the hourglass ( row 0to 3, column 0 to 3)
    for i in range(1,5):
        for j in range(1,5):

            #Calculate the sum of the current hourglass
            top = arr[i][j] + arr[i][j+1] +arr[i][j+2]
            mid = arr[i][j]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            #Calculate the total sum the hourglass
            hourglass_sum = top + mid + bottom

            #Update the max_sum if the current hourglass sum is greater
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum


        return max_sum
    #input array
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    #Calling the function
    result = hourglassSum(arr)

    print(f"The maximum houglass sum is: {result}")
