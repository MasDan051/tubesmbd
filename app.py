import streamlit as st
from sqlalchemy import text

list_students = ['', 'Annisa', 'Irma', 'Danie', 'Arsa', 'Doni', 'Tono', 'Rara', 'Alya', 'Tasya', 'Yusuf', 'Bahar', 'Rika']
list_gender = ['', 'male', 'female']
list_ToB = ['', 'Novel', 'Buku Motivasi', 'Buku Referensi', 'Buku Sejarah', 'Buku Bisnis dan Keuangan', 'Buku Ilmiah']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://danielwicaksono051:Luk9rfRm3UcV@ep-twilight-mountain-96096661.us-east-2.aws.neon.tech/daniel")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS campus_library (id serial, student_name char, gender char, type_of_book char, \
                 title char, language_book char, author char, year_of_publication int, number_of_pages int, publisher char, ISBN char, tanggal_pinjam date);')
    session.execute(query)

st.header('SIMPLE CAMPUS LIBRARY SYSTEMS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM campus_library ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO campus_library (student_name, gender, type_of_book, title, \
                          language_book, author, year_of_publication, number_of_pages, publisher, ISBN, tanggal_pinjam) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'[]', '6':'', '7':'', '8':'', '9':'', '10':'', '11':None})
            session.commit()

    data = conn.query('SELECT * FROM campus_library ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        student_name_lama = result["student_name"]
        gender_lama = result["gender"]
        ToB_lama = result["type_of_book"]
        title_lama = result["title"]
        language_book_lama = result["language_book"]
        author_lama = result["author"]
        YoB_lama = result["year_of_publication"]
        NoP_lama = result["number_of_pages"]
        publisher_lama = result["publisher"]
        ISBN_lama = result["year_of_publication"]
        tanggal_pinjam_lama = result["tanggal_pinjam"]

        with st.expander(f'a.n. {student_name_lama}'):
            with st.form(f'data-{id}'):
                student_name_baru = st.selectbox("student_name", list_students, list_students.index(student_name_lama))
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                ToB_baru = st.selectbox("type_of_book", list_ToB, list_ToB.index(list_ToB))
                title_baru = st.text_input("title", title_lama)
                language_book_baru = st.multiselect("language_book", ['Indonesia', 'English', 'Prancis'], eval(language_book_lama))
                author_baru = st.text_input("author", author_lama)
                YoB_baru = st.text_input("year_of_publication", YoB_lama)
                NoP_baru = st.text_input("number_of_pages", NoP_lama)
                publisher_baru = st.text_input("publisher", publisher_lama)
                ISBN_baru = st.text_input("ISBN", ISBN_lama)
                tanggal_pinjam_baru = st.date_input("tanggal_pinjam", tanggal_pinjam_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE campus_library \
                                          SET student_name=:1, gender=:2, type_of_book=:3, title=:4, language_book=:5, \
                                          author=:6, year_of_publication=:7, number_of_pages=:8, publisher=:9, ISBN=:10, tanggal_pinjam=11 \
                                          WHERE id=:12;')
                            session.execute(query, {'1':student_name_baru, '2':gender_baru, '3':ToB_baru, '4':title_baru, '5':str(language_book_baru), 
                                                     '6':author_baru, '7':YoB_baru, '8':NoP_baru, '9':publisher_baru, '10':ISBN_baru, '11':tanggal_pinjam_baru, '12':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM campus_library WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
