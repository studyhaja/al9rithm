# 1. 깃 명령어

#### git init
- 깃을 시작하는 명령어
#### git config
- 깃 계정 정보 설정하는 명령어
- 이름 설정: `git config user.name "some_name"`
- 이메일 설정: `git config user.email "some_email@gmail.com`

# 2. commit에 관한 주의사항
1. 첫 커밋 전 사용자 이름과 이메일 주소 설정
2. 커밋 메세지 남기기(-m)
3. 커밋할 파일을 add 해주기.

# 3. git의 3가지 작업 영역
1. working directory
2. staging area
3. repository

- working directory에서 코드 작업을 한다.
- add 명령어를 통해 작업한 코드를 staging area로 넘긴다.
- staging area에 있는 내용들을 commit 명령어를 통해 repository로 넘긴다.
- 이전 단계에서 다음 단계로 넘기지 않으면 반영되지 않는다.

![](https://images.velog.io/images/kpl5672/post/2608fc43-2e3b-4a72-8732-05676a029b6d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-05%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.47.05.png)


출처: 코드잇 git 강의 
