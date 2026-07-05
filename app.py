import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Digital Gold Token", page_icon="🪙", layout="wide")

st.title("🪙 Digital Gold Token ($DGLD)")
st.subheader("The Next Generation of Gold-Backed Assets")
st.markdown("---")

# --- ACTIVE STAKES & CLAIM PORTAL ---
st.markdown("---")
st.subheader("📋 Your Active Stakes")

# Create two columns for different stake statuses (Locked vs Ready)
col_locked, col_ready = st.columns(2)

with col_locked:
    st.markdown("### 🔒 Locked Stake")
    st.write("Amount: **1,000,000 DGLD**")
    st.write("Est. Rewards: **+6,328 DGLD**")
    st.caption("⏳ Time Remaining: 4 days, 12 hours")
    st.button("🔓 Claim DGLD", key="btn_locked", disabled=True, help="This stake is currently locked.")

with col_ready:
    st.markdown("### 🔓 Matured Stake")
    st.write("Amount: **500,000 DGLD**")
    st.write("Est. Rewards: **+3,164 DGLD**")
    st.caption("✅ Lock Period Ended (7 Days)")
    
    if st.button("🎉 Claim Stake & Rewards", key="btn_ready"):
        st.balloons()
        st.success("Success! 503,164 DGLD has been transferred to your wallet.")

st.sidebar.header("📊 Token Statistics")
st.sidebar.metric(label="Total Supply", value="10,000,000 DGLD")
st.sidebar.metric(label="Staking Pool P/A Yield", value="33% p/a")
st.sidebar.metric(label="Lock Period", value="7 Days")

col1, col2 = st.columns([1, 2])

with col1:
    st.info("Your Wallet Balance")
    st.markdown("## **4,465,000 DGLD**")
    if st.button("🔗 Connect Web3 Wallet", type="primary"):
        st.success("Wallet Connected!")

    st.warning("### Staking Portal")
    amount_to_stake = st.number_input("Amount to stake:", min_value=0, value=4465000)
    if st.button("⛏️ Stake Now (7 Days Lock)"):
        weekly_reward = amount_to_stake * 0.33 / 52
        st.write(f"Expected Earnings (7 Days): **{weekly_reward:,.2f} DGLD**")

with col2:
    st.success("### 📈 Live Gold Market Trend (Simulated)")
    days = pd.date_range(end=pd.Timestamp.now(), periods=30)
    prices = 2300 + np.random.randn(30).cumsum() * 15 
    chart_data = pd.DataFrame({"Date": days, "Price (USD/oz)": prices})
    
    fig = px.line(chart_data, x="Date", y="Price (USD/oz)", title="Gold Price Performance")
    fig.update_traces(line_color='#FFD700')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.write("© 2026 Digital Gold Token Ecosystem. Secure, Fast, and Zero Gas Fees on Staking.")
