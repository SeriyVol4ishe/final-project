## Prerequisites

> **Warning**
>
> You have to put `credentials.json` into `credentials` folder in project directory.
>
> Create Project and Service Account following the [instructions](/docs/PREREQUISITES.md#google-cloud-project).

Install `terraform`

## Local setup and run

1. Run from root project directory `terraform -chdir=terraform init`:

   ![img.png](../docs/poc/terraform/init.png)

2. Run `terraform -chdir=terraform apply -auto-approve`:

   ![img.png](../docs/poc/terraform/apply.png)

3. Check created resources in your project in GCP:

   ![img.png](../docs/poc/terraform/created_bucket.png)
   ![img.png](../docs/poc/terraform/created_datasets.png)
