from datetime import datetime, timedelta
from ..Timer.timer import ParkingTimer
from ..ticket.ticket import Ticket
from ..fees.fees import Fees



def test_ticket_creation():
    ticket = Ticket("ABC123", "A1")
    assert ticket.vehicle_id == "ABC123"
    assert ticket.parking_space_id == "A1"
    assert isinstance(ticket.timer, ParkingTimer)
    assert isinstance(ticket.fee, Fees)




def test_start_60_minute_timer():
    ticket = Ticket('ABC123', 'A1')
    # Start the 60-minute timer
    ticket.start_60_minute()

    # Check that the ticket has been deleted
    assert ticket.deleted
