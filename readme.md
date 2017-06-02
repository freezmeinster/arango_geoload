# Skrip simpel Load data lokasi indonesia

Skrip ini adalah implementasi data loading untuk platform ArangoDB. Skrip ini tidak ditujukan untuk keperluan produksi namun hanya sebagai proof of concept penggunaan [pyArango](https://github.com/tariqdaouda/pyArango). Untuk mempercepat proses input data, skrip ini memanfaatkan fitur multiprocessing dari Python. 

## Kebutuhan
Skrip ini membutuhkkan beberapa komponen antara lain :
  * [ArangoDB](https://www.arangodb.com/) server terinstall dan berjalan dengan baik
  * [Python 2.7](https://www.python.org/) terinstall. 
  * [Data Wilayah Administratif Indonesia](https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia)
  
### Installasi
buat virtualenv dengan perintah berikut:
```
mkvirtualenv geoload
```

install library pendukung dengan perintah berikut :
```
pip install -r requirements.txt
```

## Menjalankan

Untuk dapat menjalankan skrip ini pastikan kebutuhan di atas sudah dipenuhi.

Memuat data provinsi 
```
./geoload.py --type province --db mambu /home/bram/Code/Wilayah-Administratif-Indonesia/csv/provinces.csv
```

Memuat data kota/kabupaten 
```
./geoload.py --type city --db mambu /home/bram/Code/Wilayah-Administratif-Indonesia/csv/regencies.csv
```

Memuat data kecamatan 
```
./geoload.py --type district --db mambu /home/bram/Code/Wilayah-Administratif-Indonesia/csv/districts.csv
```

Memuat data desa 
```
./geoload.py --type village --db mambu /home/bram/Code/Wilayah-Administratif-Indonesia/csv/villages.csv
```