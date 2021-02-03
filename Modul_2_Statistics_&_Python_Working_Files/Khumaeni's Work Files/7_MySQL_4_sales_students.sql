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

-- SELECT * FROM students;


-- CREATE TABLE lecturers 
-- (lecturer_id char(5), 
-- lecturer_name char(20));

-- INSERT INTO lecturers VALUES
-- ('2A', 'DESI'),
-- ('2B', 'DONI'),
-- ('2C', 'DEKA'),
-- ('2D', 'ERWIN');

-- SELECT * FROM lecturers; 

-- ALTER TABLE students RENAME COLUMN
-- name TO student_name;


-- > join table

-- SELECT * FROM students;

-- SELECT students.student_name, lecturers.lecturer_name 
-- FROM lecturers INNER JOIN students 
-- ON students.lecturer_id = lecturers.lecturer_id;

-- jika nama kolom di dua tabel beda bisa dengan alternatif ini
-- SELECT student_name, lecturer_name
-- FROM lecturers L INNER JOIN students S
-- ON L.lecturer_id = S.lecturer_id;

-- SELECT students.student_name, lecturers.lecturer_name 
-- FROM students INNER JOIN lecturers
-- ON students.lecturer_id = lecturers.lecturer_id; 

-- sama2 left join tapi dituker hasilnya beda
-- SELECT L.lecturer_name, S.student_name 
-- FROM lecturers L LEFT JOIN students S 
-- ON L.lecturer_id = S.lecturer_id;
-- --
-- SELECT L.lecturer_name, S.student_name 
-- FROM lecturers L LEFT JOIN students S 
-- ON L.lecturer_id = S.lecturer_id;

-- SELECT L.lecturer_name, S.student_name
-- FROM lecturers L RIGHT JOIN students S
-- ON L.lecturer_id = S.lecturer_id;


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

