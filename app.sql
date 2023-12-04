drop table if exists campus_library ;
create table campus_library (
	id serial,
	student_name text,
	gender text,
	type_of_book text,
	title text,
	language_book text,
	author text,
	year_of_publication text,
	number_of_pages text,
	publisher text,
	ISBN text,
	tanggal_pinjam date
);

insert into campus_library (student_name, gender, type_of_book, title, language_book, author, year_of_publication, number_of_pages, publisher, ISBN, tanggal_pinjam
) 
values 
	('Annisa', 'female', 'Novel', '172 days', '["Indonesia", "English"]', 'Nadzira Shafa',2000,241,'Banjar :  Motivaksi Inspira','978-623-6483-72-5', 2023-12-01),
	('Irma', 'female', 'Novel','Laut Bercerita', '["Indonesia", "English"]', 'Leila S. Chudori',2017,379,'Kepustakaan Populer Gramedia ','9786024246945', 2023-11-30),
	('Daniel', 'male', 'Novel', 'Hujan','["Indonesia", "English"]', 'Tere Liye',2016,318,'Jakarta : Gramedia Pustaka Utama','978-602-03-2478-4', 2023-11-29),
	('Jasmine', 'male', 'Buku Motivasi', 'Mengapa Aku Berbeda: Rahasia Hidup Bahagia dan Sukses', '["Indonesia", "English"]', 'Mario Teguh',2005,224,'Gramedia Pustaka Utama','978-9792262696', 2023-11-29),
	('Arsa', 'male', 'Buku Motivasi', 'Buku Pintar Mindset: Merancang Hidup Impian dengan Pola Pikir Positif', '["Indonesia", "English", "Prancis"]', 'Ippho Santosa',2011,208,'PT Gramedia Pustaka Utama','978-9792270974' 2023-11-27),
	('Doni', 'male', 'Buku Referensi', 'Publication Manual of the American Psychological Association, 7th Edition', '["Indonesia"]', 'American Psychological Association',2019,428,'American Psychological Association','978-1433832178', 2023-11-27),
	('Tono', 'male', 'Buku Referensi', 'The Chicago Manual of Style, 17th Edition', '["Indonesia"]', 'The University of Chicago Press Editorial Staff',2017,1146,'University of Chicago Press','978-0226287058', 2023-11-26),
	('Rara', 'female', 'Buku Sejarah', 'Sejarah Indonesia Modern 1200–2004', '["English"]', 'M.C. Ricklefs',2008,408,'Palgrave Macmillan','978-0230208023', 2023-12-01),
	('Alya', 'female', 'Buku Sejarah', 'Bali: Indigenous Wisdom – Cultural Heritage', '["Indonesia"]', 'I Gusti Ngurah Bagus',2017,156,'Himpunan Penerbit Indonesia','978-6025080966', 2023-11-26),
	('Tasya', 'female', 'Buku Bisnis dan Keuangan', 'Thinking, Fast and Slow', '["Indonesia", "English"]', 'Daniel Kahneman',2011,499,'Farrar, Straus and Giroux','978-0374275631', 2023-11-25),
	('Yusuf', 'male', 'Buku Bisnis dan Keuangan', 'Flash Boys: A Wall Street Revolt','["Indonesia", "English", "Prancis"]', 'Michael Lewis',2014,274,'W. W. Norton & Company','978-0393244663', 2023-11-24),
	('Bahar', 'male', 'Buku Ilmiah', 'The Emperor of All Maladies: A Biography of Cancer', '["Indonesia", "English"]', 'Siddhartha Mukherjee',2010,596,'Scribner','978-1439170915', 2023-11-24),
	('Rika', 'female', 'Buku Ilmiah', 'Ekosistem Hutan Mangrove: Potensi dan Konservasi di Indonesia', '[ "English"]', 'Sri Sudharto',2005,432,'IPB Press','978-9794935825', 2023-11-23)
	;
	
