-- USE sales;

-- CREATE TABLE students
-- (student_id char(5),
-- name char(20),
-- lecturer_id char(5));

-- INSERT INTO students VALUES
-- ('1A', 'SANDY', '2A'),
-- ('1B', 'SALLY', '2A'),
-- ('1C', 'RENDI', '2B'),
-- ('1D', 'RONI', '2C'),
-- ('1E', 'RISA', '2E'),
-- ('1F', 'REZA', '2E');

-- CREATE TABLE lecturers 
-- (lecturer_id char(5), 
-- lecturer_name char(20));

-- INSERT INTO lecturers VALUES
-- ('2A', 'DESI'),
-- ('2B', 'DONI'),
-- ('2C', 'DEKA'),
-- ('2D', 'ERWIN');

-- SELECT * FROM students;
-- SELECT * FROM lecturers; 

-- ALTER TABLE students RENAME COLUMN
-- name TO student_name;


-- > JOIN TABLE
-- INNER JOIN akan sama saja yaitu hanya mengambil irisan
-- kuncinya ada di posisi setelah/sebelum RIGHT atau LEFT

-- SELECT * FROM students;

-- --- -- INNER JOIN
-- --- -- menampilkan hasil irisan yang sama-sama ada di kedua table
-- SELECT students.student_name, lecturers.lecturer_name -- > nama table/kolom sesuai DB
-- FROM students INNER JOIN lecturers					 -- > dibalik sama aja
-- ON students.lecturer_id = lecturers.lecturer_id;		 -- > id ketika dibalik tidak memberikan efek

-- --- -- jika nama kolom di dua tabel beda bisa dengan alternatif ini
-- SELECT student_name, lecturer_name
-- FROM lecturers L INNER JOIN students S
-- ON L.lecturer_id = S.lecturer_id;

-- SELECT students.student_name, lecturers.lecturer_name 
-- FROM students INNER JOIN lecturers
-- ON students.lecturer_id = lecturers.lecturer_id; 

-- --- -- LEFT JOIN
-- --- -- semua data di table sebelum operator LEFT JOIN akan muncul
-- --- -- tampilan data tergantung kolom mana yang akan dipilih lebih dulu dalam SELECT

-- --- -- sama2 left join tapi dituker hasilnya beda
-- SELECT L.lecturer_name, S.student_name 
-- FROM lecturers L LEFT JOIN students S 
-- ON L.lecturer_id = S.lecturer_id;

-- SELECT lecturers.lecturer_name, students.student_name
-- FROM students LEFT JOIN lecturers						-- > ketika ditukar hasilnya beda
-- ON lecturers.lecturer_id = students.lecturer_id			-- > id ketika ditukar tidak memberikan efek

-- --
-- SELECT L.lecturer_name, S.student_name 
-- FROM lecturers L LEFT JOIN students S 
-- ON L.lecturer_id = S.lecturer_id;

-- --- -- RIGHT JOIN
-- --- -- semua data di table setelah operator RIGHT JOIN akan muncul
-- SELECT L.lecturer_name, S.student_name
-- FROM lecturers L RIGHT JOIN students S
-- ON L.lecturer_id = S.lecturer_id;

-- SELECT lecturers.lecturer_name, students.student_name
-- FROM lecturers RIGHT JOIN  students
-- ON students.lecturer_id = lecturers.lecturer_id


-- menampilkan erwin risa reza, kondisi penggabungan left dan right di mana ada kondisi dengan null
-- SELECT L.lecturer_name, S.student_name
-- FROM lecturers L LEFT JOIN students S
-- ON L.lecturer_id = S.lecturer_id
-- WHERE L.lecturer_name IS NULL OR S.student_name IS NULL
-- UNION
-- SELECT L.lecturer_name, S.student_name 
-- FROM lecturers L RIGHT JOIN students S
-- ON L.lecturer_id = S.lecturer_id
-- WHERE L.lecturer_name IS NULL OR S.student_name IS NULL;

