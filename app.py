import streamlit as st
from sqlalchemy import text

list_students = ['', 'Annisa', 'Irma', 'Daniel', 'Jasmine', 'Arsa', 'Doni', 'Tono', 'Rara', 'Alya', 'Tasya', 'Yusuf', 'Bahar', 'Rika']
list_gender = ['', 'male', 'female']
list_tob = ['', 'Novel', 'Buku Motivasi', 'Buku Referensi', 'Buku Sejarah', 'Buku Bisnis dan Keuangan', 'Buku Ilmiah']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://danielwicaksono051:Luk9rfRm3UcV@ep-twilight-mountain-96096661.us-east-2.aws.neon.tech/daniel")
with conn.connect() as connection:
    query = text('CREATE TABLE IF NOT EXISTS campus_library (id serial, student_name text, gender text, type_of_book text, \
                 title text, language_book text, author text, year_of_publication int, number_of_pages int, publisher text, ISBN text, tanggal_pinjam date);')
    session.execute(query)

st.header('SIMPLE CAMPUS LIBRARY SYSTEMS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM campus_library ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.connect() as connection:
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
        tob_lama = result["type_of_book"]
        title_lama = result["title"]
        language_book_lama = result["language_book"]
        author_lama = result["author"]
        yob_lama = result["year_of_publication"]
        nop_lama = result["number_of_pages"]
        publisher_lama = result["publisher"]
        isbn_lama = result["isbn"]
        tanggal_pinjam_lama = result["tanggal_pinjam"]

        with st.expander(f'a.n. {student_name_lama}'):
            with st.form(f'data-{id}'):
                student_name_baru = st.selectbox("student_name", list_students, list_students.index(student_name_lama))
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                tob_baru = st.selectbox("type_of_book", list_tob, list_tob.index(tob_lama))
                title_baru = st.text_input("title", title_lama)
                language_book_baru = st.multiselect("language_book", ['Indonesia', 'English', 'Prancis'], eval(language_book_lama))
                author_baru = st.text_input("author", author_lama)
                yob_baru = st.text_input("year_of_publication", yob_lama)
                nop_baru = st.text_input("number_of_pages", nop_lama)
                publisher_baru = st.text_input("publisher", publisher_lama)
                isbn_baru = st.text_input("ISBN", isbn_lama)
                tanggal_pinjam_baru = st.date_input("tanggal_pinjam", tanggal_pinjam_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.connect() as connection:
                            query = text('UPDATE campus_library \
                                          SET student_name=:1, gender=:2, type_of_book=:3, title=:4, language_book=:5, \
                                          author=:6, year_of_publication=:7, number_of_pages=:8, publisher=:9, ISBN=:10, tanggal_pinjam=11 \
                                          WHERE id=:12;')
                            session.execute(query, {'1':student_name_baru, '2':gender_baru, '3':tob_baru, '4':title_baru, '5':str(language_book_baru), 
                                                     '6':author_baru, '7':yob_baru, '8':nop_baru, '9':publisher_baru, '10':isbn_baru, '11':tanggal_pinjam_baru, '12':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM campus_library WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
