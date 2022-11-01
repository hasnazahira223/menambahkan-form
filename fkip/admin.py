from django.contrib import admin

from faperta.models import UKM, JalurMasuk, MahasiswaMengikutiUKM, NilaiMahasiswa, NilaiTertinggi, PenerimaBeasiswa, Prodi
from . models import Dosen, Tenaga_Pendidik, Mahasiswa

# Register your models here.

admin.site.register(Dosen)
admin.site.register(Tenaga_Pendidik)
admin.site.register(Mahasiswa)
admin.site.register(Prodi)
admin.site.register(UKM)
admin.site.register(NilaiMahasiswa)
admin.site.register(JalurMasuk)
admin.site.register(PenerimaBeasiswa)
admin.site.register(MahasiswaMengikutiUKM)
admin.site.register(NilaiTertinggi)