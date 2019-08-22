# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through zero to len(arr)-1 elements bc the last will end up being the highest number. When you get to it you'll return arr
    for i in range(0, len(arr) - 1):
        cur_index = i #pivot set to temp
        #loop through again comparing the pivot to the other items in the array
        for j in range(i+1, len(arr)):
            #if a number in the array is less than the pivot
            if arr[j] < arr[cur_index]:
                #reset the pivot to the number
                cur_index = j
            #swap the order of the sorted array is the number is less than the pivot
        arr[i], arr[cur_index] = arr[cur_index], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True 
    while swap: 
        swap = False #while running in the loop set swap to false
        #loop through zero to len(arr)-1 elements bc the last will end up being the highest number. When you get to it you'll return arr
        for n in range(len(arr)-1):
            #if the pivot is greater than the item next to it in the array
            if arr[n] > arr[n+1]:
                #change positions with number and pivot
                arr[n], arr[n+1] = arr[n+1], arr[n]
                #reset swap to start the comparison loop over
                swap = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr