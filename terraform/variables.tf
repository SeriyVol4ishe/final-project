locals {
  credentials_path = "../${path.module}/credentials/credentials.json"
  credentials_data = jsondecode(file(local.credentials_path))
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "US"
  type        = string
}

resource "random_id" "rand" {
  byte_length = 8
}
locals {
  bucket_name_generated = "crime_data_${random_id.rand.hex}"
}
