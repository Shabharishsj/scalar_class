
A = [[1,2,3],[4,5,6],[7,8,9]]


temp = []

for i in range(0,len(A)):
    summ = 0
    for j in range(0,len(A[0])):
        summ += A[j][i]
    
    temp.append(summ)

print(max(temp))


    


