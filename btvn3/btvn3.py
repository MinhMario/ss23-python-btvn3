from core.logistics import display_flights
from core.manager import add_flight
from core.time_helper import calculate_eta
from utils.file_helper import create_log_dir

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

while True:
    print('\n===== HE THONG DIEU HANH BAY RIKKEI AVIATION =====')
    print('1. Hien thi lich trinh va Thong ke hau can')
    print('2. Tiep nhan chuyen bay moi')
    print('3. Tinh thoi gian ha canh du kien (ETA)')
    print('4. Khoi tao thu muc luu tru log he thong')
    print('5. Thoat chuong trinh')
    print('==================================================')
    choice = input('Nhap lua chon cua ban: ').strip()

    match choice:
        case '1': display_flights(flights)
        case '2': add_flight(flights)
        case '3': calculate_eta(flights)
        case '4': create_log_dir('aviation_logs')
        case '5':
            print('Cam on ky su da su dung he thong!')
            break
        case _:
            print('Lua chon khong hop le! Vui long nhap so tu 1-5.')