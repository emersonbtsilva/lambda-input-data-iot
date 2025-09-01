variable "aws_region" { default = "us-east-1" }
variable "lambda_name" { default = "GetDataIoTLambda" }
variable "lambda_role_arn" { description = "ARN da role da Lambda" }
variable "s3_bucket_name" { description = "Nome do bucket S3 para Lambda e dados" }
variable "iot_thing_name" { default = "iot_device_001" }
variable "iot_policy_name" { default = "IoTPolicy" }
variable "iot_policy_document" { default = "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [{\n    \"Effect\": \"Allow\",\n    \"Action\": \"iot:*\",\n    \"Resource\": \"*\"\n  }]\n}" }