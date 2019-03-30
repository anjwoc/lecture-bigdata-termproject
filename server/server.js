var express = require('express');
//express라이브러리 추가
//require는 import문과 기능 동일
var app = express();
var bodyParser = require('body-parser');
var fs = require("fs");

//__dirname : 현재 디렉토리 밑에 /views
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


var kafka = require('kafka-node'),
    Consumer = kafka.Consumer,
    client = new kafka.Client(),
    consumer = new Consumer(
        client,
        [
            { topic: 'test2' }
        ],
        {
            //kafkaHost: '192.168.0.200:9092',
            //autoCommit: true,
            //autoCommitIntervalMs: 5000,
            fromOffset: true,
            //encoding: 'utf8',
            //keyEncoding: 'utf8'
        }
    );

var server = app.listen(3000, function () {
    console.log("Express server has started on port 3000");
});

consumer.on('message', function (message) {
    //console.log(message.topic);
    
    //object가 json으로 바뀜
    var obj = JSON.parse(message.value);
    
    //console.log(typeof(obj.temp));
    console.log(message.value);
    

});

app.use(express.static('public'));
//html파일에서 불러오는 요소들은 public디렉터리에서 사용한다는 의미
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

//var router = require('./router/main')(app, fs);
//밑에 app.get과 같은 걸 소스 파일 하나하나씩 분리시킬때 필요
app.get('/', function (req, res) {
    console.log("/access");
    res.render('main', {
        //index.ejs에서 사용할 변수들을 html에 맞게 바꿔줌
        //<%="요기 안에잇느애들을 쓰기위해"%>
        title: "MY HOMEPAGE",
        length: 5,
        array : [1,2,3,4,5]

    })
});

app.get('/list', function (req, res) {
    console.log("/list called");
    fs.readFile(__dirname + "/../data/user.json", 'utf8', function (err, data) {
        console.log(data);
    });
});
