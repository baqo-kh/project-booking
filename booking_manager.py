import json
import os
import pandas as pd
import matplotlib.pyplot as plt

class BookingSystem:
    def __init__(self, filename="bookings.json"):
        self.filename = filename
        self.bookings = self.load_bookings()

    def load_bookings(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_bookings(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.bookings, file, ensure_ascii=False, indent=4)

    def add_booking(self, name, date, days):
        booking_id = 1 if not self.bookings else self.bookings[-1]["id"] + 1
        booking = {
            "id": booking_id,
            "name": name,
            "date": date,
            "days": days
        }
        self.bookings.append(booking)
        self.save_bookings()
        return booking_id

    def get_bookings(self):
        return self.bookings

    def delete_booking(self, booking_id):
        initial_length = len(self.bookings)
        self.bookings = [b for b in self.bookings if b["id"] != booking_id]
        if len(self.bookings) < initial_length:
            self.save_bookings()
            return True
        return False

    def export_to_csv(self):
        if not self.bookings:
            return False
        df = pd.DataFrame(self.bookings)
        df.to_csv("bookings_export.csv", index=False)
        return True

    def generate_analytics_chart(self):
        if not self.bookings:
            return False
        df = pd.DataFrame(self.bookings)
        plt.figure(figsize=(8, 5))
        plt.bar(df['name'], df['days'], color='skyblue')
        plt.xlabel('სტუმარი')
        plt.ylabel('დღეების რაოდენობა')
        plt.title('ჯავშნების ხანგრძლივობა სტუმრების მიხედვით')
        plt.tight_layout()
        plt.savefig('bookings_chart.png')
        plt.close()
        return True