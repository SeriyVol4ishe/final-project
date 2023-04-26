resource "google_storage_bucket" "crime_data_bucket" {
  force_destroy               = false
  location                    = var.region
  name                        = "${local.bucket_name_generated}"
  project                     = var.project
  public_access_prevention    = "enforced"
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
}
# terraform import google_storage_bucket.chicago_crime_raw_data chicago-crime-raw-data
