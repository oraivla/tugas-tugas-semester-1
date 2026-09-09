soal nomor 1
select first_name, last_name, salary 
from employees;

nomor 2
select first_name, last_name, salary 
from employees
where salary > 7000;

nomo 3
select first_name, last_name, salary 
from employees
order by salary desc;

nomor 4 
select concat (first_name, ' ', last_name) as "Nama Lengkap Karyawan"
from employees;

nomor 5
select concat (first_name,' ', last_name), salary as "Data Karyawan Dengan Gaji diatas 5000 pada Department 50 "
from employees
where department_id = 50 and salary > 5000
order by salary desc;


