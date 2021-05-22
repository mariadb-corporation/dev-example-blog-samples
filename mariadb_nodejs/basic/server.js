const express = require('express')
const pool = require('./db')
const app = express()
const port = 8080
const bodyParser = require("body-parser");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// GET
app.get('/tasks', async (req, res) => {
    let conn;
    try {
        conn = await pool.getConnection();
        var query = "select * from tasks";
        var rows = await conn.query(query);
        res.send(rows);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

// POST
app.post('/tasks', async (req, res) => {
    let task = req.body;
    console.log(task);
    let conn;
    try {
        conn = await pool.getConnection();
        var query = "insert into tasks (description) values (?)";
        var result = await conn.query(query, [task.description]);
        res.send(result);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.put('/tasks', async (req, res) => {
    let task = req.body;
    let conn;
    try {
        conn = await pool.getConnection();
        var query = "update tasks set description = ?, completed = ? where id = ?";
        var result = await conn.query(query, [task.description, task.completed, task.id]);
        res.send(result);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.delete('/tasks', async (req, res) => {
    let id = req.query.id;
    let conn;
    try {
        conn = await pool.getConnection();
        var query = "delete from tasks where id = ?";
        var result = await conn.query(query, [id]);
        res.send(result);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.listen(port, () => console.log(`Listening on port ${port}`));