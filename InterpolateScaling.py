class InterpolateScaling:
	def interpolate(self, a, b, n, k):
    		x = sum([k**i for i in range(1,n//2 + 1)]) * 2 + 1
		delta = (b - a) / x
		deltaTable = [delta * k ** i for i in range(n//2 + 1)]
		print(delta,deltaTable)
		value = [a]
		for j in range(n):
			value.append(value[-1] + deltaTable[abs(n//2 - j)])
		return value
