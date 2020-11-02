# Database





my SQL

SQLite # 배포단계에선 쓰지 않음/ 개발단계에서만

PostgreSQL

ORACLE





# 스키마

데이터베이스의 틀! id에는 숫자가 들어가야한다 email은 텍스트만 ... 등등 전체적인 구조





# SQL

관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어





SQL keywordks

테이블에 데이터 삽입 insert

데이터 삭제(행 제거) delete

데이터 갱신 update

데이터 검색 select



```sh







qbw00@DESKTOP-4CRJE2M MINGW64 ~/Desktop/ssafy/DB (master)
$ sqlite3 tutorial.sqlite3
SQLite version 3.33.0 2020-08-14 13:23:32
Enter ".help" for usage hints.
sqlite> .databases
main: C:\Users\qbw00\Desktop\ssafy\DB\tutorial.sqlite3
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-2424-1232
sqlite> .mode csv
sqlite> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> clear
   ...> ;
Error: near "clear": syntax error
sqlite> .clear
Error: unknown command or invalid arguments:  "clear". Enter ".help" 
for help
sqlite> .help
.archive ...             Manage SQL archives
.auth ON|OFF             Show authorizer callbacks
.backup ?DB? FILE        Backup DB (default "main") to FILE
.bail on|off             Stop after hitting an error.  Default OFF   
.binary on|off           Turn binary output on or off.  Default OFF  
.cd DIRECTORY            Change the working directory to DIRECTORY   
.changes on|off          Show number of rows changed by SQL
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.databases               List names and files of attached databases  
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options  
.dbinfo ?DB?             Show status information about the database  
.dump ?TABLE?            Render database content as SQL
.echo on|off             Turn command echo on or off
.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
.excel                   Display the output of next command in spreadsheet
.exit ?CODE?             Exit this program with return-code CODE     
.expert                  EXPERIMENTAL. Suggest indexes for queries   
.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
.filectrl CMD ...        Run various sqlite3_file_control() operations
.fullschema ?--indent?   Show schema and the content of sqlite_stat tables
.headers on|off          Turn display of headers on or off
.help ?-all? ?PATTERN?   Show help text for PATTERN
.import FILE TABLE       Import data from FILE into TABLE
.imposter INDEX TABLE    Create imposter table TABLE on index INDEX  
.indexes ?TABLE?         Show names of indexes
.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
.lint OPTIONS            Report potential schema issues.
.load FILE ?ENTRY?       Load an extension library
.log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?       Set output mode
.nullvalue STRING        Use STRING in place of NULL values
.once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE     
.output ?FILE?           Send output to FILE or stdout if FILE is omitted
.parameter CMD ...       Manage SQL parameter bindings
.print STRING...         Print literal STRING
.progress N              Invoke progress handler after every N opcodes
.prompt MAIN CONTINUE    Replace the standard prompts
.quit                    Exit this program
.read FILE               Read input from FILE
.recover                 Recover as much data as possible from corrupt db.
.restore ?DB? FILE       Restore content of DB (default "main") from 
FILE
.save FILE               Write in-memory database into FILE
.scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?        Show the CREATE statements matching PATTERN 
.selftest ?OPTIONS?      Run tests defined in the SELFTEST table     
.separator COL ?ROW?     Change the column and row separators        
.sha3sum ...             Compute a SHA3 hash of database content     
.shell CMD ARGS...       Run CMD ARGS... in a system shell
.show                    Show the current values for various settings
.stats ?on|off?          Show stats or turn stats on or off
.system CMD ARGS...      Run CMD ARGS... in a system shell
.tables ?TABLE?          List names of tables matching LIKE pattern TABLE
.testcase NAME           Begin redirecting output to 'testcase-out.txt'
.testctrl CMD ...        Run various sqlite3_test_control() operations
.timeout MS              Try opening locked tables for MS milliseconds
.timer on|off            Turn SQL timer on or off
.trace ?OPTIONS?         Output each SQL statement as it is run      
.vfsinfo ?AUX?           Information about the top-level VFS
.vfslist                 List all available VFSes
.vfsname ?AUX?           Print the name of the VFS stack
.width NUM1 NUM2 ...     Set minimum column widths for columnar output
sqlite> CREATE TABLE classmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates  examples
sqlite> .scheme table
Error: unknown command or invalid arguments:  "scheme". Enter ".help" for help
sqlite> .schema classmates)
sqlite> DROP TABLE classmates;
sqlite> .table
examples
sqlite> CREATE TABLE classmates(
   ...> name TEXT
   ...> age INT,
   ...> address TEXT
   ...> )
   ...> );
Error: near ")": syntax error
sqlite> CREATE TABLE classmates(
   ...> name TEXT,
   ...> age INT,
   ...> address TEXT
   ...> );
sqlite> INSERT INTO classmates(name, age) VALUES ('홍길동', 23);     
sqlite> INSERT INTO classmates VALUES ('홍길동', 23, '유성구');      
Error: table classmates has 3 columns but 2 values were supplied     
sqlite> name, age, address
   ...> ;
Error: near "name": syntax error
sqlite> SELECT * FROM classmates;
name,age,address
"홍길동",23,
sqlite> SELECT rowid, * FROM classmates;
rowid,name,age,address
1,"홍길동",23,
sqlite> INSERT INTO classmates VALUES ('홍길동', 23, '유성구');      
sqlite> SELECT rowid, * FROM classmates;
rowid,name,age,address
1,"홍길동",23,
2,"홍길동",23,"유성구"
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('김철 
수', 23, '대전'), ('박나래', 23, '광주'), ('이요셉', 33, '구미');    
sqlite> SELECT * FROM classmates;
name,age,address
"홍길동",23,
"홍길동",23,"유성구"
"홍길동",30,"서울"
"김철수",23,"대전"
"박나래",23,"광주"
"이요셉",33,"구미"
sqlite> SELECT name, age FROM classmates;
name,age
"홍길동",23
"홍길동",23
"홍길동",30
"김철수",23
"박나래",23
"이요셉",33
sqlite> SELECT rowid, name FROM classmates;
rowid,name
1,"홍길동"
2,"홍길동"
3,"홍길동"
4,"김철수"
5,"박나래"
6,"이요셉"
sqlite> SELECT name, age FROM classmates LIMIT 2;
name,age
"홍길동",23
"홍길동",23
sqlite> SELECT rowid, name, age FROM classmates LIMIT 2 OFFSET 2;    
rowid,name,age
3,"홍길동",30
4,"김철수",23
sqlite> SELECT rowid, name, address FROM classmate where address='서 
울';
Error: no such table: classmate
sqlite> SELECT rowid, name, address FROM classmates where address='서
울'; ;
rowid,name,address
3,"홍길동","서울"
sqlite> SELECT DISTINCT age FROM classmates;












                                                  ;




























































              age
sqlite> UPDATE classmates SET name="홍길동", address="제주도" WHRER rowid=5;

                                                  s="제주도" WHERE rowid=5; 
































































































                sqlite> UPDATE classmates SET name="홍길동", address="제주도" WHRER rowid=5;        
Error: near "WHRER": syntax error
sqlite> UPDATE classmates SET name="홍길동",address="제주도" WHERE rowid=5;
sqlite>
```





네트워크 운영체제 데이터베이스 -> 기초만이라도 대충 학습하기

전공자처럼 전문적으로 공부하긴 어렵다

필요하다면.. 빠르게 공부할 수 있다는 점을 어필하는 게 핵심 우린 비전공자니까





cs지식?

