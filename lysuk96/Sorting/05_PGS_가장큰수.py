#https://programmers.co.kr/learn/courses/30/lessons/42746
# 1트 퀵소트 : 왜 시간초과? ㅜㅜ
# 2트 cmp_to_key 정렬시 함수 매개(사용법 숙지해둘것 , 크면 1 , 같으면 0, 작으면 -1 return 하도록 함수 짜야됨)
from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        if int(a+b) > int(b+a):
            return 1
        elif int(a+b) < int(b+a):
            return -1
        else : return 0
    
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compare), reverse= True)
    # print(numbers)
    return '0' if numbers[0] == '0' else ''.join(numbers)

print(solution([3, 30, 34, 5, 9]))

#실패한 퀵소트 풀이
# def solution(numbers):
    
#     def quick_sort(arr, start, end):
#         if start >= end:
#             return
#         pivot = arr[start]
#         left = start + 1
#         right = end
#         # print('start ', start, end, arr)
#         while left <= right:
#             while left <= right and compare(arr[left], pivot):
#                 left+=1
#             while left <= right and compare(pivot, arr[right]):
#                 right-=1
            
#             if left <= right:
#                 arr[left], arr[right] = arr[right], arr[left]
#                 # print(left, right, arr)
                
#             else:
#                 arr[right], arr[start] = arr[start], arr[right]
#         # print('end ' ,left, right, arr)
                
#         quick_sort(arr, start, right-1)
#         quick_sort(arr, right+1, end)
        
#     def compare(a, b):
#         return (a+b > b+a)
    
#     numbers = list(map(str, numbers))
#     quick_sort(numbers, 0, len(numbers)-1)
#     # print(numbers)
    
#     answer = ''.join(numbers)
#     return str(int(answer))