import streamlit as st
import re
import numpy as np
import matplotlib.pyplot as plt
from math import pi

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

scores1 = {}
for question in questions_a:
    response = st.radio(question, options_a, key=question)
#responseには、ーザーがst.radioで選択した選択肢のテキストが格納されます。この例では、ユーザーが質問に対して選んだ["そうだ", "まあそうだ", "ややちがう", "ちがう"]のいずれかの文字列がresponse変数に入ります。
    scores1[question] = map_response_to_score(response)
#scores1という辞書を定義して、score1のキーに質問内容、要素にmap_response_to_score()の結果が格納されることになる。

# 素点換算表の各尺度毎に点数を計算する
    # 心理的な仕事の負担（量）の計算ロジック    
def calculate_stress_quality_scale1(scores1, gender):
    score = 15 - (scores1["1. 非常にたくさんの仕事をしなければならない"] + scores1["2. 時間内に仕事が処理しきれない"] + scores1["3. 一生懸命働かなければならない"])
    # 男性の場合    
    if gender == "男性":
        if 3 <= score <= 5:
            return "低い/少ない"
        elif 6 <= score <= 7:
            return "やや低い/少ない"
        elif 8 <= score <= 9:
            return "普通"
        elif 10 <= score <= 11:
            return "やや高い/多い"
        elif score == 12:
            return "多い"
    # 女性の場合
    elif gender == "女性":
        if 3 <= score <= 4:
            return "低い/少ない"
        elif 5 <= score <= 6:
            return "やや低い/少ない"
        elif 7 <= score <= 9:
            return "普通"
        elif 10 <= score <= 11:
            return "やや高い/多い"
        elif score == 12:
            return "多い"
    
    # 心理的な仕事の負担（質）の計算ロジック
def calculate_stress_quality_scale2(scores1, gender):
    score = 15 - (scores1["4. かなり注意を集中する必要がある"] + scores1["5. 高度の知識や技術が必要なむずかしい仕事だ"] + scores1["6. 勤務時間中はいつも仕事のことを考えていなければならない"])
    # 男性の場合
    if gender == "男性":
        if 3 <= score <= 5:
            return "低い/少ない"
        elif 6 <= score <= 7:
            return "やや低い/少ない"
        elif 8 <= score <= 9:
            return "普通"
        elif 10 <= score <= 11:
            return "やや高い/多い"
        elif score == 12:
            return "多い"
    # 女性の場合
    elif gender == "女性":
        if 3 <= score <= 4:
            return "低い/少ない"
        elif 5 <= score <= 6:
            return "やや低い/少ない"
        elif 7 <= score <= 8:
            return "普通"  # 修正された範囲
        elif 9 <= score <= 10:
            return "やや高い/多い"
        elif 11 <= score <= 12:
            return "多い"

    
    # 自覚的な身体的負担度
def calculate_stress_quality_scale3(scores1):
    score = 5 - scores1["7. からだを大変よく使う仕事だ"]    
    if score == 1:
        return "やや低い/少ない"
    elif score == 2:
        return "普通"
    elif score == 3:
        return "やや高い/多い"
    elif score == 4:
        return "高い/多い"
    return "該当なし"


    #職場の対人関係でのストレス
def calculate_stress_quality_scale4(scores1, gender):
    # Calculate the score for "職場の対人関係でのストレス"
    score = 10 - (scores1["12. 私の部署内で意見のくい違いがある"] + scores1["13. 私の部署と他の部署とはうまが合わない"]) + scores1["14. 私の職場の雰囲気は友好的である"]
    if gender == "男性":
        if score <= 3:
            return "低い/少ない"
        elif 4 <= score <= 5:
            return "やや低い/少ない"
        elif 6 <= score <= 7:
            return "普通"
        elif 8 <= score <= 9:
            return "やや高い/多い"
        else:  # score >= 10
            return "高い/多い"
    elif gender == "女性":
        if score <= 3:
            return "低い/少ない"
        elif 4 <= score <= 5:
            return "やや低い/少ない"
        elif 6 <= score <= 7:  # Adjusted based on your correction
            return "普通"
        elif 8 <= score <= 9:
            return "やや高い/多い"
        else:  # score >= 10
            return "高い/多い"

    #職場環境によるストレス
def calculate_stress_quality_scale5(scores1):
    score = 5 - scores1["15. 私の職場の作業環境（騒音、照明、温度、換気など）はよくない"]    
    if gender == "男性":
        if score == 1:
            return "やや低い/少ない"
        elif score == 2:
            return "普通"
        elif score == 3:
            return "やや高い/多い"
        elif score == 4:
            return "高い/多い"
    elif gender == "女性":
        if score == 1:
            return "低い/少ない"
        elif score == 2:
            return "普通"
        elif score == 3:
            return "やや高い/多い"
        elif score == 4:
            return "高い/多い"

    #仕事のコントロール度
def calculate_stress_quality_scale6(scores1):
    score= 15-(scores1["8. 自分のペースで仕事ができる"]+scores1["9. 自分で仕事の順番・やり方を決めることができる"]+scores1["10. 職場の仕事の方針に自分の意見を反映できる"])
    if gender == "男性":
        if 3 <= score <= 4:
            return "低い/少ない"
        elif 5<= score <=6:
            return "やや低い/少ない"
        elif 7<= score <=8:
            return "普通"
        elif 9<= score <=10:
            return "やや高い/多い"
        elif 11<= score <=12:
            return "高い/多い"
    elif gender == "女性":
        if 3 == score:
            return "低い/少ない"
        elif 4<= score <=5:
            return "やや低い/少ない"
        elif 6<= score <=8:
            return "普通"
        elif 9<= score <=10:
            return "やや高い/多い"
        elif 11<= score <=12:
            return "高い/多い"

    #技能の活用度
def calculate_stress_quality_scale7(scores1):
    score =scores1["11. 自分の技能や知識を仕事で使うことが少ない"]
    if 1 == score:
        return "低い/少ない"
    elif 2 == score:
        return "やや低い/少ない"
    elif score==3:
        return "普通"
    elif score==4:
        return "やや高い/多い"


    #仕事の適正度
def calculate_stress_quality_scale8(scores1):
    score=5-scores1["16. 仕事の内容は自分にあっている"]
    if 1 == score:
        return "低い/少ない"
    elif 2 == score:
        return "やや低い/少ない"
    elif score==3:
        return "普通"
    elif score==4:
        return "高い/多い"



    #働きがい
def calculate_stress_quality_scale9(scores1):
    score= 5-scores1["17. 働きがいのある仕事だ"]
    if 1 == score:
        return "低い/少ない"
    elif 2 == score:
        return "やや低い/少ない"
    elif score==3:
        return "普通"
    elif score==4:
        return "高い/多い"



# 計算関数をキー名に関連付ける辞書
calculations = {
    "心理的な仕事の負担（量）": calculate_stress_quality_scale1,
    "心理的な仕事の負担（質）": calculate_stress_quality_scale2,
    "自覚的な身体的負担度": calculate_stress_quality_scale3,
    "職場の対人関係でのストレス": calculate_stress_quality_scale4,
    "職場環境によるストレス": calculate_stress_quality_scale5,
    "仕事のコントロール度": calculate_stress_quality_scale6,
    "技能の活用度": calculate_stress_quality_scale7,
    "仕事の適性度": calculate_stress_quality_scale8,
    "働きがい": calculate_stress_quality_scale9
}

# 各項目のスコアを格納する辞書
results_a = {}
for scale, func in calculations.items():
    # 関数がgender引数を必要とするかどうかを判断し、適切に呼び出す
    if "gender" in func.__code__.co_varnames:
        # gender引数が必要な場合は、genderも渡す
        results_a[scale] = func(scores1, gender)
    else:
        # gender引数が不要な場合は、scores1のみ渡す
        results_a[scale] = func(scores1)

##results_aのそれぞれの要素ごとに、表の分類に応じて、素点が分類される部分を特定したいです。最終的には、レーダーチャートにして表したいです。
##レーダーチャートを描画する部分
# 文字列のスコアを数値に変換する辞書
score_values = {
    "低い/少ない": 1,
    "やや低い/少ない": 2,
    "普通": 3,
    "やや高い/多い": 4,
    "高い/多い": 5
}

# results_aの各項目に対するスコアを数値化
values = [score_values[score] for score in results_a.values()]
values += values[:1]  # チャートを閉じるために最初の値を末尾に追加

# 項目名
categories = list(results_a.keys())
N = len(categories)

# レーダーチャートを描画するための角度を計算
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# matplotlibを使用してレーダーチャートを描画
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
plt.xticks(angles[:-1], categories, color='grey', size=8)

# グリッドラインを描画
ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["低い", "やや低い", "普通", "やや高い", "高い"], color="grey", size=7)
plt.ylim(0,5)

# プロットデータの描画
ax.plot(angles, values, linewidth=1, linestyle='solid', label='スコア')
ax.fill(angles, values, 'b', alpha=0.1)



###


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

scores2 = {}

for question in questions_b:
    response = st.radio(question, options_a, key=question)
#responseには、ーザーがst.radioで選択した選択肢のテキストが格納されます。この例では、ユーザーが質問に対して選んだ["そうだ", "まあそうだ", "ややちがう", "ちがう"]のいずれかの文字列がresponse変数に入ります。
    scores2[question] = map_response_to_score(response)


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

scores3={}
for question in questions_c:
    response = st.radio(question, options_c, key=question)
    scores3[question] = map_response_to_score(response)

# 大問4
st.header("大問4: 満足度について")
questions_d = [
    "1. 仕事に満足だ",
    "2. 家庭生活に満足だ",
    # 他の質問を追加する場合はここに記述
]
options_d = ["満足", "まあ満足", "やや不満足", "不満足"]
scores4={}
for question in questions_d:
    response = st.radio(question, options_d, key=question)
    scores4[question] = map_response_to_score(response)

if st.button('回答を提出する'):
    total_score1 = sum(scores1.values())  # scores辞書の値（点数）の合計を計算
    total_score2 = sum(scores2.values())  # scores辞書の値（点数）の合計を計算
    total_score3 = sum(scores3.values())  # scores辞書の値（点数）の合計を計算
    total_score4 = sum(scores4.values())  # scores辞書の値（点数）の合計を計算
    
    st.write(f"大問1の合計点は: {total_score1}点です。")  # 合計点を表示
    st.write(f"心理的な仕事の負担（量）は: {total_score1}点です。")  # 合計点を表示    
    st.write(f"大問2の合計点は: {total_score2}点です。")  # 合計点を表示
    st.write(f"大問3の合計点は: {total_score3}点です。")  # 合計点を表示
    st.write(f"大問4の合計点は: {total_score4}点です。")  # 合計点を表示
    for scale, score in results_a.items():
        st.write(f"{scale}: {score}点")
    # Streamlitでレーダーチャートを表示
    st.pyplot(fig)


