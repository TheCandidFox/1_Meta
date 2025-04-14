from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import hashlib
import hmac

# --- CONFIGURE ACCESS ---
ACCESS_TOKEN = 'EAAL0hsUCslgBOzNBZARXh3kreFHJS13AKPCcoyPzfMvm9fmA0uoFZADXdniHKGm1RI72zrLdZAfPZCgBXPmhZAykbtBrpJuUw63fQZCp2hSa2lXvubEsHWQJLKg4ylAeObL4t9qMdZBsape58tqc8pY8qtXgBTXcCYRfKc20VYcPNdnk0f4li7YYqfcqNCnEx6w9CxbMc7zZCiysZA5ysFziLtVqpriqZCnIBkASEZD'
AD_ACCOUNT_ID = 'act_786767373171681'
APP_ID = '831809621504600'
APP_SECRET = '875adfa3f56fe47586f232f14cd411c5'


FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)




my_account = AdAccount(AD_ACCOUNT_ID)
campaigns = my_account.get_campaigns()
print(campaigns)

