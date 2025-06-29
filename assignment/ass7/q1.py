import pandas as pd
import numpy as np

data = {
    'email': ['a@gmail.com', 'expample@gmail.com', 'invalid mail', 'hello@'],
    'name': ['a', 'b', 'c', 'd'],
    'phone': ['9876543210', '12345', '9988776655', 'abc1234567']
}

df = pd.DataFrame(data)


phone_regex = r'^(\+91)?[789]\d{9}$'
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
name_regex = r'^[A-Za-z]+$'

df['valid_email'] = df['email'].str.contains(email_regex, regex=True)
df['valid_name'] = df['name'].str.contains(name_regex, regex=True)
df['valid_phone'] = df['phone'].str.contains(phone_regex, regex=True)


df['email_status'] = np.where(df['valid_email'], 'Valid', 'Invalid')
df['phone_status'] = np.where(df['valid_phone'], 'Valid', 'Invalid')

print(df)