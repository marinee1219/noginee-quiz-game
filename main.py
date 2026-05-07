import streamlit as st

st.set_page_config(page_title="のぎねぇクイズ", page_icon="❓")

st.title("💡 4択クイズゲーム")

# パスワード認証
password = st.sidebar.text_input("パスワード", type="password")

if password == "1219":
    # クイズの問題データ
    questions = [
        {
            "question": "過去に都が置かれていた都市出身は？",
            "options": ["磯田", "黒石", "ゆうすけ", "川村"],
            "answer": "黒石"
        },
        {
            "question": "過去に京都市の相撲大会で4位になったのは？",
            "options": ["磯田", "黒石", "ゆうすけ", "川村"],
            "answer": "黒石"
        },
        {
            "question": "PayPayのユーザー名がカタカナなのは？",
            "options": ["磯田", "黒石", "ゆうすけ", "川村"],
            "answer": "黒石"
        },
        {
            "question": "南草津駅から長岡京駅までの運賃は？",
            "options": ["440円", "470円", "490円", "510円"],
            "answer": "490円"
        }
    ]

    # 今何問目かを記録する仕組み
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.correct_count = 0

    # 全問終了したかチェック
    if st.session_state.quiz_index < len(questions):
        q = questions[st.session_state.quiz_index]
        
        st.subheader(f"第 {st.session_state.quiz_index + 1} 問")
        st.write(q["question"])

        # 4択ボタンを作成
        for option in q["options"]:
            if st.button(option, use_container_width=True):
                if option == q["answer"]:
                    st.success("正解！✨")
                    st.session_state.correct_count += 1
                else:
                    st.error(f"残念！ 正解は「{q['answer']}」でした。")
                
                # 次の問題へ進むためのボタンを表示
                st.session_state.quiz_index += 1
                st.button("次の問題へ 👉")
                st.rerun()
    else:
        # 結果発表
        st.balloons()
        st.header("🎉 全問終了！")
        st.write(f"あなたのスコア: {len(questions)}問中 {st.session_state.correct_count}問正解！")
        
        if st.button("もう一度挑戦する"):
            st.session_state.quiz_index = 0
            st.session_state.correct_count = 0
            st.rerun()

else:
    st.warning("パスワードを入れてね！")
