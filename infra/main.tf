resource "aws_s3_bucket" "lambda_bucket" {
  bucket = var.s3_bucket_name
}

resource "aws_iot_thing" "device" {
  name = var.iot_thing_name
}

resource "aws_iot_policy" "policy" {
  name   = var.iot_policy_name
  policy = var.iot_policy_document
}

resource "aws_iot_certificate" "cert" {
  active = true
}

resource "aws_iot_policy_attachment" "attach_policy" {
  policy = aws_iot_policy.policy.name
  target = aws_iot_certificate.cert.arn
}

resource "aws_iot_thing_principal_attachment" "attach_cert" {
  thing     = aws_iot_thing.device.name
  principal = aws_iot_certificate.cert.arn
}

resource "aws_lambda_function" "iot_lambda" {
  function_name = var.lambda_name
  role          = var.lambda_role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.13"
  s3_bucket     = aws_s3_bucket.lambda_bucket.bucket
  s3_key        = "function.zip"
  environment {
    variables = {
      IOT_THING_NAME = aws_iot_thing.device.name
    }
  }
}