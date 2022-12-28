# 원격저장소 Github (Remote Repository)
## Github?
```
Git(분산버진원격관리)을 한 정보를 공유하는 저장소
    → 버전을 관리하는 곳
작업물의 변경을 추적하고 사용자들간의 작업물 조율을 도움
```

## 연동하는 법


1. Github에서 New repository를 만든다.

2. repository의 URL를 복사한다.

3. 올리고 싶은 git에 URL를 입력한다.

    Git remote add origin URL

    Git아 원격저장소를 추가해줘 오리진을 URL에
 
 - 기타 코드
 
    Git remote -v : 원격저장소 정보 확인
    Git remote rm origin : 원격저장소 삭제

###


## ★관리코드

![UseGithub](git_github.png)
```
 저장한 파일작업 → Add → Commit (필수)
 ```

### Push

    로컬저장소에서 Github에 올린다.

    Git push origin master
        (원격저장소 명) (브랜치) 


### Pull
    Github에서 commit한 내용을 로컬저장소로 업데이트한다.
    Git pull origin master


### Clone
    Githube에 있는 버전을 복제한다.
    Clone 후 별도의 Git init은 필요없다.
    바탕화면 Git bash에서
    Git clone URL




### .Gitignore
    버전 관리와 관련 없거나 보안상 중요한 버전을 무시한다.
    .Gitignore 파일을 생성 후 내용에 무시할 파일 이름을 적는다.
    이미 commit했다면 삭제해도 기록에 남기때문에 항상 미리 만들어 놓자!
-참조 사이트
    [GITIGNORE](https://www.toptal.com/developers/gitignore/)


## 오류사항(merge conflict)

![오류](merge%20conflict.png)

    Push하고 싶은 버전이 Github에서 미리 업데이트가 있는 경우
    → Pull해서 업데이트 후 Push



## 기타 참고사항
- Pull과 Clone의 차이?

![pull_vs_clone](pull_clone.png)

    Pull은 로컬디스크에 있는 Git에 새로운 버전을 업데이트

    Clone은 최초로 가져오는 프로젝트 (=이전 버전이 없음)

- Git clone URL과 .zip 다운의 차이?
    
    Git clone URL은 이전 수정된 버전을 가져올 수 있음
    
    .zip은 마지막 수정본만 가져올 수 있음.

- Git base 복사 붙여넣기

    복사 : Ctrl + Insert

    붙여넣기 : Shift + Insert

-----

## 관련 추가 사이트

- (초심자용)[https://backlog.com/git-tutorial/kr/intro/intro1_1.html]

- (Git 완벽 책)[https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-%EB%B2%84%EC%A0%84-%EA%B4%80%EB%A6%AC%EB%9E%80%3F]


