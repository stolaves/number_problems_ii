import glob
import yaml
import pprint
import os
import re
output = {'name': 'Autograding Number Problems 2',
 'on': ['workflow_dispatch', 'repository_dispatch'],
 'permissions': {'checks': 'write', 'actions': 'read', 'contents': 'read'},
 'jobs': {'run-autograding-tests': {'runs-on': 'ubuntu-latest',
                                    'if': 'github.actor != '
                                          "'github-classroom[bot]'",
                                    'steps': []}}}
steps = [{'name': 'Checkout code', 'uses': 'actions/checkout@v4'}]         
env = {}
withhy = []                                   
for filepath in glob.iglob('../../test/test_*.py'):
    filename = filepath.split("\\")[1]
    file_array = filename[:-3].split("_")[2:]
    file_as_dashed = '-'.join(file_array)
    file_as_title = ' '.join(file_array).title()
    print(file_array)
    steps.append({'name': f'Testing {file_as_title}',
                   'id': f'testing-{file_as_dashed.lower()}',
                   'uses': 'classroom-resources/autograding-command-grader@v1',
                   'with': {'test-name': f'Testing {file_as_title}',
                            'setup-command': 'sudo '
                                             '-H '
                                             'pip3 '
                                             'install '
                                             'pytest',
                            'command': 'python3 -m '
                                       'pytest '
                                       f'test/{filename}',
                            'timeout': 1,
                            'max-score': 5}})
    env[f'TESTING-{'-'.join(file_array).upper()}_RESULTS'] = f'"${{{{steps.testing-{file_as_dashed.lower()}.outputs.result}}}}"'
    withhy.append(f"testing-{file_as_dashed}")

steps.append({'name': 'Checking Code Quality',
                'id': 'checking-code-quality',
              'uses': 'classroom-resources/autograding-command-grader@v1',
              'with': {'test-name': 'Checking '
                                     'Code '
                                     'Quality',
                        'setup-command': 'sudo '
                                         '-H '
                                         'pip3 '
                                         'install '
                                         'pylint',
                        'command': 'python3 -m '
                                   'pylint '
                                   '--disable=C0116,C0103,W0611 '
                                   'number_problems_1.py',
                        'timeout': 2,
                        'max-score': 5}})    
steps.append({'name': 'Autograding Reporter',
              'uses': 'classroom-resources/autograding-grading-reporter@v1',
               'env': env,
              'with': {'runners': ','.join(withhy)}})
output['jobs']['run-autograding-tests']['steps'] = steps

with open("classroom.yml", "w") as fp:
    fp.write(yaml.dump(output, Dumper=yaml.CDumper, sort_keys=False))

