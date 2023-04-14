# Many To One Relatioinships
관계형 데이터베이스 관계 : N:1

- foreign key : 다른 테이블 간의 관계를 만드는 데 사용


## 1. Commnet & Article
Many to one relationships : 한 개 이상의 태이블에 0~N개 이상의 관련된 관계(Commnet(N) & Article(1))

### 두 모델의 관계
- 참조 관계 : Commnet → Article
- 역참조 관계 : Article → Commnet 


### models.ForeignKey(To, on_delete=)


### 역참조 
나를 외래키로 지정한 테이블을 참조
but article에는 comment를 참조할 어더한 필드도 없다
```py
article.comment_set.all()
모델 인스턴스.related_manager.
```
- related_manager : 상대방 이름 + _set (역참조 시에 생성)
article에는 comment를 참조하게 도와줌