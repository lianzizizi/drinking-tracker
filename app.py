import streamlit as stimport pandas as pdimport datetime

初始化数据存储

if ‘drink_data’ not in st.session_state:st.session_state[‘drink_data’] = []

st.title(“🍷 喝酒管理助手”)st.write(“帮助你理性饮酒，掌控自己的饮酒习惯”)

喝酒前评估

st.header(“🥂 喝酒前评估”)reason = st.selectbox(“为什么想喝酒？”, [“放松”, “开心庆祝”, “解压”, “习惯性饮酒”, “其他”])current_mood = st.selectbox(“当前情绪如何？”, [“开心”, “平静”, “压力大”, “焦虑”, “难过”])

喝酒记录

st.header(“🍶 记录你的饮酒情况”)drink_type = st.selectbox(“选择喝的种类”, [“葡萄酒”, “啤酒”, “威士忌”, “鸡尾酒”, “清酒”, “其他”])drink_amount = st.slider(“喝了多少？(杯/瓶)”, 0, 10, 1)

date = datetime.date.today()if st.button(“📌 记录这次饮酒”):st.session_state[‘drink_data’].append({“日期”: date,“喝酒原因”: reason,“当前情绪”: current_mood,“喝酒种类”: drink_type,“喝酒量”: drink_amount,})st.success(“✅ 记录成功！”)

展示喝酒记录

st.header(“📊 你的饮酒记录”)df = pd.DataFrame(st.session_state[‘drink_data’])st.dataframe(df)

统计数据

drink_counts = df.groupby(“喝酒种类”)[“喝酒量”].sum()st.bar_chart(drink_counts)

st.write(“💡 记得适量饮酒，保持健康哦！”)