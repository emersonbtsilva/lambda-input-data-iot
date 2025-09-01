output "lambda_function_name" {
  value = aws_lambda_function.iot_lambda.function_name
}

output "iot_thing_name" {
  value = aws_iot_thing.device.name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.lambda_bucket.bucket
}
