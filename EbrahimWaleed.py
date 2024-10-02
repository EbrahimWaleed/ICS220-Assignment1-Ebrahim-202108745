# Guest class to represent a hotel guest and their information
class Guest:
    def __init__(self, guest_id, guest_name, email, phone_number, address, country, ebrahim_points):
        # Initializing the attributes for Guest objects
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.country = country
        self.ebrahim_points = ebrahim_points

    # Getter methods to access the guest attributes
    def get_guest_id(self):
        return self.guest_id

    def get_guest_name(self):
        return self.guest_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_country(self):
        return self.country

    def get_ebrahim_points(self):
        return self.ebrahim_points

    # Setter methods to modify the guest attributes
    def set_guest_id(self, guest_id):
        self.guest_id = guest_id

    def set_guest_name(self, guest_name):
        self.guest_name = guest_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_country(self, country):
        self.country = country

    def set_loyaltypoints(self, loyalty_points):
        self.loyalty_points = loyalty_points

    # Method to register a guest
    def register(self):
        return f"The Guest {self.guest_name} is registered."

    # Method to update guest profile with new information
    def update_profile(self, new_name="None", new_email="None", new_phone="None", new_address="None", new_country="None"):
        if new_name:
            self.set_guest_name(new_name)  # Update name if provided
        if new_email:
            self.set_email(new_email)  # Update email if provided
        if new_phone:
            self.set_phone_number(new_phone)  # Update phone if provided
        if new_address:
            self.set_address(new_address)  # Update address if provided
        if new_country:
            self.set_country(new_country)  # Update country if provided
        return "Profile Updated!"

    # Method to simulate making a reservation by the guest
    def make_reservation(self):
        return f"Reservation made by {self.guest_name}."


# Reservation class to represent hotel reservations
class Reservation:
    def __init__(self, reservation_id, guest, check_in, check_out, room_type, room_number, status, total_cost):
        # Initializing attributes for Reservation objects
        self.reservation_id = reservation_id
        self.guest = guest  # Guest object linked to the reservation
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type
        self.room_number = room_number
        self.status = status
        self.total_cost = total_cost

    # Getter methods to access reservation attributes
    def getreservation_id(self):
        return self.reservation_id

    def get_guest(self):
        return self.guest

    def get_check_in(self):
        return self.check_in

    def get_check_out(self):
        return self.check_out

    def get_room_type(self):
        return self.room_type

    def get_room_number(self):
        return self.room_number

    def get_status(self):
        return self.status

    def get_total_cost(self):
        return self.total_cost

    # Setter methods to modify reservation attributes
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def set_guest(self, guest):
        self.guest = guest

    def set_check_in(self, check_in):
        self.check_in = check_in

    def set_check_out(self, check_out):
        self.check_out = check_out

    def set_room_type(self, room_type):
        self.room_type = room_type

    def set_room_number(self, room_number):
        self.room_number = room_number

    def set_status(self, status):
        self.status = status

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    # Method to display reservation information
    def displayreservation(self):
        return f"Reservation {self.reservation_id} for {self.guest.guest_name}."

    # Method to calculate the total cost of the reservation based on room price and nights
    def calculate_total_cost(self, room_price, nights):
        self.total_cost = room_price * nights
        return self.total_cost

    # Method to simulate sending a confirmation email
    def email_sent(self):
        return f"Email with confirmation sent to {self.guest.email}."

    # Method to update reservation status
    def status(self, new_status):
        self.status(new_status)
        return f"Updated status to {self.status}."


# Room class to represent hotel room details
class Room:
    def __init__(self, room_id, room_type, room_price, floor, beds, wifi, availability):
        # Initializing attributes for Room objects
        self.room_id = room_id
        self.room_type = room_type
        self.room_price = room_price
        self.floor = floor
        self.beds = beds
        self.wifi = wifi
        self.availability = availability

    # Getter methods to access room attributes
    def get_room_id(self):
        return self.room_id

    def get_room_type(self):
        return self.room_type

    def get_roomprice(self):
        return self.room_price

    def get_floor(self):
        return self.floor

    def get_number_of_beds(self):
        return self.beds

    def has_wifi(self):
        return self.wifi

    def is_available(self):
        return self.availability

    # Setter methods to modify room attributes
    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_room_type(self, room_type):
        self.room_type = room_type

    def set_room_rate(self, room_rate):
        self.room_rate = room_rate

    def set_floor(self, floor):
        self.floor = floor

    def set_number_of_beds(self, number_of_beds):
        self.number_of_beds = number_of_beds

    def set_wifi(self, wifi):
        self.wifi = wifi

    def set_availability(self, availability):
        self.availability = availability

    # Method to check if the room is available
    def check_availability(self):
        return self.availability

    # Method to update the room's availability status
    def update_availability(self, is_available):
        self.set_availability(is_available)
        return f"Room {self.room_id} availability updated to {self.availability}."


# Payment class to represent payment details and processes
class Payment:
    def __init__(self, payment_id, amount, payment_method, transaction_date, status, currency, guest):
        # Initializing attributes for Payment objects
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method
        self.transaction_date = transaction_date
        self.status = status
        self.currency = currency
        self.guest = guest  # Link to Guest object

    # Getter methods to access payment attributes
    def get_payment_id(self):
        return self.payment_id

    def get_amount(self):
        return self.amount

    def get_payment_method(self):
        return self.payment_method

    def get_transaction_date(self):
        return self.transaction_date

    def get_status(self):
        return self.status

    def get_currency(self):
        return self.currency

    def get_guest(self):
        return self.guest

    # Setter methods to modify payment attributes
    def set_paymentid(self, payment_id):
        self.payment_id = payment_id

    def set_amount(self, amount):
        self.amount = amount

    def set_paymentmethod(self, payment_method):
        self.payment_method = payment_method

    def set_transactiondate(self, transaction_date):
        self.transaction_date = transaction_date

    def set_status(self, status):
        self.status = status

    def set_currency(self, currency):
        self.currency = currency

    def set_guest(self, guest):
        self.guest = guest

    # Method to process the payment
    def process_payment(self):
        self.set_status("Completed")
        return f"Payment {self.payment_id} processed successfully."

    # Method to refund a payment
    def refund_pay(self):
        self.set_status("Refunded")
        return f"Payment {self.payment_id} has been refunded."

    # Method to retrieve payment status
    def get_payment_status(self):
        return self.status


# Example guest object creation
guest1 = Guest(guest_id=101, guest_name="Ebrahim Al Hosani", email="EbrahimHosani@gmail.com",
               phone_number="050192131", address="Mohammed Bin Zayed", country="UAE", ebrahim_points=1500)
# Example reservation object creation linked to guest1
reservation1 = Reservation(reservation_id=1, guest=guest1, check_in="15-8-2024", check_out="20-8-2024",
                           room_type="Deluxe Suite", room_number=505, status="Confirmed", total_cost=0)
# Example room object creation
room1 = Room(room_id=505, room_type="Suite", room_price=500,
             floor=5, beds=2, wifi=True, availability=True)
# Example payment object creation linked to guest1
payment1 = Payment(payment_id=301, amount=2500, payment_method="Credit Card",
                   transaction_date="2024-10-01", status="Pending", currency="AED", guest=guest1)

# Register the guest
print(guest1.register())
# Update the guest profile with new email and phone number
print(guest1.update_profile(
    new_email="EbrahimWaleedHosani@gmail.com", new_phone="0501231112"))
# Calculate the total cost of the reservation based on room price and number of nights
total_cost = reservation1.calculate_total_cost(room_price=room1.room_price, nights=5)
print(f"Total reservation cost: {total_cost} AED")
# Display the reservation details
print(reservation1.displayreservation())
# Check if the room is available
print(f"Room available: {room1.is_available()}")
# Process the payment for the reservation
print(payment1.process_payment())
# Send email confirmation for the reservation
print(reservation1.email_sent())
# Refund the payment
print(payment1.refund_pay())

# Create another guest, reservation, room, and payment objects
guest2 = Guest(guest_id=102, guest_name="Waleed Al Hosani", email="Waleed Al Hosani",
               phone_number="050123122", address="Mohammed Bin Zayed", country="UAE", ebrahim_points=2500)
reservation2 = Reservation(reservation_id=2, guest=guest2, check_in="1-3-2024", check_out="4-3-2024",
                           room_type="King Suite", room_number=502, status="Confirmed", total_cost=0)
room2 = Room(room_id=502, room_type="King Suite", room_price=5000,
             floor=10, beds=4, wifi=True, availability=True)
payment2 = Payment(payment_id=302, amount=5000, payment_method="Debit Card",
                   transaction_date="1-3-2024", status="Confirmed", currency="AED", guest=guest2)

# Register the second guest
print(guest2.register())
# Update the second guest's profile
print(guest2.update_profile(
    new_email="EbrahimWaleedHosani@gmail.com", new_phone="0501231112"))
# Calculate the total cost for the second reservation
total_cost = reservation2.calculate_total_cost(room_price=room1.room_price, nights=3)
print(f"Total reservation cost: {total_cost} AED")
# Display the second reservation details
print(reservation2.displayreservation())
# Check availability for the second room
print(f"Room available: {room2.is_available()}")
# Process the second payment
print(payment2.process_payment())
# Send email confirmation for the second reservation
print(reservation1.email_sent())
# Refund the second payment
print(payment2.refund_pay())
