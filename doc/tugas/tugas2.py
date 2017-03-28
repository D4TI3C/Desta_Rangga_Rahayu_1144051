rute = {
	'lembang': ['ledeng'], 
	'ledeng': ['setiabudi'], 
	'setiabudi': ['cihampelas'], 
	'cihampelas': ['BIP'], 
	'BIP': ['Alun-alun'], 
	'Alun-alun': ['lembang']
	}

def rute_perjalanan(rute, ruteawal, ruteakhir, jalan=[]):
        jalan = jalan + [ruteawal]
        if ruteawal == ruteakhir:
            return jalan
	    if not rute.has_key(ruteawal):
            	return None
        rutejalan = None
        for x in rute[ruteawal]:
            if x not in jalan:
                rutebaru = rute_perjalanan(rute, x, ruteakhir, jalan)
                if rutebaru:
                    if not rutejalan or len(rutebaru) < len(rutejalan):
                        rutejalan = rutebaru
        return rutejalan

print("Rute :\n - lembang \n - ledeng \n - setiabudi \n - cihampelas \n - BIP \n - Alun-alun \n")
ruteawal = raw_input("Masukkan Rute Awal : ")
ruteakhir = raw_input("Masukkan Rute AKhir : ")
jalur = rute_perjalanan(rute, ruteawal, ruteakhir, jalan=[])
print 'Rute Perjalanan :', jalur