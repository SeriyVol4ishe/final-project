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
  location                   = "US"
  project                    = "final-project-382415"
}
# terraform import google_bigquery_dataset.final_project_dataset projects/final-project-382415/datasets/final_project_dataset
