import os
import pytest
from booking_manager import BookingSystem

@pytest.fixture
def system():
    test_file = "test_bookings.json"
    sys = BookingSystem(filename=test_file)
    yield sys
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_booking(system):
    booking_id = system.add_booking("Giga", "2026-11-01", 3)
    assert booking_id == 1
    assert len(system.get_bookings()) == 1

def test_delete_booking(system):
    booking_id = system.add_booking("Ana", "2026-11-05", 2)
    assert system.delete_booking(booking_id) is True
    assert len(system.get_bookings()) == 0