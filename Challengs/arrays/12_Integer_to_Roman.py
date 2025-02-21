class Solution:
    def intToRoman(self, num: int) -> str:
        v = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        total = []

        for value, symbol in v:
            if num == 0:
                break
            count = num // value
            total.append(symbol * count)
            num -= count * value
        return ''.join(total)