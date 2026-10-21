from booking_manager import BookingSystem


def main():
    system = BookingSystem()

    while True:
        print("\n--- სასტუმროს ჯავშნების სისტემა ---")
        print("1. ჯავშნის დამატება")
        print("2. ჯავშნების ნახვა")
        print("3. ჯავშნის წაშლა")
        print("4. CSV ფაილში ექსპორტი (Pandas)")
        print("5. გრაფიკის გენერაცია (Matplotlib)")
        print("6. გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-6): ")

        if choice == '1':
            name = input("მომხმარებლის სახელი: ")
            date = input("თარიღი (მაგ. 2026-10-15): ")
            try:
                days = int(input("დღეების რაოდენობა: "))
                booking_id = system.add_booking(name, date, days)
                print(f"\nწარმატება! ჯავშანი დაემატა. ID: {booking_id}")
            except ValueError:
                print("\nშეცდომა: გთხოვთ შეიყვანოთ რიცხვი დღეების რაოდენობისთვის.")

        elif choice == '2':
            bookings = system.get_bookings()
            if not bookings:
                print("\nჯავშნები არ მოიძებნა.")
            else:
                print("\nაქტიური ჯავშნები:")
                for b in bookings:
                    print(f"ID: {b['id']} | სახელი: {b['name']} | თარიღი: {b['date']} | დღეები: {b['days']}")

        elif choice == '3':
            try:
                booking_id = int(input("წასაშლელი ჯავშნის ID: "))
                if system.delete_booking(booking_id):
                    print("\nჯავშანი წარმატებით წაიშალა.")
                else:
                    print("\nჯავშანი ამ ID-ით ვერ მოიძებნა.")
            except ValueError:
                print("\nშეცდომა: შეიყვანეთ სწორი ID რიცხვის სახით.")

        elif choice == '4':
            if system.export_to_csv():
                print("\nმონაცემები წარმატებით დაექსპორტდა CSV ფაილში (bookings_export.csv).")
            else:
                print("\nსაექსპორტო ჯავშნები არ არის.")

        elif choice == '5':
            if system.generate_analytics_chart():
                print("\nგრაფიკი წარმატებით შეიქმნა (bookings_chart.png).")
            else:
                print("\nგრაფიკის შესაქმნელად ჯავშნები არ არის.")

        elif choice == '6':
            print("\nპროგრამის დასრულება...")
            break

        else:
            print("\nარასწორი არჩევანი, სცადეთ თავიდან.")


if __name__ == "__main__":
    main()