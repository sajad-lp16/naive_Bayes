data = [
    ['RED', 'SPORT', 'NO', 'YES'],
    ['RED', 'SPORT', 'NO', 'NO'],
    ['RED', 'SPORT', 'NO', 'YES'],
    ['BLACK', 'SPORT', 'NO', 'NO'],
    ['BLACK', 'SPORT', 'YES', 'YES'],
    ['BLACK', 'SPORT', 'YES', 'YES'],
    ['BLACK', 'CLASSIC', 'NO', 'NO'],
    ['RED', 'SPORT', 'YES', 'YES'],
    ['YELLOW', 'SPORT', 'YES', 'NO'],
    ['YELLOW', 'CLASSIC', 'NO', 'YES'],
    ['YELLOW', 'SPORT', 'YES', 'NO'],
    ['YELLOW', 'CLASSIC', 'YES', 'YES'],
    ['YELLOW', 'CLASSIC', 'NO', 'NO'],
]


class NaiveBaYESClassifier:

    def __init__(self, X, y):

        self.X, self.y = X, y

        self.N = len(self.X)

        self.dim = len(self.X[0])

        self.attrs = [[] for _ in range(
            self.dim)]

        self.output_dom = {}

        self.data = []

        for i in range(len(self.X)):
            for j in range(self.dim):
                if not self.X[i][j] in self.attrs[j]:
                    self.attrs[j].append(self.X[i][j])

            if not self.y[i] in self.output_dom.keys():
                self.output_dom[self.y[i]] = 1
            else:
                self.output_dom[self.y[i]] += 1
            self.data.append([self.X[i], self.y[i]])

    def classify(self, entry):

        solve = None
        max_arg = -1

        for y in self.output_dom.keys():

            prob = self.output_dom[y] / self.N  # P(y)

            for i in range(self.dim):
                cases = [x for x in self.data if x[0][i] == entry[i] and x[
                    1] == y]
                n = len(cases)
                prob *= n / self.N

            if prob > max_arg:
                max_arg = prob
                solve = y

        return solve


y = list(map(lambda v: v[3], data))

X = []
for h in data:
    X.append(h[:3])

y_train = y
X_train = X

print((len(y_train)))
print((len(X_train)))

nbc = NaiveBaYESClassifier(X_train, y_train)

input_data = input().upper()
options = input_data.split(', ')

predict = nbc.classify(options)
print(predict)
