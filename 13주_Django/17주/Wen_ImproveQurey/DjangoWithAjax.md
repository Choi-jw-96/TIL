# 비동기적 언어(Ajax)
오래 걸리는 코드를 따로 실행하고 다른 코드 수행(자바스크립트)
- 여러 일을 동시에 할 수 있다

- 문서를 매번 다시 받지 않고 다시 그린다.

## 비동기 요청
`Axios` : javascript에서 HTTP 요청을 보내는 라이브러리 주로 프론트엔드 프레임워크에서 사용(=request)
```javascript
<script>
  axios({
    method : 'HTTP 메서드',
    url : 'url요청',
  })
```