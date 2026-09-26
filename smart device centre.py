from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def show_device(self, n):
        print("Device Name:", n)

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now ON")


class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Fan is now ON")


class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is now ON")


l = SmartLight()
f = SmartFan()
s = SmartSpeaker()

l.show_device("Living Room Light")
l.turn_on()

f.show_device("Bedroom Fan")
f.turn_on()

s.show_device("Music Speaker")
s.turn_on()


class SecurityCamera:
    def check_status(self):
        print("Security Camera is recording")


class DoorLock:
    def check_status(self):
        print("Door Lock is secure")


d = [SecurityCamera(), DoorLock()]

print("")
print("===== SMART DEVICE STATUS =====")

for x in d:
    x.check_status()

print("===============================")