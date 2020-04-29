# config/routes.rb

"""
post "delete_account" => "admin#delete_account"
# extension settngs
get "extension-settings/:id/mute" => "extension_settings#mute"

# forward non-namespaced routes to api namespace
get 'auth/params' => "api/auth#auth_params"
post "auth/sign_in" => "api/auth#sign_in"
post "auth" => "api/auth#register"
post "auth/update" => "api/auth#update"
post "auth/change_pw" => "api/auth#change_pw"

post "items/sync" => "api/items#sync"
post "items/backup" => "api/items#backup"

delete "items" => "api/items#destroy"
resources "items", :controller => "api/items"
"""

