import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu 10 sinh viên
data = {
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình", "Lê Văn Cường",
        "Phạm Thị Dung", "Hoàng Văn Đức", "Vũ Thị Hà",
        "Đặng Văn Hùng", "Bùi Thị Lan", "Đỗ Văn Minh",
        "Ngô Thị Ngọc"
    ],
    "Chuyên cần": [9, 8, 7, 10, 6, 9, 8, 7, 10, 8],
    "Giữa kỳ":    [8, 7, 6, 9, 5, 8, 7, 8, 9, 6],
    "Cuối kỳ":    [9, 8, 7, 9, 6, 9, 8, 7, 10, 7]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.1
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.6
).round(2)

# Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Bảng điểm
st.subheader("1. Bảng điểm 10 sinh viên")
st.dataframe(df, hide_index=True, use_container_width=True)

# Điểm trung bình lớp
st.subheader("2. Điểm trung bình của lớp")
st.metric("Điểm trung bình", f"{df['Tổng kết'].mean():.2f}")

# Cao nhất và thấp nhất
st.subheader("3. Sinh viên có điểm cao nhất và thấp nhất")
col1, col2 = st.columns(2)

with col1:
    sv_max = df.loc[df["Tổng kết"].idxmax()]
    st.success(f"Cao nhất: {sv_max['Họ tên']} - {sv_max['Tổng kết']:.2f}")

with col2:
    sv_min = df.loc[df["Tổng kết"].idxmin()]
    st.warning(f"Thấp nhất: {sv_min['Họ tên']} - {sv_min['Tổng kết']:.2f}")

# Số sinh viên đạt
st.subheader("4. Số sinh viên đạt")
st.write(f"Số sinh viên đạt từ 5 điểm: {(df['Tổng kết'] >= 5).sum()}/10")

# Chọn sinh viên
st.subheader("5. Tra cứu điểm sinh viên")
ten_sv = st.selectbox("Chọn một sinh viên:", df["Họ tên"])
sv = df[df["Họ tên"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Họ tên']}")
st.write(f"**Chuyên cần:** {sv['Chuyên cần']}")
st.write(f"**Giữa kỳ:** {sv['Giữa kỳ']}")
st.write(f"**Cuối kỳ:** {sv['Cuối kỳ']}")
st.write(f"**Tổng kết:** {sv['Tổng kết']:.2f}")
st.write(f"**Xếp loại:** {sv['Xếp loại']}")

# Biểu đồ cột
st.subheader("6. Biểu đồ điểm tổng kết")
st.bar_chart(df.set_index("Họ tên")["Tổng kết"])

# Thông tin người thực hiện
st.divider()
st.caption("Họ và tên: Nguyễn Lê Thái Bảo | MSSV: 070207011461")
