from math import *
import eel


class Palindrom:
    s = ""

    def alg(self, inps):
        self.s = inps
        n = len(self.s)
        if n < 2:
            return self.s
        P = [[False for _ in range(n)] for _ in range(n)]
        longest = self.s[0]

        # j is the length of palindrome
        for j in range(1, n + 1):
            for i in range(n - j + 1):
                # if length is less than 3, checking s[i] == s[i+j-1] is sufficient
                P[i][i + j - 1] = self.s[i] == self.s[i + j - 1] and (j < 3 or P[i + 1][i + j - 2])
                if P[i][i + j - 1] and j > len(longest):
                    longest = self.s[i:i + j]
        return longest


class House:
    max_elem = 1
    max_g = 1
    max_p = 1
    max_m = 1

    def alg(self, a, b, c ,m):
        self.max_g = a
        self.max_p = b
        self.max_m = c
        self.max_elem = m
        answer = (factorial((self.max_elem) / (factorial(self.max_elem - (self.max_g+self.max_p+self.max_m)))))
        return answer


newpal = Palindrom()
newhouse = House()



@eel.expose
def add_str(st):
    return newpal.alg(st)

@eel.expose
def add_el(a, b, c ,m):
    return newhouse.alg(int(a), int(b), int(c), int(m))


eel.init("web")
eel.start("index.html", size=(1000, 900))