# git subtree push --prefix=public public main
git init
git remote add private https://github.com/username/project-private.git
git remote add public https://github.com/username/project-public.git

git add .
git commit -m "Initial commit"
git push private main

# 3. 推送public文件夹到公开仓库
git subtree push --prefix=public public main