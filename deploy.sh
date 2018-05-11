cd ./public
git init
git config user.name "wlxklyh"  #修改name
git config user.email "linyanhou@qq.com"  #修改email
git add .
git commit -m "Mac deploy"
git push --force --quiet "https://github.com/wlxklyh/wlxklyh.github.com" master:master