import numpy as np


def handler(event, context):
    arr = np.random.randint(0, 100, size=(3, 3))
    return {
        "statusCode":200,
        "body":{"message": "Hello from Lambda!", "array": arr.tolist()}
    }

