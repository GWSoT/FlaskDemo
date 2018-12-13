# Flask Demo
Simple Flask application with two requests: GET and POST

## How to use?

```sh
curl -X GET http://localhost:9999/clients

curl -X POST http://localhost:9999/clients \
-H "Content-Type: application/json" \
-d '{"first_name":"Jane", "last_name":"Doe", "email":"jdoe@example.com", "gender":"Female", "id":"101"}'
```

## Tasks

1. Create 'get by id' method
2. Create 'delete by id' method
3. Create 'update by id' method
4. (*) Add database support

## Configure development environment

### Install PyCharm
1. Go to [Downloads Page](https://www.jetbrains.com/pycharm/download/)
2. Select your OS (Windows, Linux or MacOS)
3. Download Community Edition
4. Follow Installation Instructions (on the left, under the big PyCharm logo)
### Create new project 
Click 'Create new project' and select path
* Note: if you got 'ModuleNotFoundError: No module named 'distutils.core''
    ```sh
    $ sudo apt-get install python3-distutils
    ```
### Configure virtual environment
1. File -> Settings -> Project: <project-name> -> Project Interpreter 
2. Click the Gear button in top right corner 
3. Add -> Virtualenv Environment -> New environment
    * Location -> path to virual environment, by default - in the root of the project
    * Base Interpreter - path to python interpreter script; here you can set python version if possible
4. Click 'OK'. You should have 'pip' and 'setuptools' installed
### Install dependencies
#### Pip - package installer for Python
Used like this: 
```sh
$ pip install <package-name>
```
To install list of packages from file (which is ussually called 'requirements.txt'): 
```sh
pip install -r <path-to-file> 
```
#### In PyCharm: 
1. File -> Settings -> Project: <project-name> -> Project Interpreter -> '+' button on the right side 
2. Type the name of package
3. Choose the package in the list below
4. Click 'Install package'
### Create first Python script
1. Right-click the project name
2. New -> Python File
3. Type the file name (without .py)
4. Click 'OK'