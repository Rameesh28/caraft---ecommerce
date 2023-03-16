from django import forms



class userform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)


class shopform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)


class userlog(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)

class shoplog(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)


class productform(forms.Form):
    pname=forms.CharField(max_length=30)
    pid=forms.CharField(max_length=10)
    price=forms.IntegerField()
    des=forms.CharField(max_length=100)
    image=forms.ImageField()