class A:
    def __init__(self, n, color = (0, 200, 0)):
        self.color = color
        self.n = self.seq(n)

    def seq(self, n):
        a, b, c = 0, 1 ,2
        while True:
            yield a, b, c
            a, b, c = b, c, c + 1
            if (a, b, c) == (n-2, n-1, n):
                a, b, c = 1, 2, 3

    def get_col(self):
        return self.color

    def get_seq(self):
        return  next(self.n)


class B:
    def __init__(self, n, min_color=(99, 33, 107), max_color=(255, 100, 255)):
        self.n = n
        self.min_color = min_color
        self.max_color = max_color
        self.generator = self.gradient_generator()

    def lerp(self, start, end, t):
        return int(start + (end - start) * t)

    def gradient_generator(self):
        i = 0
        while True:
            t = i / (self.n - 1)
            r = self.lerp(self.min_color[0], self.max_color[0], t)
            g = self.lerp(self.min_color[1], self.max_color[1], t)
            b = self.lerp(self.min_color[2], self.max_color[2], t)
            yield (r, g, b)
            i = (i + 1) % self.n

    def get_col(self):
        return next(self.generator)

    def get_seq(self):
        return list(range(15))