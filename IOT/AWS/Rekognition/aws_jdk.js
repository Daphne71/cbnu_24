var AWS = require('aws-sdk');

AWS.config.update({
    accessKeyId: ' sldkfjsldkjfls ',
    secretAccessKey: '  sldkfjsldkjflskdjf ',
    region: 'ap-southeast-2'
});

var params = {
    Image: {
        S3Object: {
            Bucket : " ",
            Name : " "
        }
    },
    MaxLabels: 5,
    MinConfidence : 80
};

const rekognition = new AWS.Rekognition();
rekognition.detectLabels(params, function(err, data) {
    if (err) console.log(err, err.stack);
    else console.log(data);
});
