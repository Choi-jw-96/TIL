from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 복수 조회 articles
def index(request):
    # DB의 전체 게시글 조회 요청
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# 단수조회 article
def detail(request, pk):
    article = Article.objects.get(pk=pk) #(컬럼=url)
    # print(article)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # new페이지에서 보낸 사용자 데이터를 받음
    # print(request.GET)
    title = request.POST.get('title') #GET까지 딕셔너리 .get부터 딕셔너리 메서드
    content = request.POST.get('content')
    # 받은 데이터를 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 2
    article = Article(title=title, content=content)
    article.save()
    # 3
    # Article.objects.create(title=title, content=content)
    # content = {
    #     'title' : title,
    #     'content' : content
    # }
    # 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 이동 URL반환
    # return redirect("articles:index")

    # 생성한 글의 단일 조회로 응답
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=pk)
    # 조회한 데이터 삭제
    article.delete()
    return redirect("articles:index")


def edit(request, pk):
    # 수정 데이터 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 수정 작업 과정
    # 데이터 조회
    article = Article.objects.get(pk=pk)
    # 데이터 수정
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    # 데이터 저장
    article.save()

    return redirect('articles:detail', article.pk)