const Koa = require('koa');
const KoaRouter = require('koa-router');
const KoaParser = require('koa-bodyparser');

const app = new Koa();
const router = new KoaRouter();

// Hello World
// app.use(async ctx => {
//   ctx.body = 'Hello World';
// });

router.get('/projects', async (ctx) => {
    ctx.body = 'Hello Test';
});


router.use(KoaParser());
router.post('/projects/api/temperature', async (ctx) => {
    ctx.body = `Temperature is ${ctx.request.body.temperature}`;
});


// Router
app.use(router.routes()).use(router.allowedMethods());



app.listen(3000);