import streamlit as st
import yaml
from utils import detect_sqli

st.set_page_config(page_title="SQLi-Guard", page_icon="🛡️")

# Sidebar: CIA Triad
with st.sidebar:
    st.title("🧠 Security Primer")
    with open("threats.yaml") as f:
        threats = yaml.safe_load(f)
        st.markdown("## 🔐 CIA Triad")
        for k, v in threats["CIA_Triad"].items():
            st.markdown(f"**{k}**: {v}")
        st.markdown("## 🧱 Controls")
        for k, v in threats["Controls"].items():
            st.markdown(f"**{k}**: {v}")

# Main App
learn_mode = st.toggle("🔍 Learn Mode")

st.title("🛡️ SQL Injection Demo")
user_input = st.text_input("💬 Enter input to test for SQL injection")

if user_input:
    matches = detect_sqli(user_input)
    if matches:
        st.error("🚨 SQL Injection Detected!")
        for pat, desc in matches:
            st.markdown(f"- **Pattern:** `{pat}`")
            if learn_mode:
                st.markdown(f"  ↪️ *Why it's risky:* {desc}")
    else:
        st.success("✅ Input appears safe.")

st.markdown("---")
st.subheader("🧭 Common Attack Paths")
st.graphviz_chart("""
digraph G {
    "User Input" -> "SQL Injection" -> "Data Leak"
    "User Input" -> "Privilege Abuse" -> "Unauthorized Changes"
    "User Input" -> "Inference Attack" -> "PII Exposure"
    "User Input" -> "DoS Attack" -> "Service Disruption"
}
""")
st.markdown("### 🛡️ Prevention Tips")
st.markdown("""
- **Input Validation**: Always validate and sanitize user inputs.
- **Parameterized Queries**: Use prepared statements to prevent SQL injection.
- **Web Application Firewalls**: Deploy WAFs to filter out malicious traffic.
- **Regular Security Audits**: Conduct regular audits and penetration testing.
""")