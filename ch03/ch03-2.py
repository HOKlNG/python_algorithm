"""
<2> 큰 수의 법칙 /해설 3-2.py

배열의 크기를 N, 숫자가 더해지는 횟수 M,그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.


[입력조건]
첫째 줄에 N(2<=N <=1,000) M(1<=M <=10,000), K(1<=K<=10,000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.


풀이 1회 :
2021-10-10(일) - 이해를 잘 못해서 참고해서 푼편.. // 더 잘풀린 답 있음..
"""


















def ch_3_2_20211010():
    n,m,k = map(int,input().split())
    data = list(map(int,input().split()))

    data.sort()

    first = data[-1]
    second = data[-2]

    result = 0

    while True:
        for i in range(k):
            if m != 0:
                result +=first
                m -= 1
            else:
                break
        if m !=   0:
            result += second
            m -= 1
        else:
            break

    return result



print(ch_3_2_20211010())

