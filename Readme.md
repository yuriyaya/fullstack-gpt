# 5. Memory
## 5.0 ConversationBufferMemory
보통 ChatGPT 사용 할 때 이전 대화가 계속 저장되지는 않음. 열려 있는 세션에서 유지되는 경우가 있는데, 이런 저장된 내용이 있으면 context 안에서 답변이 나오므로 더 효율적임.
답변을 저장하는 방식에 여러가지가 있는데, 0번 챕터는 무작정 저장하는 방식.
여러번 같은거 물어봐도 계속 추가해서 저장해 줌. 메모리가 계속 늘어나므로 대화가 지속되면 메모리 소모도 비례해서 커지게 됨.
## 5.1 ConversationBufferWindowMemory
window의 사이즈를 정해놓고 정해놓은 숫자 만큼의 대화를 기억함.
메모리는 절약할 수 있지만 예전 대화는 잃어버림
## 5.2 ConversationSummaryMemory
대화 내용을 요약해서 저장해 줌.
초기에는 간단한 문장을 말 잘 하는 모드로 저장해 주기 때문에 토큰이 더 들 수는 있지만, 대화 내용이 길어질수록 더 유용함.
## 5.3 ConversationSummaryBufferMemory
Buffer와 Summary를 통합해서 사용할 수 있도록 해줌
기본적으로 설정된 max token에 도달할 때 까지는 Buffer와 동일하게 동작하지만
max token을 넘어가게 되면 이전 내용을 잃어버리는게 아니라 summary 해서 가지고 있음. 
## 5.4 ConversationKGMemory
## 5.5 Memory on LLMChain
## 5.6 Chat Based Memory
## 5.7 LCEL Based Memory
## 5.8 Recap