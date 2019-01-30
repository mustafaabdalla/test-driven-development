number_type =(int, float, complex)

class Calculator:

    @staticmethod

    def validate_values(a,b):

        if not isinstance(a, number_type) and not isinstance(b, number_type):

            return ValueError
        

    def add(self, a, b):

        self.validate_values(a, b)
        return a + b