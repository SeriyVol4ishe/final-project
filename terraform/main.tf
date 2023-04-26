terraform {
  required_version = ">= 1.0"
  backend "local" {}
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
    random = {
      source = "hashicorp/random"
    }
  }
}

provider "google" {
  project = var.project
  region = var.region
  credentials = file(var.credentials)
}

