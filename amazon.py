#pandas ي أداة تحليل بيانات مفتوحة المصدر ومعالجتها سريعة وقوية ومرنة وسهلة الاستخدام
import pandas as pd
#numpy وهى مكتبة يتم استعمالها لانها تحتوى على mathimatics functions
import numpy as np
#Matplotlib هي مكتبة للتخطيط للغة برمجة بيثون وملحقها الرقمي للرياضيات NumPy.
import matplotlib.pyplot as plt
#seabornمكتبة تصور البيانات الإحصائية في Python
import seaborn as sns

#هنستدعي الملف بتاعنا و نعمله encoding من الاتيني للانجليزي 
data_set=pd.read_csv(r"D:\PYTHON\amazon fires\amazon.csv",encoding='latin1')

#الفانكشن دي بتظهر اول 5 صفوف عشان تتطلع علي الداتا و تشوفها 
#بين القوسين بنحط عدد الصفوف الي عايزين نظهرها 
data_set.head(20)

#هنشيل عمود date عشان منتكرر 
#وملهوش لازمه 
data_set.drop("date",inplace=True,axis=1)

data_set.head()
#فانكشن isna بتشوف القيم الفاضيه في كل عمود 
#و بنجمعهم في فانكشن sum
data_set.isna().sum()
#هنجيب معلومات عن الداتا ببتاعتي و بيانات احصائيه 
data_set.describe()
#عايز اعرف انواع الداتا عندنا نوعهم ايه 
data_set.dtypes
#هنجيب كل مدينه و عدد الحرايق الي حصلت فيها 
print(data_set.groupby(["state"]).count())
#هنحول الداتا دي لجراف عن طريق sns
sns.countplot(x="state",data=data_set)
#هنجييب الحرايق بس لكل سنه مش لكل مدينه و المره دي رسم بياني خطي
sns.lineplot(data=data_set,x="year",y="number")
#هنجيب علاقه الحروق بالشهور 
sns.swarmplot(x="month",y="number",data=data_set)
#نفس العلاقه الي قبلها بس بلرمس بياني مختلف 
sns.boxplot(x="month",y="number",data=data_set)
#علاقه المدن بالنسبه للارقم 
sns.boxplot(x="state",y="number",data=data_set)
temp={1:17.9,2:-13.9,3:-7.6,4:3.3,5:10.9,6:15.7,7:18.6,8:17.8,9:11.5,10:5.3,11:5.2,12:-12.8}
#عايزين نجيب رقم يدل علي الشهور 
data_set.month.unique()
#هندي كل شهر رقم لسهوله التعامل معاه 
month_number={'Janeiro':1, 'Fevereiro':2, 'Março':3, 'Abril':4, 'Maio':5, 'Junho':6, 'Julho':7,
'Agosto':8, 'Setembro':9, 'Outubro':10, 'Novembro':11, 'Dezembro':12}
#هنبدل العمود الي اسمه الهور بارقام الشهور نفسها 
data_set["month_number"]=data_set.month.map(month_number)
#هنتاكد ان العمود اتغير 
data_set.head()
#هنضيف درجات الحراره لكل شهر
data_set["temp"]=data_set["month_number"].map(temp)
#هنمسح عموايد ملهاش لازمه معانا 
data_set.drop("month_number",axis=1)
#هنجيب العلاقه بين درجه الحراره و الحرايق
sns.lineplot(x="temp",y="number",data=data_set)