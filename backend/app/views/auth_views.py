# app/controllers

import hashlib
# Create your views here.
from django.views import View
from django.http import JsonResponse

class AuthParamsView(View):
    def get(self, request):
        print(request.GET)
        return JsonResponse({
          'identifier': request.GET['email'],
          'pw_cost': 110000,
          'pw_nonce': hashlib.sha224(request.GET['email'].encode()).hexdigest(), # Digest::SHA2.hexdigest(email + Rails.application.secrets.secret_key_base),
          'version': '003',
        })


class SignInView(View):
    def post(self, request):
        print(request.POST)
        return JsonResponse({'foo': 'bar'})


# {:user=>#

# <User uuid: "70c0b758-b356-440a-95e0-485338fe2120", 
# email: "suhailvs@gmail.com", 
# pw_func: nil, 
# pw_alg: nil, 
# pw_cost: 110000, 
# pw_key_size: nil, 
# pw_nonce: "8c21696b3bbc9b02b8f5cdc809b8f59c5f6f2eca6ece9d2db5...", 
# encrypted_password: "$2a$11$EdBP8fuPOPwJO0ozNsLXyeOf6MSHXxPmSCk7tCItzx/...", 
# created_at: "2020-04-29 13:24:26", 
# updated_at: "2020-04-29 14:09:50", 
# pw_salt: nil, 
# version: "003", 
# updated_with_user_agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36...", 
# locked_until: nil, 
# num_failed_attempts: 0>, 

# :token=>"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI3MGMwYjc1OC1iMzU2LTQ0MGEtOTVlMC00ODUzMzhmZTIxMjAiLCJwd19oYXNoIjoiYmZlMzYwYTQ0ZWNlZGU0MWQzZTEwMjc1MDhiOThjMzVlZDM3NzkzNWZkZDgzMjJhZWFiZWQ1MDNlNjVhN2I4OCJ9.S1bxBRFBkT8f6TmXW38mVBxSsN7fzNNhTxnfyvYJOvk"
# }