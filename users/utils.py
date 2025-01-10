import random
from django.core.mail import send_mail
from .models import User

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email_otp(email):
    otp = generate_otp()
    try:
        user, created = User.objects.get_or_create(email=email)
        user.email_otp = otp
        user.is_email_verified = False
        user.save()

        # Send OTP via email
        send_mail(
            subject="Your Email OTP Verification Code",
            message=f"Your OTP is: {otp}",
            from_email="tayeyohanis8@gmail.com",  # Change to your app's email
            recipient_list=[email],
        )
        return True
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return False
