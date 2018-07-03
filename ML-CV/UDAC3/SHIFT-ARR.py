arr = [1,2,3,4,5]

output = []
n = 5
front = arr[(-1*n):]
print(front)
output.extend(front)
end = arr[:((len(arr)-n))]
print(end)
output.extend(end)
print(output)



shift_right = lambda arr,n: arr if n == len(arr) else arr[(-1*n):] + arr[:((len(arr)-n))]

x = shift_right(arr, 5)
print(x)