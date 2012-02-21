#!/bin/bash

$commit_comment = $1

git commit -am "$commit_comment"
git push -u origin master

echo "Done!"
