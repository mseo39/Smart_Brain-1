# git-lfs 대용량 파일 github 업로드

## 1. git-lfs를 설치한다

```txt
git lfs install
```

## 2. 100MB 이상의 파일을 관리대상으로 지정

```txt
git lfs track "파일명"
```

> git 폴더 안에 .gitattributes 파일이 생성되서 관리대상으로 지정된다.

## 3. 일반적인 push 방법으로 push

```txt
git add -A
git commit -m "코멘트"
git push origin master
```
