#!/bin/bash
set -e

FUNCTION_NAME="GetDataIoTLambda"
REGION=${AWS_REGION:-us-east-1}
ZIP_FILE="function.zip"

echo ">> Empacotando código Lambda"
cd src
zip -r9 ../$ZIP_FILE .
cd ..

echo ">> Atualizando função $FUNCTION_NAME"
aws lambda update-function-code \
  --function-name $FUNCTION_NAME \
  --zip-file fileb://$ZIP_FILE \
  --region $REGION

echo ">> Deploy concluído com sucesso!"
