import streamlit as st
from streamlit_option_menu import option_menu

# 设置全局页面配置
st.set_page_config(
    page_title="OP manage tool",
    page_icon="❄",
    layout="wide", )

choice = ""

# 设置侧边栏
with st.sidebar:
    choice = option_menu("菜单", ["主页", '配置reload', '前端发布', '实用小工具'],
                         icons=['house', 'list-task', 'list-task', 'list-task'], menu_icon="cast", default_index=0)


# 留白方法
def space(line_num=1):
    for num in range(line_num):
        st.write("")


if choice == "主页":
    st.header('**主页**')
    st.markdown('暂时不知道干点啥...留白')
    space(12)
    st.image("images/Taylor-Swift-New-HD.webp")
    st.snow()