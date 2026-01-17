import streamlit as st

# Tiêu đề ứng dụng
st.title("📚 Quản lý Thời Khóa Biểu")

# Danh sách môn học theo ngày
schedule = {
    "Thứ Hai": ["Toán", "Ngữ văn", "Tiếng Anh", "Lịch sử"],
    "Thứ Ba": ["Vật lý", "Hóa học", "Sinh học", "Thể dục"],
    "Thứ Tư": ["Ngữ văn", "Địa lý", "Tin học", "Tiếng Anh"],
    "Thứ Năm": ["Toán", "Hóa học", "Công nghệ", "Âm nhạc"],
    "Thứ Sáu": ["Sinh học", "Ngữ văn", "Mỹ thuật", "Thể dục"],
    "Thứ Bảy": ["Toán", "Vật lý", "Tin học", "Tiếng Anh"],
    "Chủ Nhật": ["Nghỉ học 🎉"]
}

# Selectbox chọn ngày
option_day = st.selectbox("📅 Chọn ngày trong tuần:", list(schedule.keys()))

# Hiển thị môn học của ngày đã chọn
st.subheader(f"📖 Thời khóa biểu cho {option_day}:")
subjects = schedule[option_day]

for i, subject in enumerate(subjects, start=1):
    st.write(f"{i}. {subject}")

# Thêm tính năng tải thời khóa biểu
print_schedule = st.checkbox("📥 Tải thời khóa biểu của ngày")
if print_schedule:
    ans = f"Thời khóa biểu cho {option_day}:\n"
    for i, subject in enumerate(subjects, start=1):
        ans += f"{i}. {subject}\n"
    st.download_button("Tải xuống", ans, file_name=f"TKB_{option_day}.txt")
