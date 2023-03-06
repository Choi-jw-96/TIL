# Semantic Web
웹 데이터를 의미론적으로 표현하고 연결하는 개념

컴퓨터가 데이터의 *내용과 문맥을 더 효율적으로 이애*하고 더 지능적으로 활용

→ 요소가 목적의 역할/ 어떻게 보이나

## [Semantic in HTML](01.html)
기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소

(검색 엔진 및 개방자가 웹페이지를 이해하기 쉽게 만들어줌)


### 대표적인 semantic element
div대신 알아보기 쉽게 이런 태그로 작성해 보자
- header
- nav
- main
- article
- section
- aside
- footer

## Semantic in HTML

### [oocss](02.html)
object-oriendted csss

객체 지향적 접근법을 적용하여 css를 구성하는 방법론

ex. 카드의 기본구조(card, card-title..) 버튼의 기본구조 (button, button-color)

### [B.E.M].(03.html)
Block Element Modifier

블록, 요소, 수정자를 사용해 클래스 이름을 구조화 하는 방법론

#### Block
**문단 전체**에 적용된 요소 & 요소를 담고 있는 **컨테이너**
재사용 가능한 독립적인 블록으로 **가장 바깥쪽 상위요소**
재사용을 위해 **margin, padding을 적용하지 않음**

#### Element
block이 포함하고 있는 한 조각
블록을 구성하는 종속적 **하위요소**


#### Modifier
block 또는 element의 **속성**

--- 
참고
### 의미론적인 마크업의 이점
- 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
- 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 주가직인 도움

### 클래스 이름이 너무 길어지는게 아닐까?
- 빠르고 명확한 표기가 중요

### OOCSSS & BEM 목적
- 재사용 가능한 모듈로 분리함으로써 유지 보수성과 확장성을 향상


### [emmet 표기법](https://docs.emmet.io/cheat-sheet/)
-div.kdt
-div.wrapper>ul.list>li.item-$*5>a{link $}