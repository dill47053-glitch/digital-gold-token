import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Digital Gold Token", page_icon="🪙", layout="wide")

# 2. Sidebar Menu Setup
st.sidebar.title("🪙 DGT Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to:", ["🥩 Staking Dashboard", "📄 Read Whitepaper"])

st.sidebar.markdown("---")
st.sidebar.info("Securely Powered by Solana Blockchain.")

# ================= SIDEBAR STATISTICS =================
st.sidebar.header("📊 Token Statistics")
st.sidebar.metric(label="Total Supply", value="10,000,000 DGT")
st.sidebar.metric(label="Staking Pool P/A Yield", value="33% p/a")
st.sidebar.metric(label="Lock Period", value="7 Days")

# ================= PAGE 1: STAKING DASHBOARD =================
if page == "🥩 Staking Dashboard":
    st.title("🪙 Digital Gold Token ($DGT)")
    st.subheader("The Next Generation of Gold-Backed Assets")
    st.markdown("---")

    # Download Button Code
    try:
        with open("DGT_Whitepaper.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Download Whitepaper PDF",
            data=PDFbyte,
            file_name="DGT_Whitepaper.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        pass

    # Layout: Active Stakes & Wallet Action
    col_stakes, col_wallet = st.columns([1.2, 1])

    with col_stakes:
        st.subheader("📋 Your Active Stakes")
        
        # Stake 1: Locked
        with st.container():
            st.markdown("### 🔒 Locked Stake")
            st.markdown("- **Amount:** *1,000,000 DGT*")
            st.markdown("- **Est. Rewards:** *+6,328 DGT*")
            st.markdown("- **⏳ Time Remaining:** 4 days, 12 hours")
            st.button("🔓 Claim DGT", disabled=True, key="btn_lock1")
            
        st.markdown("---")
        
        # Stake 2: Matured
        with st.container():
            st.markdown("### 🔓 Matured Stake")
            st.markdown("- **Amount:** *500,000 DGT*")
            st.markdown("- **Est. Rewards:** *+3,164 DGT*")
            st.markdown("- **✅ Lock Period Ended (7 Days)**")
            if st.button("🎉 Claim Stake & Rewards", key="btn_claim2"):
                st.success("Successfully claimed 503,164 DGT to your wallet!")

    with col_wallet:
        st.subheader("Your Wallet Balance")
        st.title("4,465,000 DGT")
        st.button("🔗 Connect Web3 Wallet", use_container_width=True)
        
        st.markdown("---")
        st.subheader("Staking Portal")
        stake_amount = st.number_input("Amount to stake:", min_value=1000, max_value=4465000, value=4465000, step=1000)
        
        if st.button("⛏️ Stake Now (7 Days Lock)", use_container_width=True):
            st.success(f"Successfully staked {stake_amount:,} DGT for 7 days!")

    st.markdown("---")
    st.subheader("📈 Live Gold Market Trend (Simulated)")
    
    # Gold Chart Data
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    prices = np.linspace(2280, 2340, 30) + np.random.normal(0, 15, 30)
    df_chart = pd.DataFrame({'Date': dates, 'Price (USD/oz)': prices})
    
    fig = px.line(df_chart, x='Date', y='Price (USD/oz)', title="Gold Price Performance")
    fig.update_traces(line_color='#FFD700')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.caption("© 2026 Digital Gold Token Ecosystem. Secure, Fast, and Zero Gas Fees on Staking.")

# ================= PAGE 2: READ WHITEPAPER =================
elif page == "📄 Read Whitepaper":
    st.title("📄 Official $DGT Whitepaper")
    st.subheader("Open the technical specifications securely")
    st.markdown("---")
    
    st.info("💡 Chrome security might block embedded PDFs. Click the button below to view the official Whitepaper securely in a new tab:")
    
    whitepaper_url = "https://github.com/dill47053-glitch/digital-gold-token/blob/main/DGT_Whitepaper.pdf"
    st.link_button("🌐 Open Whitepaper Online", whitepaper_url, use_container_width=True)
    
    st.markdown("---")
    st.caption("You can also download the copy directly from the Staking Dashboard page.")
