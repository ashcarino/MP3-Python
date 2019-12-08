def f(x):
    result = x**10+x+1 
    return result

def least_norm_error_vector(experimental_points,n):
    error_array=[0]*n 
    for i in range(0,n):
        error_array[i]=experimental_points[i][1] - f(experimental_points[i][0])
    return error_array

n=int(input("Enter number of experimental points you wish to input:"))
experimental_points=[] 

print("Now enter the data point in order pairs:")
for i in range(0,n):
    experimental_points.append([int(j) for j in input("Enter two value: ").split()])

error_array = least_norm_error_vector(experimental_points,n)
print("Error array is:\n")
print(error_array)
