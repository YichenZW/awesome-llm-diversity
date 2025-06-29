This is the devoloper repo.

### Setup

```
git remote add private git@github.com:YichenZW/awesome-llm-diversity-dev.git
git remote add public git@github.com:YichenZW/awesome-llm-diversity.git
```

### Push to developer repo
```
git add .
git commit -m <message>
git push private main
```


### Push to public repo
```
git subtree push --prefix=public public main
```
