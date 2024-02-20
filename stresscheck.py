import streamlit as st
import re

# Email Address (半角英数チェック)
email = st.text_input("Email Address")
if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    st.error("メールアドレスは半角英数で入力してください。")

# 職場コード
workplace_code = st.selectbox("職場コードを選択してください", ["コード1", "コード2", "コード3", "その他"])

# 職場名
workplace_name = st.selectbox("職場名を選択してください", ["職場A", "職場B", "職場C", "その他"])

# 氏名（スペースなしチェック）
name = st.text_input("氏名")
if ' ' in name:
    st.error("氏名にスペースを入れないでください。")

# ふりがな（スペースなしチェック）
furigana = st.text_input("ふりがな")
if ' ' in furigana:
    st.error("ふりがなにスペースを入れないでください。")

# 社員番号 (半角英数チェック)
employee_number = st.text_input("社員番号")
if employee_number and not re.match(r'^[A-Za-z0-9]+$', employee_number):
    st.error("社員番号は半角英数で入力してください。")

# 生年月日
birthdate = st.date_input("生年月日を記入してください")

# 性別
gender = st.radio("性別", ["男性", "女性"])

def map_response_to_score(response):
    mapping = {
        # Mapping for the first type of responses
        "そうだ": 1, "まあそうだ": 2, "ややちがう": 3, "ちがう": 4,
        # Mapping for the second type of responses
        "ほとんどなかった": 1, "ときどきあった": 2, "しばしばあった": 3, "ほとんどいつもあった": 4,
        # Mapping for the third type of responses
        "非常に": 1, "かなり": 2, "多少": 3, "全くない": 4,
        # Mapping for the fourth type of responses
        "満足": 1, "まあ満足": 2, "やや不満足": 3, "不満足": 4,
    }
    return mapping.get(response, 0)  # Default to 0 if response not found

# 大問1
st.header("大問1: あなたの仕事について")
questions_a = [
    "1. 非常にたくさんの仕事をしなければならない",
    "2. 時間内に仕事が処理しきれない",
    "3. 一生懸命働かなければならない",
    "4. かなり注意を集中する必要がある",
    "5. 高度の知識や技術が必要なむずかしい仕事だ",
    "6. 勤務時間中はいつも仕事のことを考えていなければならない",
    "7. からだを大変よく使う仕事だ",
    "8. 自分のペースで仕事ができる",
    "9. 自分で仕事の順番・やり方を決めることができる",
    "10. 職場の仕事の方針に自分の意見を反映できる",
    "11. 自分の技能や知識を仕事で使うことが少ない",
    "12. 私の部署内で意見のくい違いがある",
    "13. 私の部署と他の部署とはうまが合わない",
    "14. 私の職場の雰囲気は友好的である",
    "15. 私の職場の作業環境（騒音、照明、温度、換気など）はよくない",
    "16. 仕事の内容は自分にあっている",
    "17. 働きがいのある仕事だ",
]
options_a = ["そうだ", "まあそうだ", "ややちがう", "ちがう"]
scores = {}

for question in questions_a:
    # Collect each response using a unique key based on the question number
    response = st.radio(question, options_a, key=question)
    # Map the response to a score and store it in the scores dictionary
    scores[question] = map_response_to_score(response)

# 大問2
st.header("大問2: 最近1か月間のあなたの状態について")
questions_b = [
    "1. 活気がわいてくる",
    "2. 元気がいっぱいだ",
    "3. 生き生きする",
    "4. 怒りを感じる",
    "5. 内心腹立たしい",
    "6. イライラしている",
    "7. ひどく疲れた",
    "8. へとへとだ",
    "9. だるい",
    "10. 気がはりつめている",
    "11. 不安だ",
    "12. 落着かない",
    "13. ゆううつだ",
    "14. 何をするのも面倒だ",
    "15. 物事に集中できない",
    "16. 気分が晴れない",
    "17. 仕事が手につかない",
    "18. 悲しいと感じる",
    "19. めまいがする",
    "20. 体のふしぶしが痛む",
    "21. 頭が重かったり頭痛がする",
    "22. 首筋や肩がこる",
    "23. 腰が痛い",
    "24. 目が疲れる",
    "25. 動悸や息切れがする",
    "26. 胃腸の具合が悪い",
    "27. 食欲がない",
    "28. 便秘や下痢をする",
    "29. よく眠れない",
]

options_b = ["ほとんどなかった", "ときどきあった", "しばしばあった", "ほとんどいつもあった"]

for question in questions_b:
    # Collect the response using a unique key based on the question number
    response = st.radio(question, options_b, key=question)
    # Map the response to a score
    score = map_response_to_score(response)
    # Store or process the score as needed


# 大問3
st.header("大問3: あなたの周りの方々について")
questions_c = [
    "1. 次の人たちはどのくらい気軽に話ができますか？・上司",
    "2. 次の人たちはどれくらい気軽に話ができますか？・職場の同僚",
    "3. 次の人たちはどれくらい気軽に話ができますか？・配偶者、家族、友人等",
    "4. あなたが困った時、次の人たちはどのくらい頼りになりますか？・上司",
    "5. あなたが困った時、次の人たちはどれくらい頼りになりますか？・職場の同僚",
    "6. あなたが困った時、次の人たちはどれぐらい頼りになりますか？・配偶者、家族、友人等",
    "7. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・上司",
    "8. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・職場の同僚",
    "9. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・配偶者、家族、友人等",
]
options_c = ["非常に", "かなり", "多少", "全くない"]

for question in questions_c:
    # Collect the response using a unique key based on the question number
    response = st.radio(question, options_c, key=question)
    # Map the response to a score
    score = map_response_to_score(response)
    # Store or process the score as needed

# 大問4
st.header("大問4: 満足度について")
questions_d = [
    "1. 仕事に満足だ",
    "2. 家庭生活に満足だ",
    # 他の質問を追加する場合はここに記述
]
options_d = ["満足", "まあ満足", "やや不満足", "不満足"]

for question in questions_d:
    # Collect the response using a unique key based on the question number
    response = st.radio(question, options_d, key=question)
    # Map the response to a score
    score = map_response_to_score(response)
    # Store or process the score as needed

if st.button('回答を提出する'):
    # Calculate total scores for each section
    total_score_a = sum(map_response_to_score(response) for question, response in scores.items() if question.startswith("1."))
    total_score_b = sum(map_response_to_score(response) for question, response in scores.items() if question.startswith("2."))
    total_score_c = sum(map_response_to_score(response) for question, response in scores.items() if question.startswith("3."))
    total_score_d = sum(map_response_to_score(response) for question, response in scores.items() if question.startswith("4."))

    # Display the total scores
    st.subheader("提出結果")
    st.write(f"大問1の合計点: {total_score_a}")
    st.write(f"大問2の合計点: {total_score_b}")
    st.write(f"大問3の合計点: {total_score_c}")
    st.write(f"大問4の合計点: {total_score_d}")
