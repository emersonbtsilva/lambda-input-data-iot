terraform {
  backend "s3" {
    bucket = var.s3_bucket_name
    key    = "${var.environment}.tfstate"
    region = "us-east-1"
  }
}