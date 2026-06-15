import math

def display_flights(flights):
    if not flights:
        print('Khong co chuyen bay nao.')
        return
    print('----- DANH SACH CHUYEN BAY & HAU CAN -----')
    for i, f in enumerate(flights, 1):
        boxes = math.ceil(f['passengers'] / 10)
        print(f"{i}. Ma: {f['flight_id']} | Khoi hanh: {f['depart_time']} | "
              f"So khach: {f['passengers']} | Du phong: {boxes} thung nuoc.")