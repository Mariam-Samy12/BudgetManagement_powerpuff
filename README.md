# يا شباب اقروا الخطوات دي علشان تنزلوه عندكم
###سحب الكود (Clone):
```
git clone https://github.com/Mariam-Samy12/BudgetManagement_powerpuff.git
cd budgetproject
```
###عشان المكتبات متدخلش في بعضها، اعملوا venv جديدة:
```
python -m venv venv
او اي اسم غير ven
```
###تفعيل البيئلا
```
venv\Scripts\activate
```
###هم حاجة كل حاجة انا نزلتها تكون عندكم فنزلوا
```
pip install -r requirements.txt
```

###نا مرفعتش قواعد البيانات فلازم تجيبوها عندكم
```
python manage.py migrate
```

###رنوا السيرفر لو اشتغل يبقا مبروك
```
python manage.py runserver
```
