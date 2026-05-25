import streamlit as st

# KELAS NODE KATEGORI
class KategoriNode:
    def __init__(self, nama_kategori):
        self.nama = nama_kategori
        self.sub_kategori = [] #ini adalah 'anak' / cabang dari kategori

    def tambah_sub(self, node_kategori):
        self.sub_kategori.append(node_kategori)
        return node_kategori # mengembalikan node agar mudah disambung (chaining)
    
    def dapatkan_tree_string(self, level=0):
        indentasi = "    " * level
        simbol = "->" if level > 0 else "-"

        print(f"{indentasi}{simbol}{self.nama}")

        for sub in self.sub_kategori:
            sub.tampilkan_tree(level + 1)

    def cari_node(self, target_nama):
        #mencari node spesifik untuk menambahkan anak dibawahnya
        if self.nama.lower() == target_nama.lower():
            return self
        
        for sub in self.sub_kategori:
            hasil = sub.cari_node(target_nama)
            if hasil:
                return hasil
            
        return None
    
    def cari_jalur(self,target, path=""):
        #mencari jaliir lengkap (breadcrumb) seperti studi kasus sebelumnya
        jalur_saat_ini = path + " > " + self.nama if path else self.nama

        if self.nama.lower() == target.lower():
            return jalur_saat_ini
        
        for sub in self.sub_kategori:
            hasil = sub.cari_jalur(target, jalur_saat_ini)
            if hasil:
                return hasil
            
            return None

# ============================
def jalankan_program():
    print("=== selamat datag di pembuatan struktur kategori ===")
    nama_root = input("masukkan nama kategori utama (root) [misal: toko saya]: ")
    if not nama_root:
        nama_root = "Toko Saya"

    root = KategoriNode(nama_root)

    while True:
        print("\n" + "="*40)
        print("MENU PILIHAN")
        print("1. Lihat Struktur Kategori")
        print("2. Tambah Sub Kategori Baru")
        print("3. Cari Jalur Kategori")
        print("4. Keluar")
        print("="*40)

        pilihan = input("pilih menu (1/2/3/4): ")

        if pilihan == '1':
            print("\n---STRUKTUR SAAT INI---")
            root.tampilkan_tree()

        elif pilihan == '2':
            induk_nama = input("\n masukkan nama kategori induk tempat anda ingin menambahkan cabang: ")
            induk_node = root.cari_node(induk_nama)

            if induk_node:
                anak_nama = input(f"masukkan nama sub kategori baru di bawah '{induk_node.nama}': ")
                induk_node.tambah_sub(KategoriNode(anak_nama))
                print(f"berhasil menambahkan '{anak_nama}' di bawah '{induk_node.nama}'")
            else:
                print(f"kategori '{induk_nama}' tidak ditemukan! pastikaan ejaannya benar")

        elif pilihan == '3':
            target_cari = input("\nmasukkan nama kategori yang ingin dicari jalurnya: ")
            hasil = root.cari_jalur(target_cari)

            if hasil:
                print(f"Ditemukan! Jalur: {hasil}")
            else:
                print(f"Kategori '{target_cari}' tidak ditemukan dalam sistem")

        elif pilihan == '4':
            print("\nTerima Kasih telah mencoba simulasi Tree! Sampai Jumpa")
            break

        else:
            print("\n pilihan tidak valid,silahkan masukkan angka 1, 2, 3 atau 4")

#menjalankan program jika file ini di eksekusi
if __name__ == "__main__":
    jalankan_program()