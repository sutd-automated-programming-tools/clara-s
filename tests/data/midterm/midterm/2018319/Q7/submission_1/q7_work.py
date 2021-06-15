# MID-TERM EXAM: QUESTION 7

def decompose(pence):
	total = 0
	for i in range(pence//200+1):
		for j in range((pence-i*200)//100+1):
			for k in range((pence-i*200-j*100)//50+1):
				for l in range((pence-i*200-j*100-k*50)//25+1):

					for m in range((pence-i*200-j*100-k*50-l*25)//10+1):
						for n in range((pence-i*200-j*100-k*50-l*25-m*10)//5+1):
							for o in range(((pence-i*200-j*100-k*50-m*10-n*5))//2+1):
								for p in range(((pence-i*200-j*100-k*50-m*10-n*5-o*2))//1+1):
									total+=1

	return total