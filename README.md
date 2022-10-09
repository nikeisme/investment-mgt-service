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
 
## api

![image](https://user-images.githubusercontent.com/99165573/194735665-d45b771f-07be-49ec-8489-537ad98232a3.png)

 
