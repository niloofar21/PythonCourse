Fib = [1,1]
for i in range(2,10):
    Fib.append(Fib[i-2]+Fib[i-1])


''' "another way to do the same thing"
Fib = [1,1]
for i in range(1,9):
    Fib.append(Fib[-2]+Fib[-1])
"This will give the same output" '''
