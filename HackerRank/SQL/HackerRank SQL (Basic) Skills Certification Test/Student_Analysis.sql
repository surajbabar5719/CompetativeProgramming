select si.roll_number,name
from student_information si inner join 
examination_marks em on si.roll_number=em.roll_number
where subject_one+subject_two+subject_three < 100; 
