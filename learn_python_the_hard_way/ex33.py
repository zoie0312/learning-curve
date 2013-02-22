def ite(ite_max, inc):
	i = 0
	numbers = []

	for i in range(0, ite_max):
		print "At the top i is %d" % i
		numbers.append(i)
	
		#i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
		
ite(10 	, 2)