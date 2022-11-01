from django.db import models
from django.db import models

# Create your models here.

class Dosen(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField()

class Tenaga_Pendidik(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    alamat = models.TextField()

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField()

class Prodi(models.Model):
    prodi = models.CharField(max_length=200)
    jumlah_mahasiswa = models.CharField(max_length=200)
    dosen = models.CharField(max_length=200)
    jumlah_kelas = models.CharField(max_length=200)
    mata_kuliah = models.CharField(max_length=200)

class UKM(models.Model):
    jadwal_kumpulan = models.CharField(max_length=200)
    tanggal_berdirinya = models.CharField(max_length=200)
    tempat_kumpulan = models.CharField(max_length=200)

class NilaiMahasiswa(models.Model):
    mata_kuliah = models.CharField(max_length=200)
    angkatan = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    kelas = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)

class JalurMasuk(models.Model):
    nama_jalur = models.CharField(max_length=200)
    tanggal_penerimaan = models.CharField(max_length=200)
    angkatan = models.CharField(max_length=200)

class PenerimaBeasiswa(models.Model):
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    angkatan = models.CharField(max_length=200)
    nama_beasiswa = models.CharField(max_length=200)

class MahasiswaMengikutiUKM(models.Model):
    nama = models.CharField(max_length=200)
    ukm = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    kelas = models.CharField(max_length=200)

class NilaiTertinggi(models.Model):
    nama = models.CharField(max_length=200)
    mata_kuliah = models.CharField(max_length=200)
    angkatan = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    kelas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)