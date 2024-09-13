$currentDirectory = Get-Location
$directoryName = $currentDirectory.Name

git init

gh repo create $directoryName --public --source=. --remote=origin


git add .

git commit -m update

git branch -m main

git push -u origin main