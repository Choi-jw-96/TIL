# Grid system web design

## 개요
**Responsive Web Design**

디바이스 종류/크기와 무관하게 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
- 12개의 column
- 6개의 breakpoint
로 구현한다


## [Grid system Breapoints](01.html)
웹 페이지를 다양한 화면 크기에 적절하게 배치하기 위한 6개의 분기점

![Grid_system_Breapoint](Grid_system_Breapoint.png)

각 breakpoints 마다 설정된 최대 너비 값 **이상으로** 화면이 커지면 grid system 동작이 변경된

```html
<div class="container">
    <div class="row g-0">
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
            <div class="box">col</div>
        </div>
    </div>
</div>
```

## Summary


---
참고

[Grid cards](02.html)

참고 블로그
[blog](https://ishadeed.com/article/responsive-design/)