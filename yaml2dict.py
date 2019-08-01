import yaml
import sys

with open("app_endpoint.yml", 'r') as stream:
        try:
                masterConfig = yaml.load(stream)
        except yaml.YAMLError as exc:
                print(exc)


orig_stdout = sys.stdout
f = open('app_endpoint.cfg', 'w')
sys.stdout = f
print(masterConfig)
sys.stdout = orig_stdout
f.close()
