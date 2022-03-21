# AZ Iranian Bank Gateway (v1.6.15 Forked)
## [AZ Iranian Bank Gateway (Main Repository)](https://github.com/ali-zahedi/az-iranian-bank-gateways)

## Changes
### added `payer` filed to `Bank` model.

---

File `models.banks.py` Line `7-10`
```python
from django.contrib.auth import get_user_model


User = get_user_model()
```

File `models.banks.py` Line `74-79`
```python
payer = models.ForeignKey(
    User,
    null=True,
    on_delete=models.CASCADE,
    related_name='payments',
    verbose_name='پرداخت کننده')
```

File `models.banks.py` Line `126`
```python
return '{}-{}-{}'.format(self.pk, self.payer.username, self.tracking_code)
```

---

File `banks.banks.py` Line `25`
```python
_payer = None
```

File `banks.banks.py` Line `80-87`
```python
def get_payer(self):
    """get the payer"""
    return self._payer

def set_payer(self, payer):
    """set payer"""
    self._payer = payer

```

File `banks.banks.py` Line `126`
```python
payer=self.get_payer(),
```

File `banks.banks.py` Line `209`
```python
self.set_payer(self._bank.payer)
```

---

File `views/samples.py` Line `19`
```python
if form.is_valid() and request.user.is_authenticated:
```

File `views/samples.py` Line `27`
```python
bank.set_payer(request.user)
```

File `views/samples.py` Line `30-31`
```python
if mobile_number:
    bank.set_mobile_number(mobile_number)  # اختیاری
```

---

File `admin.py` Line `11,26,46,63`
```python
'payer',
```

## Usage

```python
bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
print(bank_record.payer.username)  # prints the payer's username
```

```python
payer = User.objects.get(pk=request.pk)
print(payer.payments.all())  #  prints all user's payments
print(payer.payments.filter(status='Complete'))  #  prints Completed user's payments
```