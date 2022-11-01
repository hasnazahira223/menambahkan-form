from django.shortcuts import render

from faperta.models import UKM, JalurMasuk, MahasiswaMengikutiUKM, NilaiMahasiswa, NilaiTertinggi, PenerimaBeasiswa, Prodi
from . models import Dosen, Tenaga_Pendidik, Mahasiswa

# Create your views here.

def fkip(request):
    dosen = Dosen.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    prodi = Prodi.objects.all()
    ukm = UKM.objects.all()
    nilai_mahasiswa = NilaiMahasiswa.objects.all()
    jalur_masuk = JalurMasuk.objects.all()
    penerima_beasiswa = PenerimaBeasiswa.objects.all()
    mahasiswa_mengikuti_ukm = MahasiswaMengikutiUKM.objects.all()
    nilai_tertinggi = NilaiTertinggi.objects.all()
    

    context = {
        'dataDosen': dosen,
        'dataTenaga_Pendidik': tenagaPendidik,
        'dataMahasiswa': mahasiswa,
        'dataProdi': prodi,
        'dataUkm': ukm,
        'dataNilai_Mahasiswa': nilai_mahasiswa,
        'dataJalur_Masuk': jalur_masuk,
        'dataPenerima_Beasiswa': penerima_beasiswa,
        'dataMahasiswa_Mengikuti_Ukm': mahasiswa_mengikuti_ukm,
        'dataNilai_Tertinggi': nilai_tertinggi,
    }
    return render(request, 'indexfkip.html', context)
