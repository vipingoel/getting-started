class Person:
    i_walk_on_two_legs = "Yes"

    def __init__(self, name):
        self.my_name_is = name

    @classmethod
    def props(cls):
        print(cls.i_walk_on_two_legs)
        print(cls.my_name_is)

    def __instance_props(self):
        print(self.i_walk_on_two_legs)
        print(self.my_name_is)


p = Person("vipin")
p._Person__instance_props()
