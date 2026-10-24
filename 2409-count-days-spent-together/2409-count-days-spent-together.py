class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice,arriveBob)
        end = min(leaveAlice,leaveBob)

        if start > end:
            return 0

        start_month, start_day = map(int, start.split("-"))   
        end_month, end_day = map(int, end.split("-")) 

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        st_day_year = sum(days[:start_month - 1]) + start_day
        end_day_year = sum(days[:end_month - 1]) + end_day

        return end_day_year - st_day_year + 1