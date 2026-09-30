class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for card in sorted(count):
            if count[card] == 0:
                continue

            freq = count[card]

            for i in range(k):
                if count[card + i] < freq:
                    return False

                count[card + i] -= freq

        return True