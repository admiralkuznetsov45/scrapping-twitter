import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import nest_asyncio
import os
import json
from datetime import datetime


nest_asyncio.apply()

async def buka_kelompok_barang(kd):
    """Membuka URL kelompok barang berdasarkan input kd."""
    driver = webdriver.Chrome()
    try:
        url = f"https://tkdn.kemenperin.go.id/sertifikat_idx.php?kd={kd}"
        driver.get(url)
        print(f"Berhasil membuka URL: {url}")
        return driver
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

async def scrap_data_kelompok_barang_pagination(driver, kd, page_limit=None):
    """Melakukan scrapping data dari tabel kelompok barang dengan pagination."""
    if driver is None:
        return

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div[1]/div[2]/table/tbody'))
        )

        header = ["Perusahaan", "Jenis Produk", "Spesifikasi", "Tipe", "Merk", "Nilai TKDN"]
        print("\t".join(header))

        page_number = 1
        all_data = []

        while True:
            rows = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/div/div[1]/div[2]/table/tbody/tr')

            for row in rows:
                cells = row.find_elements(By.XPATH, './td[position()>=2 and position()<=7]')
                row_data = [cell.text.strip() for cell in cells]
                print("\t".join(row_data))
                all_data.append(dict(zip(header, row_data)))

            next_page = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/div/div/div[1]/div/div[2]/ul/li[position()=last()]/a')

            if next_page and "..." not in next_page[0].text:
                if page_limit and page_number >= page_limit:  # Check page limit
                    break
                next_page[0].click()
                page_number += 1
                time.sleep(2)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div[1]/div[2]/table/tbody'))
                )
            else:
                break
        return all_data

    except Exception as e:
        print(f"Terjadi kesalahan saat scrapping data: {e}")
    finally:
        driver.quit()

def create_folder(kd):
    """Membuat folder hasil scrapping."""
    folder_name = f"hasil-scrapping-kd-{kd}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def save_data_to_json(data, kd):
    """Menyimpan data ke file JSON, dimulai dari id_data = 1, dan menambahkan kategori kelompok barang."""
    if not data:
        return

    kelompok_barang_dict = {
        1: "Bahan Penunjang Pertanian",
        2: "Mesin dan Peralatan Pertanian",
        3: "Mesin dan Peralatan Pertambangan",
        4: "Mesin dan Peralatan Migas",
        5: "Alat Berat, Konstruksi dan Material Handling",
        6: "Mesin dan Peralatan Pabrik",
        7: "Bahan Bangunan/Konstruksi",
        8: "Logam dan Barang Logam",
        9: "Bahan Kimia dan Barang Kimia",
        10: "Peralatan Elektronika",
        11: "Peralatan Kelistrikan",
        12: "Peralatan Telekomunikasi",
        13: "Alat Transport",
        14: "Bahan dan Peralatan Kesehatan",
        15: "Peralatan Laboratorium",
        16: "Komputer dan Peralatan Kantor",
        17: "Pakaian dan Perlengkapan Kerja",
        18: "Peralatan Olahraga dan Pendidikan",
        19: "Sarana Pertahanan",
        20: "Barang Lainnya",
    }
    
    kelompok_barang = kelompok_barang_dict.get(kd, "Kelompok Barang Tidak Diketahui")

    folder_name = create_folder(kd)
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d--%H-%M-%S")
    file_name = f"hasil-scrapping-kd-{kd}-{timestamp}.json"
    file_path = os.path.join(folder_name, file_name)

    # Mengubah data ke dictionary dengan id_data dimulai dari 1
    json_data = []
    for i, row in enumerate(data[1:], start=1):  # Mulai dari index 1 (baris ke-1)
        # Menambahkan kelompok barang ke dictionary
        row_with_kelompok = {"Kelompok Barang": kelompok_barang, **row}
        json_data.append({"id_data": i, **row_with_kelompok})  # Gabungkan id_data dengan data lainnya

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print(f"Data disimpan di: {file_path}")

async def main():
    """Fungsi utama untuk menjalankan skrip asinkron."""
    kelompok_barang_dict = {
        1: "Bahan Penunjang Pertanian",
        2: "Mesin dan Peralatan Pertanian",
        3: "Mesin dan Peralatan Pertambangan",
        4: "Mesin dan Peralatan Migas",
        5: "Alat Berat, Konstruksi dan Material Handling",
        6: "Mesin dan Peralatan Pabrik",
        7: "Bahan Bangunan/Konstruksi",
        8: "Logam dan Barang Logam",
        9: "Bahan Kimia dan Barang Kimia",
        10: "Peralatan Elektronika",
        11: "Peralatan Kelistrikan",
        12: "Peralatan Telekomunikasi",
        13: "Alat Transport",
        14: "Bahan dan Peralatan Kesehatan",
        15: "Peralatan Laboratorium",
        16: "Komputer dan Peralatan Kantor",
        17: "Pakaian dan Perlengkapan Kerja",
        18: "Peralatan Olahraga dan Pendidikan",
        19: "Sarana Pertahanan",
        20: "Barang Lainnya",
    }

    print("Daftar Kode Kelompok Barang:")
    for kd, nama_kelompok in kelompok_barang_dict.items():
        print(f"{kd}: {nama_kelompok}")

    kd_input = int(input("Masukkan kode kelompok barang (1-20): "))  # Perubahan: 1-20
    page_limit = int(input("Masukkan batas halaman (opsional, tekan Enter untuk semua halaman): ") or 0)
    if 1 <= kd_input <= 20:  # Perubahan: 1-20
        driver = await buka_kelompok_barang(kd_input)
        if driver:
            all_data = await scrap_data_kelompok_barang_pagination(driver, kd_input, page_limit if page_limit > 0 else None)
            save_data_to_json(all_data, kd_input)
    else:
        print("Kode kelompok barang tidak valid. Masukkan angka antara 1 dan 20.")  # Perubahan: 1-20

if __name__ == "__main__":
    asyncio.run(main())