# 3. Welcome to Langchain
## 3.0 LLMs and Chat Models
## 3.1 Predict Messages
predict 함수와 달리 predict_messages 함수는 여러가지 setting을 넣어서 대화할 수 잇음.
- SystemMessage : 사람과 대화하는 AI system에 대한 셋팅. 답변하는 AI에게 일종의 contesxt 부여. 예제에서는 지리 전문가이고 한국 사람으로 설정함
- AIMessage : 답변을 할 AI에 대한 셋팅. 예제에서는 이름을 부여함
- HumanMessage : 이게 유저가 ChatGPT한테 물어보는 질문 내용. 예제에서는 지리적인 정보와 이름을 한국어로 물어보았음. System을 지리 전문가와 한국어를 할 수 있는 것으로 먼저 셋팅하였고, AI의 이름은 영수라고 했기 때문에 이를 종합적으로 판단해서 한국어로 답변을 준것.
## 3.2 Prompt Templates
prompt를 template으로 만들어서 사용하기