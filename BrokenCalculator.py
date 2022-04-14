# Дается два числа исходное и цель, можно проводить только две операции -1 и *2,
# дать ответ минимальное кол-во операции за которое от старта до значения добраться можно

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2:
                target += 1
            else:
                target //= 2

        return ans + startValue - target