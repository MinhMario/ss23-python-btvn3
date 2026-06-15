from datetime import datetime

def check_duplicate_id(flight_id, flights):
    for f in flights:
        if f['flight_id'] == flight_id:
            return True
    return False

def add_flight(flights):
    print('----- TIEP NHAN CHUYEN BAY MOI -----')

    flight_id = input('Nhap ma chuyen bay: ').strip().upper()
    if check_duplicate_id(flight_id, flights):
        print(f'>> Ma {flight_id} da ton tai! Khong the them.')
        return

    while True:
        passengers = input('Nhap so luong hanh khach: ').strip()
        if not passengers.isdigit() or int(passengers) <= 0:
            print('So hanh khach khong hop le.')
        else:
            passengers = int(passengers)
            break

    while True:
        depart_time = input('Nhap thoi gian cat canh (YYYY-MM-DD HH:MM:SS): ').strip()
        try:
            datetime.strptime(depart_time, '%Y-%m-%d %H:%M:%S')
            break
        except ValueError:
            print('Sai dinh dang thoi gian! Vui long nhap dung chuan YYYY-MM-DD HH:MM:SS')

    while True:
        duration = input('Nhap so phut bay: ').strip()
        if not duration.isdigit() or int(duration) <= 0:
            print('So phut bay khong hop le.')
        else:
            duration = int(duration)
            break

    flights.append({
        'flight_id': flight_id,
        'passengers': passengers,
        'depart_time': depart_time,
        'duration_min': duration
    })
    print(f'>> Them chuyen bay {flight_id} thanh cong!')