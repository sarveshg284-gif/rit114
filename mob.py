
import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(
    page_title="Virtual Love Game 💖",
    page_icon="💖",
    layout="centered"
)

# Session State
if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

# Custom CSS
st.markdown("""
<style>

.block-container{
    max-width:400px;
    margin:auto;
    padding-top:20px;
}

.stButton > button{
    width:100%;
    height:60px;
    font-size:24px;
    font-weight:bold;
    border-radius:20px;
    border:none;
    background:linear-gradient(45deg,#ff1493,#ff69b4);
    color:white;
}

@keyframes pulse {
    from {transform: scale(1);}
    to {transform: scale(1.05);}
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style="
    background:linear-gradient(180deg,#ffe6f2,#ffffff);
    border-radius:30px;
    padding:20px;
    text-align:center;
    box-shadow:0 0 20px rgba(0,0,0,0.15);">
<h1 style="color:#ff1493;">
💖 __________💖
</h1>

</div>
""", unsafe_allow_html=True)

st.write("")

# YES Button

# NO Button Game
components.html(
"""
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    overflow:hidden;
    background:transparent;
    font-family:Arial,sans-serif;
}

#noBtn{
    position:absolute;
    top:120px;
    left:50%;
    transform:translateX(-50%);
    width:140px;
    height:55px;
    background:#ff4da6;
    color:white;
    border:none;
    border-radius:30px;
    font-size:18px;
    font-weight:bold;
    cursor:pointer;
    box-shadow:0 5px 15px rgba(0,0,0,0.25);
}

</style>

</head>

<body>

<button id="noBtn"> 😜</button>

<script>

const btn = document.getElementById("noBtn");

const texts = [
    "NO 😜",
    "Try Again 😂",
    "Wrong Button 🤣",
    "Catch Me 😎",
    "Impossible 😝",
    "Not Today 😆",
    "Too Slow 😜",
    "Love Me 😍"
];

function moveButton() {

    const maxX = window.innerWidth - 150;
    const maxY = window.innerHeight - 100;

    btn.style.left = Math.random() * maxX + "px";
    btn.style.top = Math.random() * maxY + "px";

    btn.innerHTML =
        texts[Math.floor(Math.random() * texts.length)];
}

btn.addEventListener("mouseover", moveButton);
btn.addEventListener("touchstart", moveButton);

</script>

</body>
</html>
""",
height=450
)

# Gift Section
if st.session_state.show_gift:

    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 0 20px rgba(255,105,180,.4);
            margin-top:20px;
        ">

        <h2>💕 I knew it! 💕</h2>

        <div style="font-size:90px;">
            🎁 🎁 🎁
        </div>

        <h3>🌸 Here is your gift 🌸</h3>

        <div style="font-size:70px;">
            💐 🧸 🍫
        </div>

        <p style="font-size:22px;color:#ff1493;">
            You are special ❤️
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    
