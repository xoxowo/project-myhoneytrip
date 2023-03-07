# :tada: project-myhoneytrip (wecode35) 

## 프로젝트 개요 :speech_balloon:
### 프로젝트 목표
마이리얼 트립을 모티브하여 신혼 여행을 떠나기 위해 필요한 항공 서비스를 제공하는 국내 최대 여행 서비스 플랫폼

### 개발 기간 및 인원
- 개발 기간 : 2022-08-01 ~ 2022-08-12 (12일)
- 개발 인원 : 7 명

- Backend  : 안상현, 음정민, **황유정**
- Frontend : 구단희, 김익현, 신수정, 이강철

#### 적용 기술 및 협업 툴
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white">&nbsp;

- 협업 툴 : Slack, Trello, Github, Notion

## 프로젝트 구조
### DB 모델링
<img width="1020" alt="스크린샷 2022-08-12 오후 12 50 01" src="https://user-images.githubusercontent.com/99232122/184281793-0633dd6f-21e1-4959-9f50-82abb42d9b9d.png">

## 📄 구현 기능에 대한 소개
### 사용자 검색 결과 기반 비행 스케줄 API구현 (**황유정**)

 1. 항공권 검색 시 필수 조건(출발지, 도착지, 가는 날, 오는 날(돌아오는 날), 탑승객 수)에 따른 검색 결과를 반환합니다.
  * 돌아오는 날 미지정 시 가는 날(편도)에 대한 검색 결과만 반환합니다.
  * 검색 결과 항공사 별 조건 검색이 가능합니다.
  * 기본 정렬은 최저 가격순으로 나열됩니다.
  * Unit test 완료하였습니다.
  
### 배운 점 & 아쉬운 점
- select_related 활용
생각보다 규모가 큰 DB 모델링에서 어떻게 사용자가 원하는 검색 결과를 모두 가져와 보여줘야할지 고민을 많이 했습니다. 복잡할 수록 DB를 🎯 히트하면 좋지않기 때문에 select_related를 활용하여 flitering 하는 방법을 선택했습니다. q객체를 사용하여 적용해볼까도 고민했었지만 q객체에 대한 개념도 부족했고 활용 방법을 인지하지 못했기 때문에 q 객체는 활용하지 못했습니다.

- Unit test 작성
테스트코드를 작성하는 방법에 대해서 얕게 학습하고 적용해봤다가 여러 오류를 만나고 해결해봤습니다. 코드가 어떤 원리로 기대값을 예상하며 코드를 작성하는지 공식문서와 mdn 글을 보고 한층 더 알게되었습니다. 

## 🎬 사이트 시현 영상
https://user-images.githubusercontent.com/99232122/184281715-92bcc9a4-fe11-4405-9c61-a79ed58b75f0.mov


## 프로젝트 배포 주소
http://2nd-myhoneytrip.s3-website.ap-northeast-2.amazonaws.com/

#### Reference
이 프로젝트는 학습 목적 및 상업 목적으로 만들었기 때문에 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
