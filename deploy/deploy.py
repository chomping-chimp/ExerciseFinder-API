import os
import json
import re
import subprocess

print(subprocess.run(["./deploy/deploy.sh"]))

os.chdir("./deploy")
with open('containers.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

version = json_object['flask']['image']
temp = re.findall(r'\d+', version)
version_num = int(temp[0])
new_version = f"{version[0:-2]}{version_num+1}"
json_object['flask']['image'] = new_version

with open("containers.json", "w") as outfile:
    json.dump(json_object, outfile)

print("Wrote new version to containers file")

print(subprocess.run([
    "aws", "lightsail", "create-container-service-deployment",
    "--service-name", "exercise-api", "--containers", "file://containers.json",
    "--public-endpoint", "file://public-endpoint.json"
]))
