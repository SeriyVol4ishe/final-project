variable "credentials" {
  description = "Absolute path to service account's key"
  type        = string
  default     = "/home/bamboleo/PycharmProjects/final-project/keys/final-project-382415-972971564a58.json"
}

variable "project" {
  description = "Project"
  default     = "final-project-382415"
  type        = string
}
variable "project_number" {
  description = "Project number"
  default     = "623811574632"
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
