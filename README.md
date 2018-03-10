# sanic-boilerplate
An example of Sanic application boilerplate using blueprints


## Project structure
<big><pre>
  ├─ [sanic-boilerplate/](https://github.com/altager/sanic-boilerplate)     # All application code located in this directory.
  │  ├─ [app/](/app/)                 # Application code
  │  │  ├─ [sample_module/](/app/sample_module/) 
  |  |  |  ├─ [`__init`__.py](/app/sample_module/__init__.py)     # Here we define sample_module bluerprint
  |  |  |  ├─ [views.py](/app/sample_module/views.py)          # Controller for sample_module
  |  |  ├─ [templates/](/app/templates/)      # All project templates located here
  |  |  |  ├─ [sample_module](/app/templates/sample_module)
  |  |  |  |  ├─ [sample_page.html](/app/templates/sample_module/sample_page.html)
  |  |  |  ├─ [base.html](/app/templates/base.html)   # Base extendable jinja2 template
  |  |  |  ├─ [index.html](/app/templates/index.html)
  |  |  ├─ [`__init__`.py](/app/__init__.py)          # Application initialization here (registering blueprints, loading config, etc)
  ├─ [Dockerfile](Dockerfile)
  ├─ [.gitignore](.gitignore)
  ├─ [README.md](README.md)
  ├─ [config.py](config.py)                 # Class-based configurations 
  ├─ [docker-compose.yml](docker-compose.yml)
  ├─ [requirements.txt](requirements.txt)
  ├─ [run.py](run.py)                       # Create and run app
 </pre></big>
