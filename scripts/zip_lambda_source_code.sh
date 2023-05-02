#!/bin/bash

# Recursively find all folders in the lambda_functions/source
# folder, zip them, and move them to a new folder under the
# lambda_functions/zip folder.
mkdir -p lambda_functions/zip
# find lambda_functions/source/ -type d -exec sh -c 'echo "$@"; zip -r "$@".zip "$@"; mkdir -p lambda_functions/zip/"$@"; mv lambda.zip lambda_functions/zip/"$@";' -- {} \;
for d in lambda_functions/source/* ; do
    echo "$d"
    zip -j -r "lambda".zip "$d"
    NEW_FOLDER_NAME=$(basename "$d")
    mkdir -p "lambda_functions/zip/$NEW_FOLDER_NAME"
    mv lambda.zip "lambda_functions/zip/$NEW_FOLDER_NAME"
done