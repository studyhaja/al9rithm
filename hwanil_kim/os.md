# Process Management

## 1. job vs process
### 작업(Job) / 프로그램(Program)
- 실행 할 프로그램 + 데이터
- 컴퓨터 시스템에 실행 요청 전의 상태

### Process
- 실행을 위해 시스템(커널)에 등록된 작업
- 시스템 성능 향상을 위해 커널에 의해 관리 됨
![](https://images.velog.io/images/kpl5672/post/b9f039cd-14c2-4599-b37a-ea1772bab736/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.18.45.png)
![](https://images.velog.io/images/kpl5672/post/9b9bd035-2238-4e31-85ae-12da98c7ba09/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.19.22.png)

## 2. 프로세스의 정의
### : 실행중인 프로그램
- 커널에 등록되고 커널의 관리하에 있는 작업
- 각종 자원들을 요청하고 할당 받을 수 있는 개체
- 프로세스 관리 블록(PCB)을 할당 받은 개체
- 능동적인 개체(active entity)
  - 실행 중에 각종 자원 요구, 할당, 반납하며 진행
### Process Control Block(PCB)이란?
- 커널 공간(Kernel space) 내에 존재
- 각 프로세스들에 대한 정보를 관리

## 3. 프로세스의 종류
![](https://images.velog.io/images/kpl5672/post/27050323-9b34-416e-9e41-ebb587f0c5da/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.22.12.png)
## 4. 자원의 개념
### : 커널의 관리 하에 프로세스에게 할당/반납 되는 수동적 개체(passive entity)
#### 자원의 분류
- HW resources
  - processor, memory, disk, monitor, keyboard, Etc.
- HW resources
  - Message, signal, files, installed SWs, Etc.

Process Control Block(PCB)
프로세스의 상태(Process states)
프로세스 관리를 위한 자료구조
인터럽트 
인터럽트 처리과정
Context Switching(문맥 교환)
