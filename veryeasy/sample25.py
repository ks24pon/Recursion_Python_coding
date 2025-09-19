# enumerate
def getMaxIndex(arr):
    maxValueIndex = 0
    for i, value in enumerate(arr):
        if value >= arr[maxValueIndex]:
            maxValueIndex = i
    return maxValueIndex