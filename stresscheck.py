import streamlit as st
import re
import numpy as np
import pandas as pd
import streamlit as st


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
            return "高い/多い"
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
            return "高い/多い"
    
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
            return "高い/多い"
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
            return "高い/多い"

    
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

#results_aのキーには尺度の名前が、要素部分には'低い/少ない', 'やや低い/少ない', '普通', 'やや高い/多い', '高い/多い'のいずれかが入っている。


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
    response = st.radio(question, options_b, key=question)
#responseには、ーザーがst.radioで選択した選択肢のテキストが格納されます。この例では、ユーザーが質問に対して選んだ["そうだ", "まあそうだ", "ややちがう", "ちがう"]のいずれかの文字列がresponse変数に入ります。
    scores2[question] = map_response_to_score(response)

# 素点換算表の各尺度毎に点数を計算する
    # 活気    
def calculate_stress_reaction1(scores2, gender):
    score = scores2["1. 活気がわいてくる"]+scores2["2. 元気がいっぱいだ"]+scores2["3. 生き生きする"]
    if 3 == score:
        return "低い/少ない"
    elif 4 <= score<=5:
        return "やや低い/少ない"
    elif 6 <= score<=7:
        return "普通"
    elif 8 <= score<=9:
        return "やや高い/多い"
    elif 10 <= score<=12:
        return "高い/多い"
    # イライラ感    
def calculate_stress_reaction2(scores2, gender):
    score = scores2["4. 怒りを感じる"]+scores2["5. 内心腹立たしい"]+scores2["6. イライラしている"]
    if gender == "男性":
        if 3 == score:
            return "低い/少ない"
        elif 4<= score <=5:
            return "やや低い/少ない"
        elif 6<= score <=7:
            return "普通"
        elif 8<= score <=9:
            return "やや高い/多い"
        elif 10<= score <=12:
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
    # 疲労感
def calculate_stress_reaction3(scores2, gender):
    score = scores2["7. ひどく疲れた"]+scores2["8. へとへとだ"]+scores2["9. だるい"]
    if gender == "男性":
        if 3 == score:
            return "低い/少ない"
        elif 4== score:
            return "やや低い/少ない"
        elif 5<= score <=7:
            return "普通"
        elif 8<= score <=10:
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
        elif 9<= score <=11:
            return "やや高い/多い"
        elif 12== score:
            return "高い/多い"
    #不安感
def calculate_stress_reaction4(scores2, gender):
    score = scores2["10. 気がはりつめている"]+scores2["11. 不安だ"]+scores2["12. 落着かない"]
    if gender == "男性":
        if 3 == score:
            return "低い/少ない"
        elif 4== score:
            return "やや低い/少ない"
        elif 5<= score <=7:
            return "普通"
        elif 8<= score <=9:
            return "やや高い/多い"
        elif 10<= score <=12:
            return "高い/多い"
    elif gender == "女性":
        if 3 == score:
            return "低い/少ない"
        elif 4== score:
            return "やや低い/少ない"
        elif 5<= score <=7:
            return "普通"
        elif 8<= score <=10:
            return "やや高い/多い"
        elif 11<= score<=12:
            return "高い/多い"

    #抑うつ感
def calculate_stress_reaction5(scores2, gender):
    score = scores2["13. ゆううつだ"]+scores2["14. 何をするのも面倒だ"]+scores2["15. 物事に集中できない"]+scores2["16. 気分が晴れない"]+scores2["17. 仕事が手につかない"]+scores2["18. 悲しいと感じる"]
    if gender == "男性":
        if 6 == score:
            return "低い/少ない"
        elif 7<= score<=8:
            return "やや低い/少ない"
        elif 9<= score <=12:
            return "普通"
        elif 13<= score <=16:
            return "やや高い/多い"
        elif 17<= score <=24:
            return "高い/多い"
    elif gender == "女性":
        if 6 == score:
            return "低い/少ない"
        elif 7<= score<=8:
            return "やや低い/少ない"
        elif 9<= score <=12:
            return "普通"
        elif 13<= score <=17:
            return "やや高い/多い"
        elif 18<= score<=24:
            return "高い/多い"
    #身体愁訴
def calculate_stress_reaction6(scores2, gender):
    score = scores2["19. めまいがする"] +scores2["20. 体のふしぶしが痛む"] + scores2["21. 頭が重かったり頭痛がする"] +scores2["22. 首筋や肩がこる"] + scores2["23. 腰が痛い"] + scores2["24. 目が疲れる"] +scores2["25. 動悸や息切れがする"] + scores2["26. 胃腸の具合が悪い"] + scores2["27. 食欲がない"] +scores2["28. 便秘や下痢をする"] + scores2["29. よく眠れない"]
    if gender == "男性":
        if 11 == score:
            return "低い/少ない"
        elif 12<= score<=15:
            return "やや低い/少ない"
        elif 16<= score <=21:
            return "普通"
        elif 22<= score <=26:
            return "やや高い/多い"
        elif 27<= score <=44:
            return "高い/多い"
    elif gender == "女性":
        if 11 <= score<=13:
            return "低い/少ない"
        elif 14<= score<=17:
            return "やや低い/少ない"
        elif 18<= score <=23:
            return "普通"
        elif 24<= score <=29:
            return "やや高い/多い"
        elif 30<= score<=44:
            return "高い/多い"

calculations_reactions = {
    "活気": calculate_stress_reaction1,
    "イライラ感": calculate_stress_reaction2,
    "疲労感": calculate_stress_reaction3,
    "不安感": calculate_stress_reaction4,
    "抑うつ感": calculate_stress_reaction5,
    "身体愁訴": calculate_stress_reaction6
}
# 各項目のスコアを格納する辞書
results_b = {}
for scale, func in calculations_reactions.items():
    # 関数がgender引数を必要とするかどうかを判断し、適切に呼び出す
    if "gender" in func.__code__.co_varnames:
        # gender引数が必要な場合は、genderも渡す
        results_b[scale] = func(scores2, gender)
    else:
        # gender引数が不要な場合は、scores2のみ渡す
        results_b[scale] = func(scores2)



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

    # 上司からのサポート    
def calculate_stress_support1(scores3, gender):
    score = 15-(scores3["1. 次の人たちはどのくらい気軽に話ができますか？・上司"]+scores3["1. 次の人たちはどのくらい気軽に話ができますか？・上司"]+scores3["7. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・上司"])
    if gender == "男性":
        if 3 <= score<=4:
            return "低い/少ない"
        elif 5 <= score<=6:
            return "やや低い/少ない"
        elif 7 <= score<=8:
            return "普通"
        elif 9 <= score<=10:
            return "やや高い/多い"
        elif 11 <= score<=12:
            return "高い/多い"
    elif gender == "女性":
        if 3 == score:
            return "低い/少ない"
        elif 4 <= score<=5:
            return "やや低い/少ない"
        elif 6 <= score<=7:
            return "普通"
        elif 8 <= score<=10:
            return "やや高い/多い"
        elif 11 <= score<=12:
            return "高い/多い"
    # 同僚からのサポート    
def calculate_stress_support2(scores3):
    score = 15-(scores3["2. 次の人たちはどれくらい気軽に話ができますか？・職場の同僚"]+scores3["5. あなたが困った時、次の人たちはどれくらい頼りになりますか？・職場の同僚"]+scores3["8. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・職場の同僚"])
    if 3 <= score<=5:
        return "低い/少ない"
    elif 6 <= score<=7:
        return "やや低い/少ない"
    elif 8 <= score<=9:
        return "普通"
    elif 10 <= score<=11:
        return "やや高い/多い"
    elif 12 == score:
        return "高い/多い"

    # 家族・友人からのサポート    
def calculate_stress_support3(scores3):
    score = 15-(scores3["3. 次の人たちはどれくらい気軽に話ができますか？・配偶者、家族、友人等"]+scores3["6. あなたが困った時、次の人たちはどれぐらい頼りになりますか？・配偶者、家族、友人等"]+scores3["9. あなたの個人的な問題を相談したら、次の人たちはどのくらい聞いてくれますか？・配偶者、家族、友人等"])
    if 3 <= score<=6:
        return "低い/少ない"
    elif 7 <= score<=8:
        return "やや低い/少ない"
    elif 9 == score:
        return "普通"
    elif 10 <= score<=11:
        return "やや高い/多い"
    elif 12 == score:
        return "高い/多い"

calculations_support = {
    "上司からのサポート": calculate_stress_support1,
    "同僚からのサポート": calculate_stress_support2,
    "家族・友人からのサポート": calculate_stress_support3
}

# 各項目のスコアを格納する辞書
results_c = {}
for scale, func in calculations_support.items():
    # 関数がgender引数を必要とするかどうかを判断し、適切に呼び出す
    if "gender" in func.__code__.co_varnames:
        # gender引数が必要な場合は、genderも渡す
        results_c[scale] = func(scores3, gender)
    else:
        # gender引数が不要な場合は、scores2のみ渡す
        results_c[scale] = func(scores3)


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

    # 仕事や生活の満足度    
def calculate_stress_satisfaction1(scores4):
    score = 10-(scores4["1. 仕事に満足だ"]+scores4["2. 家庭生活に満足だ"])
    if 2 <= score<=3:
        return "低い/少ない"
    elif 4 == score:
        return "やや低い/少ない"
    elif 5 <= score<=6:
        return "普通"
    elif 7 == score:
        return "やや高い/多い"
    elif 8 == score:
        return "高い/多い"
calculations_satisfaction = {
    "仕事や生活の満足度":calculate_stress_satisfaction1
}

# 各項目のスコアを格納する辞書
results_d = {}
for scale, func in calculations_satisfaction.items():
    # 関数がgender引数を必要とするかどうかを判断し、適切に呼び出す
    if "gender" in func.__code__.co_varnames:
        # gender引数が必要な場合は、genderも渡す
        results_c[scale] = func(scores4, gender)
    else:
        # gender引数が不要な場合は、scores4のみ渡す
        results_d[scale] = func(scores4)

#高ストレス者のロジック作成
# 評価値に基づいてポイントを割り当てる関数
def assign_points(value, reverse=False):
    points = {"低い/少ない": 1, "やや低い/少ない": 2, "普通": 3, "やや高い/多い": 4, "高い/多い": 5}
    if reverse:  # reverseがTrueの場合、ポイントの割り当てを逆転させます。
        points = {k: 6-v for k, v in points.items()}
    return points.get(value, 0)  # 評価値に対応するポイントを返します。

# 大問１の合計ポイントを計算する
total_points_a = 0
for key, value in results_a.items():
    if key in ["心理的な仕事の負担（量）", "心理的な仕事の負担（質）", "自覚的な身体的負担度", "職場の対人関係でのストレス", "職場環境によるストレス"]:
        total_points_a += assign_points(value, reverse=True)  # この範囲のキーに対してはポイントを逆転させます。
    else:
        total_points_a += assign_points(value)  # それ以外のキーには通常のポイント割り当てを使用します。
#  大問2の合計ポイントを計算する
total_points_b = 0
for key, value in results_b.items():
    if key in ["イライラ感","疲労感","不安感","抑うつ感","身体愁訴"]:
        total_points_b += assign_points(value, reverse=True)  # この範囲のキーに対してはポイントを逆転させます。
    else:
        total_points_b += assign_points(value)  # それ以外のキーには通常のポイント割り当てを使用します。
#  大問3の合計ポイントを計算する
total_points_c = 0
for key, value in results_c.items():
    total_points_c += assign_points(value)  # それ以外のキーには通常のポイント割り当てを使用します。





if st.button('回答を提出する'):
   
    columns = ['Category', '低い/少ない', 'やや低い/少ない', '普通', 'やや高い/多い', '高い/多い']
    
    rows_a = []  # 空のリストを初期化、大問1
    for category, rating in results_a.items():
        new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
        new_row['Category'] = category
        new_row[rating] = '〇'
        rows_a.append(new_row)  # リストに辞書を追加
    df_a = pd.DataFrame(rows_a, columns=columns)  # リストからDataFrameを作成

    rows_b = []  # 空のリストを初期化、大問2
    for category, rating in results_b.items():
        new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
        new_row['Category'] = category
        new_row[rating] = '〇'
        rows_b.append(new_row)  # リストに辞書を追加
    df_b = pd.DataFrame(rows_b, columns=columns)  # リストからDataFrameを作成

    rows_c = []  # 空のリストを初期化、大問2
    for category, rating in results_c.items():
        new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
        new_row['Category'] = category
        new_row[rating] = '〇'
        rows_c.append(new_row)  # リストに辞書を追加
    df_c = pd.DataFrame(rows_c, columns=columns)  # リストからDataFrameを作成

    rows_d = []  # 空のリストを初期化、大問2
    for category, rating in results_d.items():
        new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
        new_row['Category'] = category
        new_row[rating] = '〇'
        rows_d.append(new_row)  # リストに辞書を追加
    df_d = pd.DataFrame(rows_d, columns=columns)  # リストからDataFrameを作成
    
    # Fill the DataFrame
    st.table(df_a)
    st.table(df_b)
    st.table(df_c)
    st.table(df_d)
    st.write("")
        # 条件を評価
    if (total_points_b <= 12) or ((total_points_a + total_points_c <= 26) and (total_points_b <= 17)):
        # 条件を満たす場合、メッセージを表示
        st.write("あなたは高ストレス者に該当します。医師の面接指導を受けていただくことをおすすめします。")
    else:
        # 条件を満たさない場合、別のメッセージを表示（必要に応じて）
        st.write("高ストレスのリスクは低いようです")
    st.write("面接を希望される方は以下の申出窓口にご連絡下さい。○○○○（メール：****@**** 電話：****-****）※面接指導を申出した場合は、ストレスチェック結果は会社側に提供されます。また、面接指導の結果、必要に応じて就業上の措置が講じられることになります。※医師の面接指導ではなく、相談をご希望の方は、下記までご連絡下さい。○○○○（メール：****@**** 電話：****-****")
    text_a=text
    text = """
    １）セルフケアとはメンタルヘルス対策におけるセルフケアとは「労働者自身がストレスやこころの健康について理解し、自らのストレスを予防、軽減するあるいはこれに対処すること」で、以下が目標になります。①正しい知識を学ぶことにより、労働者自身がストレスや心身の不調に気づくことができるようになる。②労働者自身がストレスに気づくことにより、自発的にストレスに適切に対処できる。③そうして、労働者はストレスに対して自分で予防・軽減ができるようになる。２）セルフケアの基本セルフケアの基本は規則正しい生活を保ち、適切な食事、睡眠、運動を日々心がけることです。それに加えて、ストレス解消法、ストレス対処法などが挙げられます。１．食事野菜を多く食べる、塩分・脂質・糖質摂取を控えめにする等、食生活に注意しましょう。自然食品は、加工食品・高脂肪が中心のメニューに比べてストレス軽減効果が高いことが知られています。青魚に含まれる DHA・EPA に抗うつ効果が期待できるという研究結果もあります。２．睡眠心身の疲労回復には睡眠が不可欠です。毎日十分な睡眠時間を確保しましょう。睡眠時間の不足や睡眠の質の悪化により、生活習慣病や、うつ病などのこころの病につながってきます。逆に、不眠症は、こころの病の症状として現れることもあります。眠たくないのに無理に眠ろうとすると、かえって緊張を高め、眠りへの移行を妨げます。眠くなってから寝床に就き、起床時刻を一定に保つようにしましょう。仕事や生活上の都合で、夜間に必要な睡眠時間を確保できない時は、午後の早い時刻に 30 分以内の短い昼寝をするのが効果的です。適度な運動習慣、朝食摂取が睡眠覚醒リズムを保つのに有用です。また、就寝前にリラックスすることがスムースな入眠に有効です。例えば、入浴は、ぬるめと感じる湯温で適度な時間、ゆったりとするとよいでしょう。就寝直前の激しい運動や夜食摂取は、入眠を妨げますし、就寝前の飲酒や喫煙は睡眠の質を悪化させます。就寝前 3～4 時間以内のカフェイン摂取も入眠や睡眠の質に影響し、利尿作用で夜中に尿意で目が覚める原因にもなります。これらはいずれも就寝前は控えるようにしましょう。就寝前の寝室の明るすぎる白色照明は、睡眠の質を低下させます。眠りを邪魔せず心地よいと感じられる程度に調整しましょう。寝床に入ってからの携帯電話操作も覚醒を助長させるので控えましょう。睡眠に関連する問題で、日常生活や勤務に悪い影響が出てきて、自分では対処できない時には、早めに専門家に相談するようにしましょう。３．運適度な有酸素運動（息が上がらない程度）にはストレス軽減効果があります。普段から活動的な生活を送るようにしましょう。４．ストレス解消法ストレスへの対処法としては、行動の工夫、考え方の工夫、リラクセーションの 3 つがあります。・行動の工夫：大きなストレスを感じているようでしたら、そのストレスの原因となる問題を分解・整理し、優先順位をつけてみましょう。優先順位の高い問題から解決策をリストアップして、実行しやすい方法から試すことが効果的です。・考え方の工夫：イライラや不安を感じる場合、その原因として考え方のクセが関係していることもあります。仕事がうまくいかなかった原因を過度に自分に求め、失敗した状況が今後もずっと続くと考えていませんか？このような時は、別の視点から状況を眺め直してみることをお勧めします。・リラクセーション：こころと体の状態は密接に関係しています。リラクセーションは、体の緊張を解きほぐすことで、こころの緊張を解きほぐす方法です。腹式呼吸、アロマテラピー、入浴、音楽などあなたに合ったリラックスの方法を、普段から見つけておくとよいでしょう。ストレスへの対処では、上記のほか、家族、友人、上司や同僚など周りの人に相談しサポートを求めることも有効です。普段から気軽に相談できる相手や、信頼のおける人と良好な関係を築いておくよう心がけると良いでしょう。３）うつ病のサイン～自分で気づく変化もし、以下の項目に当
