const Sequelize = require("sequelize");

const sequelize = new Sequelize("todo", "app_user", "Password123!", {
  host: "127.0.0.1",
  port: 3306,
  dialect: 'mariadb',
  define: {
    timestamps: false
  }
});

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.tasks = require("./models/task.model.js")(sequelize, Sequelize);

module.exports = db;