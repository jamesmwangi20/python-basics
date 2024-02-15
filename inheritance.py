class Human:
    def james(self):
        print("i can walk")


    def tom(self):
        print("can run")

# hh = Human()
# print(hh.james())


# how to inherit
class Racoon(Human):
    def racoon(self):
        print("can smile")

j = Racoon()
print(j.james(), j.tom(), j.racoon())





