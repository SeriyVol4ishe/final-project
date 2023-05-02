resource "google_bigquery_dataset" "dataset" {
  access {
    role          = "OWNER"
    special_group = "projectOwners"
  }

  access {
    role          = "READER"
    special_group = "projectReaders"
  }

  access {
    role          = "WRITER"
    special_group = "projectWriters"
  }

  dataset_id                 = "dataset"
  delete_contents_on_destroy = false
  location                   = var.region
  project                    = local.credentials_data.project_id
}
