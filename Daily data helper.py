class DailyMessage:

    def __init__(self):
        self.m = ""

    def get_message(self):
        self.m = input("Enter today's message: ")

    def print_message(self):
        print("Message in uppercase:", self.m.upper())


d = DailyMessage()
d.get_message()
d.print_message()


class HelperSession:

    def __init__(self):
        print("Daily Data Helper session created")

    def __del__(self):
        print("Daily Data Helper session ended")


def create_session():
    print("Making helper session...")
    s = HelperSession()
    print("Session is ready...")
    return s


print("")
print("Calling create_session() function...")
s = create_session()
print("Program is still running...")


class PairFinder:

    def find_pair(self, nums, t):
        l = {}

        for i, n in enumerate(nums):
            x = t - n

            if x in l:
                return (l[x], i)

            l[n] = i

        return None


nums = (10, 20, 30, 40, 50, 60, 70)

t = int(input("Enter target sum to search: "))

r = PairFinder().find_pair(nums, t)

if r is not None:
    print("index1=%d, index2=%d" % r)
else:
    print("No matching pair found.")

del s
print("Program End")