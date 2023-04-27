# Handing http requests
HTTP requests 처리에 따른 view 함수 구조의 변화

new = 페이지를 생성할때 필요한 입력을 하러 가는 페이지 (GET)
creat = 생성하는 요청을 처리하는 method(POST)

둘을 합치면?
views.py
```py
def new_create(request):
    # HTTP requests method POST라면
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```