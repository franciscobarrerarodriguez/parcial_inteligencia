def beautify(arr):
    result = ""
    for i in range(len(arr)):
        result = result+"{}\n".format(arr[i])
    return result
