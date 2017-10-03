totPalavra = int(input())
for i in range(totPalavra):
	palavra = input()
	if len(palavra) == 3:
		if (palavra[1] == "n" and palavra[2] == "e") or (palavra[0] == "o" and palavra[1] == "n") or (palavra[0] == "o" and palavra[2] == "e"):
			num = 1
		elif (palavra[0] == "t" and palavra[1] == "h") or (palavra[1] == "h" and palavra[2] == "o") or (palavra[0] == "t" and palavra[2] == "o"):
			num = 2
	else:
		if (palavra[0] == "t" and palavra[1] == "h" and palavra[2] == "r" and palavra[3] == "e") or (palavra[0] == "t" and palavra[1] == "h" and palavra[2] == "r" and palavra[4] == "e") or (palavra[0] == "t" and palavra[1] == "h" and palavra[3] == "e" and palavra[4] == "e") or (palavra[0] == "t" and palavra[2] == "r" and palavra[3] == "e" and palavra[4] == "e") or (palavra[1] == "h" and palavra[2] == "r" and palavra[3] == "e" and palavra[4] == "e"):
			num = 3
	print(num)

