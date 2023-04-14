class Math:
    number = 3

    def add(self):
        pass
    def __init__(self) -> None:
        pass
    

a = Math()

result = a.add()


a = []


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# Article 클래스의 인스터스 생성
article = Article()

# article 인스턴스에 title과 content인스터스 변수값을 저장
article.title = '제목'
article.content = '내용'

# 테이블에 레코드 하나 생성을 위해 저장(중요! 저장이 되야 pk가 생성!)
article.save()


# 생성 2번째 방법
article = Article(title ='second', content='django!')
article.save()

#모든 게시글 출력
articles = Articles.object.all()
for article in articels:
    ...:     print(article.pk)  (기본값==id)
    ...:     print(article.title)
    ...:     print(article.content)
    ...:     print(article.created_at)



# 생성 3번째 방법(save기능 내장)
Article.objects.create(title ='third', content='django!')



# 단일 데이터 조회(무조건 pk랑 비교)
# 조건에 해당 셀이 없거나 중복이 있다면 error
article = Article.objects.get(pk=1)
article


# 특정 데이터 조회
# 중복 조회 가능 & 해당 셀이 없어도 빈 Queryset 출력
article = Article.objects.filter(content='django!')
article

# 세부 조건(dj로 시작하는 경우)
Article.objects.filter(content__startswith='dj')