---find a city names where city is is a even value

select * from CITY WHERE MOD(ID,2)=0;

---Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

SELECT COUNT(CITY) - COUNT(DISTINCT(CITY)) AS DIFF FROM STATION;


----Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
 ---(i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes
 ---first when ordered alphabetically.
select city, len from (select city, length(city) as len from station order by length(city) asc, city asc) where rownum=1
union
select city, len from (select city, length(city) as len  from station order by length(city) desc, city asc) where rownum=1;


--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
--SUBSTR(COLUMN_NAME,START,LENGTH)
select CITY FROM STATION WHERE UPPER(SUBSTR(CITY,1,1)) IN ('A', 'E', 'I', 'O', 'U');


--Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE UPPER(SUBSTR(CITY,LENGTH(CITY),1)) IN ('A', 'E', 'I', 'O', 'U');


---Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of
--each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.),
--secondary sort them by ascending ID.
SELECT NAME FROM STUDENTS  WHERE MARKS>75 ORDER BY UPPER(SUBSTR(NAME,LENGTH(NAME)-2,3)) ASC;