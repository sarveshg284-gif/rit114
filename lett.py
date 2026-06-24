```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Animated Love Letter 💌",
    page_icon="💖",
    layout="centered"
)

if "open" not in st.session_state:
    st.session_state.open = False

st.title("💌 Animated Love Letter")

col1, col2 = st.columns(2)

with col1:
    if st.button("💖 OPEN"):
        st.session_state.open = True

with col2:
    if st.button("🔒 CLOSE"):
        st.session_state.open = False

state = "open" if st.session_state.open else "close"

html = f"""
<!DOCTYPE html>
<html>
<head>

<style>

* {{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,sans-serif;
}}

body {{
background:linear-gradient(135deg,#ffd6e8,#f6e7ff);
overflow:hidden;
}}

.container {{
display:flex;
justify-content:center;
align-items:center;
height:330px;
position:relative;
}}

.envelope {{
position:relative;
width:320px;
height:220px;
background:#ff758f;
border-radius:12px;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
overflow:hidden;
}}

.flap {{
position:absolute;
top:0;
left:0;
width:100%;
height:120px;
background:#ff5c7c;
clip-path:polygon(0 0,100% 0,50% 100%);
transform-origin:top;
transition:1s;
z-index:5;
}}

.open .flap {{
transform:rotateX(180deg);
}}

.letter {{
position:absolute;
left:35px;
width:250px;
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 5px 15px rgba(0,0,0,0.25);
transition:1s;
z-index:2;
}}

.close .letter {{
top:140px;
}}

.open .letter {{
top:20px;
}}

.message {{
text-align:center;
color:#444;
}}

.message h2 {{
color:#ff4d6d;
margin-bottom:10px;
}}

.message p {{
margin:8px 0;
}}

.heart {{
position:absolute;
font-size:22px;
animation:float 5s linear infinite;
opacity:.8;
}}

@keyframes float {{
0% {{
transform:translateY(250px);
opacity:0;
}}

50% {{
opacity:1;
}}

100% {{
transform:translateY(-250px);
opacity:0;
}}
}}

.h1 {{ left:20px; animation-delay:0s; }}
.h2 {{ left:80px; animation-delay:1s; }}
.h3 {{ left:150px; animation-delay:2s; }}
.h4 {{ left:220px; animation-delay:3s; }}
.h5 {{ left:280px; animation-delay:4s; }}

</style>

</head>

<body>

<div class="container {state}">

<div class="heart h1">❤️</div>
<div class="heart h2">💕</div>
<div class="heart h3">💖</div>
<div class="heart h4">💘</div>
<div class="heart h5">💝</div>

<div class="envelope">

<div class="flap"></div>

<div class="letter">

<div class="message">

<h2>💌 Dear Crush 💌</h2>

<p>You are the most beautiful part</p>

<p>of my every day ❤️</p>

<p>Whenever I see you,</p>

<p>my heart skips a beat 💓</p>

<p>and my world feels magical ✨</p>

<p><b>Forever Yours 💖</b></p>

</div>

</div>

</div>

</div>

</body>
</html>
"""

components.html(html, height=380)
```
