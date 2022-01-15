alphabet = "abcdefghijklmnopqrstuvwxyz"

words = []
for w in open("words.txt","r").readlines():
	w = w.strip().lower()	

	if(len(w) == 5 and all(c in alphabet for c in w)):
		words.append(w)


print("Loaded",len(words),"words.")

template = []
present = set()
for _ in range(5):
	template.append(set(list(alphabet)))

def filter(words,template,present):
	next_words = []
	for w in words:
		passed = True
		for i,c in enumerate(w):
			if c not in template[i]:
				passed = False
		passed = passed and all(c in w for c in present)
		if passed:
			next_words.append(w)
	return next_words
	
for _ in range(10):
	guess = input("Guess 5 letter word: ").strip().lower()
	result = input("Enter result\n. = present\n# = confirmed\n_ = not-present\n>")
	for i,r in enumerate(result):
		c = guess[i].strip().lower()
		if r == "#":
			template[i] = set([c])	
		elif r == ".":
			present.add(c)
			template[i].remove(c)
		elif guess.count(c) <= 1:
			for j in range(5):
				if c in template[j]:
					template[j].remove(c)
	remaining_words = filter(words,template,present)
	print(f"There are {len(remaining_words)} left...")
	for i in range(min(len(remaining_words),10)):
		print("\t",remaining_words[i])
	print()
	print()
		
		
