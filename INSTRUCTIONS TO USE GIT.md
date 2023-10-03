INSTRUCTIONS TO USE GIT
1) Always work in your own branch. Go to your branch(ashwin, tejal, dhrutika) using:
git checkout ashwin
2) Always take a pull before you start working. Make sure you are pulling from main branch
and not from your own branch! Use the command:
git pull origin main
3) After making changes in your branch check it! Use:
git status
4) After making sure the code is in working condition stage it. Use:
git add .
OR
git add filename
5) Commit these changes in your branch and use appropriate message. Use:
git commit -m "message"
6) Now merge it with main branch. First you need to checkout to main: 
git checkout main
Then you merge:
git merge ashwin
7) Now you may get a conflict message here. If so then resolve conflicts in vs code. Once all conflicts are resolved, commit in main. CHECK if it is working. Kindly contact if otherwise. Then move forward
8) Push it in main:
git push
9) Remember you cannot push in your own branch, only commit.
10) You will NOT commit in main branch(except in merge conflicts), only merge and push.
11) Once done working, kindly checkout to you rown branch. Maake sure you are not in main.