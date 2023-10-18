0. installed mysql on both servers
1. CREATE USER 'holberton*user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
   GRANT REPLICATION CLIENT ON *.\_ TO 'holberton_user'@'localhost';
   FLUSH PRIVILEGES;
2. creating a database and table and granting select permission to holberton user
3. CREATE USER 'replica*user'@'%' IDENTIFIED BY '0721229400www';
   GRANT REPLICATION SLAVE ON *.\_ TO 'replica_user'@'%';
   FLUSH PRIVILEGES;
   GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

4.
