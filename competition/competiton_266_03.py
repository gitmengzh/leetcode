"""

"""


def minimizedMaximum(n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        if n == 1:
            return min(quantities)
        elif sum(quantities) % n == 0:
            return int(sum(quantities) / n)
        else:
            return sum(quantities) // n + 1

if __name__  == "__main__":
    n = 1
    quantities = [15, 10, 10]
    print(minimizedMaximum(n, quantities))