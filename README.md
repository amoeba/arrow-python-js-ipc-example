# arrow-python-js-ipc-example

Example showing how to send Arrow RecordBatches from a Python backend to a web browser.

## Server

```sh
cd server
python -m pip install -r requirements.txt
flask --app server.py run --port 3000
```

## Client

```
cd client
npm install
npm run build
npm run start
```

Visit http://localhost:5000 and you should see:

```
[ {"f0": 1, "f1": "foo", "f2": true}, {"f0": 2, "f1": "bar", "f2": null}, {"f0": 3, "f1": "baz", "f2": false}, {"f0": 4, "f1": null, "f2": true} ]
```
