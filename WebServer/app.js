'use strict';

const Koa = require('koa'),
KoaRouter = require('koa-router'),
KoaParser = require('koa-bodyparser'),
dotenv    = require('dotenv'),
mysql     = require('mysql2'),
render    = require('koa-ejs'),
path      = require('path');

const app = new Koa();
const router = new KoaRouter();
router.use(KoaParser());
app.use(router.routes()).use(router.allowedMethods());
const db = require('./database.js');
dotenv.config();

render(app, {
    root: path.join(__dirname, 'views'),
    layout: 'template',
    viewExt: 'html',
    cache: false,
    debug: false
});

// Index
router.get('/', async (ctx) => {
    var data = await db.getRecord();
    await ctx.render('index', {
        data: data
    });
});


router.get('/projects', async (ctx) => {
    ctx.body = 'Testing';
});

router.post('/projects/api/temperature', async (ctx) => {
    ctx.body = `Temperature is ${ctx.request.body.temperature}`;
});

app.on('error', (err, ctx) => {
    log.error('Error 500: Internal Server Error', err);
});

app.listen(3000);