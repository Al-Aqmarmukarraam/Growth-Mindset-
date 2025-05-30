#streamlit
import streamlit as st
import random

st.set_page_config(page_title= "growth mindset project")
st.title("Growth Mindset Challenge: with steamlit")

st.header("🟢 Embark On Your Journey Of Growth!")
st.write("Embrace challenges, learn from mistakes, and unlock your true potential. this AI-powered app guides you in building a growth mindset through reflection, engaging challenges, and meaningful achievements.🌟")

#quote section
st.header("\ | / Daily Growth Mindset Wisdom")
st.write("『Success is not the end, failure is not the downfall; what truly matters is the courage to keep going.』— Inspired by Winston Churchill ")

st.header("Ready For Today’s Challenge? ⚡")
user_input  = st.text_input("Describe The Challenge You’re Dealing With ✍")


#condition
if user_input:
    messages = [
        "Keep advancing toward your dreams. 💪",
        "Stay strong and push forward! 💪",
        "Every step you take matters. 💪",
        "Believe in yourself and never give up! 💪",
    ]
    st.success(f"You're facing: {user_input}. {random.choice(messages)}")
else:
    failure_messages = [
        "It's okay to feel stuck—take a deep breath and try again. 🔧 Tell us about what you are facing or your challenge to get started — and remember, you are not alone.",
        "Even small steps count. Don’t give up now. 🔧 Tell us about what you are facing or your challenge to get started — and remember, you are not alone.",
        "Failure is part of growth. Keep moving! 🔧 Tell us about what you are facing or your challenge to get started — and remember, you are not alone.",
        "Every great story has setbacks. Yours isn't over. 🔧 Tell us about what you are facing or your challenge to get started — and remember, you are not alone.",
    ]
    st.warning(f"You're facing: {user_input}. {random.choice(failure_messages)}")


#reflexing
st.header("🔍Reflect on your progress🌱")
reflection = st.text_area("Write Your Reflection Here:")

if user_input:
    success_reflection_msgs = [
        "Look back at what you've achieved so far 🔎",
        "Celebrate your small wins and learn from them 🎉",
        "Use your past experiences to fuel your future progress 🚀",
        "Pause to appreciate your journey and its lessons 🌿",
        "Reflecting on progress helps you grow stronger every day 🌅",
    ]
    st.success(f"You're facing: {user_input}. {random.choice(success_reflection_msgs)}")
else:
    failure_reflection_msgs = [
        "Setbacks teach us important lessons—take a moment to reflect 🧠",
        "Every challenge faced is a step toward growth 🌱",
        "Reflection turns failure into valuable experience 🔄",
        "Look inward, learn deeply, and keep moving forward 🚶‍♂",
        "Use reflection to transform obstacles into opportunities 🌟",
    ]
    st.info(f"You're facing: {user_input}. {random.choice(failure_reflection_msgs)}")


#achievements
st.header("Celebrate Your Wins🏆✨")
achievement = st.text_input("Share Things You've Recently Accomplished:")

if user_input:
    success_achievement_msgs = [
        "You’re making amazing progress—keep shining! 🏆",
        "Every achievement is a step closer to your dreams! 🏆",
        "Celebrate your victories, big and small! 🏆",
        "Your hard work is paying off—stay unstoppable! 🏆",
        "Keep conquering your goals one achievement at a time! 🏆",
    ]
    st.success(f"You're facing: {user_input}. {random.choice(success_achievement_msgs)}")
else:
    st.info("There is no small or big achievement—every achievement counts! 🏆")

#footer 
st.write("- - -")
st.write("✲꘏ ꘏ ꘏ ꘏✲")
st.write("🎆🎇Trust in your abilities; growth is continuous, not a fixed endpoint.🎉🎊")
st.write("© Created By Al-Aqmar Mukarram 2025 | All Rights Reserved")