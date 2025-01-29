const mysql = require('mysql2');

const dotenv = require('dotenv');
dotenv.config()

const pool = mysql.createPool({
    host: process.env.MYSQL_HOST,
    user: process.env.MYSQL_USERNAME,
    password: process.env.MYSQL_PASSWORD,
    database: process.env.MYSQL_DATABASE
}).promise()

async function getRecord() {
    var rows = [null];
    [rows] = await pool.query('SELECT * FROM temps')
    try {
    } catch (error) {
    }
    return rows
}

module.exports = { getRecord };