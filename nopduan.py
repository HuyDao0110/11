import streamlit as st

with st.form('Order đồ uống'):
    st.title("_*..₊୨🍸 𝐎𝐫𝐝𝐞𝐫 𝐲𝐨𝐮𝐫 𝐝𝐫𝐢𝐧𝐤 🍸୧₊..*_")

    drinks = (
        'Trà sữa truyền thống',
        'Trà sữa matcha',
        'Trà sữa trái cây',
        'Trà đen macchiato',
        'Trà oolong kem cheese',
        'Trà xanh chanh dây',
        'Cà phê sữa đá',
        'Sinh tố xoài'
    )
    option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)

    sizes = (
        'Nhỏ (350ml)',
        'Vừa (500ml)',
        'Lớn (700ml)'
    )
    option_size = st.selectbox('Chọn size ly:', sizes)

    sugars = (
        'Đường trắng',
        'Đường nâu',
        'Ít đường',
        'Không thêm đường',
        'Mật ong'
    )
    option_sugar = st.selectbox('Bạn thích thêm loại đường nào cho đồ uống của bạn?', sugars)

    jellys = (
        'Thạch rau câu',
        'Thạch nha đam',
        'Thạch phô mai',
        'Thạch trái cây',
        'Không thêm thạch'
    )
    option_jelly = st.selectbox('Bạn thích thêm loại thạch nào cho đồ uống của bạn?', jellys)

    toppings = (
        'Trân châu đen',
        'Trân châu trắng',
        'Pudding trứng',
        'Kem cheese',
        'Hạt dẻ',
        'Không thêm topping'
    )
    option_toppings = st.multiselect('Bạn muốn thêm topping nào? (có thể chọn nhiều)', toppings)

    note = st.text_input("Ghi chú cho quán")

    nums = st.slider('Số lượng bạn muốn đặt:', 1, 10, 1)

    bill = {
        'Loại đồ uống:': option_drink,
        'Size ly:': option_size,
        'Loại đường:': option_sugar,
        'Loại thạch:': option_jelly,
        'Topping thêm:': ", ".join(option_toppings) if option_toppings else "Không thêm",
        'Số lượng:': nums,
        'Ghi chú cho quán:': note
    }

    submitted = st.form_submit_button("Xác nhận")
    if submitted:
        st.write('✅ Bạn đã chọn:')
        for x, y in bill.items():
            st.write(x, y)
        st.balloons()

print_bill = st.checkbox('In hoá đơn')
if print_bill:
    ans = ''
    for x in bill:
        ans += str(x) + ' ' + str(bill[x]) + '\n'
    st.download_button('📥 Tải hóa đơn', ans)















