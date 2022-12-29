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


## 주의사항 
- 병합 시 동일한 내용이 충동할 수 있어 Status 확인이 필수!


---

## 추가사항
* git log --oneline -graph : 변화를 그래프로 보여준다