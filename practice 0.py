import streamlit as st

# アプリのタイトル
st.title('HPデザイン提案ツール')

# ユーザー入力フォーム
with st.form("input_form"):
    industry = st.selectbox('業種を選択してください', ['飲食業', 'IT・テクノロジー', '教育', 'その他'])
    image = st.radio('HPのイメージを選択してください', ['モダン', 'クラシック', 'ポップ'])
    target_audience = st.radio('ターゲット層を選択してください', ['若年層', '中年層', '高齢層'])
    submit_button = st.form_submit_button("提案を見る")

# 提案表示
if submit_button:
    st.header('あなたのHPにおすすめのデザイン')
    # ここに、選択に応じたデザイン提案のロジックを実装します
    if industry == '飲食業':
        if image == 'モダン':
            st.write('モダンなデザインの飲食店向けHPをおすすめします。')
        elif image == 'クラシック':
            st.write('クラシックな雰囲気の飲食店向けHPをおすすめします。')
        else:
            st.write('ポップでカラフルな飲食店向けHPをおすすめします。')
    # 他の業種やイメージに応じた提案を追加する
    else:
        st.write('ご指定の条件に合ったデザイン提案を行います。')
