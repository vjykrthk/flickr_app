# flickr_app

### Installation instruction
```
git clone git@github.com:vjykrthk/flickr_app.git
cd to flick_app folder
pip install -r requirements.txt
```
### Run the application
```
python manage.py runserver
```
### End points descriptions
#### Login curl command
```
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/login/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "karthik",
	"password": "karthik"
}'
```
#### Login Sample Response
```
{"key":"a802042d0c75e7e8564e044a755e6042f1672808"}
```
The 'key' in the response is the token.
#### Get list of groups curl command
```
curl --request GET \
  --url http://127.0.0.1:8000/api/v1/groups/ \
  --header 'authorization: Token a802042d0c75e7e8564e044a755e6042f1672808' \
```
#### Get group detail curl command
```
curl --request GET \
  --url 'http://127.0.0.1:8000/api/v1/groups/1/?page=1' \
  --header 'authorization: Token a802042d0c75e7e8564e044a755e6042f1672808'
```
#### Get photos list curl command
```
curl --request GET \
  --url 'http://127.0.0.1:8000/api/v1/photos/?group=4&page2' \
  --header 'authorization: Token a802042d0c75e7e8564e044a755e6042f1672808'
```
#### Get photo detail curl command
```
curl --request GET \
--url http://127.0.0.1:8000/api/v1/photos/34/ \
--header 'authorization: Token a802042d0c75e7e8564e044a755e6042f1672808'
```
#### Logout curl command
```
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/logout/ \
  --header 'authorization: Token a802042d0c75e7e8564e044a755e6042f1672808' \
```
