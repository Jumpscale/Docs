* Fork the project, add changes then send us a [Pull request](https://help.github.com/articles/using-pull-requests/)
* Documentation is added as a git [Submodule](http://git-scm.com/book/en/v2/Git-Tools-Submodules) in github [Jumpscale_core7](https://github.com/Jumpscale/jumpscale_core7) project
* Documentation is under the directory *(docs)* but by default you'll not see documentation in the cloned Repo for the **1st time** until you do this:
 ```
# First time only
$ git submodule init
$ git submodule update
```

- If you already have the docs folder and you want to **get updates**:
 ```
# Get Updates
$ git pull
$ git submodule update
```

- If you want to **make changes to the docs** then:
 ```
# Contribute
$ cd docs
$ git checkout master  # make sure you're in master branch in docs
# Change files
$ git add -A # add all changes / Optionally add them one by one
$ git commit
$ git push # push docs
$ cd .. # jumpscale_core7
$ git add -A # add the changes in submodule [This is required]
$ git commit
$ git push  # push jumpscale_core7
```

