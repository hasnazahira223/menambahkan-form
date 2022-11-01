from django.forms import ModelForm
from django import forms
from faperta.models import UKM, Dosen, JalurMasuk, MahasiswaMengikutiUKM, NilaiMahasiswa, NilaiTertinggi, PenerimaBeasiswa, Prodi
from faperta.models import Tenaga_Pendidik
from faperta.models import Mahasiswa

class FormDosen (ModelForm): 
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }

class FormTenagaPendidik (ModelForm): 
    class Meta:
        model = Tenaga_Pendidik
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'unit' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswa (ModelForm): 
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'nim' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }

class FormProdi (ModelForm): 
    class Meta:
        model = Prodi
        fields = '__all__'

        widgets = {
            'prodi' : forms.TextInput({'class':'form-control'}),
            'jumlah_mahasiswa' : forms.TextInput({'class':'form-control'}),
            'dosen' : forms.TextInput({'class':'form-control'}),
            'jumlah_kelas' : forms.TextInput({'class':'form-control'}),
            'mata_kuliah' : forms.TextInput({'class':'form-control'}),
        }

class FormUKM (ModelForm): 
    class Meta:
        model = UKM
        fields = '__all__'

        widgets = {
            'jadwal_kumpulan' : forms.TextInput({'class':'form-control'}),
            'tanggal_berdirinya' : forms.TextInput({'class':'form-control'}),
            'tempat_kumpulan' : forms.TextInput({'class':'form-control'}),
        }

class FormNilaiMahasiswa (ModelForm): 
    class Meta:
        model = NilaiMahasiswa
        fields = '__all__'

        widgets = {
            'mata_kuliah' : forms.TextInput({'class':'form-control'}),
            'angkatan' : forms.TextInput({'class':'form-control'}),
            'semester' : forms.TextInput({'class':'form-control'}),
            'kelas' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
        }

class FormJalurMasuk (ModelForm): 
    class Meta:
        model = JalurMasuk
        fields = '__all__'

        widgets = {
            'nama_jalur' : forms.TextInput({'class':'form-control'}),
            'tanggal_penerimaan' : forms.TextInput({'class':'form-control'}),
            'angkatan' : forms.TextInput({'class':'form-control'}),
        }

class FormPenerimaanBeasiswa (ModelForm): 
    class Meta:
        model = PenerimaBeasiswa
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'angkatan' : forms.TextInput({'class':'form-control'}),
            'nama_beasiswa' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswaMengikutiUKM (ModelForm): 
    class Meta:
        model = MahasiswaMengikutiUKM
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'ukm' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'kelas' : forms.TextInput({'class':'form-control'}),
        }

class FormNilaiTertinggi (ModelForm): 
    class Meta:
        model = NilaiTertinggi
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'mata_kuliah' : forms.TextInput({'class':'form-control'}),
            'angkatan' : forms.TextInput({'class':'form-control'}),
            'semester' : forms.TextInput({'class':'form-control'}),
            'kelas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
        }
