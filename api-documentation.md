
<p align="center" style="font-size: 35px;">
  <b>BitBlast API Documentation</b>
</p><br>


<p align="center" style="font-size: 30px;">
  <b>API's of UserAuth_app</b>
</p><br>

# 1. First Admin User Creation API

This API allows the creation of the first admin user in the system. If an admin user already exists, it will return an error. Only the POST method is allowed for this endpoint.

**URL** : `http://<your-domain>/api/v1/create_first_admin/`

**Method** : `POST`

## Request

**Headers** : 
- **Content-Type** : `application/json`

**Body Parameters**

- **username** : (string) The desired username for the admin user (required).
- **password** : (string) The password for the admin user (required).
- **email** : (string) The email address of the admin user (optional).
- **role** : (string) The role of the admin user (required).


**Example Request Body**

```json
{
    "username": "admin_user",
    "password": "securepassword",
    "email": "admin_user@example.com",
    "role": "Admin"
}
```
## Response
**Successful Response (Status Code: `201`)**

- **success** : (string) Success message indicating that the admin user was created successfully.

**Example Response Body**

```json
{
    "success": "Admin user created successfully."
}
```

## Error Responses

**Admin User Already Exists (Status Code: `400`)**

- **error**: (string) Error message indicating that an admin user already exists.

**Example Response Body** 

```json
{
    "error": "Admin user already exists."
}
```
**Missing Parameters (Status Code: `400`)**
- **detail**: (string) Error message indicating that both username and password are required.

**Example Response Body** 
```json
{
    "error" : "Username and password are required."
}
```
**Method Not Allowed (Status Code: `405`)**
- **detail** : (string) Error message indicating that the GET method is not allowed for this endpoint.

**Example Response Body** 

```json
{
    "error": "GET method is not allowed."
}
````

## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/create_first_admin/ \
-H "Content-Type: application/json" \
-d '{
    "username": "admin_user",
    "password": "securepassword",
    "email": "admin_user@example.com",
    "role": "Admin"
}'
```
<hr>
<br>
<br>

# 2. Check Admin User Exists API

This API checks if there is an existing admin user in the system. It returns a JSON response indicating whether an admin user exists or not.

**URL** : `http://<your-domain>/api/v1/check-admin-user-exists/`

**Method** : `GET`

**Note** :
- Before using this API to check for the existence of an admin user, ensure that an admin user has been created. You can find the Create First Admin API documentation [here](#1-first-admin-user-creation-api).

## Response
**Successful Response (Status Code: `200`)**

- **exists** : (boolean) A boolean value indicating whether an admin user exists (true) or not (false).

**Example Response Body (Admin User Exists)**

```json
{
    "exists": true
}
```
**Example Response Body (Admin User Does Not Exist)**

```json
{
    "exists": false
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/check-admin-user-exists/ \
-H "Content-Type: application/json
```
<hr>
<br>
<br>

# 3. User Registration API

This API allows administrators to register a new user with specified details such as username, password, role, email, first name, and last name.

**URL** : `http://<your-domain>/api/v1/register/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required
- Only users with the Admin role can access this endpoint due to the IsAllowedRole permission class.

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters**

- **username** : (string) The username of the new user.
- **password** : (string) The password of the new user.
- **role** : (string) The role of the new user.
- **email** : (string) The email of the new user.
- **first_name** : (string) The first name of the new user.
- **last_name** : (string) The last name of the new user.

**Example Request Body**

```json
{
    "username": "new_user",
    "password": "new_password",
    "role": "Admin",
    "email": "new_user@example.com",
    "first_name": "New",
    "last_name": "User"
}
```
## Response
**Successful Response (Status Code: `201`)**

-	**id** : (integer) The ID of the newly created user.
-	**username** : (string) The username of the newly created user.
-	**role** : (string) The role of the newly created user.
-	**email** : (string) The email of the newly created user.
-	**first_name** : (string) The first name of the newly created user.
-	**last_name** : (string) The last name of the newly created user.


**Example Response Body**

```json
{
    "username": "new_user",
    "role": "Admin",
    "email": "new_user@example.com"
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "username": ["This field is required."],
    "email": ["Enter a valid email address."],
    "password": ["This field is required."]
}
```
**Authentication Errors (Status Code: `401`)**
- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail" : "Invalid token."
}
```
**Permission Denied (Status Code: `403`)**
- **detail** : (string) Error message indicating that the user does not have permission to access this endpoint.

**Example Response Body** 

```json
{
    "detail": "You do not have permission to perform this action."
}
````

## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/register/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "new_password",
    "role": "User",
    "email": "new_user@example.com",
    "first_name": "New",
    "last_name": "User"
}'
```
<hr>
<br>
<br>

# 4. User Login API

This API allows users to login with his credentials like- username & password.

**URL** : `http://<your-domain>/api/v1/register/`

**Method** : `POST`

**Permissions** :
- Open to all authenticated users.

**Note** :
- Before using this API, ensure that an user has been created or registered. You can find the Create user API documentation [here](#3-user-registration-api).

## Request

**Headers** : 
- **Content-Type** : `application/json`

**Body Parameters**

- **username** : (string) The username of the new user.
- **password** : (string) The password of the new user.
- **role** : (string) The role of the new user.

**Example Request Body**

```json
{
    "username": "new_user",
    "password": "new_password",
    "role": "Standard"
}
```
## Response
**Successful Response (Status Code: `200`)**

-	**token** : (string) The authentication token.
-	**username** : (string) The username of the user.
-	**role** : (string) The role of the user.

**Example Response Body**

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "username": "new_user",
    "role": "Standard"
}
```

## Error Responses

**Missing Parameters (Status Code: `400`)**

- **error**: (string) Error message indicating missing parameters.

**Example Response Body** 

```json
{
       "error": "Please provide both username and password"
}
```
**Invalid Credentials (Status Code: `401`)**
- **detail**: (string) Error message indicating invalid credentials.

**Example Response Body** 
```json
{
    "error": "Invalid credentials"
}
```


## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/d-login/ \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "new_password",
    "role": "Standard "
}'
```
<hr>
<br>
<br>

# 5. LDAP User Login API

This API allows ldap users to login with his credentials like- username & password.

**URL** : `http://<your-domain>/api/v1/ldap-login/`

**Method** : `POST`

**Permissions** :
- Open to all authenticated users.

## Request

**Headers** : 
- **Content-Type** : `application/json`

**Body Parameters**

- **username** : (string) The username of the new user.
- **password** : (string) The password of the new user.
- **role** : (string) The role of the new user.

**Example Request Body**

```json
{
    "username": "new_user",
    "password": "new_password",
    "role": "Standard"
}
```
## Response
**Successful Response (Status Code: `200`)**

-	**token** : (string) The authentication token.
-	**username** : (string) The username of the user.
-	**role** : (string) The role of the user.

**Example Response Body**

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "username": "ad_user",
    "role": "Standard"
}
```

## Error Responses

**Missing Parameters (Status Code: `400`)**

- **error**: (string) Error message indicating missing parameters.

**Example Response Body** 

```json
{
       "error": "Please provide both username and password"
}
```
**Invalid Credentials (Status Code: `401`)**
- **detail**: (string) Error message indicating invalid credentials.

**Example Response Body** 
```json
{
    "error": "Invalid credentials"
}
```


## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/ldap-login/ \
-H "Content-Type: application/json" \
-d '{
    "username": "ad_user",
    "password": "ad_password",
    "role": "Standard "
}'
```
<hr>
<br>
<br>





# 6. User Details API

This API retrieves the details of the authenticated user. The user must be authenticated to access this endpoint.

**URL** : `http://<your-domain>/api/v1/get-user-info/`

**Method** : `GET`

**Note** :
- Before using this API, ensure that an user has been created or registered. You can find the Create user API documentation [here](#3-user-registration-api).

## Request

**Headers** :
- **Content-Type** : `application/json`

## Response
**Successful Response (Status Code: `200`)**

-	**username** : (string) The username of the authenticated user.
-	**email** : (string) The email address of the authenticated user.
-	Other details can be added as needed.

**Example Response Body**

```json
{
    "username": "example_user",
    "email": "example_user@example.com"
}
```
## Error Response

**Authentication Error (Status Code:`401`)**
- **detail** : (string) Error message indicating that authentication credentials were not provided or are invalid.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/get-user-info/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>

# 7. List all Users API

This API retrieves a list of all users along with their roles. Only users with the Admin role can access this endpoint due to the IsAllowedRole permission. 

**URL** : `http://<your-domain>/api/v1/users/`

**Method** : `GET`

**Permissions** :

- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response
**Successful Response (Status Code: `200`)**

An array of user objects with the following fields:

-	**id** : (integer) The unique identifier of the user.
-	**username** : (string) The username of the user.
-	**first_name** : (string) The first name of the user.
-	**last_name** : (string) The last name of the user.
-	**email** : (string) The email address of the user.
-	**role** : (string) The role of the user.
-	**is_superuser** : (boolean) Indicates if the user is a superuser.
-	**is_staff** : (boolean) Indicates if the user is staff.
-	**is_active** : (boolean) Indicates if the user account is active.
-	**date_joined** : (string) The date and time when the user account was created.


**Example Response Body**

```json
[
    {
        "id": 79,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "email": "admin@gmail.com",
        "role": "Admin",
        "is_superuser": true,
        "is_staff": true,
        "is_active": true,
        "date_joined": "2024-06-29T07:27:31.384241Z"
    }
]
```
## Error Response

**Authentication Error  (Status Code:`401`)**
- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```

**Permission Denied (Status Code: `403`)**

- **detail**: (string) Error message indicating that the user does not have permission to access this endpoint. 

**Example Response Body**
{
    "detail": "You do not have permission to perform this action."
}

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/users/ \
-H "Authorization: Token <your-auth-token>"
```
<hr>
<br>
<br>

# 8. Save AD Groups and Members API

This API retrieves Active Directory (AD) groups and their members, then saves them into the application's database.

**URL** : `http://<your-domain>/api/v1/save-ad-groups/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response
**Successful Response (Status Code: `200`)**

- **message** : (string) Success message indicating that LDAP groups and members were saved successfully.

**Example Response Body**

```json
{
    "message": "LDAP groups and members saved successfully"
}
```
## Error Response

**Authentication Error (Status Code:`401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Server Error (Status Code:`500`)**

- **error** : (string) Error message indicating a server-side issue occurred during LDAP retrieval or database saving.

**Example Response Body**

```json
{
    "error": "LDAP server unreachable."
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/save-ad-groups/ \
-H "Authorization: Token <your-auth-token>"
```
<hr>
<br>
<br>


# 9. List AD Groups with Members API

This API retrieves Active Directory (AD) groups along with their members. Only users with the Admin role can access this endpoint due to the IsAllowedRole permission.

**URL** : `http://<your-domain>/api/v1/list-gmember/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response
**Successful Response (Status Code: `200`)**

**groups** : (list) A list of objects containing information about each AD group and its members.
- **group_name** : (string) The name of the AD group.
- **members** : (list) A list of usernames of members belonging to the AD group.

**Example Response Body**

```json
{
    "groups": [
        {
            "group_name": "Group1",
            "members": ["user1", "user2"]
        },
        {
            "group_name": "Group2",
            "members": ["user3", "user4", "user5"]
        }
    ]
}
```
## Error Response

**Authentication Error (Status Code:`401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Server Error (Status Code:`500`)**

- **error** :  (string) Error message indicating a server-side issue occurred during LDAP retrieval or database saving.

**Example Response Body**

```json
{
    "error": "LDAP server unreachable."
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/list-gmember/ \
-H "Authorization: Token <your-auth-token>"
```
<hr>
<br>
<br>




# 10. Save AD Users API

This API retrieves users from Active Directory (AD) and saves their usernames to the application's database. Only users with the Admin role can access this endpoint due to the IsAllowedRole permission.

**URL** : `http://<your-domain>/api/v1/save-ad-users/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response
**Successful Response (Status Code: `200`)**

**users** : (list) A list of objects containing information about each user saved to the database.

- **sAMAccountName** : (string) The sAMAccountName (username) of the user.


**Example Response Body**

```json
{
    "users": [
        {"sAMAccountName": "user1"},
        {"sAMAccountName": "user2"},
        {"sAMAccountName": "user3"}
    ]
}
```
## Error Response

**Authentication Error (Status Code:`401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Server Error (Status Code:`500`)**

- **error** :  (string) Error message indicating a server-side issue occurred during LDAP retrieval or database saving.

**Example Response Body**

```json
{
    "error": "LDAP server unreachable."
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/save-ad-users/ \
-H "Authorization: Token <your-auth-token>"
```
<hr>
<br>
<br>


# 11. Assign or Change Role API

This API allows administrators to assign or change the role of a specific user identified by their username.

**URL** : `http://<your-domain>/api/v1/users/<str:username>/assign-role/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required
- Only users with the Admin role can access this endpoint due to the IsAllowedRole permission class.

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters**

**role** : (string) The role to assign or change for the user. Must be one of the following choices:
- 'Admin'
- 'Standard'


**Example Request Body**

```json
{
    "role": "Standard"
}
```
## Response
**Successful Response (Status Code: `201`)**

- **message** : (string) Success message indicating that the role for the user has been successfully changed.


**Example Response Body**

```json
{
    "message": "Role for <username> changed to <role>"
}
```

## Error Responses

**User Not Found (Status Code: `404`)**

- **error**: (string) Error message indicating that the specified user does not exist.

**Example Response Body** 

```json
{
    "error": "User not found"
}
```
**Invalid Role (Status Code: `400`)**
- **detail**: : (string) Error message indicating that the provided role is invalid.

**Example Response Body** 
```json
{
    "error": "Invalid role"
}
```
**Authentication Error (Status Code: `401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body** 

```json
{
    "detail": "Authentication credentials were not provided."
}
````

## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/users/<username>/assign-role/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json" \
-d '{
    "role": "Standard"
}'
```
<hr>
<br>
<br>

# 12. Get User Role API

Retrieve the role of a user by their username. 

**URL** : `http://<your-domain>/api/v1/users/<str:username>/user-role/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

**Path Parameter** :
- **username** : (string)The username of the user whose role is being retrieved.

## Response
**Successful Response (Status Code: `200`)**

- Successfully retrieved the user role.

**Example Response Body**

```json
{
  "role": "admin"
}
```
## Error Response

**Not Found (Status Code:`404`)**
- **detail** : The user with the specified username does not exist.

**Example Response Body**

```json
{
  "error": "User not found"
}
```

## Example Usage

**cURL**
```json
curl -X GET \
  http://yourapi.com/users/<username>/user-role/ \
  -H "Authorization: Token <your_token>"
```
<hr>
<br>
<br>


# 13. Assign Roles to AD Group Members API

This API assigns a specified role to all members of a given Active Directory (AD) group.

**URL** : `http://<your-domain>/api/v1/assign-role-group/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required
- Only users with the Admin role can access this endpoint due to the IsAllowedRole permission class.

**Note** :
- Ensure that the specified AD group and its members exist in the system. If the group does not exist, the endpoint will return a 400 error. To check if an AD group exists, you can use the List AD Groups with Members API [here](#9-list-ad-groups-with-members-api).

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters**

-  **group_name** : (string) The name of the AD group.
-  **role_name** : (string) The role to be assigned to the group members.
-  **sAMAccountNames** : (list) A list of `sAMAccountNames` of the group members (optional for logging purposes).

**Example Request Body**

```json
{
    "group_name": "Developers",
    "role_name": "Admin",
    "sAMAccountNames": ["user1", "user2", "user3"]
}
```
## Response
**Successful Response (Status Code: `201`)**

-	**success** : (boolean) Indicates whether the role assignment was successful.
-	**message** : (string) A message indicating the result of the role assignment.

**Example Response Body**

```json
{
    "success": true,
    "message": "Roles assigned to members of Developers"
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

-	**success** : (boolean) Indicates the failure of the role assignment.
-	**message** : (string) Error message indicating validation errors or that the group does not exist.

**Example Response Body** 

```json
{
    "success": false,
    "message": "group_name, role_name, and sAMAccountNames are required."
}
```
or

```json
{
    "success": false,
    "message": "Group Developers does not exist"
}
```
**Internal Server Error (Status Code: `500`)**

-	**success** : (boolean) Indicates the failure of the role assignment.
-	**message** : (string) Error message indicating an internal server error.

**Example Response Body** 
```json
{
    "success": false,
    "message": "An unexpected error occurred"
}
```
**Method Not Allowed (Status Code: `405`)**

-	**success** : (boolean) Indicates the failure of the role assignment.
-	**message** : (string) Error message indicating that the request method is not allowed.

**Example Response Body** 

```json
{
    "success": false,
    "message": "Invalid request method"
}
````

## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/assign-role-group/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json" \
-d '{
    "group_name": "Developers",
    "role_name": "Admin",
    "sAMAccountNames": ["user1", "user2", "user3"]
}'
```
<hr>
<br>
<br>

# 14. Get AD Group Role API

This API retrieves the assigned role of a specified Active Directory (AD) group.

**URL** : `http://<your-domain>/api/v1/fetch-group-role/<str:group_name>/`

**Method** : `GET`

**Note** :
- Ensure that the specified AD group exists and has an assigned role. If the group does not exist or has no assigned role, appropriate error responses will be returned.

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required
- Only users with the Admin role can access this endpoint due to the IsAllowedRole permission class.

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

**URL  Parameter** :
- **group_name** : (string) The name of the AD group. This should be URL-encoded if it contains special characters..

## Response
**Successful Response (Status Code: `200`)**

- 	success: (boolean) Indicates whether the role retrieval was successful.
-	group_name: (string) The name of the AD group.
-	role_name: (string) The name of the role assigned to the AD group.

**Example Response Body**

```json
{
    "success": true,
    "group_name": "Developers",
    "role_name": "Admin"
}
```
## Error Response

**Not Found (Status Code:`404`)**
-	**success** : (boolean) Indicates the failure of the role retrieval.
-	**message** : (string) Error message indicating that no role is assigned to the specified group.

**Example Response Body**

```json
{
    "success": false,
    "message": "No role assigned to group Developers"
}
```

**Internal Server Error (Status Code:`500`)**
-	**success** : (boolean) Indicates the failure of the role retrieval.
-	**message** : (string) Error message indicating that no role is assigned to the specified group.

**Example Response Body**

```json
{
    "success": false,
    "message": "An unexpected error occurred."
}
```
## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/fetch-group-role/<str:group_name>/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 15. Ckeck Connection Status API

This API checks if the application is connected to the required services or systems and returns the connection status.

**URL** : `http://<your-domain>/api/v1/is-connected/`

**Method** : `GET`

**Note** :
- Ensure that the specified AD group exists and has an assigned role. If the group does not exist or has no assigned role, appropriate error responses will be returned.

## Request

**Headers** :
- **Content-Type** : `application/json`

## Response
**Successful Response (Status Code: `200`)**

- **is_connected** : (string) Indicates the connection status. This is retrieved from the `settings.IS_CONNECTED` attribute.

**Example Response Body**

```json
{
    "is_connected": "true"
}

```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/is-connected/ \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 16. Assign Roles to AD Group Members API

This API logs out the authenticated user by deleting their token. This effectively invalidates the user's session.

**URL** : `http://<your-domain>/api/v1/logout/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `201`)**

- **detail** : (string) A message indicating that the user has been successfully logged out.

**Example Response Body**

```json
{
    "detail": "Successfully logged out."
}
```

## Error Responses

**Authentication Errors (Status Code: `401`)**

-	**detail** : (string) Error message indicating authentication failure.

**Example Response Body** 

```json
{
    "detail": "Invalid token."
}
```

## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/logout/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>



<p align="center" style="font-size: 30px;">
  <b>API's of Provider1_api</b>
</p><br>

# 1. Add and Get Provider API

This API allows users to add and get the list of all added providers.

**URL** : `http://<your-domain>/api/v1/providers/`

**Method** : `POST` , `GET`

**Note** :
- You can add different-different providers using different-different parameters, like:- CloudStack, Kuberenetes, OpenStack, OpenShift [here](#all-providers-parameters).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters**

-	**provider_name** : (string) The name of the provider.
-	**key_name** : (string) The key name of the provider.
-	**provider_url** : (string) The URL of the provider.
-	**secret_key** : (string) The secret key of the provider.
-	**access_token** : (string) The access token of the provider.
-	**kubeconfig_data** : (string) The kubeconfig data of the provider.
-	**OpenstackUsername** : (string) The OpenStack username.
-	**tenant_name** : (string) The tenant name.
-	**OpenstackPassword** : (string) The OpenStack password.
-	**auth_url** : (string) The authentication URL.
-	**region** : (string) The region.
-	**OpenShift_username** : (string) The OpenShift username.
-	**OpenShift_password** : (string) The OpenShift password.
-	**api_url** : (string) The API URL.


**Example Request Body**

```json
{
    "provider_name": "ExampleProvider",
    "key_name": "exampleKey",
    "provider_url": "http://example.com",
    "secret_key": "secret123",
    "access_token": "token123",
    "kubeconfig_data": "kubeconfigData",
    "OpenstackUsername": "openstackUser",
    "tenant_name": "tenantName",
    "OpenstackPassword": "openstackPassword",
    "auth_url": "http://auth.url",
    "region": "region",
    "OpenShift_username": "openshiftUser",
    "OpenShift_password": "openshiftPassword",
    "api_url": "http://api.url"
}
```
## Response
**Successful Response (Status Code: `201`)**

-   **id** : (integer) The ID of the newly created provider.
-	**provider_name** : (string) The name of the provider.
-	**key_name** : (string) The key name of the provider.
-	**provider_url** : (string) The URL of the provider.
-	**secret_key** : (string) The secret key of the provider.
-	**access_token** : (string) The access token of the provider.
-	**kubeconfig_data** : (string) The kubeconfig data of the provider.
-	**openStackuser** : (string) The OpenStack username.
-	**tenant_name** : (string) The tenant name.
-	**openstackpassword** : (string) The OpenStack password.
-	**auth_url** : (string) The authentication URL.
-	**region** : (string) The region.
-	**OpenShift_username** : (string) The OpenShift username.
-	**OpenShift_password** : (string) The OpenShift password.
-	**api_url** : (string) The API URL.
-	**is_connected** : (boolean) Indicates if the provider is connected.


**Example Response Body**

```json
{
    "id": 1,
    "provider_name": "ExampleProvider",
    "key_name": "exampleKey",
    "provider_url": "http://example.com",
    "secret_key": "secret123",
    "access_token": "token123",
    "kubeconfig_data": "kubeconfigData",
    "openStackuser": "openstackUser",
    "tenant_name": "tenantName",
    "openstackpassword": "openstackPassword",
    "auth_url": "http://auth.url",
    "region": "region",
    "OpenShift_username": "openshiftUser",
    "OpenShift_password": "openshiftPassword",
    "api_url": "http://api.url",
    "is_connected": true
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "detail": "Invalid input data."
}
```
**Authentication Errors (Status Code: `401`)**
- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail" : "Invalid token."
}
```
## Example Usage

**cURL**
```json
curl -X POST http://<your-domain>/api/v1/providers/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token <your_token>" \
     -d '{
          "provider_name": "ExampleProvider",
          "key_name": "exampleKey",
          "provider_url": "http://example.com",
          "secret_key": "secret123",
          "access_token": "token123",
          "kubeconfig_data": "kubeconfigData",
          "OpenstackUsername": "openstackUser",
          "tenant_name": "tenantName",
          "OpenstackPassword": "openstackPassword",
          "auth_url": "http://auth.url",
          "region": "region",
          "OpenShift_username": "openshiftUser",
          "OpenShift_password": "openshiftPassword",
          "api_url": "http://api.url"
     }'
```

or 

```json
curl -X GET http://<your-domain>/api/v1/providers/ \
     -H "Authorization: Token <your_token>"
```

<hr>

## All Providers Parameters

**1. CloudStack Provider Body Parameters:** 
```json
{
    "provider_name": "CloudStack",
    "key_name": " ",
    "provider_url": "http://example.com",
    "secret_key": "exampleSecret",
    "access_token": "exampleAccessToken",
}
```
 
**2. Kubernetes Provider Body  Parameters:**
 
```json
{
    "provider_name": "Kubernetes",
    "key_name": " ",
    "kubeconfig_data": "exampleKubeconfigData",
}
```
 
 
**3. OpenStack Provider Body Parameters:**
 
```json
{
    "provider_name": "Openstack",
    "key_name": " ",
    "OpenstackUsername": "exampleOpenstackUsername",
    "tenant_name": "exampleTenantName",
    "OpenstackPassword": "exampleOpenstackPassword",
    "auth_url": "http://exampleAuthUrl.com",
    "region": "exampleRegion"
}
```

**4. OpenShift Provider Body Parameters:**
 
```json
{
    "provider_name": "OpenShift",
    "key_name": " ",
    "OpenShift_username": "exampleKubeconfigData",
    "OpenShift_password": "exampleKubeconfigData",
    "api_url": " ",
}
```
<hr>
<br>
<br>



# 2. Retrieve Providers by User ID  API

This API allows authenticated users to retrieve the list of connected providers associated with their user account.

**URL** : `http://<your-domain>/api/v1/providers/user-providers/`

**Method** : `GET`

**Note** :
- You can add different-different providers [here](#1-add-and-get-provider-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `201`)**

- **providers** : (list) A list of connected providers associated with the authenticated user.


**Example Response Body**

```json
[
    {
        "id": 1,
        "provider_name": "ExampleProvider1",
        "key_name": "exampleKey1",
        "provider_url": "http://example1.com",
        "secret_key": "secret123",
        "access_token": "token123",
        "kubeconfig_data": "kubeconfigData1",
        "openStackuser": "openstackUser1",
        "tenant_name": "tenantName1",
        "openstackpassword": "openstackPassword1",
        "auth_url": "http://auth1.url",
        "region": "region1",
        "OpenShift_username": "openshiftUser1",
        "OpenShift_password": "openshiftPassword1",
        "api_url": "http://api1.url",
        "is_connected": true
    }
]
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "detail": "Invalid input data."
}
```
**Authentication Errors (Status Code: `401`)**
- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail" : "Invalid token."
}
```

**Permission Error (Status Code: `403`)**

- **Detail** : (String) Error Message Indicating Permission Failure.

**Example Response Body**
```json
{
    "detail": "You do not have permission to perform this action."
}
```

## Example Usage

**cURL**

```json
curl -X GET http://<you-domain>/api/v1/providers/user-providers/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 3. Retrieve Providers by Provider Name  API

This API retrieves details of a provider based on the authenticated user and the provider name.

**URL** : `http://<your-domain>/api/v1/providers/by-username-and-name/{provider_name}/`

**Method** : `GET`

**Note** :
- You can add different-different providers [here](#1-add-and-get-provider-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters** :
- **provider_name** : (string) The name of the provider to fetch details.

## Response
**Successful Response (Status Code: `201`)**

- **providers** : (list)  A list of connected providers associated with the authenticated user the provider name.


**Example Response Body**

```json
{
    "id": 1,
    "user_id": 123,
    "provider_name": "Kubernetes",
    "Key_name": "example_key",
    "provider_url": "https://example.com",
    "secret_key": "example_secret",
    "access_token": "example_token",
    "kubeconfig_data": "example_kubeconfig",
    "openStackuser": "example_openstack_user",
    "tenant_name": "example_tenant",
    "openstackpassword": "example_openstack_password",
    "auth_url": "https://example-auth.com",
    "region": "example_region",
    "OpenShift_username": "example_openshift_user",
    "OpenShift_password": "example_openshift_password",
    "api_url": "https://example-api.com",
    "is_connected": true
}
```

## Error Responses

**Not Found (Status Code: `404`)**

- **error**: If no provider exists with the specified provider_name for the authenticated user.

**Example Response Body** 

```json
{
    "detail": "Not found."
}
```
**Unauthorized Error (Status Code: `401`)**
- **detail**: (String) If the request is not authenticated with a valid token.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```
## Example Usage

**cURL**

```json
curl -X GET http://172.16.1.190:8000/api/v1/providers/by-username-and-name/<provider_name>/ \
-H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>

# 4. Toggle Provider Status API

This API toggles the status (enabled/disabled) of a specified provider. It changes the `is_enabled` status of the provider and returns the updated status.

**URL** : `http://<your-domain>/api/v1/toggle-provider-status/<provider_id>/`

**Method** : `POST`

**Note** :
- You can add different-different providers [here](#1-add-and-get-provider-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters** :
- **provider_id** : (string) The ID of the provider whose status is to be toggled.

## Response
**Successful Response (Status Code: `200`)**

-	**provider_id** : (integer) The ID of the provider.
-	**is_enabled** : (boolean) The updated status of the provider (true if enabled, false if disabled).
-	**provider_name** : (string) The name of the provider.

**Example Response Body**

```json
{
    "provider_id": 123,
    "is_enabled": true,
    "provider_name": "Provider Name"
}
```

## Error Responses

**Provider Not Found (Status Code: `404`)**

- **error**: Error message indicating that the provider was not found.

**Example Response Body** 

```json
{
    "detail": "Not found."
}
```
**Permission Denied  (Status Code: `403`)**
- **detail**: Error message indicating that the user does not have permission to perform this action.

**Example Response Body** 
```json
{
    "detail": "You do not have permission to perform this action."
}
```
## Example Usage

**cURL**

```json
curl -X POST http://<your-domain>/api/v1/toggle-provider-status/<provider_id>/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>

# 5. Provider List View API

This API retrieves a list of all main providers.

**URL** : `http://<your-domain>/api/v1/provider-list/`

**Method** : `GET`

**Note** :
- You can add different-different providers [here](#1-add-and-get-provider-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters** :
- **provider_id** : (integer) The ID of the provider whose status is to be toggled.

## Response
**Successful Response (Status Code: `201`)**

-	id : (Integer) The ID of the provider.
-	provider_name : (String) The name of the provider.
-	key_name : (String) The key name associated with the provider.
-	provider_url : (String) The URL of the provider.
-	secret_key : (String) The secret key of the provider.
-	access_token : (String) The access token of the provider.
-	kubeconfig_data : (String) The kubeconfig data of the provider.
-	openStackuser : (String) The OpenStack username of the provider.
-	tenant_name : (String) The tenant name of the provider.
-	openstackpassword : (String) The OpenStack password of the provider.
-	auth_url : (String) The authentication URL of the provider.
-	region : (String) The region of the provider.
-	OpenShift_username : (String) The OpenShift username of the provider.
-	OpenShift_password : (String) The OpenShift password of the provider.
-	api_url : (String) The API URL of the provider.
-	is_connected : (Boolean) Indicates whether the provider is connected (true) or not (false).

**Example Response Body**

```json
[
    {
        "id": 1,
        "provider_name": "Main Provider 1",
        "key_name": "KeyName1",
        "provider_url": "http://example.com",
        "secret_key": "secret_key_value",
        "access_token": "access_token_value",
        "kubeconfig_data": "kubeconfig_data_value",
        "openStackuser": "openStackUsername",
        "tenant_name": "tenantName",
        "openstackpassword": "openstackPassword",
        "auth_url": "authUrl",
        "region": "region",
        "OpenShift_username": "OpenShiftUsername",
        "OpenShift_password": "OpenShiftPassword",
        "api_url": "apiUrl",
        "is_connected": true
    },
    {
        "id": 2,
        "provider_name": "Main Provider 2",
        "key_name": "KeyName2",
        "provider_url": "http://example.org",
        "secret_key": "secret_key_value_2",
        "access_token": "access_token_value_2",
        "kubeconfig_data": "kubeconfig_data_value_2",
        "openStackuser": "openStackUsername2",
        "tenant_name": "tenantName2",
        "openstackpassword": "openstackPassword2",
        "auth_url": "authUrl2",
        "region": "region2",
        "OpenShift_username": "OpenShiftUsername2",
        "OpenShift_password": "OpenShiftPassword2",
        "api_url": "apiUrl2",
        "is_connected": false
    }
    // Additional provider entries
]
```

## Error Responses

**Unauthorized Error (Status Code: `401`)**

- **error**: If the request is not authenticated with a valid token.

**Example Response Body** 

```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Forbidden Error (Status Code: `403`)**
- **detail**: (String) If the request is not authenticated with a valid token.

**Example Response Body** 
```json
{
    "detail": "You do not have permission to perform this action."
}
```
## Example Usage

**cURL**

```json
curl -X GET http://<your-domain>/api/v1/provider-list/ \
-H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>



<p align="center" style="font-size: 30px;">
  <b>API's of Project_api</b>
</p><br>


# 1. Project Get and Create API

This API allows authenticated users to create a new project. The request must include the project name.

**URL** : `http://<your-domain>/api/v1/project/`

**Method** : `POST`, `GET`

**Note** :
- Before creation of projects, users have to login [here](#4-user-login-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters** :
- **project_name** : (string) The name of the new project. This field is required.

**Example Request Body**
```json
{
    "project_name": "New Project"
}
```

## Response
**Successful Response (Status Code: `201`)**

-	**id** : (integer) The ID of the newly created project.
-	**project_name** : (string) The name of the newly created project.
-	**user** : (integer) The ID of the user who created the project.

**Example Response Body**

```json
{
    "id": 1,
    "project_name": "New Project",
    "user": 2
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "error": "Project name is required"
}
```
**Project Already Exists (Status Code: `400`)**

- **detail**: (string) Error message indicating that the project already exists.

**Example Response Body** 
```json
{
    "error": "Project already exists"
}
```

**Authentication Error (Status Code: `401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

{
    "detail": "Invalid token."
}


## Example Usage

**cURL**

```json
curl -X POST http://<your-domain>/api/v1/project/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json" \
-d '{
    "project_name": "New Project"
}'
```
<hr>
<br>
<br>

# 2. Project Rename API

This API allows authenticated users to rename an existing project. The request must include the new project name.

**URL** : `http://<your-domain>/api/v1/project/<project_id>/rename/`

**Method** : `PUT`

**Note** :
- A project must be created before it can be renamed. You can create a project using the Project Creation API [here](#1-project-get-and-create-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Path Parameters** :
- **project_id** : (integer) The ID of the project to be renamed. This is part of the URL.

**Body Parameters**

-	**new_project_name** : (string) The new name for the project. This field is required.

**Example Request Body**

```json
{
    "new_project_name": "Renamed Project"
}
```

## Response
**Successful Response (Status Code: `200`)**

-	**id** : (integer) The ID of the renamed project.
-	**project_name** : (string) The new name of the project.
-	**user** : (integer) The ID of the user who renamed the project.

**Example Response Body**

```json
{
    "id": 1,
    "project_name": "Renamed Project",
    "user": 2
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "error": "Project name is required"
}
```
**Project Already Exists (Status Code: `400`)**

- **detail**: (string) Error message indicating validation errors, such as missing new_project_name or project name already exists.

**Example Response Body** 
```json
{
    "error": "new_project_name is required"
}
```

or

```json
{
    "error": "Project with the new name already exists"
}
```

**Authentication Error (Status Code: `401`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "detail": "Invalid token."
}
```

## Example Usage

**cURL**

```json
curl -X PUT http://<your-domain>/api/v1/project/1/rename/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json" \
-d '{
    "new_project_name": "Renamed Project"
}'
```
<hr>
<br>
<br>


# 3. List Conpute Offerings API

This API allows authenticated users to retrieve a list of compute service offerings from an external service. The request to the external service is signed using an API key and a secret key.

**URL** : `http://<your-domain>/api/v1/compute_offerings/`

**Method** : `GET`

**Note** :
-	**Environment Variables** : Ensure the following environment variables are set:
-	**BASEURL** : The base URL of the external service.
-	**API_KEY** : The API key for accessing the external service.
-	**SECRET_KEY_ENCODED** : The encoded secret key for signing the request.


**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response

**Successful Response (Status Code: `200`)**

-	**compute_offerings** : (list) A list of compute service offerings, each containing:
-	**name** : (string) The name of the offering.
-	**cpunumber** : (integer) The number of CPUs.
-	**cpuspeed** : (integer) The CPU speed.
-	**memory** : (integer) The amount of memory.


**Example Response Body**

```json
{
    "compute_offerings": [
        {
            "name": "Standard",
            "cpunumber": 2,
            "cpuspeed": 2000,
            "memory": 4096
        },
        {
            "name": "High CPU",
            "cpunumber": 4,
            "cpuspeed": 2500,
            "memory": 8192
        }
    ]
}
```
## Error Response

**Error Fetching Offerings (Status Code:`500`)**

- **error** : (string) Error message indicating the failure reason.

**Example Response Body**

```json
{
 "error": "Error: Unable to fetch compute offerings."
}
```

or

```json
{
    "error": "Error: <detailed error message>"
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/compute_offerings/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 4. Flavor List API

This API allows authenticated users to retrieve a list of flavors from OpenStack. Each flavor includes details about RAM, virtual CPUs, disk space, and visibility.

**URL** : `http://<your-domain>/api/v1/flavors/`

**Method** : `GET`

**Note** :
**OpenStack Connection** : Ensure the following environment variables are set:
•	**AUTH_URL** : The authentication URL for OpenStack.
•	**PROJECT_NAME** : The name of the project in OpenStack.
•	**USERNAME** : The username for OpenStack authentication.
•	**PASSWORD** : The password for OpenStack authentication.
•	**USER_DOMAIN_NAME** : The user domain name in OpenStack.
•	**PROJECT_DOMAIN_NAME** : The project domain name in OpenStack.


**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response

**Successful Response (Status Code: `200`)**

A list of flavors, each containing:

-	**flavor_id** : (string) The ID of the flavor.
-	**name** : (string) The name of the flavor.
-	**ram** : (integer) The amount of RAM in MB.
-	**vcpus** : (integer) The number of virtual CPUs.
-	**disk** : (integer) The disk space in GB.
-	**is_public** : (boolean) Whether the flavor is public or not.


**Example Response Body**

```json
[
    {
        "flavors": {
            "flavor_id": "1",
            "name": "m1.tiny"
        },
        "ram": 512,
        "vcpus": 1,
        "disk": 1,
        "is_public": true
    },
    {
        "flavors": {
            "flavor_id": "2",
            "name": "m1.small"
        },
        "ram": 2048,
        "vcpus": 1,
        "disk": 20,
        "is_public": true
    }
]
```
## Error Response

**Error Fetching Flavors (Status Code:`500`)**

- **error** : (string) Error message indicating the failure reason.

**Example Response Body**

```json
{
    "error": "Error: Unable to connect to OpenStack."
}
```

or

```json
{
    "error": "Error: <detailed error message>"
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/flavors/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 5. Get Project By Users API

This API allows authenticated users to retrieve all projects associated with their account. Each project contains details about the project name, creation date, and other relevant information.

**URL** : `http://<your-domain>/api/v1/project/user/`

**Method** : `GET`

**Note** :
- Before get the project list, users have to create the projects [here](#1-project-get-and-create-api).


**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** :
- **Content-Type** : `application/json`
- **Authorization** : `Token <you_token>`

## Response

**Successful Response (Status Code: `200`)**

- A list of projects associated with the authenticated user.

**Example Response Body**

```json
[
    {
        "id": 1,
        "user": 1,
        "project_name": "Project A",
        "created_at": "2023-06-01T12:34:56Z",
        "updated_at": "2023-06-01T12:34:56Z"
    },
    {
        "id": 2,
        "user": 1,
        "project_name": "Project B",
        "created_at": "2023-06-15T09:12:34Z",
        "updated_at": "2023-06-15T09:12:34Z"
    }
]
```
## Error Response

**Unauthorized (Status Code:`401`)**

- **error** : (string) Error message indicating the user is not authenticated.

**Example Response Body**

```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Forbidden (Status Code:`403`)**

- **error** : : (string) Error message indicating the user does not have permission to access this endpoint.

**Example Response Body**

```json
{
    "detail": "You do not have permission to perform this action."
}
```

## Example Usage

**cURL**
```json
curl -X GET http://<your-domain>/api/v1/project/user/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>

# 6. Cluster Create and Get API

This API allows authenticated users to create a cluster and retrieve the list of all clusters.

**URL** : `http://<your-domain>/api/v1/cluster/`

**Method** : `POST`, `GET`

**Note** :
- Before creating a cluster, ensure that a project has been created using the [Project API](#1-project-get-and-create-api) and a provider has been added using the [Provider API](#1-add-and-get-provider-api).

- Users can use the [All Cluster Creation Parameters](#all-cluster-creation-parameters)

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters** :

-	**db_user** : (string) Database username.
-	**db_password** : (string) Database password.
-	**project** : (integer) ID of the project under which the cluster should be created.
-	**cluster_name** : (string) Name of the cluster.
-	**cluster_type** : (string) Type of the cluster (e.g., Standalone, Multiple).
-	**postgres_version** : (string) Version of PostgreSQL.
-	**backup_method** : (string) Backup method for the cluster.
-	**storageClass** : (string) Storage class (specific to OpenShift).
-	**size** : (string) Size of the cluster.
-	**flavor_id** : (string) Flavor ID (specific to CloudStack).
-	**computeOffering** : (string) Compute offering (specific to CloudStack).
-	**storageOffering** : (string) Storage offering (specific to CloudStack).
-	**mount_point** : (string) Mount point (specific to CloudStack).
-	**provider** : (string) Name of the provider associated with the cluster.


**Example Request Body**
```json
{
    "db_user": "example_user",
    "db_password": "example_password",
    "project": 1,
    "cluster_name": "example_cluster",
    "cluster_type": "Standalone",
    "postgres_version": "12.5",
    "backup_method": "pg_dump",
    "storageClass": "standard",
    "size": "medium",
    "flavor_id": "1234",
    "computeOffering": "standard",
    "storageOffering": "standard",
    "mount_point": "/mnt/data",
    "provider": "Kubernetes"
}
```

## Response
**Successful Response (Status Code: `201`)**

**Example Response Body**

```json
{
    "id": 1,
    "user": 1,
    "project": 1,
    "cluster_name": "example_cluster",
    "cluster_type": "Standalone",
    "postgres_version": "12.5",
    "backup_method": "pg_dump",
    "provider": "Kubernetes",
    "created_at": "2024-07-02T12:00:00Z",
    "updated_at": "2024-07-02T12:00:00Z"
}
```

## Error Responses

**Validation Errors (Status Code: `400`)**

- **error**: (string) Error message indicating validation errors.

**Example Response Body** 

```json
{
    "detail": "Invalid input data."
}
```
**Authentication Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail": "Invalid token."
}
```

**Not Found (Status Code: `404`)**

- **detail** : (string) Error message indicating authentication failure.

**Example Response Body**

```json
{
    "error": "User with the provided ID does not exist."
}
```
or

```json
{
    "error": "No Project! has been selected.."
}
```


## Example Usage

**cURL**

```json
curl -X POST http://<your-domain>/api/v1/clusters/ \
-H "Content-Type: application/json" \
-H "Authorization: Token <your_token>" \
-d '{
    "db_user": "example_user",
    "db_password": "example_password",
    "project": 1,
    "cluster_name": "example_cluster",
    "cluster_type": "Standalone",
    "postgres_version": "12.5",
    "backup_method": "pg_dump",
    "storageClass": "standard",
    "size": "medium",
    "flavor_id": "1234",
    "computeOffering": "standard",
    "storageOffering": "standard",
    "mount_point": "/mnt/data",
    "provider": "Kubernetes"
}'
```
or

```json
curl -X GET http://<your-domain>/api/v1/clusters/ \
     -H "Authorization: Token <your_token>"
```

<hr>

## All Cluster Creation Parameters

**1. CloudStack Cluster Creation Parameters:**

```json
{
    "db_user": "postgres",
    "db_password": "linux",
    "project": "14",
    "cluster_name": "testing-cluster-cloudstack",
    "cluster_type": "Standalone",
    "postgres_version": "15",
    "backup_method": "nfs",     // optional
    "provider": "Cloudstack",
    "computeOffering": "basic1-nested",
    "storageOffering": "2",
}
```

**2. Kubernetes Cluster Creation Parameters:** 

```json
{
    "db_user": "postgres",
    "db_password": "linux",
    "project": "14",
    "cluster_name": "testing-cluster-kubernetes",
    "cluster_type": "Standalone",
    "postgres_version": "15",
    "provider": "Kubernetes",
    "kubeconfig_data": " ",
    "backup_method": "nfs",     //optional

}
```


**3. OpenStack Cluster Creation Parameters:** 

```json
{
    "db_user": "postgres",
    "db_password": "linux",
    "project": "14",
    "cluster_name": "testing-cluster-OpenStack",
    "cluster_type": "Standalone",
    "postgres_version": "15",
    "backup_method": " ",
    "provider": "OpenStack",
    "openstackusername": " ",
    "openstackpassword": " ",
    "auth_url": " ",
    "region": "",
    "tenant_name": ""
}
```


**4. OpenShift Cluster Creation Parameters:** 

```json
{
    "db_user": "postgres",
    "db_password": "linux",
    "project": "14",
    "cluster_name": "testing-cluster-OpenShift",
    "cluster_type": "Standalone",
    "postgres_version": "15",
    "backup_method": " ",
    "provider": "OpenShift",
    "api_url": " ",
    "OpenShift_username": "",
    "OpenShift_password": "",   
    "storage_class": "",
    "size": ""
}
```
<hr>
<br>
<br>


# 7. Get Pipeline Status API

This API allows authenticated users to get the status and artifacts of the latest pipeline associated with their user ID.

**URL** : `http://<your-domain>/api/v1/get_pipeline_status/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters** :

-	**project_id** (integer) : The ID of the project.
-	**cluster_name** (string) : The name of the cluster.
-	**cluster_type** (string) : The type of the cluster (e.g., Standalone, Multiple).
-	**postgres_version** (string) : The version of PostgreSQL.
-	**provider_name** (string) : The name of the provider.


**Example Request Body**
```json
{
    "project_id": 1,
    "cluster_name": "ExampleCluster",
    "cluster_type": "Standalone",
    "postgres_version": "13",
    "provider_name": "ExampleProvider"
}
```

## Response
**Successful Response (Status Code: `200`)**

**Example Response Body**

```json
{
    "status": "success",
    "artifacts": "example_artifact_data"
}
```

## Error Responses

**Authentication Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http:// <your-domain>/api/v1/get_pipeline_status/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token" \
  -d '{
        "project_id": 1,
        "cluster_name": "ExampleCluster",
        "cluster_type": "Standalone",
        "postgres_version": "13",
        "provider_name": "ExampleProvider"
      }'
```
<hr>
<br>
<br>


# 8. Delete Pipeline Status API

This API allows authenticated users to get the status of the latest pipeline associated with their user ID and delete the pipeline record from the `pipeline_dict` if the pipeline status is either 'success' or 'failed'.

**URL** : `http://<your-domain>/api/v1/get_dele_pipeline_status/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

**Example Response Body**

```json
{
    "status": "success"
}
```

## Error Responses

**Authentication Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating authentication failure.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http:// <your-domain>/api/v1/get_dele_pipeline_status/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token"
```
<hr>
<br>
<br>


# 9. Get Clusters By Users API

This API allows authenticated users to retrieve all clusters associated with their user ID.

**URL** : `http://<your-domain>/api/v1/cluster/user/`

**Method** : `GET`

**Note** :
- Ensure that before getting the list of clusters by users, first users have create a [cluster](#6-cluster-create-and-get-api).

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

- A list of clusters associated with the authenticated user.

**Example Response Body**

```json
[
    {
        "id": 1,
        "user_id": 1,
        "project_id": 2,
        "cluster_name": "example_cluster",
        "cluster_type": "type_a",
        "database_version": "v1",
        "provider_name": "provider_x",
        "created_at": "2024-07-02T12:34:56Z"
    },
    ...
]
```

## Error Responses

**Unauthorized Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating the user is not authenticated.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Example Usage

**cURL**

```json
curl -X GET http://<your-domain>/api/v1/cluster/user/ \
-H "Authorization: Token <your-auth-token>" \
-H "Content-Type: application/json"
```
<hr>
<br>
<br>


# 10. Get Clusters By Projects API

This API allows authenticated users to retrieve all clusters associated with a specific project ID.

**URL** : `http://<your-domain>/api/v1/cluster/project/<int:project_id>/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

**Note** :
- Ensure that before getting the list of clusters by project, first users have create a [cluster](#6-cluster-create-and-get-api).

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Path Parameters**
- **project_id** : The ID of the project for which to retrieve clusters.

## Response
**Successful Response (Status Code: `200`)**

- A list of clusters associated with the authenticated user.

**Example Response Body**

```json
[
    {
        "id": 1,
        "user_id": 1,
        "project_id": 2,
        "cluster_name": "example_cluster",
        "cluster_type": "type_a",
        "database_version": "v1",
        "provider_name": "provider_x",
        "created_at": "2024-07-02T12:34:56Z"
    },
    ...
]
```

## Error Responses

**Unauthorized Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating the user is not authenticated.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Not Found (Status Code: `404`)**

**Example Response Body**

```json
{
    "error": "Not found"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  http://<your domain>/api/v1/cluster/project/<project-id>/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token"
```
<hr>
<br>
<br>


# 11. Get Cluster Content By Cluster Name API

This API allows authenticated users to retrieve all database credentials associated with a specific cluster name.

**URL** : `http://<your-domain>/api/v1/result/content/<str:cluster_name>/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

**Note** :
- Ensure that before getting the content or artifacts of clusters by cluster name, first users have create a [cluster].(#6-cluster-create-and-get-api)

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Path Parameters**
- **cluster_name** : The name of the cluster for which to retrieve database credentials.

## Response
**Successful Response (Status Code: `200`)**

- A list of clusters associated with the authenticated user.

**Example Response Body**

```json
[
    {
        "id": 1,
        "user_id": 1,
        "project_id": 2,
        "cluster_name": "example_cluster",
        "cluster_type": "type_a",
        "database_version": "v1",
        "provider_name": "provider_x",
        "created_at": "2024-07-02T12:34:56Z"
    },
    ...
]
```

## Error Responses

**Unauthorized Errors (Status Code: `401`)**

- **detail**: (string) Error message indicating the user is not authenticated.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Not Found (Status Code: `404`)**

**Example Response Body**

```json
{
    "error": "Not found"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  http://<your domain>/api/v1/result/content/<cluster_name> / \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token"
```
<hr>
<br>
<br>


# 12. Get Backup Method By Cluster Name API

This API allows authenticated users to retrieve the backup method associated with a specific cluster name.

**URL** : `http://<your-domain>/api/v1/get_backup_method/<str:cluster_name>/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

**Note** :
- Ensure that before getting the backup methods of clusters by cluster name, first users have create a [cluster].(#6-cluster-create-and-get-api)

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Path Parameters**
- **cluster_name** : The name of the cluster for which to retrieve the backup method.

## Response
**Successful Response (Status Code: `200`)**

- A list of clusters associated with the authenticated user.

**Example Response Body**

```json
{
    "backup_method": "method_name"
}
```

## Error Responses

**Unauthorized Errors (Status Code: `401`)**

- **detail**: (string)  Error message indicating the user is not authenticated.

**Example Response Body** 
```json
{
    "detail": "Authentication credentials were not provided."
}
```
**Not Found (Status Code: `404`)**

**Example Response Body**

```json
{
    "error": "Cluster not found"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  http://<your domain> /api/v1/get_backup_method/<cluster name>/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token"
```
<hr>
<br>
<br>


# 13. List Storage Classes API

This API retrieves a list of StorageClasses from an OpenShift cluster after authenticating with provided credentials.

**URL** : `http://<your-domain>/api/v1/list_storage_classes/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Body Parameters**

-	**api_url** : URL of the OpenShift API.
-	**OpenShift_username** : Username for authentication.
-	**OpenShift_password** : Password for authentication.

**Example Request Body**

```json
{
  "api_url": "https://openshift.example.com:6443",
  "OpenShift_username": "admin",
  "OpenShift_password": "password123"
}
```

## Response
**Successful Response (Status Code: `200`)**

- Returns a list of storage classes available in the OpenShift cluster.

**Example Response Body**

```json
[
  {
    "name": "standard"
  },
  {
    "name": "fast"
  }
]
```

## Error Responses

**Bad Request(Status Code: `400`)**

- **detail**: Invalid JSON in the request body.

**Example Response Body** 
```json
{
  "error": "Invalid JSON"
}
```
**Internal Server Error (Status Code: `500`)**

**detail** : Failed to login to OpenShift or any other unexpected error.

**Example Response Body**

```json
{
  "error": "Failed to login to OpenShift"
}
```

or

```json
{
  "error": "An unexpected error occurred"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http://<your-domain>/list_storage_classes/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "api_url": "https://openshift.example.com:6443",
    "OpenShift_username": "admin",
    "OpenShift_password": "password123"
  }'
```
<hr>
<br>
<br>

# 14. Kubernetes Storage Classes API

The `K8s_storage_classes` API allows authenticated users to retrieve a list of storage classes from a Kubernetes cluster.

**URL** : `http://<your-domain>/api/v1/k8s_storage_classes/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

Returns a list of storage classes available in the Kubernetes cluster.

**Body** : A JSON object containing a list of storage classes, with each storage class including the following fields:
-	**name** : The name of the storage class.
-	**provisioner** : The provisioner of the storage class.
-	**reclaim_policy** : The reclaim policy of the storage class.
-	**volume_binding_mode** : The volume binding mode of the storage class.
-	**allow_volume_expansion** : Indicates whether volume expansion is allowed.
-	**creation_timestamp** : The timestamp when the storage class was created.


**Example Response Body**

```json
{
  "storage_classes": [
    {
      "name": "standard",
      "provisioner": "k8s.io/minikube-hostpath",
      "reclaim_policy": "Delete",
      "volume_binding_mode": "Immediate",
      "allow_volume_expansion": true,
      "creation_timestamp": "2023-06-15T12:34:56Z"
    },
    {
      "name": "fast",
      "provisioner": "k8s.io/minikube-fast",
      "reclaim_policy": "Retain",
      "volume_binding_mode": "WaitForFirstConsumer",
      "allow_volume_expansion": false,
      "creation_timestamp": "2023-06-16T12:34:56Z"
    }
  ]
}
```

## Error Responses

**Internal Server Error (Status Code: `500`)**

**detail** : Any exception that occurs (e.g., Kubernetes configuration error).

**Example Response Body**

```json
{
  "error": "An error message describing the exception"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  http://<your-domain>/K8s_storage_classes/ \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>


# 15. Delete Clusters API

This API allows authenticated users to delete a cluster from the database and trigger a destroy pipeline.

**URL** : `http://<your-domain>/api/v1/delete-cluster/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

**Note** :
- Ensure that before Deleting the clusters, first users have create a [cluster](#6-cluster-create-and-get-api).

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Data**

The request must be a JSON object containing the following fields:
-	**cluster_name** : The name of the cluster to be deleted.
-	**provider_name** : The name of the provider associated with the cluster.

**Example Request Body**
```json
{
  "cluster_name": "example-cluster",
  "provider_name": "Kubernetes"
}
```

## Response
**Successful Response (Status Code: `200`)**

- Indicates that the destroy pipeline was triggered successfully and the cluster was deleted.

**Example Response Body**

```json
{
  "message": "Destroy pipeline triggered successfully."
}
```

## Error Responses

**Bad Request (Status Code: `404`)**

- **error**: The specified cluster or provider was not found.

**Example Response Body** 
```json
{
  "error": "Cluster not found."
}
```

or

```json
{
  "error": "Provider not found."
}
```

**Internal Server  Error (Status Code: `500`)**

- **detail** : Failed to trigger the destroy pipeline.

**Example Response Body**

```json
{
  "error": "Failed to trigger Destroy pipeline."
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http://<your-domain>/delete-cluster/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "cluster_name": "example-cluster",
    "provider_name": "Kubernetes"
  }'
```
<hr>
<br>
<br>

<p align="center" style="font-size: 30px;">
  <b>API's of ADSapp</b>
</p><br>


# 1. Update LDAP Settings API

This API allows authenticated and authorized users to update LDAP settings in the Django settings file.

**URL** : `http://<your-domain>/api/v1/update_ldap_settings/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Data**

The request must be a JSON object containing the following fields:
-	**ldapServerURI** : The URI of the LDAP server.
-	**ldapServerBIND_DN** : The bind DN for the LDAP server.
-	**ldapServerBIND_PASSWORD** : The bind password for the LDAP server.
-	**ldapGroupSearch** : The group search query for the LDAP server.
-	**True** : A flag to indicate if the connection is successful.

**Example Request Body**
```json
{
  "ldapServerURI": "ldap://example.com",
  "ldapServerBIND_DN": "cn=admin,dc=example,dc=com",
  "ldapServerBIND_PASSWORD": "password123",
  "ldapGroupSearch": "cn=groups,dc=example,dc=com",
  "True": "True"
}
```

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the LDAP settings were updated successfully.

**Example Response Body**

```json
{
  "message": "LDAP settings updated successfully"
}
```

## Error Responses

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while updating the LDAP settings.

**Example Response Body** 
```json
{
  "error": "An error message describing the exception"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http://<your-domain>/update_ldap_settings/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "ldapServerURI": "ldap://example.com",
    "ldapServerBIND_DN": "cn=admin,dc=example,dc=com",
    "ldapServerBIND_PASSWORD": "password123",
    "ldapGroupSearch": "cn=groups,dc=example,dc=com",
    "True": "True"
  }'
```
<hr>
<br>
<br>

# 2. Reset LDAP Settings API

This API allows authenticated users to reset LDAP settings in the Django settings file by clearing the relevant variables.

**URL** : `http://<your-domain>/api/v1/reset_ldap_settings/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the LDAP settings were disabled successfully.

**Example Response Body**

```json
{
  "message": "LDAP settings disabled successfully"
}
```

## Error Responses

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while resetting the LDAP settings.

**Example Response Body** 
```json
{
  "error": "An error message describing the exception"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  http://<your-domain>/reset_ldap_settings/ \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>

# 3. Get AD Users API

This API allows authenticated users with a specific role to retrieve usernames from an Active Directory (AD) server using LDAP.

**URL** : `http://<your-domain>/api/v1/ad-users/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required
- **IsAllowedRole** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the AD users' usernames were retrieved successfully.

**Example Response Body**

```json
{
  "user_names": [
    "user1",
    "user2",
    "user3"
  ]
}
```

## Error Responses

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while retrieving the AD users.

**Example Response Body** 
```json
{
  "error": "An error message describing the exception"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  http://<your-domain>/ad-users/ \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>


<p align="center" style="font-size: 30px;">
  <b>API's of Backup_app</b>
</p><br>

# 1. Check Server Status API

This API allows authenticated users to check the status of a server using Barman, a backup and recovery manager for PostgreSQL databases.

**URL** : `http://<your-domain>/api/v1/barman/check`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Query Parameters**

-	**server_name** : The name of the server to check.
-	**storage_method** : The storage method used by Barman.
-	**username** : The username of the authenticated user.

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the server was successfully checked.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Server is online and accessible.",
  "details": "Additional details about the server status."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: if `server_name` is not provided.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Server name is required."
}
```

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while checking the server status.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "An error occurred while checking server status."
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  'http://<your-domain>/barman/check/?server_name=my-server&storage_method=my-storage' \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>


# 2. List Servers API

This API allows authenticated users to list servers managed by Barman, a backup and recovery manager for PostgreSQL databases, based on a specified storage method.

**URL** : `http://<your-domain>/api/v1/barman/list-servers`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Query Parameters**

-	**storage_method** : The storage method used by Barman to filter servers.
-	**username** : The username of the authenticated user.


## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the list of Barman servers was retrieved successfully.

**Example Response Body**

```json
{
  "servers": [
    "server1",
    "server2",
    "server3"
  ]
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: if `storage_method` is not provided.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Storage method is required."
} 
```

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while listing servers.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "An error occurred while checking server status."
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  'http://<your-domain>/barman/list-servers/?storage_method=my-storage' \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>


# 3. List Backups API

This api allows authenticated users to list backups managed by Barman for a specific server, based on a specified storage method.

**URL** : `http://<your-domain>/api/v1/barman/list-backups`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Query Parameters**

-	**server_name** : The name of the server for which backups are to be listed.
-	**storage_method** : The storage method used by Barman to filter backups.
-	**username** : The username of the authenticated user.

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the list of Barman backups was retrieved successfully.

**Example Response Body**

```json
{
  "backups": [
    {
      "name": "backup1",
      "timestamp": "2023-01-01T12:00:00Z",
      "size": "1.5GB"
    },
    {
      "name": "backup2",
      "timestamp": "2023-01-02T12:00:00Z",
      "size": "2.0GB"
    }
  ]
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: if `server_name` is not provided.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Server name is required."
} 
```

**Internal Server Error (Status Code: `500`)**

- **error**: An error occurred while listing Barman backups.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "An error occurred while listing Barman backups."
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  'http://<your-domain>/barman/list-backups/?server_name=my-server&storage_method=my-storage' \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>

# 4. Create Backups API

This API allows authenticated users to create a backup for a specified server managed by Barman, with optional configurations for retention policy.

**URL** : `http://<your-domain>/api/v1/barman/backup`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Query Parameters**

-	**server_name** : The name of the server to be backed up.
-	**backup_name** (optional) : The name to assign to the backup.
-	**storage_method** : The storage method used by Barman to store backups.
-	**username** : The username of the authenticated user.
-	**retention** : Optional retention policy for the backup, specified as a string with values like "7d", "1m", "1y", where d denotes days, m denotes months, and y denotes years.

## Response
**Successful Response (Status Code: `200`)**

- **success** : Successfully created the backup.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Backup created successfully."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: if `server_name` is not provided.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Server name is required."
} 
```

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/backup/?server_name=my-server&backup_name=my-backup&storage_method=my-storage&retention=7d%0A1m%0A-1' \
  -H "Authorization: Token <your-token>"
```
<hr>
<br>
<br>


# 5. Add Server Config API

This API allows authenticated users to add a server configuration for Barman, including SSH connection details, database credentials, and storage method.

**URL** : `http://<your-domain>/api/v1/barman/add-server`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**server_name** : The name of the server to configure.
-	**ssh_host** : The SSH hostname or IP address of the server.
-	**db_name** : The name of the database managed by Barman.
-	**db_pass** : The password for the database user (barman).
-	**ssh_key** : The SSH key for connecting to the server.
-	**storage_method** : The storage method used by Barman to store backups.
-	**username** : The username of the authenticated user.


## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the server configuration file and necessary settings were successfully created.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Configuration file created for my-server"
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If any required parameters `(server_name, ssh_host, db_name, db_pass, ssh_key, storage_method)` are missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "All parameters are required."
} 
```
**Internal Server Error (Status Code: `500`)**

- **error** : An error occurred while creating the server configuration.

**Example Response Body**

{
  "status": "error",
  "message": "An error occurred while creating the configuration file."
}


## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/add-server/' \
  -H 'Authorization: Token <your-token>' \
  -d 'server_name=my-server&ssh_host=example.com&db_name=mydb&db_pass=mypassword&ssh_key=ssh-rsa ABCD1234...&storage_method=rsync'
```
<hr>
<br>
<br>



# 6. Recover Backup API

This API allows authenticated users to recover a backup using Barman. It requires specifying the server name, backup ID, destination directory, and target server name for recovery.

**URL** : `http://<your-domain>/api/v1/barman/recover`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**server_name** : The name of the Barman server from which to recover the backup.
-	**backup_id** : The ID or name of the backup to be recovered.
-	**destination_directory** : The directory where the recovered backup will be placed.
-	**target_server_name** : The name or IP address of the target server where the recovery will take place.
-	**storage_method** : The storage method used by Barman to store backups.
-	**username** : The username of the authenticated user.



## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the recovery command was successfully executed.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Recovery process initiated."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If any required parameters `(server_name, backup_id, destination_directory, target_server_name)` are missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "All parameters are required."
} 
```
**Internal Server Error (Status Code: `500`)**

- **error** : An error occurred during the recovery process.

**Example Response Body**

{
  "status": "error",
  "message": "An error occurred during backup recovery."
}


## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/recover/' \
  -H 'Authorization: Token <your-token>' \
  -d 'server_name=my-server&backup_id=backup1&destination_directory=/restore_dir&target_server_name=target-server&storage_method=rsync'
```
<hr>
<br>
<br>


# 7. Switch Wal API

This API allows allows authenticated users to force a WAL (Write-Ahead Log) switch and archive the WAL file for a specified Barman server.

**URL** : `http://<your-domain>/api/v1/barman/switch-wal`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**server_name** : The name of the Barman server for which to switch and archive the WAL file.
-	**storage_method** : The storage method used by Barman.
-	**username** : The username of the authenticated user.


## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the WAL switch command was successfully executed.

**Example Response Body**

```json
{
  "status": "success",
  "message": "WAL switch executed successfully."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If the required parameter `server_name` is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Server name is required."
} 
```
**Internal Server Error (Status Code: `500`)**

- **error** : An error occurred during the WAL switch process.

**Example Response Body**

{
  "status": "error",
  "message": "An error occurred during WAL switch."
}

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/switch-wal/' \
  -H 'Authorization: Token <your-token>' \
  -d 'server_name=my-server&storage_method=rsync'
```
<hr>
<br>
<br>



# 8. Schedule Backup API

This API allows authenticated users to schedule a backup for a specified Barman server. The backup schedule can be configured with specific retention policies and scheduled to run at specified times.

**URL** : `http://<your-domain>/api/v1/barman/schedule-backup`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**server_name** (string) : The name of the Barman server for which to schedule the backup (required).
-	**storage_method** (string) : The storage method used by Barman (required).
-	**retention** (string) : Retention policies, each specified on a new line (required).
-	**schedule_hour** (string) : The hour at which to schedule the backup (default is '0' if not provided).
-	**schedule_minute** (string) : The minute at which to schedule the backup (default is '0' if not provided).
-	**schedule_day** (string) : The day of the week or day of the month to schedule the backup (optional).

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the backup was successfully scheduled.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Backup scheduled for my-server"
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If the required parameter is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "All parameters are required."
} 
```
**Internal Server Error (Status Code: `500`)**

- **error** : If a cron job already exists for the specified server or any other error occurs during scheduling.

**Example Response Body**

{
  "status": "error",
  "message": "A cron job already exists for server 'my-server'."
}

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/schedule-backup/' \
  -H 'Authorization: Token <your-token>' \
  -d 'server_name=my-server&storage_method=rsync&retention=7d\n30d\n365d&schedule_hour=2&schedule_minute=30&schedule_day=Sunday'
```
<hr>
<br>
<br>


# 9. Update Schedule API

This API allows authenticated users to update the schedule and retention policies of an existing backup for a specified Barman server. Users can also remove the scheduled backup.

**URL** : `http://<your-domain>/api/v1/barman/update-scheduled-backups`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**server_name** (string) : The name of the Barman server for which to schedule the backup (required).
-	**storage_method** (string) : The storage method used by Barman (required).
-	**retention** (string) : Retention policies, each specified on a new line (required).
-	**schedule_hour** (string) : The hour at which to schedule the backup (default is '0' if not provided).
-	**schedule_minute** (string) : The minute at which to schedule the backup (default is '0' if not provided).
-	**schedule_day** (string) : The day of the week or day of the month to schedule the backup (optional).

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the scheduled backup was successfully updated or removed.

**Example Response Body**

```json
{
  "status": "success",
  "message": "Scheduled backup removed successfully."
}
```

or

```json
{
  "status": "success",
  "message": "Retention period updated successfully."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If the required parameter is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Server name and storage method are required."
} 
```
**Internal Server Error (Status Code: `500`)**

- **error** : If any error occurs during the update process.

**Example Response Body**

```json
{
  "status": "error",
  "message": "An error message"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/update-scheduled-backups/' \
  -H 'Authorization: Token <your-token>' \
  -d 'server_name=my-server&storage_method=rsync&retention=7d\n30d\n365d&schedule_hour=2&schedule_minute=30&schedule_day=Sunday'
```
<hr>
<br>
<br>


# 10. Get Scheduled Servers API

This API allows allows authenticated users to retrieve a list of Barman servers with scheduled backups, along with their retention periods and scheduled times.

**URL** : `http://<your-domain>/api/v1/barman/get-scheduled-servers/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**storage_method** (string) : The storage method used by Barman (required).

## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the scheduled servers were successfully retrieved.

**Example Response Body**

```json
{
  "status": "success",
  "message": [
    {
      "server_name": "my-server",
      "retention_period": "7 DAYS",
      "scheduled_time": "30 2 * * 0"
    },
    {
      "server_name": "another-server",
      "retention_period": "30 DAYS",
      "scheduled_time": "0 0 * * 0"
    }
  ]
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If the required parameter `storage_method` is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Storage method is required."
}
```
**Internal Server Error (Status Code: `500`)**

- **error** : If any error occurs during the retrieval process.

**Example Response Body**

```json
{
  "status": "error",
  "message": "An error message"
}
```

## Example Usage

**cURL**

```json
curl -X GET \
  'http://<your-domain>/barman/get-scheduled-servers/?storage_method=rsync' \
  -H 'Authorization: Token <your-token>'
```
<hr>
<br>
<br>


# 11. Add NFS Mount API

This API allows allows authenticated users to mount a remote NFS (Network File System) directory to a local path on the server and update the Barman configuration accordingly.

**URL** : `http://<your-domain>/api/v1/barman/mount-nfs/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**remote_host** (string, required): The remote NFS host.
-	**remote_path** (string, required): The remote NFS path.
-	**username** (inferred from authentication): The authenticated user's username.


## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the NFS mount point was successfully added and the entry was added to /etc/fstab.

**Example Response Body**

```json
{
  "message": "NFS mount point /var/lib/barman/nfs/<username> added successfully and entry added to /etc/fstab",
  "status": "success"
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If any required parameter (`remote_host, remote_path, username`) is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "All parameters are required."
}
```
**Internal Server Error (Status Code: `500`)**

- **error** : If any error occurs during the NFS mount process.

**Example Response Body**

```json
{
  "error": "An error message"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/mount-nfs/?remote_host=remote.example.com&remote_path=/remote/path' \
  -H 'Authorization: Token <your-token>'
```
<hr>
<br>
<br>


# 12. Mount S3 Bucket API

This API allows authenticated users to mount an S3 bucket to a local path on the server and update the Barman configuration accordingly.

**URL** : `http://<your-domain>/api/v1/barman/mount-s3/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**bucket_name** (string, required): The name of the S3 bucket.
-	**access_key** (string, required): The access key for the S3 bucket.
-	**secret_key** (string, required): The secret key for the S3 bucket.
-	**url** (string, required): The URL endpoint for the S3 service.
-	**username** (inferred from authentication): The authenticated user's username.


## Response
**Successful Response (Status Code: `200`)**

- **success** : Indicates that the S3 bucket was successfully mounted and the Barman configuration was updated

**Example Response Body**

```json
{
  "message": "S3 bucket <bucket_name> mounted successfully",
  "status": "success"
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

- **error**: If any required parameter (`bucket_name, access_key, secret_key, url, username`) is missing.

**Example Response Body** 
```json
{
  "status": "error",
  "message": "All parameters are required."
}
```
**Internal Server Error (Status Code: `500`)**

- **error** : If any error occurs during the S3 bucket mounting process.

**Example Response Body**

```json
{
  "error": "An error message"
}
```

## Example Usage

**cURL**

```json
curl -X POST \
  'http://<your-domain>/barman/mount-s3/?bucket_name=my-bucket&access_key=my-access-key&secret_key=my-secret-key&url=https://s3.amazonaws.com' \
  -H 'Authorization: Token <your-token>'
```
<hr>
<br>
<br>


# 13. List Mount Points API

This API retrieves the list of NFS and S3 mount points for the authenticated user.

**URL** : `http://<your-domain>/api/v1/barman/list-mount-points/`

**Method** : `GET`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

## Response
**Successful Response (Status Code: `200`)**

**Example Response Body**

```json
{
  "status": "success",
  "nfs_mount_points": [
    {
      "host_path": "remote_host:remote_path",
      "mount_point": "/var/lib/barman/nfs/username"
    },
    ...
  ],
  "s3_mount_points": [
    {
      "access_key": "your_access_key",
      "secret_key": "your_secret_key",
      "mount_point": "/var/lib/barman/s3/username"
    }
  ]
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Invalid Username."
}
```
**Internal Server Error (Status Code: `500`)**

**Example Response Body**

```json
{
  "status": "error",
  "message": "Error message"
}
```

## Example Usage

**cURL**

```json
curl -X GET "http://your-domain.com/barman/list-mount-points" \
     -H "Authorization: Token your_auth_token"
```
<hr>
<br>
<br>


# 14. Unmount API

This unmounts a specified storage (NFS or S3) for the authenticated user.

**URL** : `http://<your-domain>/api/v1/barman/unmount/`

**Method** : `POST`

**Permissions** :
- **IsAuthenticated** : Required

## Request

**Headers** : 
- **Content-Type** : `application/json`
- **Authorization** : `Token <your_token>`

**Request Parameters**

-	**bucket_name** (string, required): The name of the S3 bucket.
-	**access_key** (string, required): The access key for the S3 bucket.
-	**secret_key** (string, required): The secret key for the S3 bucket.
-	**url** (string, required): The URL endpoint for the S3 service.
-	**username** (inferred from authentication): The authenticated user's username.


## Response
**Successful Response (Status Code: `200`)**

**Example Response Body**

```json
{
  "status": "success",
  "message": "/var/lib/barman/nfs/<username> unmounted successfully."
}
```

## Error Responses

**Bad Request (Status Code: `400`)**

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Invalid parameters."
}
```
**Not Found (Status Code: `404`)**

**Example Response Body** 
```json
{
  "status": "error",
  "message": "Mount point not found."
}
```

**Internal Server Error (Status Code: `500`)**

**Example Response Body**

```json
{
  "status": "error",
  "message": "<error_message>"
}
```

## Example Usage

**cURL**

```json
curl -X POST "http://<your-django-server>/barman/unmount" \
     -H "Authorization: Token <your-auth-token>" \
     -d "storage_method=nfs"
```
<hr>
<br>
<br>