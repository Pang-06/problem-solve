class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False
        self.student_id = None
        self.student_name = None

    def book(self, student_id, student_name):
        if not self.is_booked:
            self.is_booked = True
            self.student_id = student_id
            self.student_name = student_name
            return True
        return False

    def cancel_booking(self):
        if self.is_booked:
            self.is_booked = False
            self.student_id = None
            self.student_name = None
            return True
        return False

    def __str__(self):
        if self.is_booked:
            return f"Seat {self.seat_number}: {self.student_id} - {self.student_name}"
        return f"Seat {self.seat_number}: Available"


class Booking:
    def __init__(self, total_seats=25):
        self.seats = [Seat(i + 1) for i in range(total_seats)]

    def display_seats(self):
        for seat in self.seats:
            print(seat)

    def get_available_seats(self):
        available = [seat for seat in self.seats if not seat.is_booked]
        for seat in available:
            print(seat)
        return available

    def get_booked_seats(self):
        booked = [seat for seat in self.seats if seat.is_booked]
        for seat in booked:
            print(seat)
        return booked

    def book_seat(self, seat_number, student_id, student_name):
        if 1 <= seat_number <= len(self.seats):
            return self.seats[seat_number - 1].book(student_id, student_name)
        return False

    def cancel_booking(self, seat_number):
        if 1 <= seat_number <= len(self.seats):
            return self.seats[seat_number - 1].cancel_booking()
        return False


def main():
    booking = Booking()
    while True:
        print("\nMenu:")
        print("1: แสดงที่นั่งสอบทั้งหมด")
        print("2: แสดงที่นั่งที่ยังว่างอยู่")
        print("3: กำหนดที่นั่งสอบให้กับนักศึกษา")
        print("4: ยกเลิกการกำหนดที่นั่ง")
        print("5: ออกจากโปรแกรม")

        choice = input("เลือกเมนู: ")

        if choice == "1":
            booking.display_seats()
        elif choice == "2":
            booking.get_available_seats()
        elif choice == "3":
            seat_number = int(input("ป้อนหมายเลขที่นั่ง: "))
            student_id = input("ป้อนรหัสนักศึกษา: ")
            student_name = input("ป้อนชื่อนักศึกษา: ")
            if booking.book_seat(seat_number, student_id, student_name):
                print("จองที่นั่งสำเร็จ!")
            else:
                print("ที่นั่งนี้ถูกจองแล้วหรือหมายเลขไม่ถูกต้อง")
        elif choice == "4":
            seat_number = int(input("ป้อนหมายเลขที่นั่งที่ต้องการยกเลิก: "))
            if booking.cancel_booking(seat_number):
                print("ยกเลิกการจองสำเร็จ!")
            else:
                print("ที่นั่งนี้ยังไม่ถูกจองหรือหมายเลขไม่ถูกต้อง")
        elif choice == "5":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")


if __name__ == "__main__":
    main()
