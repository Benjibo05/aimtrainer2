class Båt:
    def __init__(self, namn, längd):
        self.namn = namn
        self.längd = längd

    def print_info(self):
        print(f"{self.namn} är {self.längd} meter lång")

class SegelBåt(Båt):
    def __init__(self, namn, längd, segel_area):
        super().__init__(namn, längd)
        self.segel_area = segel_area

    def print_info(self):
        print(f"{self.namn} är {self.längd} meter lång och seglet är {self.segel_area} kvadratmeter")

class MotorBåt(Båt):
    def __init__(self, namn, längd, motor, hästkraft):
        super().__init__(namn, längd)
        self.motor = motor
        self.hästkraft = hästkraft

    def print_info(self):
        print(f"{self.namn} är {self.längd} meter lång och har motorn {self.motor} med {self.hästkraft} hästkrafter")

min_segelbåt = SegelBåt("The Black Pearl", 30, 150)
min_segelbåt.print_info()



min_motorbåt = MotorBåt("Freds båt", 12, "Verado V12", 600)
min_motorbåt.print_info()
