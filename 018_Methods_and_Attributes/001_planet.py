class Planet:

    shape = 'round'  # class level attribute

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):  # instance only attribute
        return f'{self.name} is orbiting in the {self.system}'
    
    # decorator
    @classmethod  # class level method
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    # decorator - This is a method which does not have access to self  
    #             and does not have access to the class itself.
    # It only has access to the parameters that we pass it explicitly.
    # It is accessible on the instance and the class itself.
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

print(Planet.commons())  # This class method is accessible on the class
print(naboo.commons())   # and instances of the class.
print(Planet.spin())
print(Planet.spin('a very high speed'))
print(naboo.spin('a very high speed'))
