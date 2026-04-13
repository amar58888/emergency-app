import streamlit as st
import datetime
import time

st.set_page_config(
    page_title="Emergency App",
    page_icon="🚨",
    layout="centered"
)

# UI
st.title("🚨 Emergency Alert System")
st.write("Tap below in case of emergency")

location = "📍 Bangalore, India (Demo)"

if "tap_count" not in st.session_state:
    st.session_state.tap_count = 0

if "show_call" not in st.session_state:
    st.session_state.show_call = False


def trigger_emergency():
    time_now = datetime.datetime.now()

    st.error("🚨 EMERGENCY ACTIVATED 🚨")
    st.write(f"🕒 {time_now}")
    st.write(location)
    st.write("📩 Alert sent (simulated)")

    # sound
    st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3")

    # save log
    with open("emergency_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Emergency at {time_now} | Location: Bangalore\n")

    time.sleep(1)
    st.session_state.show_call = True


# MAIN BUTTON
if st.button("🚨 TRIGGER EMERGENCY"):
    trigger_emergency()

# SECRET TRIGGER
if st.button("🔒 Hidden Trigger"):
    st.session_state.tap_count += 1

    if st.session_state.tap_count >= 3:
        trigger_emergency()
        st.session_state.tap_count = 0


# FAKE CALL
if st.session_state.show_call:
    st.markdown("## 📞 Incoming Call")
    st.write("🚓 Emergency Contact Calling...")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("❌ Reject"):
            st.session_state.show_call = False

    with col2:
        if st.button("✅ Accept"):
            st.success("📞 Call Connected")
            st.session_state.show_call = False