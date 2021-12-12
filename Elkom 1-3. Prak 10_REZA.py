list_nama, list_nilai = [], []

while True:
	print("""\nP R O G R A M  L I S T
 1. Input Data
 2. View Data
 3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa
 4. Hitung Nilai Rata-Rata Tiap Praktikum 
 5. Mencari Nilai Rata-Rata Praktikum Mahasiswa
 6. Update Nilai Praktikum Mahasiswa 
 7. Exit""")
 
	menu = int(input("Pilih menu yang tersedia: "))
	
	if menu == 1:
		print("\n[ 1. INPUT DATA ]")
		nama = str(input("Masukkan nama mahasiswa/i: "))
		nilai1 = int(input("Masukkan nilai praktikum 1: "))
		nilai2 = int(input("Masukkan nilai praktikum 2: "))
		nilai3 = int(input("Masukkan nilai praktikum 3: "))
		list_nama.append(nama)
		list_nilai.append([nilai1, nilai2, nilai3])
		
	elif menu == 2:
		print("\n[ 2. VIEW DATA ]")
		print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3 ")
		print("---------------------------------")
		for nama in list_nama:
			nilai1 = list_nilai[list_nama.index(nama)][0]
			nilai2 = list_nilai[list_nama.index(nama)][1]
			nilai3 = list_nilai[list_nama.index(nama)][2]
			print(f"{nama}\t{nilai1}\t{nilai2}\t{nilai3}")
			
	elif menu == 3:
		print("\n[ 3. HITUNG RATA-RATA PRAK TIAP MAHASISWA/I]")
		for nama in list_nama:
			data_nilai = list_nilai[list_nama.index(nama)]
			rerata = sum(data_nilai) / len(data_nilai)
			print(f"{nama}\t = {rerata}")
			