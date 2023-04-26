# Usage
## Prerequisites
Install terraform
## Local setup and run
1. First change product number, product name and credentials path in `variables.tf`
![img.png](../poc/terraform/variables.png)
2. Then run from root project directory `terraform -chdir=terraform init`
![img.png](../poc/terraform/init.png)
3. Run `terraform -chdir=terraform apply -auto-approve`
![img.png](../poc/terraform/apply.png)
