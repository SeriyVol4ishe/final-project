# Usage

## Prerequisites

Install `terraform`

## Local setup and run

1. First change product number, product name and credentials path in `variables.tf`:
   
    ![img.png](../docs/poc/terraform/variables.png)

2. Then run from root project directory `terraform -chdir=terraform init`:

   ![img.png](../docs/poc/terraform/init.png)

3. Run `terraform -chdir=terraform apply -auto-approve`:

   ![img.png](../docs/poc/terraform/apply.png)

4. Check created resources in your project in GCP:

   ![img.png](../docs/poc/terraform/created_bucket.png)
   ![img.png](../docs/poc/terraform/created_datasets.png)
