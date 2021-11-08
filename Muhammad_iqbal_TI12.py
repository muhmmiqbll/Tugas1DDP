nama = "Ahmad"
agama = "Islam"
anak = 2
gajiPokok = 4000000
tunjanganJabatan = 0.20 * gajiPokok

# kalkulasi

if(anak > 2 and anak <= 5):
    tunjangan = 0.20 * gajiPokok
elif(anak > 1 and anak <= 2):
    tunjangan = 0.10 * gajiPokok
else:
    tunjangan = 0
gajiKotor = gajiPokok+tunjanganJabatan+tunjangan
zakatProfesi = (0.025, 0)[
    agama == "Islam" and gajiKotor >= 6000000] * gajiKotor
gajiBersih = gajiKotor - 0.025
pegawai = "Pegawai 1"
title = pegawai

print(title)
print('------------------'
      '\nNama Pegawai\t\t:', nama,
      '\nAgama\t\t\t:', agama,
      '\nJumlah Anak\t\t:', anak,
      '\nGaji Pokok\t\t:', 'Rp.', gajiPokok,
      '\nTunjangan Jabatan\t:', 'Rp.', tunjanganJabatan,
      '\nTunjangan Keluarga\t:', 'Rp.', tunjangan,
      '\nGaji Kotor\t\t:', 'Rp.', gajiKotor,
      '\nZakat Profesi\t\t:', 'Rp.', zakatProfesi,
      '\nTake Home Pay\t\t:', 'Rp.', gajiBersih,
      )


nama = "Alex"
agama = "Kristen"
anak = 5
gajiPokok = 6000000
tunjanganJabatan = 0.20 * gajiPokok

# if Multi Kondisi

if(anak > 2 and anak <= 5):
    tunjangan = 0.20 * gajiPokok
elif(anak > 1 and anak <= 2):
    tunjangan = 0.10 * gajiPokok
else:
    tunjangan = 0
gajiKotor = gajiPokok+tunjanganJabatan+tunjangan
zakatProfesi = (0, 0.025)[
    agama == "Islam" and gajiKotor >= 6000000] * gajiKotor
gajiBersih = gajiKotor-zakatProfesi
pegawai = 'Pegawai 2'
title = pegawai
print("-----------------------------------------")
print(title)
print('------------------'
      '\nNama Pegawai\t\t:', nama,
      '\nAgama\t\t\t:', agama,
      '\nJumlah Anak\t\t:', anak,
      '\nGaji Pokok\t\t:', 'Rp.', gajiPokok,
      '\nTunjangan Jabatan\t:', 'Rp.', tunjanganJabatan,
      '\nTunjangan Keluarga\t:', 'Rp.', tunjangan,
      '\nGaji Kotor\t\t:', 'Rp.', gajiKotor,
      '\nZakat Profesi\t\t:', 'Rp.', zakatProfesi,
      '\nTake Home Pay\t\t:', 'Rp.', gajiBersih,
      )