from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
     return "Hello, DevOps! Version 1.0.0!"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)











# // const express = require('express');

# // const app = express();

# // app.get('/', (req, res) => {
# //   res.send('Hello, DevOps!');
# // });

# // app.listen(5000, () => {
# //   console.log('Server started on port 5000');
# // });
