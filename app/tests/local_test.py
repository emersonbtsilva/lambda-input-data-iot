
import json
from unittest.mock import patch, MagicMock
from app.src import lambda_function

with open("app/tests/event.json") as f:
    event = json.load(f)

# Mock do boto3.client.publish
with patch("app.src.lambda_function.client") as mock_client:
    mock_client.publish = MagicMock(return_value=None)
    result = lambda_function.lambda_handler(event, None)
    print(result)