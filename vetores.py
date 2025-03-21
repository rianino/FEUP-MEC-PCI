def soma_vetores(X,Y):
    if len(X) == len(Y):
        Z = [0] * len(X)
        for i in range(len(X)):
            Z[i] = X[i] + Y[i]
        return Z
    

