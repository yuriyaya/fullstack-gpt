# 5. Memory
## 5.0 ConversationBufferMemory
보통 ChatGPT 사용 할 때 이전 대화가 계속 저장되지는 않음. 열려 있는 세션에서 유지되는 경우가 있는데, 이런 저장된 내용이 있으면 context 안에서 답변이 나오므로 더 효율적임.
답변을 저장하는 방식에 여러가지가 있는데, 0번 챕터는 무작정 저장하는 방식.
여러번 같은거 물어봐도 계속 추가해서 저장해 줌. 메모리가 계속 늘어나므로 대화가 지속되면 메모리 소모도 비례해서 커지게 됨.
## 5.1 ConversationBufferWindowMemory
## 5.2 ConversationSummaryMemory
## 5.3 ConversationSummaryBufferMemory
## 5.4 ConversationKGMemory
## 5.5 Memory on LLMChain
## 5.6 Chat Based Memory
## 5.7 LCEL Based Memory
## 5.8 Recap