#題目一
class MyClass:
    def __init__(self, attribute1, attribute2, attribute3):
        """
        建構子函式，用於初始化類別的屬性。
        
        Parameters:
        - attribute1: 第一個屬性
        - attribute2: 第二個屬性
        - attribute3: 第三個屬性
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    def function1(self):
        """
        第一個副函式
        """
        print(f"Function 1 called with attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")

    def function2(self):
        """
        第二個副函式
        """
        print(f"Function 2 called with attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")

    def function3(self):
        """
        第三個副函式
        """
        print(f"Function 3 called with attributes: {self.attribute1}, {self.attribute2}, {self.attribute3}")


# 建立三個物件
obj1 = MyClass("Value1A", "Value1B", "Value1C")
obj2 = MyClass("Value2A", "Value2B", "Value2C")
obj3 = MyClass("Value3A", "Value3B", "Value3C")

# 呼叫副函式 (共呼叫9次)
obj1.function1()
obj1.function2()
obj1.function3()

obj2.function1()
obj2.function2()
obj2.function3()

obj3.function1()
obj3.function2()
obj3.function3()

#題目二
class Luggage:
    def __init__(self, luggage_id, weight, departure_airport, destination_airport, passenger_name):
        self.luggage_id = luggage_id
        self.weight = weight
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.passenger_name = passenger_name

    def display_info(self):
        print(f"Luggage ID: {self.luggage_id}")
        print(f"Weight: {self.weight} kg")
        print(f"Departure Airport: {self.departure_airport}")
        print(f"Destination Airport: {self.destination_airport}")
        print(f"Passenger Name: {self.passenger_name}")
        print()

    def update_luggage_id(self, new_luggage_id):
        self.luggage_id = new_luggage_id

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_departure_airport(self, new_departure_airport):
        self.departure_airport = new_departure_airport

    def update_destination_airport(self, new_destination_airport):
        self.destination_airport = new_destination_airport

    def update_passenger_name(self, new_passenger_name):
        self.passenger_name = new_passenger_name


class BoardingPass:
    def __init__(self, passenger_name, boarding_pass_number, boarding_time, gate_number, seat_location):
        self.passenger_name = passenger_name
        self.boarding_pass_number = boarding_pass_number
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.seat_location = seat_location

    def display_info(self):
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Boarding Pass Number: {self.boarding_pass_number}")
        print(f"Boarding Time: {self.boarding_time}")
        print(f"Gate Number: {self.gate_number}")
        print(f"Seat Location: {self.seat_location}")
        print()

    def update_passenger_name(self, new_passenger_name):
        self.passenger_name = new_passenger_name

    def update_boarding_pass_number(self, new_boarding_pass_number):
        self.boarding_pass_number = new_boarding_pass_number

    def update_boarding_time(self, new_boarding_time):
        self.boarding_time = new_boarding_time

    def update_gate_number(self, new_gate_number):
        self.gate_number = new_gate_number

    def update_seat_location(self, new_seat_location):
        self.seat_location = new_seat_location


def query_luggage_by_id(luggage_list, luggage_id):
    for luggage in luggage_list:
        if luggage.luggage_id == luggage_id:
            luggage.display_info()


# 主函式
def main():
    luggage1 = Luggage("L001", 20, "Airport1", "Airport2", "Passenger1")
    luggage2 = Luggage("L002", 15, "Airport2", "Airport3", "Passenger2")
    luggage3 = Luggage("L003", 25, "Airport3", "Airport4", "Passenger3")

    boarding_pass1 = BoardingPass("Passenger1", "BP001", "12:00 PM", "Gate A", "A1")
    boarding_pass2 = BoardingPass("Passenger2", "BP002", "1:30 PM", "Gate B", "B2")
    boarding_pass3 = BoardingPass("Passenger3", "BP003", "3:00 PM", "Gate C", "C3")

    # 查詢行李
    query_luggage_by_id([luggage1, luggage2, luggage3], "L002")

    # 修改行李資訊
    luggage2.update_weight(18)
    luggage2.update_destination_airport("Airport4")

    # 重新查詢行李
    query_luggage_by_id([luggage1, luggage2, luggage3], "L002")

if __name__ == "__main__":
    main()
