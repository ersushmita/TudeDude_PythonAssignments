from mimetypes import inited

git config --global user.name "ersushmita"
git config --global user.email "ersushmita@gmail.com"
git config --global color.ui auto
git init
git remote add origin https://github.com/ersushmita/python_assignments.git
git pull origin main
git status
git add .
git status
git commit -m "commit message"
git push
# copy code starting with 'git'

#to create seperate branch
git checkout -b "TuteDude_Python_Assignments"

#To move to any created branch i.e. main
git checkout "main"

#To save code files from github website to the system
git clone #paste URL from <code> in website