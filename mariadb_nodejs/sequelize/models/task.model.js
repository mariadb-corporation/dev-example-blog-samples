module.exports = (sequelize, Sequelize) => {
    const Task = sequelize.define("task", {
      id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        primaryKey: true
      },
      description: {
        type: Sequelize.STRING,
        allowNull: false
      },
      completed: {
        type: Sequelize.BOOLEAN,
        allowNull: false,
        defaultValue: false 
      }
    });
    return Task;
  };