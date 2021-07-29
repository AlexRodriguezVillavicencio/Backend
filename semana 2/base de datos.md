mysql

 >mysql -h 127.0.0.1 -u root -p  (para entrar)
 >mysql -h localhost -u root -p  (para entrar)

 >exit                    
 (para salir)
 -------------
 antes en laragon debes iniciar todo


 en la terminal:
 >show databases;  
 (para ver mis base de datos creadas o las que tengo)

 >use mysql 
 (para saber si ya estoy en la base de datos)

 >show tables; 
 (para ver todas las tablas que tengo)

 >select * from user;     
 (para seleccionar una tabla)


describe user;   (para que traiga toda la estructura de la tabla)
--------------------------------
>create database usistema;
(para crear una base datos)

>create user 'usistema'@'localhost' identified by '1234567';
(para crear un usuario y no utilizar el usuario root si no uno propio)
------------------------------------------
mysql> select Host,User from user;
+-----------+-----------------+
| Host      | User            |
+-----------+-----------------+
| %         | flask@localhost |
| localhost | mysql.session   |
| localhost | mysql.sys       |
| localhost | root            |
+-----------+-----------------+
4 rows in set (0.00 sec)
------------------------------------------

>grant all privileges on usistema.* to usistema@localhost;
(Para asignar privilegios o permisos)



>create table alumnos;
(para crear una tabla)



> create user 'pos'@'localhost' indentified by '1234567';


para modelar nuestros datos de forma grafica:

https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-community-8.0.26-winx64.msi


*****************************´+********************


C:\laragon\www
λ mysql -h localhost -u usistema -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.33 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| usistema           |
+--------------------+
2 rows in set (0.00 sec)

mysql> create table alumnos
    -> (nombre varchar(20),
    -> email varchar(20),
    -> sexo char(1)
    -> );
ERROR 1046 (3D000): No database selected
mysql> use usistema;
Database changed
mysql> create table alumnos
    -> (nombre varchar(20),
    -> email varchar(20),
    -> sexo char(1)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql>

*******************+*********************************
>mysql -h localhost -u usistema -p usistema < creartablas.sql