resource "google_storage_bucket" "crime_data_bucket" {
  force_destroy               = false
  location                    = var.region
  name                        = "${local.bucket_name_generated}"
  project                     = local.credentials_data.project_id
  public_access_prevention    = "enforced"
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
}
