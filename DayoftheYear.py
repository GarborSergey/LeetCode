# Сколько дней прошло с начала года?
class Solution:
    def dayOfYear(self, date: str) -> int:
        result = 0
        month_days = {'01': 31,
                      '02': 28,
                      '03': 31,
                      '04': 30,
                      '05': 31,
                      '06': 30,
                      '07': 31,
                      '08': 31,
                      '09': 30,
                      '10': 31,
                      '11': 30,
                      '12': 31,
                      }

        date = date.split('-')
        year = int(date[0])
        month = date[1]
        day = int(date[2])

        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            month_days['02'] = 29

        if month != '01':
            for m in month_days.keys():
                if int(month) > int(m):
                    result += month_days[m]

        return result + day
