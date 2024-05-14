# make a code to create a terraform file

import os

def terraform_file():
    file = open("terra.tf", "w")
    file.write("provider \"aws\" {\n")
    file.write("  region = \"us-west-2\"\n")
    file.write("}\n")
    file.write("resource \"aws_instance\" \"example\" {\n")
    file.write("  ami           = \"ami-0c55b159cbfafe1f0\"\n")
    file.write("  instance_type = \"t2.micro\"\n")
    file.write("}\n")
    file.close()

terraform_file()

os.system("terraform init")
os.system("terraform apply -auto-approve")
os.system("terraform destroy -auto-approve")

# Path: Alumnos/ES/Diego_Pitarch/COPILOT/terraform.py
# make a code to create a terraform file

