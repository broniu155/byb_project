::Add an if statment to make folder
if exist "new_folder" mkdir "if_folder"

::conditions for folder creation if-else statement 
if exist "if_folder" (
    mkdir "hyperionDev" 
) else (
    mkdir "new-projects"
)
