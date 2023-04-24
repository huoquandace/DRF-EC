## Dự án CleanCode team6

### Cài đặt và Cấu hình  
_(Hướng dẫn dành cho Ubuntu, Mac)_  
1. Cài đặt docker và docker-compose  
2. Clone code và cài đặt  
``` 
git clone ...
```
Cd vào thư mục dự án
``` 
cd CLEANCODE
```
Copy file enviroment variables mặc định
``` 
cp .env.example .env
```
sau đó, cập nhật giá trị cho các biến trong file .env  


### Các thao tác trong project
| Action | Run command |
| --------------------- |:--------------:|
| Build dự án   |```make build```|
| Up dự án      |```make up```|
| Down dự án      |```make down```|
| Xem log của container web |```make logs```|
| Restart container web |```make restart```|
| Vào shell docker  |```make shell```|
| Vào att  |```make att```|



### Các thao tác trong shell
| Action | Run command |
| --------------------- |:--------------:|
| Tạo user        |```python manage.py createsuperuser``` |
| Create file migrations    |```python manage.py makemigrations```  |
| Apply migrations          |```python manage.py migrate```  |


### Tài liệu tham khảo
