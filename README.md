# 2023-1 Web Server Computing
< 소프트웨어학부 소프트웨어전공 20213091 최지원 >
<br />
국민대학교 소프트웨어융합대학 교과목 웹 서버 컴퓨팅 수업의 실습 및 응용 코드를 관리하는 저장소입니다.



## 디렉토리 구조 (main 기준)

* config-django-rest
  * DRF(django-rest-framework)를 이용한 django 프로젝트의 예제 코드입니다.
* config-django-student
  * DRF를 이용한 CRUD를 FBV(function based view)와 CBV(class based view)로 구현하는 프로젝트의 예제 코드입니다.
* tutorial
  * authentication & permission을 적용한 django 프로젝트의 예제 코드입니다.


## 브랜치 구조

* main
  * 모든 프로젝트: 아래 브랜치에서 작업한 모든 django project가 존재하는 브랜치입니다.
* django-auth-permission
  * tutorial 프로젝트               : 인증 및 권한 설정과 관련된 코드가 작성되어 있습니다.
* django-rest
  * config-django-rest 프로젝트     : DRF 기본 이용과 관련된 코드가 작성되어 있습니다.
* django-students             
  * config-django-student 프로젝트  : CBV, FBV를 이용한 CRUD와 관련된 코드가 작성되어 있습니다.