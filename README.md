# News Aggregator in Django

## Steps to setup project

1. Fork the repo (top right)
2. Clone the repo locally onto your machine using
`git clone https://github.com/yourusername/news_agg.git`
3. Setup a python virtual env with Django installed.[See this Digital Ocean blog post](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)

## Steps to run project
Launch terminal and type the below commands -
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver 8000`

## Best practices to commit
After setting up your project, using the steps listed above, launch terminal in the directory where your repo exists and proceed with the below steps. 
1. Create a new branch in your local repository on your local machine. Give it a name related to the features you add.
Below the branch is called 'branch_name'. 
The checkout commands sets the working branch to the one you have just created. 

        git checkout -b branch_name
        
2. Edit your files. Stage them for commits using - 

        git add <file_1> <file_2> 

   or to add all files changed, use
        
        git add .
        
3. Commit your changes into git history using
        
        git commit -m "Useful commit message explaining changes in brief"
        
4. Push your changes to your forked repository on GitHub

        git push origin branch_name
        
5. Create a pull request on GitHub, and get it merged!
