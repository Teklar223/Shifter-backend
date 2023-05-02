# Shifter-backend
## ENV setup
* sudo should not be required, but is probably safe.

#### 0. ```cd */Shifter-backend```

#### 1. ```python3 -m venv ./.venv``` </br>

#### 2. Activate the environment: </br>

##### Posix System:
* ``` bash/zsh ``` - $ ``` source .venv/bin/activate ```
* ``` fish ``` - $ ``` source .venv/bin/activate.fish ```
* ``` csh/tcsh ``` - $ ``` source .venv/bin/activate.csh ```
* ``` PowerShell ``` - $ ```  .venv/bin/Activate.ps1 ```

##### Windows
* ``` cmd.exe ``` - ``` C:\> .venv\Scripts\activate.bat ```
* ``` PowerShell ``` - ``` PS C:\> .venv\Scripts\Activate.ps1 ```

#### 3. ``` pip install -r ./requirements.txt ```

#### *. ``` pip freeze > requirements.txt ``` when installing/upgrading libraries

### Django Links
* https://stackoverflow.com/questions/55805865/is-django-a-mvc-or-mvt-framework
* https://docs.djangoproject.com/en/4.1/faq/
* https://dev.to/kozlovzxc/django-templates-with-react-4hko
* https://dennisivy.com/django-skills-roadmap
* https://github.com/codingforentrepreneurs/Try-Django
* https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org
* https://stackoverflow.com/questions/tagged/django?tab=Votes

### Hosting tutorials
* [blogpost](https://realpython.com/django-hosting-on-heroku/#step-7-deploy-your-django-project-to-heroku)

### How to setup postgreDB for local/dev settingg
* [blogpost](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
