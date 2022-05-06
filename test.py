# Time diffrence #
#----------------#
# from datetime import datetime, timedelta
  
# updated = ( datetime.now() +
#            timedelta(hours=1, minutes=5)).strftime('%H:%M:%S')
# print(datetime.now().strftime('%H:%M:%S'))
# print( updated )



# Meeting message test #
#----------------------#
# date = '2021-08-19'
# time = '13:24:56'
# url = 'https://support.huaweicloud.com/intl/en-us/productdesc-msgsms/sms_templates.html#section1'
# mettingId = '111-1111-111'
# passcode = '123'
# body="""
# Hi, Dear

# Reminder: The "interview schedule" at D:{DATE}&T:{TIME} is about to start. Join the meeting on time.

# Join metting
# {URL}

# Metting ID: {METTINGID}
# Passcode: {PASSCODE}

# """.format(DATE=date, TIME=time, URL=url, METTINGID=mettingId, PASSCODE=passcode)

# print(body)