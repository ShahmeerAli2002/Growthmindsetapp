import streamlit as st
import random
import pandas as pd

if "users" not in st.session_state:
    st.session_state.users = {}

st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 30px;
    }
    .stButton>button {
        background-color: #6a5acd;
        color: white;
        border-radius: 15px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #483d8b;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #6a5acd;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 Programming Learning Adventure!")
st.markdown("""
    <div style='background-color: #e6e6fa; padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <h3 style='color: #483d8b; text-align: center;'>Master Programming, Transform Your Future! 💻</h3>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/code.png")
    st.header("👨‍💻 Programmer Profile")
    name = st.text_input("👤 Enter Your Coder Name:")
    goal = st.text_input("🎯 Set Your Coding Goal:")
    programming_style = st.selectbox(
        "💻 Select Your Programming Path:",
        ["Frontend Developer 🎨", "Backend Developer ⚙️", "Full Stack Developer 🔧", "Mobile Developer 📱", "AI/ML Developer 🤖"]
    )
    st.markdown("---")
    st.markdown("### 🎪 Learning Features")
    st.markdown("""
        • 🏆 Level Up Your Coding Skills
        • 💫 Earn Coding Badges
        • 🤝 Join Coding Projects
        • 🎯 Complete Coding Challenges
        • 🌈 Track Your Progress
    """)

if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "Coding Level": 5,
            "Project Progress": 5,
            "Code Journal": "",
            "Achievements": ["Beginner Coder 💻"],
            "Days Coding": 1,
            "XP Points": 0
        }

    st.markdown(f"""
        <div style='background-color: #e6e6fa; padding: 25px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <h2 style='color: #483d8b; text-align: center;'>💻 Welcome, {name}! 💻</h2>
            <p style='font-size: 20px; text-align: center;'>Your Coding Goal: <span style='color: #6a5acd; font-weight: bold;'>{goal}</span></p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("🌟 Coding Wisdom of the Day")
    quotes = [
        "Every bug fixed makes you stronger!",
        "Code is poetry!",
        "Debug your way to success!",
        "Clean code is the best code!",
        "Keep coding, keep learning!",
        "Your potential is limitless!",
        "Practice makes perfect code!",
        "Every expert was once a beginner!"
    ]
    
    if st.button("🎲 Get Coding Wisdom!", key="quote"):
        quote = random.choice(quotes)
        st.markdown(f"""
            <div style='background-color: #e6e6fa; padding: 25px; border-radius: 15px; text-align: center; animation: glow 2s infinite;'>
                <p style='font-size: 24px; font-weight: bold; color: #483d8b;'>{quote}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("⚡ Skill Tracker")
    col1, col2 = st.columns(2)
    
    with col1:
        power = st.slider(
            "Coding Level (1-10)",
            1, 10, st.session_state.users[name]["Coding Level"],
            help="Rate your coding skills today!"
        )
        st.session_state.users[name]["Coding Level"] = power
        
    with col2:
        progress = st.slider(
            "Project Progress (1-10)",
            1, 10, st.session_state.users[name]["Project Progress"],
            help="How far have you progressed in your project?"
        )
        st.session_state.users[name]["Project Progress"] = progress

    xp_gained = (power + progress) * 10
    st.session_state.users[name]["XP Points"] += xp_gained

    level = st.session_state.users[name]["XP Points"] // 100
    st.markdown(f"""
        <div style='background-color: #e6e6fa; padding: 15px; border-radius: 15px; text-align: center;'>
            <h3>Level {level} Coder</h3>
            <p>XP Points: {st.session_state.users[name]["XP Points"]}</p>
            <div style='background-color: #ddd; border-radius: 10px;'>
                <div style='background-color: #6a5acd; width: {(st.session_state.users[name]["XP Points"] % 100)}%; height: 20px; border-radius: 10px;'></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    achievements = {
        100: "Code Apprentice 🥉",
        300: "Code Warrior 🥈",
        500: "Code Master 🥇",
        1000: "Code Legend 👑"
    }

    for xp, badge in achievements.items():
        if st.session_state.users[name]["XP Points"] >= xp and badge not in st.session_state.users[name]["Achievements"]:
            st.session_state.users[name]["Achievements"].append(badge)
            st.balloons()
            st.success(f"🎊 New Achievement Unlocked: {badge}!")

    st.markdown("---")
    st.subheader("📖 Code Journal")
    st.session_state.users[name]["Code Journal"] = st.text_area(
        "Document your coding journey:",
        value=st.session_state.users[name]["Code Journal"],
        height=150
    )

    if st.button("💾 Save Journal", key="journal"):
        st.balloons()
        st.success("Your progress has been saved! 💾")

    st.markdown("---")
    st.subheader("🏆 Coders Leaderboard")
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df['Total Skill'] = df['Coding Level'] + df['Project Progress']
    df = df.sort_values(by=['Total Skill'], ascending=False)
    
    st.markdown("""
        <style>
        .dataframe {
            background-color: #e6e6fa;
            border-radius: 15px;
            padding: 15px;
        }
        </style>
    """, unsafe_allow_html=True)
    st.table(df[['Coding Level', 'Project Progress', 'Total Skill']])

    st.markdown("---")
    st.subheader("💻 Daily Coding Challenge")
    if st.button("🎯 Get New Challenge"):
        challenges = [
            "Create a simple calculator program!",
            "Build a to-do list application!",
            "Write a program to sort an array!",
            "Create a password generator!",
            "Build a simple game using Python!"
        ]
        st.info(f"Today's Challenge: {random.choice(challenges)}")

else:
    st.markdown("""
        <div style='background-color: #e6e6fa; padding: 30px; border-radius: 15px; text-align: center;'>
            <h2>💻 Welcome to the Programming Learning Adventure!</h2>
            <p style='font-size: 20px;'>Enter your coder name in the sidebar to begin your journey!</p>
        </div>
    """, unsafe_allow_html=True)