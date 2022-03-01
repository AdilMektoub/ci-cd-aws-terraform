terraform{
    backend "s3" {
        bucket = "davoclock-aws-cicd-pipeline"
        encrypt = true
        key = "terraform.tfstate"
        region = "eu-west-3a"
    }
}

provider "aws" {
    region = "eu-west-3a"
}