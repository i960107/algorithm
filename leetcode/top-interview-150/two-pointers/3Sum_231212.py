from typing import List


# 중복 없애는 방법이 가장 중요!!
# 1) 배열에서 중복을 제거한다, -> [0,0,0]이 정답이 될 수 있음
# 2) 이전에 ans배열에 삽입된 triplet을 체크한다.[-2,-2,4] [-2, -1, 3], [-2,-2,4]가 될 수 있음.
# 3) set으로 visited를 체크한다.. 오래걸림.
class Solution:
    # 만약 인덱스를 반환하는 거라면?
    # 아예 중복 자체를 없애는 것 안됨.
    def threeSum_fail(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print("정렬", nums)

        # 중복 없애기
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pos] = nums[i]
                pos += 1

        print("중복 없음", nums)
        answer = []
        # 어떻게 distinct triplet할 수 있지?
        # 원래 배열에서 중복을 없앤다?
        for i in range(pos):
            j, k = i + 1, pos - 1
            while j < k:
                print("ijk", i, j, k)
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    # 중복 없으므로 어떤 포인트든 하나만 옮기면 됨.
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return answer

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 인덱스에 중복이 없어야 한다 x 값에 중복이 없어야한다.
        # 바로 이전 triplet과 비교한다? 안됨. [-4,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

        answer = []
        visited = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet_str = ''.join(str(x) for x in triplet)
                    # answer and answer[-1] != triplet하면 첫번째 쌍이 들어가지 않음 주의!
                    if triplet_str not in visited:
                        answer.append(triplet)
                        visited.add(triplet_str)
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return answer

    # 세개 포인터가 모두 종복값을 가지면 안됨!
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            # ==로 비교하면 안됨. 이전에 while문으로 전진한만큼
            # while ans and i < len(nums) - 1 and ans[-1][0] == nums[i]:
            # while문으로 전진하기보다 for문 종료조건으로 체크하면 더 쉬움.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    # total == 0
                    ans.append([nums[i], nums[j], nums[k]])
                    # 한칸씩 옮긴 후 같은 값인지 체크.
                    # while ans and j < len(nums) - 1 and ans[-1][1] == nums[j]:
                    #     j += 1
                    # while ans and k > 0 and ans[-1][2] == nums[k]:
                    #     k -= 1
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1

        return ans


s = Solution()
# print(s.threeSum([-1, 0, 0, 1, 1]))
# print(s.threeSum([0, 1, 1]))
# print(s.threeSum([0, 0, 0]))
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))
