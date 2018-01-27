const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp(functions.config().firebase);

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions

// http 요청으로 token 값 추가하기
exports.sendToken = functions.https.onRequest((request, response) => {
    const token = request.body.token;

    const data = {
        'token': token
    };

    // 요청 받은 token으로 db를 업데이트한다.
    return admin.database().ref('/tokens').push(data).then(snapshot => {
        return response.send(data);
    });
});

// db에 내용 추가했을때 트리거
exports.addDB = functions.database.ref('/message/{uuid}').onCreate(event => {
    const original = event.data.val();

    console.log(original);
});

// http 응답으로 db 내용 읽어주기
exports.getFamilyChatData = functions.https.onRequest((req, res) => {
    const uuid = req.query.id;
    console.log(`${uuid}`);

    return admin.database().ref('/message').orderByChild('time', snapshot => {
        console.log(snapshot.key + " was " + snapshot.val().message + " meters tall");
    })
});

// return admin.database().ref('/message').on('value', snapshot => {
//     res.send(snapshot.val());
// }, error => {
//     console.log(error);
//     res.send(error);
// });
