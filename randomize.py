# store pool 1 proxies into an array
pool1File = open("proxies1.txt", "r")
pool1 = []
for line in pool1File:
	pool1.append(line)
pool1File.close()

# store pool 2 proxies into an array
pool2File = open("proxies2.txt", "r")
pool2 = []
for line in pool2File:
	pool2.append(line)
pool2File.close()

# add the proxies in order to combined.txt
resultFile = open("combined.txt", "a")
if(len(pool1) >= len(pool2)): # pool 1 has more proxies in it or equal amount
	for i, proxy in enumerate(pool1):
		resultFile.write(proxy)
		if(i < len(pool2)):
			resultFile.write(pool2[i])
else: # pool 2 has more proxies in it
	for i, proxy in enumerate(pool2):
		resultFile.write(proxy)
		if(i < len(pool1)):
			resultFile.write(pool1[i])