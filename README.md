# BPMResourcesScript

## How to commit code in github
```
$ git init

git add .
# Adds the files in the local repository and stages them for commit. 
To unstage a file, use 'git reset HEAD YOUR-FILE'

$ git status
# Show the status of file (like new, modified, deleted)

$ git commit -m "First commit"
# Commits the tracked changes and prepares them to be pushed to a remote repository. 
To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

$ git remote add origin <<remote repository URL>>
# Sets the new remote

$ git remote -v
# Verifies the new remote URL

$ git push -u origin master
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```
