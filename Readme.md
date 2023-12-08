# 8. Private GPT
## 8.0 Introduction
## 8.1 HuggingFaceHub
HuggingFaceHub에 올라와 있는 llm 모델을 사용하는 방법. 회원 가입 후 token 생성. token을 설정해줘야 동작함.

예시로는 Mistral model을 사용해서 instruct prompt를 가지고 응답을 얻는 방법에 대해서 보여줌.
## 8.2 HuggingFacePipeline
model을 다운 받아서 동작하는 방법: gpt2 사용 (text generation에 그냥 그냥 쓸만. 용량도 적당함)

약 500MB정도 다운 받은듯...?
## 8.3 GPT4All
falcon 모델 다운(거의 4G) 받아서 로컬에 있는 모델에 질문 하는 것도 가능
## 8.4 Ollama
command line tool 같은건가. 다운로드하고 앱 설치 하면 커맨드 창에서 ollama라는 명령어를 사용해서 특정 모델을 실행하고(ollama run mistral) 그 상태에서 질문을 넣을 수 있음.

mistral 사용 했을 때 약 4G를 다운 받음 ㅜㅜ
## 8.5 Conclusions