'''
거스름돈
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	7821	4944	4362	63.484%
문제
타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.



입력
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

출력
제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.

예제 입력 1 
380
예제 출력 1 
4
'''

a = 500
b = 100
c = 50
d = 10
e = 5
f = 1

def Taro(coin, count):
    if coin >= a :
        coin = coin - a
        count = count+1
        return Taro(coin, count)
    elif a > coin >= b :
        coin = coin - b
        count = count+1
        return Taro(coin, count)
    elif b > coin >= c :
        coin = coin - c
        count = count+1
        return Taro(coin, count)
    elif c > coin >= d :
        coin = coin - d
        count = count+1
        return Taro(coin, count)
    elif d > coin >= e :
        coin = coin - e
        count = count+1
        return Taro(coin, count)
    elif e > coin >= f :
        coin = coin - f
        count = count+1
        return Taro(coin, count)
    elif coin == 0 :
        return count
    

if __name__ == "__main__" :
    count = 0
    cash = 1000
    coin_str = input()
    coin = int(coin_str)
    print(Taro(1000-coin, 0))
        


