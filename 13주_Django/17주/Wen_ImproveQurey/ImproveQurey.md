# 쿼리 개선
반복되는 쿼리를 줄여서 로딩속도를 올리자
### select_related (InnerJoin)
- 원인 : 각 게시글 출력 시 유저 이름 반복 평가

### prefeprefetch_related
역참조 시 전부 가져오고 싶을때