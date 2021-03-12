N = int(input())
X = int(input())
Y = int(input())
T = int(input())

A = [i for i in range(X,N+1,X)]
B = [j for j in range(Y,N+1,Y)]
print("ListA =",A)
print("ListB =",B)

# print all pairs from both ListA & ListB whose sum is equal to T.
for i in A:
    if not(i > T):
        for j in B:
            if i+j ==T:
                print(i , j)
