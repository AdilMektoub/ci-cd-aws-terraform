provider "aws" {
  region = "eu-west-3"
}

resource "aws_vpc" "main" {
    cidr_block = "10.0.0.0/16"
}