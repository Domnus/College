def soma(x):
	return x + 1

def mult(x):
	return x * 2

def compose(f, g):
	return lambda x: f(g(x))

def pipe(f, g):
	return lambda x: g(f(x))

if __name__ == '__main__':

	resultCompose = compose(soma, mult)
	resultPipe = pipe(soma, mult)

	print(resultCompose(10))
	print(resultPipe(10))