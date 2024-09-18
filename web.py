import streamlit as st

if "lista" not in st.session_state:
    st.session_state.lista = ["első", "második", "harmadik"]

def hozzair():
    elem =st.session_state["ujelem"]
    st.session_state.lista.append(elem)
    print(st.session_state.lista)


st.title("my first webapp")
st.subheader("ez a subheader")

for i, x in enumerate(st.session_state.lista):
    chkbox = st.checkbox(x, key=x)
    if chkbox: #is checked
        st.session_state.lista.pop(i)
        del st.session_state[x]
        st.rerun()
st.text_input("input he", "Ures",placeholder="mint pl ezt", key ="ujelem", on_change=hozzair)
print("Futottam!")
print(st.session_state.lista)
st.session_state
