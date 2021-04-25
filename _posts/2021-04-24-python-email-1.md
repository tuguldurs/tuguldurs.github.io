---
title: 'send gmail through python'
date: 2021-04-24
permalink: /posts/2012/04/python-email/
tags:
  - python
  - email
---

Using only [smtplib](https://docs.python.org/3/library/smtplib.html) and [getpass](https://docs.python.org/3/library/getpass.html) you can send your email from the terminal:

```python
import sys

import smtplib
import getpass as gp

me    = 'tuguldur.s@gmail.com'
gmail = 'smtp.gmail.com:587'

def msgheader(to):
    header  = f'From: {me}\n'
    header += f'To: {to}\n\n'
    return header

def sendgmail(to, msg):
    header = msgheader(to)
    msg  = header + msg
    serv = smtplib.SMTP(gmail)
    # start encryption
    serv.starttls()
    pwd  = gp.getpass(f'>>> pwd for {me} :')
    serv.login(me, pwd)
    serv.sendmail(me, [to], msg)
    serv.quit()


if __name__ == "__main__":
    sendgmail(sys.argv[1], sys.argv[2])
```
run it as:
```
$ python3 sendgmail.py sukhbold.1@osu.edu 'my test message'
```
Note that your message needs to have a header with at least From/To fields, otherwise the message body alone won't be recognized as valid. For gmail users you may need to turn on the access for "Less secure app" in your account settings. Since we are using TLS the gmail port should be 587, [see here](https://support.google.com/a/answer/176600?hl=en#zippy=%2Cuse-the-gmail-smtp-server). Finally, note the receiving address(<code>to</code>) is passed as a list in <code>serv.sendmail()</code>; this is in case you have multiple recipients.
