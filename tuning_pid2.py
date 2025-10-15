import numpy as np

def ziegler_nichols_tuning(Ku, Tu):
    """
    Menghitung parameter PID menggunakan metode Ziegler-Nichols (Metode Osilasi/Batas Stabilitas).

    Args:
        Ku (float): Ultimate Gain (Gain batas osilasi yang tidak teredam).
        Tu (float): Ultimate Period (Periode osilasi pada Ku).

    Returns:
        dict: Kamus berisi nilai Kp, Ti, Td, Ki, dan Kd untuk berbagai jenis kontrol.
    """
    
    # ----------------------------------------------------
    # 1. Kontrol P (Proporsional)
    # Kp = 0.5 * Ku
    # ----------------------------------------------------
    Kp_P = 0.5 * Ku
    
    # ----------------------------------------------------
    # 2. Kontrol PI (Proporsional-Integral)
    # Kp = 0.45 * Ku
    # Ti = Tu / 1.2
    # Ki = Kp / Ti
    # ----------------------------------------------------
    Kp_PI = 0.45 * Ku
    Ti_PI = Tu / 1.2
    Ki_PI = Kp_PI / Ti_PI

    # ----------------------------------------------------
    # 3. Kontrol PID (Proporsional-Integral-Derivatif)
    # Kp = 0.6 * Ku
    # Ti = Tu / 2
    # Td = Tu / 8
    # Ki = Kp / Ti
    # Kd = Kp * Td
    # ----------------------------------------------------
    Kp_PID = 0.6 * Ku
    Ti_PID = Tu / 2
    Td_PID = Tu / 8
    Ki_PID = Kp_PID / Ti_PID
    Kd_PID = Kp_PID * Td_PID
    
    results = {
        "P": {
            "Kp": Kp_P
        },
        "PI": {
            "Kp": Kp_PI,
            "Ti": Ti_PI,
            "Ki": Ki_PI
        },
        "PID": {
            "Kp": Kp_PID,
            "Ti": Ti_PID,
            "Td": Td_PID,
            "Ki": Ki_PID,
            "Kd": Kd_PID
        }
    }
    
    return results

# =======================================================
# MASUKAN (INPUT)
# Anda harus mendapatkan Ku dan Tu dari sistem fisik/simulasi Anda
# =======================================================
# Contoh nilai hasil eksperimen:
# Anggap sistem mulai berosilasi stabil pada gain = 5.0
Ku_input = float(input("Masukkan nilai Ku (Ultimate Gain): "))
# Anggap periode osilasi saat itu adalah 2.0 detik
Tu_input = float(input("Masukkan nilai Tu (Ultimate Period): "))

# =======================================================
# EKSEKUSI PROGRAM
# =======================================================
try:
    if Ku_input <= 0 or Tu_input <= 0:
        raise ValueError("Ku dan Tu harus lebih besar dari nol.")
        
    tuning_parameters = ziegler_nichols_tuning(Ku_input, Tu_input)

    print("--- Hasil Tuning PID Ziegler-Nichols (Metode Osilasi) ---")
    print(f"Nilai Input: Ku = {Ku_input:.4f} | Tu = {Tu_input:.4f} detik\n")

    # Tampilkan Hasil P
    print("1. Kontrol P (Proporsional)")
    print(f"   Kp = {tuning_parameters['P']['Kp']:.4f}\n")
    
    # Tampilkan Hasil PI
    print("2. Kontrol PI (Proporsional-Integral)")
    print(f"   Kp = {tuning_parameters['PI']['Kp']:.4f}")
    print(f"   Ti = {tuning_parameters['PI']['Ti']:.4f} detik")
    print(f"   Ki = {tuning_parameters['PI']['Ki']:.4f} (Ki = Kp/Ti)\n")

    # Tampilkan Hasil PID
    print("3. Kontrol PID (Proporsional-Integral-Derivatif)")
    print(f"   Kp = {tuning_parameters['PID']['Kp']:.4f}")
    print(f"   Ti = {tuning_parameters['PID']['Ti']:.4f} detik")
    print(f"   Td = {tuning_parameters['PID']['Td']:.4f} detik")
    print(f"   Ki = {tuning_parameters['PID']['Ki']:.4f} (Ki = Kp/Ti)")
    print(f"   Kd = {tuning_parameters['PID']['Kd']:.4f} (Kd = Kp*Td)")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")