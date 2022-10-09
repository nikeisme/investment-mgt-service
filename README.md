# investment-mgt-service

> 주어진 고객 투자 데이터를 응답하는 REST API 개발


## 📚 기술스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 


## ERD 설계
![image](https://user-images.githubusercontent.com/99165573/194735301-7936fab2-c46c-4da1-83a5-30c9bf43be29.png)


## 폴더 구조
```
📦investment-mgt-service
 ┣ 📂api
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂backend_core
 ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┣ 📜deploy.py
 ┃ ┃ ┣ 📜local.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂csv
 ┃ ┣ 📜account_asset_info_set.csv
 ┃ ┣ 📜account_basic_info_set.csv
 ┃ ┗ 📜asset_group_info_set.csv
 ┣ 📂venv
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜manage.py
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜requirements.txt
 ┗ 📜upload_csv.py
 ```
 
## 실행 방법
 ```
Terminal 접속 -> cd venv 입력 -> pipenv shell 입력 -> python manage.py runserver 입력 -> 브라우저에서 http://127.0.0.1:8000/ 실행
```
 
 
## api

![image](https://user-images.githubusercontent.com/99165573/194735665-d45b771f-07be-49ec-8489-537ad98232a3.png)



- **고객의 투자화면 (계좌명, 증권사, 계좌번호, 총 자산) 을 조회할 수 있습니다.**
![image](https://user-images.githubusercontent.com/99165573/194735855-efdb2797-c298-4dae-a08a-09ec962297c0.png)<br>

- **고객의 투자 상세 화면 ( 계좌명, 증권사, 계좌번호, 계좌 총 자산, 투자원금, 총 수익금, 수익률)을 조회할 수 있습니다. **
![image](https://user-images.githubusercontent.com/99165573/194736017-52fdfd30-fd3b-45c1-9aea-5cee9e1b21ec.png)<br>

- **고객의 보유 종목 화면 ( 보유 종목명, 보유 종목의 자산군, 보유 종목의 평가 금액 , 보유 종목 ISIN)을 조회할 수 있습니다.**
![image](https://user-images.githubusercontent.com/99165573/194736075-56e7d66d-8de5-43b9-b77d-64598fd0f43e.png)<br>

- **입금 거래 정보 (계좌번호,고객 명, 거래 금액) 을 거래 정보 식별자 ( 요청 데이터 묶음을 식별하는 key 값)으로 서버에 등록합니다.**
![image](https://user-images.githubusercontent.com/99165573/194736105-bb1ec9dd-f127-4e48-ba9b-b36fdc99fce2.png)<br>

## Trouble shooting

### 요청 데이터 hash 하여 입금 결과 데이터 응답 

- **요청 데이터**
```
- 데이터 STring 을 hash / 응답받은 거래 정보 식별자
{
"signature": "82b64b05dfe897e1c2bce88a62467c084d79365af1", // "123123아이작
1000" 을 sha512 hash 한 값.
"transfer_identifier": 111
}

```

- **응답 데이터**
```
입금 결과 데이터
ex) "status": true
```
