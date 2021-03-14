### 1. SCP(Service control policies)
- organizaion 권한 관리하는 기능.
- SCPs offer central control over the maximum available permissions for all accounts in your organization
- AWS services, resources, individual API actions 에 관한 권한도 관리할 수 있다.
- organization 내의 user or role 이 특정 IAM permission 을 부여받았어도, SCP가 이를 금지한다면 해당 행동은 금지된다.
- root user도 SCP의 영향을 받는다.
- service-linked role은 scp의 영향을 받지 않는다.
### 2.  S3 Glacier vault, vault lock policy 
(vault: 금고) 
- An S3 Glacier vault is a container for storing archives. 
- When you create a vault, you specify a vault name and the AWS Region in which you want to create the vault. 
- ***S3 Glacier Vault Lock*** allows you to easily deploy and enforce compliance controls for individual S3 Glacier vaults with a vault lock policy. 
- You can specify controls such as “write once read many” (WORM) in a vault lock policy and lock the policy from future edits. 
- enforce compliance control 을 하려면 vault를 사용해야 한다!

참고: 
- s3 Access Control List(ACls) : manage access to buckets and objects. <br>***can't be used to enforce compliance controls***
- s3 lifecycle policy: transit objects to another storage class, archive them, or delete them after a pecified period <br>
***can't be used to enforce compliance controls***
### 3. AWS Site-to-Site VPN(=VPN Connection)
- on-premise와 VPC를 안전하고 빠르게 연결해줌.
- enables you to securely connect your on-premises network or branch office site to your Amazon VPC. 
- You can securely extend your data center or branch office network to the cloud with an AWS Site-to-Site VPN connection.
 - A VPC VPN Connection utilizes IPSec to establish encrypted network connectivity between your on-premises network and Amazon VPC over the Internet. 
 - IPsec is a protocol suite for securing IP communications by authenticating and encrypting each IP packet in a data stream.
 
 - 참고
    - AWS Direct Connect: encryption 지원 안함. 
    - AWS DataSync: on-premise와 aws간에 large amounts of data를 옮길 때 사용. <br> on-premise와 aws간 network 연결기능은 없다.
### 4. AWS Storage Gateway
- AWS Storage Gateway는 사실상 무제한의 클라우드 스토리지에 대한 온프레미스 액세스 권한을 제공하는 하이브리드 클라우드 스토리지 서비스입니다.
- 게이트웨이는 온프레미스 애플리케이션을 클라우드 스토리지에 원활하게 연결하고 지연 시간이 짧은 액세스를 위해 로컬 위치에 데이터를 캐싱합니다.
- File, Volume, Tape 세가지 타입이 있다. NFS, SMB같은 file 프로토콜을 사용해 s3에 데이터를 저장하고 접근한다.
### 5. VPC endpoint, AWS PrivateLink
- can access SQS using VPC endpoints, without using public IPs, and without needing to traverse the public internet. 
- VPC endpoints for Amazon SQS are powered by AWS PrivateLink, a highly available, scalable technology that enables you to privately connect your VPC to supported AWS services.
- They also provide reliable connectivity to Amazon SQS without requiring an internet gateway, Network Address Translation (NAT) instance, VPN connection, or AWS Direct Connect connection. 
- With VPC endpoints, the data between your Amazon VPC and Amazon SQS queue is transferred within the Amazon network, helping protect your instances from internet traffic.
- AWS PrivateLink simplifies the security of data shared with cloud-based applications by eliminating the exposure of data to the public Internet. 
- AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network. 
- AWS PrivateLink makes it easy to connect services across different accounts and VPCs to significantly simplify the network architecture.
### 6.  network address translation (NAT)
- You can use a network address translation (NAT) instance in a public subnet in your VPC to enable instances in the private subnet to initiate outbound IPv4 traffic to the Internet or other AWS services,<br>
 but prevent the instances from receiving inbound traffic initiated by someone on the Internet.
### 7. cross-zone load balancing 
- AZ1에 ec2 1대, AZ2에 ec2 4대가 있다 치자. cross-zone load balancing이 enabled되어있다면, <br>
모든 ec2가 20% 씩 동일하게 트래픽을 받는다. <br>
반면 이 기능이 해제되어 있다면, AZ1에 50%, AZ2d에 50%이 할당되면서 az1 인스턴스는 50%, az2의 인스턴스는 각각 12.5%씩 받게 된다.
### 8. EC2 dedicated hosts
- 이걸 이용하면 하드웨어가 오직 나에게만 할당된다(공유 x). 서버와 묶인 소프트웨어(윈도우 같은)를 안정적으로 계속 사용할 수 있고, 많은 것을 통제할 수 있다.
### 9. AWS DataSync
- an online data transfer service that simplifies, automates, and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.
- S3, EFS, Fsx for windows File Server, CloudWatch, CloudTrail 들과 연결 가능하다.
- fully automates and accelerates moving large active datasets to AWS.
### 10. AWS Transfer Family
- provides fully managed support for file transfers directly into and out of Amazon S3.(only S3)
### 11. basic monitoring vs detailed monitoring
- baisc monitoring이 디폴트인 경우: 1) launch template 설정시, 2)콘솔을 통해 launch configuration 설정 시 
- detaild monitoring이 디폴트인 경우: CLI 또는 SDK를 통해 launch configuration을 설정할 때.
### 12. RAID0, 1
I/O performance가 fault tolerance보다 중요할 땐 RAID0을 써라!
### 13. Route 53
- alias queries는 과금 x. CNAME은 과금 o. <br>
- alias는 s3, cloudfront distributions 같은 route 53 hosted zone내의 다른 record로 보내기 가능.
- CNAME은 다른 DNS record에게만 보내기 가능.

### 14. database migrations to AWS 
- 자체 db에서 aws DB 이전은 homogeneous와 heterogeneous로 나뉜다. 전자는 oracle to oracle처럼 같은 종류의 db로의 이전을 말하고, <br>
후자는 다른 종류의 db로의 이전이다. <br>
- heterogeneous migration을 할 땐 아래 2 가지 서비스를 이용하면 된다.
- AWS Schema Conversion Tool: source schema, code를 타켓 db에 맞게 변형시켜 준다.
- AWS Database Migration Service: on premise -> aws db로의 db migration을 도와주는 서비스.
![스크린샷 2021-02-27 오후 3 48 56](https://user-images.githubusercontent.com/70195733/109378129-67569880-7913-11eb-817b-7d120ad6d393.png)

### 15. AWS Glue
: fully managed extract, transform, and load(ETL) services that makes it easy for customers to prepare and load their data for analytics.<br>
batch ETL data processing 할 때 사용한다.
### 16. Basic Schema Copy 
- AWS Database Migration Service의 한 가능으로, db 스키마와 pk를 빠르게 target db로 복사해준다.
- 이걸 하려면 타켓 db에 지금 옮기려는 것과 똑같은 이름의 db가 존재하면 안된다.
- 같은 종류의 db끼리만 가능하다.
- 인덱스, fk같은건 안옮겨진다.

### 17. Server Side Encryption vs Client Side Encryption
SSE: 서버가 데이터를 encrypt해서 저장하고, client에게 보내주기 전에 decrypt해서 보내는 방법. <br>
Client Side Encryption: client측에서 데이터를 encrypt해서 서버에게 보내고, 서버는 받은 그대로 저장했다가 다시 client에게 보냄. client가 decrypt함.

### 18. AWS KMS(Key management Service)
- "encryption" 단어를 보면, 거의 KMS에 대한 얘기라고 보면 된다.
- fully integated with IAM for authorization
- seamlessly integrated into:
    - EBS: encrypt volumes
    - s3: serve rside encryption of objects
    - Redshift: encryption of data
    - RDS: encryption of data
    - SSM: Parameter store
    - Etc...
![스크린샷 2021-02-27 오후 4 18 48](https://user-images.githubusercontent.com/70195733/109378628-86efc000-7917-11eb-92d9-28060f69ea26.png)
- KMS key는 region에 국한되기 때문에, 예를들어 volume을 다른 region으로 옮겨갈 땐 새로운 키를 만들어야 한다.
![스크린샷 2021-02-27 오후 4 22 47](https://user-images.githubusercontent.com/70195733/109378716-1eeda980-7918-11eb-863a-5af5924b8bf7.png)

### 19. AWS Secrets Manager

- storing secrets service
- capability to force rotation of secrets every X days.
- Automate generation of secrets on rotation(uses Lambda)
- Integrations with RDS
- encrypted using KMS
### 20. AWS Shield
- Standard: 꽁짜, DDOS 어택 방어. layer 3, layer 4 공격 방어, - activated for every AWS customer
- Advanced: $3,000 per month per organization. 더 많은 것들 방어. EC2, ELB, CloudFront, Global Accelerator, Route 53등.
- 24/7 AWS DDoS response team

### 21. AWS WAF(Web Application Firewall)
- prtects your web applications from common web exploits (Layer 7)
- layer 7 is HTTP (vs Layer 4 is TCP)
- WAF는 layer7에서 작동. ALB, API GAteway, CloudFront 딱 이 3가지 에서만 작동한다.
- WAF를 사용하기 위해선 Web ACL(Web Access Control List)를 정의해야 한다!

#### WEB ACL
- Rules can include: IP addresses, HTTP headers, HTTP body, URI strings
- Protects from common attack - SQL injection, Cross-Site Scripting(CSS)
- Size constraints(예. 5mb이상 쿼리는 금지), geo-match(block countries)
- Rate-based rules(to count occurences of events) for DDoS protection

#### AWS Firewall Manager
- Manage rules in all accounts of an Organization
  - WAF rules(ALB, API Gateway, CloudFront)
  - AWS Shield Advanced(ALB, CLB, Elatic IP, CloudFront)
  - SG for EC2 and ENI resources in VPC
![스크린샷 2021-02-27 오후 9 30 28](https://user-images.githubusercontent.com/70195733/109387167-13fc3e80-7943-11eb-981c-b2449ab98499.png)

### 22.
### 23.
### 24.
### 25.
### 26.
### 27.
### 28.
#