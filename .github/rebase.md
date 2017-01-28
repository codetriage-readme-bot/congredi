# Git workflow

feature workflow:
```
git branch feature_name
git checkout feature_name
-edit-
git commit -m "feature"
git checkout master
git merge feature_name
git branch -d feature_name
```

rebase to avoid merge commits:
```
git pull --rebase origin master
-if conflicts arise-
git rebase --continue
-if it gets bad-
git rebase --abort
```

pull-request mode:
```
git checkout -b feature_name
git push origin feature_name
git pull origin feature_name
```

```
master
develop
    feature <->
    release -> bugfixes -> master & develop
branch off: develop
merge into: master

git merge master release-0.1
git tag -a 0.1 -m "thing we did"
```

```
git checkout -b issue#10
git commit -m "fixed #10"
git checkout master
git merge issue#10
git checkout develop
git merge issue#10


```
preserving feature branches:
```
git checkout develop
git merge --no-ff
```

hotfixes:
```
master -> hotfix -> master/develop
git checkout -b hotfix-thing
git commit -m "one"
git commit -m "two"
git fetch origin master git rebase -i origin/master
git push -u origin hotfix-thing
git checkout master
git merge --no-ff hotfix-thing
git checkout development
git merge --no-ff hotfix-thing
git push origin master
git push origin development
```

squash model
```
git checkout -b private_feature_branch
touch file1.txt
git add file1.txt
git commit -am "WIP"
git checkout master
git merge --squash private_feature_branch
git commit -v
```
rebase interactively:
```
git rebase --interactive master
git rebase -i origin/development
```

release:
```
open pr
```

feature:
```
feature-xyz
undecase, '-' not ' ', 
```


labels:
```
addition:blank
concerning:feature
environment:production
feedback:meeting/discussion/question/tutorials
improvement:speed/accuracy
inactive:duplicate/wont fix/
platform:os
priority:low/high/extreme
problem:bug/security
```
changelog:
```
Example:
March 27, 2015 - Joseph - Version 1.1
Site.Master.aspx - 2-50
	Added Documentation
Site.css 1-20
Added coding styles
```
release changelog:
```
1.3.2
* abcd lakjfl

```