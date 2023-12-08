import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📃",
)

st.title("DocumentGPT")

# with st.chat_message("human"):
#     st.write("Hello")

# with st.chat_message("ai"):
#     st.write("How are you")

# with st.status(
#     "Embedding file...",
#     expanded=True,
# ) as status:
#     time.sleep(3)
#     st.write("Getting the file")
#     time.sleep(3)
#     st.write("Embedding the file")
#     time.sleep(3)
#     st.write("Caching the file")
#     status.update(
#         label="Done",
#         state="complete",
#     )

if "msgs" not in st.session_state:
    st.session_state["msgs"] = []

# st.write(st.session_state["msgs"])


def send_message(msg, role, save=True):
    with st.chat_message(role):
        st.write(msg)
    if save:
        st.session_state["msgs"].append({"msg": msg, "role": role})


for msg in st.session_state["msgs"]:
    send_message(msg["msg"], msg["role"], False)


msg = st.chat_input("Send a message to the ai")

if msg:
    send_message(msg, "human")
    time.sleep(2)
    send_message(f"You said: {msg}", "ai")
