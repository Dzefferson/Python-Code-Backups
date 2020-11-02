def fibonaci(n):
    fibs = [0, 1]
    i = 2
    while len(fibs) < n:
        fibs.append(fibs[i-1]+fibs[i-2])
        i += 1
    
    return fibs

print(fibonaci(6))
