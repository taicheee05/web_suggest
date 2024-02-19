import streamlit as st

# 大問1
st.header("大問1: あなたの仕事について")
questions_a = [
    "あなたの現在の仕事の満足度は？",
    # 他の質問を追加する場合はここに記述
]
options_a = ["そうだ", "まあそうだ", "ややちがう", "ちがう"]

for question in questions_a:
    st.radio(question, options_a, key=question)

# 大問2
st.header("大問2: 最近1か月間のあなたの状態について")
questions_b = [
    "最近感じたストレスのレベルは？",
    # 他の質問を追加する場合はここに記述
]
options_b = ["ほとんどなかった", "ときどきあった", "しばしばあった", "ほとんどいつもあった"]

for question in questions_b:
    st.radio(question, options_b, key=question)

# 大問3
st.header("大問3: あなたの周りの方々について")
questions_c = [
    "家族とのコミュニケーションはどうですか？",
    # 他の質問を追加する場合はここに記述
]
options_c = ["非常に", "かなり", "多少", "全くない"]

for question in questions_c:
    st.radio(question, options_c, key=question)

# 大問4
st.header("大問4: 満足度について")
questions_d = [
    "あなたの生活の満足度は？",
    # 他の質問を追加する場合はここに記述
]
options_d = ["満足", "まあ満足", "やや不満足", "不満足"]

for question in questions_d:
    st.radio(question, options_d, key=question)
