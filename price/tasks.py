import json
from celery import shared_task
from django.core.mail import send_mail
from pricing_module import settings
from.models import Price_Calculate
from .serializers import userSerializer
@shared_task(bind=True)
def send_email_task(self):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer
    final_dict={}
    earning_report=[]
    for data in queryset:
        final_dict['Distance_Base_Price']=data.Distance_Base_Price
        final_dict['Distance_travel']=data.Distance_travel
        final_dict['Distance_Additional_Price']=data.Distance_Additional_Price
        final_dict['Time_in_hours']=data.Time_in_hours
        earning_report.append(final_dict.copy())
    mail_subject = "Daily Earning Report"
    message = json.dumps(earning_report)
    to_email = 'patilakshay739@gmail.com'
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "Done"

