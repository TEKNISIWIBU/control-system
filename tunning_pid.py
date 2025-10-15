import numpy as np
import matplotlib.pyplot as plt

# ================================
# 1. MODEL PLANT (FIRST ORDER)
# ================================
K = 1.0      # gain sistem
tau = 2.0    # konstanta waktu (s)
Ts = 0.01    # waktu sampling (s)
t_end = 60   # durasi simulasi (s)

# fungsi update plant
def plant(y, u):
    """Model first-order system: dy/dt = (-y + K*u)/tau"""
    dydt = (-y + K*u)/tau
    return y + Ts*dydt

# ================================
# 2. CARI Ku DAN Pu (Closed Loop)
# ================================

def find_ultimate_gain():
    """Naikkan Kp sampai sistem berosilasi stabil, return Ku & Pu"""
    Ku = float(input("masukkan nilai Ku :"))
    Pu = float(input("masukkan nilai pu :"))
    setpoint = 1.0

    for Kp_test in np.arange(0.5, 100, 0.5):
        y = 0.0
        e_prev = 0.0
        t = 0.0

        history_t = []
        history_y = []

        while t < t_end:
            e = setpoint - y
            u = Kp_test * e  # P only
            y = plant(y, u)

            history_t.append(t)
            history_y.append(y)
            t += Ts

        y_arr = np.array(history_y)
        t_arr = np.array(history_t)

        # ambil bagian akhir saja (deteksi osilasi stabil)
        tail = int(0.6 * len(y_arr))
        y_tail = y_arr[tail:]
        t_tail = t_arr[tail:]

        # deteksi puncak
        peaks_idx = (np.diff(np.sign(np.diff(y_tail))) < 0).nonzero()[0] + 1
        if len(peaks_idx) >= 4:
            periods = np.diff(t_tail[peaks_idx])
            Pu_candidate = np.mean(periods[-3:])  # rata-rata 3 periode terakhir
            amplitude = (np.max(y_tail[peaks_idx[-3:]]) - np.min(y_tail[peaks_idx[-3:]]))/2

            # deteksi stabil: amplitudo tidak menyusut atau membesar drastis
            if amplitude > 0.05:
                Ku = Kp_test
                Pu = Pu_candidate
                print(f"[INFO] Osilasi stabil ditemukan pada Kp={Ku:.2f}, Pu={Pu:.2f} s")
                return Ku, Pu

    print("[WARN] Tidak ditemukan osilasi stabil, coba perbesar range Kp.")
    return Ku, Pu

Ku, Pu = find_ultimate_gain()

# ================================
# 3. HITUNG PARAMETER PID
# ================================

def ziegler_nichols_pid(Ku, Pu):
    Kp = 0.6 * Ku
    Ti = Pu / 2.0
    Td = Pu / 8.0
    Ki = Kp / Ti
    Kd = Kp * Td
    return Kp, Ki, Kd

if Ku is not None:
    Kp_pid, Ki_pid, Kd_pid = ziegler_nichols_pid(Ku, Pu)
    print("\n=== PARAMETER PID HASIL ZIEGLER–NICHOLS ===")
    print(f"Kp = {Kp_pid:.3f}")
    print(f"Ki = {Ki_pid:.3f}")
    print(f"Kd = {Kd_pid:.3f}")
else:
    exit()

# ================================
# 4. SIMULASI PID DENGAN PARAMETER
# ================================

t_values = np.arange(0, t_end, Ts)
y_values = []
u_values = []

y = 0.0
e_prev = 0.0
I = 0.0
setpoint = 1.0

for t in t_values:
    e = setpoint - y
    I += e * Ts
    D = (e - e_prev)/Ts

    u = Kp_pid*e + Ki_pid*I + Kd_pid*D

    # batasi output agar simulasi realistis
    u = max(min(u, 10), -10)

    y = plant(y, u)

    y_values.append(y)
    u_values.append(u)
    e_prev = e

# ================================
# 5. PLOT HASIL
# ================================

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t_values, y_values, label='Output')
plt.axhline(setpoint, color='r', linestyle='--', label='Setpoint')
plt.ylabel('Output')
plt.title('Simulasi PID - Ziegler–Nichols')
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(t_values, u_values, label='Control signal (u)')
plt.ylabel('u(t)')
plt.xlabel('Waktu [s]')
plt.grid()

plt.tight_layout()
plt.show()
