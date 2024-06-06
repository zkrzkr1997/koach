### Register

* Endpoint path: /register
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response shape (JSON):
    ```json
    {"message": "User registered successfully"}


### Login

* Endpoint path: /login
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response shape (JSON):
    ```json
    {"message": "Login successful"}


### Translate

* Endpoint path: /translate
* Endpoint method: POST

* Request shape (form):
  * text: string

* Response shape (JSON):
    ```json
    {
        "message": "Translation successful",
        "translated_text": translated_text
    }
