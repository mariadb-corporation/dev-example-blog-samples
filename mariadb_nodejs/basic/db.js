// Use the MariaDB Node.js Connector
var mariadb = require('mariadb');

// Create a connection pool
var pool = 
  mariadb.createPool({
    host: "127.0.0.1", 
    port: 3306,
    user: "app_user", 
    password: "Password123!",
    database: "todo"
  });

// Expose a method to establish connection with MariaDB SkySQL
module.exports={
  getConnection: async function(){
    return pool.getConnection();
  }
} 
