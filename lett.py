import streamlit as st

st.set_page_config(page_title="Love Letter", layout="centered")

st.markdown("""
<style>

body{
    background-color:#ece1ef;
}

.box{
    display:flex;
    justify-content:center;
    margin-top:50px;
}

.envelope{
    width:300px;
    height:220px;
    background:#f46d7a;
    border-radius:8px;
    position:relative;
    overflow:hidden;
}

.letter{
    width:220px;
    background:white;
    padding:15px;
    border-radius:8px;
    position:absolute;
    left:25px;
    transition:0.8s;
    box-shadow:0 5px 10px rgba(0,0,0,0.2);
}

.open{
    top:20px;
}

.close{
    top:150px;
}

.text{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.title("💌 Love Letter")

if "open" not in st.session_state:
    st.session_state.open = False


col1, col2 = st.columns(2)

with col1:
    if st.button("OPEN"):
        st.session_state.open = True

with col2:
    if st.button("CLOSE"):
        st.session_state.open = False


state = "open" if st.session_state.open else "close"

html = f"""
<div class="box">
    <div class="envelope">

        <div class="letter {state}">
            <div class="text">
                <p><b>To: Crush</b></p>
                <h4>Dear crush, you are so beautiful</h4>
                <p>That every time I see you</p>
                <p>my world stops ❤️</p>
            </div>
        </div>

    </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
