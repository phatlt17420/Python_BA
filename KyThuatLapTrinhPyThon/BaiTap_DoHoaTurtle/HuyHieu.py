import turtle as t
import math

t.speed(0)
t.pensize(2)
t.getscreen().colormode(255)
# Chọn màu cho răng và màu cho vòng tròn tâm
MAU_RANG = "orange"
MAU_TAM = "orange"


def ve_nua_elip_nhon(t, x_tam, y_tam, r_lon, r_nho, goc_xoay_do):
    rad_xoay = math.radians(goc_xoay_do)
    t.penup()

    # 1. Thiết lập màu sắc và bắt đầu tô
    t.fillcolor(MAU_RANG)
    t.begin_fill()

    # Vẽ nửa elip
    for i in range(-90, 91, 10):
        rad = math.radians(i)
        ex_goc = r_lon * math.cos(rad)
        ey_goc = r_nho * math.sin(rad)

        ex_xoay = ex_goc * math.cos(rad_xoay) - ey_goc * math.sin(rad_xoay)
        ey_xoay = ex_goc * math.sin(rad_xoay) + ey_goc * math.cos(rad_xoay)

        t.goto(x_tam + ex_xoay, y_tam + ey_xoay)
        t.pendown()

    # 2. Kết thúc tô màu cho 1 cái răng
    t.end_fill()


# --- Cấu hình ---
R_vong_tron = 150
so_luong = 15

# Vẽ các bánh răng trước
for i in range(0, 360, 360 // so_luong):
    rad_vt = math.radians(i)
    x = R_vong_tron * math.cos(rad_vt)
    y = R_vong_tron * math.sin(rad_vt)
    ve_nua_elip_nhon(t, x, y, 30, 20, i)

# --- Vẽ và tô màu vòng tròn tâm ---
t.penup()
t.goto(0, -R_vong_tron)
t.setheading(0)
t.fillcolor(MAU_TAM)
t.begin_fill()
t.pendown()
t.pensize(3)
t.circle(R_vong_tron)
t.end_fill()






t.mainloop()