import streamlit as st

# Cấu hình trang web
st.set_page_config(page_title="Tool Soi Cầu BCR & TX", page_icon="🎲", layout="centered")

# Tiêu đề chính
st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>🤖 TOOL SOI CẦU BCR & TÀI XỈU</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Hệ thống phân tích xu hướng Baccarat & Tài Xỉu chuyên nghiệp</p>", unsafe_allow_html=True)
st.markdown("---")

# Chọn trò chơi ở Sidebar (Thanh bên trái)
game_choice = st.sidebar.selectbox("🎯 Chọn Trò Chơi", ["🎲 Baccarat (Player/Banker)", "⚖️ Tài Xỉu"])

# ==================== PHẦN 1: BACCARAT ====================
if game_choice == "🎲 Baccarat (Player/Banker)":
    st.subheader("🎲 Phân tích Cầu Baccarat")
    
    if "bcr_history" not in st.session_state:
        st.session_state.bcr_history = []

    def analyze_baccarat(history_list):
        if len(history_list) == 0:
            return "⚠️ Chưa có dữ liệu. Vui lòng bấm chọn kết quả các ván ở bên dưới."

        filtered = [x for x in history_list if x != 'T']
        b_count = history_list.count('B')
        p_count = history_list.count('P')
        t_count = history_list.count('T')

        report = f"### 📊 KẾT QUẢ PHÂN TÍCH BACCARAT\n"
        report += f"📜 **Lịch sử chuỗi:** `{' - '.join(history_list)}`\n\n"
        report += f"📈 **Thống kê:** 🔴 Banker: **{b_count}** | 🔵 Player: **{p_count}** | ⚪ Hòa: {t_count}\n\n"

        if len(filtered) < 3:
            report += f"⚠️ *Chưa đủ dữ liệu (cần ít nhất 3 ván B hoặc P).*\n"
            return report

        last_four = filtered[-4:] if len(filtered) >= 4 else filtered

        if len(set(last_four[-3:])) == 1:
            streak_side = "🔴 BANKER (ĐỎ)" if last_four[-1] == 'B' else "🔵 PLAYER (XANH)"
            report += f"🔥 **CẢNH BÁO: CẦU BỆT ĐANG CHẠY!**\n- Gợi ý: **Theo đuổi cầu ({streak_side}).**\n"
        elif len(filtered) >= 4 and filtered[-4:] == ['B', 'P', 'B', 'P']:
            report += f"⚡ **PHÁT HIỆN CẦU 1-1!** Gợi ý: Đánh **🔴 BANKER (ĐỎ)**.\n"
        elif len(filtered) >= 4 and filtered[-4:] == ['P', 'B', 'P', 'B']:
            report += f"⚡ **PHÁT HIỆN CẦU 1-1!** Gợi ý: Đánh **🔵 PLAYER (XANH)**.\n"
        else:
            if b_count > p_count:
                report += f"💡 **Nhận định:** Bên **Banker** đang chiếm ưu thế nhẹ."
            elif p_count > b_count:
                report += f"💡 **Nhận định:** Bên **Player** đang chiếm ưu thế nhẹ."
            else:
                report += f"💡 **Nhận định:** Cầu đang cân bằng, nên quan sát thêm."

        return report

    # Nút bấm Baccarat
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔴 BANKER (B)", use_container_width=True, type="primary"):
            st.session_state.bcr_history.append('B')
            st.rerun()
    with col2:
        if st.button("🔵 PLAYER (P)", use_container_width=True, type="secondary"):
            st.session_state.bcr_history.append('P')
            st.rerun()
    with col3:
        if st.button("⚪ TIE (T)", use_container_width=True):
            st.session_state.bcr_history.append('T')
            st.rerun()

    c_back, c_reset = st.columns(2)
    with c_back:
        if st.button("↩️ Xóa ván cuối", use_container_width=True, key="bcr_back"):
            if st.session_state.bcr_history:
                st.session_state.bcr_history.pop()
                st.rerun()
    with c_reset:
        if st.button("🗑️ Xóa tất cả", use_container_width=True, key="bcr_reset"):
            st.session_state.bcr_history = []
            st.rerun()

    st.markdown("---")
    st.markdown(analyze_baccarat(st.session_state.bcr_history))

# ==================== PHẦN 2: TÀI XỈU ====================
else:
    st.subheader("⚖️ Phân tích Cầu Tài Xỉu")
    
    if "tx_history" not in st.session_state:
        st.session_state.tx_history = []

    def analyze_taixiu(history_list):
        if len(history_list) == 0:
            return "⚠️ Chưa có dữ liệu. Vui lòng bấm chọn kết quả các ván ở bên dưới."

        t_count = history_list.count('T')
        x_count = history_list.count('X')

        report = f"### 📊 KẾT QUẢ PHÂN TÍCH TÀI XỈU\n"
        report += f"📜 **Lịch sử chuỗi:** `{' - '.join(history_list)}`\n\n"
        report += f"📈 **Thống kê:** 🔴 Tài: **{t_count}** | 🔵 Xỉu: **{x_count}**\n\n"

        if len(history_list) < 3:
            report += f"⚠️ *Chưa đủ dữ liệu (cần ít nhất 3 ván).*\n"
            return report

        last_four = history_list[-4:] if len(history_list) >= 4 else history_list

        if len(set(last_four[-3:])) == 1:
            streak_side = "🔴 TÀI" if last_four[-1] == 'T' else "🔵 XỈU"
            report += f"🔥 **CẢNH BÁO: CẦU BỆT ĐANG CHẠY!**\n- Gợi ý: **Theo đuổi cầu ({streak_side}).**\n"
        elif len(history_list) >= 4 and history_list[-4:] == ['T', 'X', 'T', 'X']:
            report += f"⚡ **PHÁT HIỆN CẦU 1-1!** Gợi ý: Đánh **🔴 TÀI**.\n"
        elif len(history_list) >= 4 and history_list[-4:] == ['X', 'T', 'X', 'T']:
            report += f"⚡ **PHÁT HIỆN CẦU 1-1!** Gợi ý: Đánh **🔵 XỈU**.\n"
        else:
            if t_count > x_count:
                report += f"💡 **Nhận định:** Cửa **Tài** đang chiếm ưu thế nhẹ."
            elif x_count > t_count:
                report += f"💡 **Nhận định:** Cửa **Xỉu** đang chiếm ưu thế nhẹ."
            else:
                report += f"💡 **Nhận định:** Cầu đang cân bằng, nên quan sát thêm."

        return report

    # Nút bấm Tài Xỉu
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 TÀI (T)", use_container_width=True, type="primary"):
            st.session_state.tx_history.append('T')
            st.rerun()
    with col2:
        if st.button("🔵 XỈU (X)", use_container_width=True, type="secondary"):
            st.session_state.tx_history.append('X')
            st.rerun()

    c_back, c_reset = st.columns(2)
    with c_back:
        if st.button("↩️ Xóa ván cuối", use_container_width=True, key="tx_back"):
            if st.session_state.tx_history:
                st.session_state.tx_history.pop()
                st.rerun()
    with c_reset:
        if st.button("🗑️ Xóa tất cả", use_container_width=True, key="tx_reset"):
            st.session_state.tx_history = []
            st.rerun()

    st.markdown("---")
    st.markdown(analyze_taixiu(st.session_state.tx_history))