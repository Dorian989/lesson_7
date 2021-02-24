class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
       ans = ''
       if len(self.input) == len(other.input):
           for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                   return 'problems with form_1'

                summed = [x + y for x, y in zip(line_1, line_2)]
                ans += ' '.join(map(str, summed)) + '\n'


       else:
           return 'problems with form_2'
       return ans



matr_1 = Matrix([[10, 20], [37, 45], [43, 90]])
matr_2 = Matrix([[21, 60], [25, 19], [30, 25]])

print(matr_1)
print()
print(matr_2)
print()
print(matr_1 + matr_2)
