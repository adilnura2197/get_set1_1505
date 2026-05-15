class Car:
    company_name = "Chevrolet"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"Rang: {self.color}")
        print(f"Kompaniya: {Car.company_name}")


c1 = Car("Cobalt", "Oq")
c2 = Car("Malibu", "Qora")
c3 = Car("Tracker", "Kulrang")

c1.show_info()

print("--------------")

c2.show_info()

print("--------------")

c3.show_info()
