# Git Branch

![branch](branch.png)

## 정의

```
여러 개발자와 협력 시 섞이는 문제를 예방기위해 독자적인 흐름 관리를 위해 변경하는 법.

Branch 변경 후 작업을 Commit해도 원래 Branch에게는 log가 보이지 않는다.

반드시 원래 Branch가 Merge해야한다.

```

## ★Branch 문법
---
### git branch 브랜치명
* 브랜치를 생성

### git checkout/switch 브랜치명
* 브랜치를 변경

### git checkout -b 브랜치명
* 브랜치를 생성 + 변경
### git branch -d 브랜치명
* 브랜치를 삭제
### git branch
* 브랜치 목록
### git merge 브랜치명
* 브랜치들을 병합한다


## Github Flow 기본원칙
1. master branch는 **배포가능한 상태**일 것!
2. feature banch는 각 **기능의 의도**를 알 수 있게 작성할 것!
3. commit message는 [명확](Good_commit_message)하게 작성할 것!
4. pull request를 통해 리뷰를 요청하여 Merge할 것!
5. 반드시 master가 Merge할 것!

## 권한이 없는 저장소 수정은?

1. fork하여 내 저장소로 옮긴다
2. clone하여 수정 후
3. push하여 내 저장소에 저장 후
4. pull requset로 master에게 리뷰를 요청한다.



## 주의사항 
- 병합 시 동일한 내용이 충동할 수 있어 Status 확인이 필수!


---

## 추가사항
* git log --oneline -graph : 변화를 그래프로 보여준다