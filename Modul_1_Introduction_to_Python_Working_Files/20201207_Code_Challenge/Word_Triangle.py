### List jumlah huruf
x = 0
y = 1
list_jumlah_huruf = [] 				# list untuk pjg kata yang valid

for i in range(10):
    x += y
    list_jumlah_huruf.append(x)
    y += 1

print(list_jumlah_huruf)


def segitigaKata(kata): 	
	try: 
		num = 0
		kata = kata.replace(" ", "")
		n = len(kata)
		index_n = list_jumlah_huruf.index(n)

		if n in list_jumlah_huruf: 
			for i in range(0, index_n + 1): 			
				for j in range(0, i + 1): 				
					print(kata[num], end=" ") 				
					num += 1			
				print('\n')

			num = 0
			for i in range(0, index_n + 1): 								
				for j in range(0, index_n + 1 - i):
					print(kata[num], end=" ")
					num += 1
				print("\r")

		else:
			print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')

	except:
		print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
	
	
segitigaKata('Purwadhika')
segitigaKata('Purwadhika Startup and Coding School @BDG')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('Mantap jiwa')