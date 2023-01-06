from io import BytesIO

from flask import Flask, send_file
from flask_cors import CORS
import pyarrow as pa

app = Flask(__name__)
CORS(app)

@app.get("/data")
def batch_get():
    data = [
        pa.array([1, 2, 3, 4]),
        pa.array(['foo', 'bar', 'baz', None]),
        pa.array([True, None, False, True])
    ]

    batch = pa.record_batch(data, names=['f0', 'f1', 'f2'])

    sink = pa.BufferOutputStream()

    with pa.ipc.new_stream(sink, batch.schema) as writer:
        writer.write_batch(batch)

    return send_file(BytesIO(sink.getvalue().to_pybytes()), "data.arrow")

