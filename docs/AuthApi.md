# portainer_ce_api.AuthApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](AuthApi.md#authenticate_user) | **POST** /auth | Authenticate
[**logout**](AuthApi.md#logout) | **POST** /auth/logout | Logout
[**validate_o_auth**](AuthApi.md#validate_o_auth) | **POST** /auth/oauth/validate | Authenticate with OAuth


# **authenticate_user**
> AuthAuthenticateResponse authenticate_user(body)

Authenticate

Use this endpoint to authenticate against Portainer using a username and password.

### Example
```python
from __future__ import print_function
import time
import portainer_ce_api
from portainer_ce_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer_ce_api.AuthApi()
body = portainer_ce_api.AuthAuthenticatePayload() # AuthAuthenticatePayload | Credentials used for authentication

try:
    # Authenticate
    api_response = api_instance.authenticate_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authenticate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticatePayload**](AuthAuthenticatePayload.md)| Credentials used for authentication | 

### Return type

[**AuthAuthenticateResponse**](AuthAuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

### Example
```python
from __future__ import print_function
import time
import portainer_ce_api
from portainer_ce_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = portainer_ce_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer_ce_api.AuthApi(portainer_ce_api.ApiClient(configuration))

try:
    # Logout
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_o_auth**
> AuthAuthenticateResponse validate_o_auth(body)

Authenticate with OAuth

### Example
```python
from __future__ import print_function
import time
import portainer_ce_api
from portainer_ce_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer_ce_api.AuthApi()
body = portainer_ce_api.AuthOauthPayload() # AuthOauthPayload | OAuth Credentials used for authentication

try:
    # Authenticate with OAuth
    api_response = api_instance.validate_o_auth(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->validate_o_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthOauthPayload**](AuthOauthPayload.md)| OAuth Credentials used for authentication | 

### Return type

[**AuthAuthenticateResponse**](AuthAuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

