output "s3_website_url" {
  value = aws_s3_bucket_website_configuration.website.website_endpoint
}

output "cloudfront_url" {
  value = "https://${aws_cloudfront_distribution.cdn.domain_name}"
}