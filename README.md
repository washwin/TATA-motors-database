# TATA-motors-database
INSTRUCTIONS TO USE GIT
1) Always work in your own branch. Go to your branch using:
git checkout ashwin
2) Always take a pull before you start working. Make sure you are pulling from main branch
and not from your own branch! Use the command:
git pull origin master
3) After making changes in your branch check it! Use:
git status
4) After making sure the code is in working condition stage it. Use:
git add .
OR
git add filename
5) Commit these changes in your branch and use appropriate message. Use:
git commit -m "message"
6) Now merge it with main branch. First you need to checkout to main 
git checkout main
Then you merge:
git merge ashwin
7) Push it in main
git push
8) Remember you can only commit in your own branch and not push.
9) You will NOT commit in main branch, only merge and push.