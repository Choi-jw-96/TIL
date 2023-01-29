# 목차 주요 내용

## [스텍, 큐](Stack_Queue.md)
```
Stack 스택
    `후입선출` 방식
    이전 작업을 되돌릴 때

    괄호매칭

Queue 큐
    선입선출

    list.pop()으로 활용 가능

    deque
    양방향으로 입출력
    큐보다 삽입 추출이 빠르다
    >from collections import deque 
    appendleft(), poplieft()
```

## [힙, 셋](Heap_Set.md)
```
중요도를 기준으로 `우선순위를 결정`
→ `우선순위 큐`

Heap 힙
    최대값, 최소값을 빠르게 찾도록 해줌
    중복값 허용
    삽입 삭제 수정 조회 연산 속도가 리스트 보다 빠르다
    >import heapq   
    heapq.heapify() : 정렬  
    heapq.heappop(list[]) : 삭제    
    heapq.heappush(list, item)

Set 셋
    집합을 나타내는 데이터 구조
    중복 없음

     | : 합집합    
     `-` : 차집합    
     & : 교집합 
     ^ : 대칭차집합
 ```




