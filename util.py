WEIGHT_HHZ = 8
WEIGHT_RAM = 7
WEIGHT_SSD = 0.2
WEIGHT_PRICE = -0.002


def disp_rank(inch):
    if inch < 14: return 30
    if inch < 15: return 50
    if inch < 16: return 75
    if inch < 17: return 80
    return 85


def get_rank(cpu_hhz, ram_gb, ssd_gb, disp_inch, price):
    return cpu_hhz * WEIGHT_HHZ + ram_gb * WEIGHT_RAM + ssd_gb * WEIGHT_SSD + disp_rank(disp_inch) + price * WEIGHT_PRICE
