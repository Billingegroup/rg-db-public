![CI](https://github.com/billingegroup/rg-db-public/actions/workflows/main.yml/badge.svg)
# rg-db-public
Billinge Group Public Research Group Database


This repo contains public facing data from the Billinge Group in the Applied
Physics and Applied Mathematics department at Columbia University.  It will be used 
to build the group dynamic web-site at `https://billingegroup.github.io` using
regolith (https://github.com/regro/regolith).  Regolith will also build 
people's public facing cv's and publication lists from this information here.

You need to be a current or former member of the Billinge Group at Columbia
University to update entries in this database.  Please reach out to Prof. 
Billinge (sb2896@columbia.edu) if you are interested in joining the group.

For group members, the current branching workflow is to directly clone this 
repo to your local, make pushes to branches directly on this GitHub repository
and create a PR into the default branch `main`.  We are no longer using a
forking workflow (i.e., don't create a fork).

These commands might help you get going:
```
cd dbs
git clone git@github.com:Billingegroup/rg-db-public.git
git checkout <branch_name>
git add <files>
git commit -m "an informative commit message"
git push -u origin <branch_name>
```
then go to GitHub to open a PR into `main`, so it will look like 
`base:main <- compare:<branch_name>`

Do not ever merge directly into main (actually you shouldn't be able to on GitHub).
This merge will be done by Prof. Billinge after review.   

To prevent nasty accidents,
1. create a file in `rg-db-public/.git/hooks` called `pre-commit` and copy-paste the 
 following into it and save it
2. Mark the new file as executable: `chmod +x rg-db-public/.git/hooks/pre-commit`.

This will prevent you accidentally making local changes to your main branch that won't 
be mergeable.
```
#!/bin/sh
#
# To prevent accidental commits to main,
# copy this file, with name 
#    "pre-commit" 
# to the 
#    .git/hooks (notice the dot in front of git)
# directory in this 
# repo

branch="$(git rev-parse --abbrev-ref HEAD)"

if [ "$branch" = "main" ]; then
  echo "You can't commit directly to main branch"
  exit 1
fi
```
