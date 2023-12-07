# 4. Model IO
## 4.0 Introduction
## 4.1 FewShotPromptTemplate
답변을 어떻게 하는지 미리 예제를 주면(=few shot) 새로운 질문을 했을 때 대답을 example 형식에 맞춰서 해주게 됨
이미 형식화 된 데이터가 있다고 하면 좀 더 유효한 답변을 얻을 수 있음.
## 4.2 FewShotChatMessagePromptTemplate
이전 챕터와 동일한데 ChatMessagePromptTemplate을 이용하는 방법
## 4.3 LengthBasedExampleSelector
example을 어떤것을 선택하느냐에 따라 결과가 달라질 수 있어서 인지(?) example을 선택하는 방법을 구현하는 법에 대한 내용.
단순히 길이로 자를 수도 있고, 리스트에 담긴 예제 중 일부만 선택해서 넣을 수 있음.
예시로 돌려본게 별로 복잡하지 않은 경우라 example selector가 별로 체감이 되지 않는 것일 수도 있지만, 비용을 위해 예제를 일부만 넣어야 한다거나, example의 패턴이 다양해서 특정 example만 넣어야 할 경우에 적용할 수 있지 않을까...
## 4.4 Serialization and Composition
## 4.5 Caching
## 4.6 Serialization
