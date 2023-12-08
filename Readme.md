# 6. RAG - Retrieval Augmented Generation
## 6.0 Introduction
input으로 주어진 source만 참고해서 질문에 대한 답을 생성
## 6.1 Data Loaders and Splitters
retrieving: data -> load -> transform(split) -> embed -> store

data loader: file을 load하기. text뿐만이 아니라 다양한 파일 포맷을 지원함

splitter: 파일을 분할하기. 단순 분할의 경우 분할된 크기가 비교적 크게 됨. chunk size를 지정해 주거나, 특별한 separator가 있는 경우 그것을 입력으로 해서 분할할 수 있음.
## 6.2 TikToken
AI 모델이 하는 것 처럼 token base로 source data를 encoding 하도록 하기
## 6.3 Vectors
## 6.4 Vector Store
## 6.5 Langsmith
## 6.6 RetrievalQA
## 6.7 Recap
## 6.8 Stuff LCEL Chain
## 6.9 Map Reduce LCEL Chain
## 6.10 Recap