투포인터를 사용해서 푸는 풀이는 패스하는게 나을 듯.. (정글에서 투포인터 유형 중요했으면 풀라고 했겠지)

이 문제는 특이하게 아래와 같이 arr[mid] == target 일 때 탈출해도 되는데

if(arr[mid] == target): 
        return mid 
    elif arr[mid] > target:
        end = mid -1
        res = mid
    else:
        start = mid +1

다른 문제랑 다르게 문제 조건에서 "특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다."
라는 언급이 있어서 그럼.. 

하지만 나는 다른 문제와 일관된 로직을 가져가고 싶어서 시간은 조금 낭비하더라도 
아래와 같이 변형해서 풀었고 그래도 통과함!

if(arr[mid] >= target): #이렇게 써도 통과~
    res = mid
    end=mid-1
else:
    start= mid+1