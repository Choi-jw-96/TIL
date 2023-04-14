# URSs

## URL dispatcher
URL 패턴을 정의하고 해당 패턴에 일치하는 요청을 처리할 view 함수를 연결(매핑)


## 변수와 URL
### variable rounting
url 일부에 변수를 포함시키는 것
(변수는 view 함수의 인자로 전달 할 수 있음)

```
<path_converter:variable_name>
path('<>', views.)
```
#### path_converter
URL 변수의 타입을 지정(str, int...5가지 타입 지정)

## App의 URL


## URL 이름 지정
### Naming URL patterns
URL에 이름을 지정하는 것
```
urls
name = 'dinner'
```

### url tag
주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
```
{% url 'dinner' %}
```