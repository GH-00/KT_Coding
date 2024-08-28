'''
세로 길이는 무조건 3이다.
규칙을 찾자

크게보면 6칸 짜리 조립된 블럭과 3칸짜리 막대로 모든 타일을 채워야한다.
6칸 짜리 블록은 3(파란색 2 + 보라색 1)가지가 될 수 있다.

그럼 가로가 한 칸씩 늘어남에 따라 경우의 수를 추가해 나가보자.
DP 활용

dp[i] = k
i번째 까지 봤을 때, 모든 경우의 수 k

dp[i] = (dp[i-1]*1 + dp[i-2]*2 + dp[i-3]*5)%1000000007

한 칸이 추가될 수 있는 경우는 1개
두 칸이 추가될 수 있는 경우는 2개
세 칸이 추가될 수 있는 경우는 위 경우를 포함하는 경우는 제외하고 가로로 쌓은 부분 총 5개

'''

def solution(n):
    answer = 0
    dp = [0]*100001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10

    for i in range(4, n+1):
        dp[i] = (dp[i-1]*1 + dp[i-2]*2 + dp[i-3]*5)%1000000007
    
    answer = dp[n]
    return answer

n = 4
print(solution(n))