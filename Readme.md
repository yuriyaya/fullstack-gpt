# 9. Quiz GPT
## 9.0 Introduction
## 9.1 WikipediaRetriever
Wikipedia에서 입력한 키워드로  검색해서 결과를 받아오고, 문서로 사용할 수 있음.
## 9.2 GPT-4 Turbo
GPT 모델에 따라서 가격과 context window(한번에 볼 수 있는 토큰의 갯수)가 다름.

예제로 사용하고 있는 1984 챕터의 경우 전체가 7700 토큰 정도 되므로 한 챕터를 몽땅 다 넣을 수 있는 context window를 가진 모델을 쓰면 나누지 않아도 되서 좋음.

적절한 context window와 적절한 가격, 응답속도를 가진 모델을 선택해서 사용해야 함. 현재 시점에서는 GPT 3.5 Turbo가 적당히 저렴한듯 (최신은 GPT-4 Turbo)

Tokenizer: https://platform.openai.com/tokenizer
## 9.3 Questions Prompt
문서를 주고 quiz를 생성하도록 하기. prompt를 자세하게 써서 의도에 맞게 생성하도록 해야 함.

wikipedia retriever는 왜인지 작동을 하지 않는다. 에러 발생... 검색해도 이유를 모르겠음.
==> top_k_results를 5로 하니까 잘 동작함. 1로 하면 동작 안함...
## 9.4 Formatter Prompt
formatting prompt를 만들고 생성한 퀴즈를 formatting chain에 넣어서 원하는대로 formatting 해달라고 함.
## 9.5 Output Parser
## 9.6 Caching
## 9.7 Grading Question
## 9.8 Function Calling
## 9.9 Conclusion