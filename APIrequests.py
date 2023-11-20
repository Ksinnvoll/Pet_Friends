import requests

#Pet requests
data = {
  "id": 111,
  "category": {
    "id": 111,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 111,
      "name": "string"
    }
  ],
  "status": "available"
}
res_add_pet = requests.post(f'https://petstore.swagger.io/v2/pet?data={data}',
                            headers={'accept':'application/json', 'Content-Type': 'application/json'},
                            json=data)      #Add new pet
print(f'Добавление нового питомца. Ответ сервера: {res_add_pet.status_code}')

res_upload_image = requests.post(f'https://petstore.swagger.io/v2/pet/111/uploadImage',
                                 headers={'accept':'application/json', 'Content-Type':'multipart/form-data',},
                                 data='file')
print(f'Добавление изображения. Ответ сервера: {res_upload_image.status_code}')

res_update = requests.put(f'https://petstore.swagger.io/v2/pet?data={data}',
                          headers={'accept':'application/json', 'Content-Type': 'application/json'},
                          json=data)        #Update pet
print(f'Изменение данных о питомце. Ответ сервера: {res_update.status_code}')

status = 'available'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept':'application/json'})       #Find pets by status
print(f'Отображение питомцев по статусу. Ответ сервера: {res.status_code}')


res_ID = requests.get(f'https://petstore.swagger.io/#/pet/getPetById?petId=id',
                   headers={'accept':'application/json'})       #Find pet by ID
print(f'Нахождение питомца по ID. Ответ сервера: {res_ID.status_code}')

api_key = '112233'
res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/111',
                             headers={'accept':'application/json','api_key':'api_key'})     #Delete pet
print(f'Удаление питомца. Ответ сервера: {res_delete.status_code}')

#Store requests
orderID = 'orderID'
res_orderID = requests.get(f'https://petstore.swagger.io/#/store/getOrderById?orderID={orderID}',
                   headers={'accept':'application/json'})      #Find purchase order by ID
print(f'Поиск заказа по ID. Ответ сервера: {res_orderID.status_code}')

order_data = {
  "id": 123,
  "petId": 111,
  "quantity": 0,
  "shipDate": "2023-05-31T09:13:09.181Z",
  "status": "placed",
  "complete": True
}
res_new_order = requests.post(f'https://petstore.swagger.io/v2/store/order',
                              headers={'accept':'application/json', 'Content-Type': 'application/json'},
                              json=order_data)      #New order
print(f'Новый заказ. Ответ сервера: {res_new_order.status_code}')

res_delete_order = requests.delete(f'https://petstore.swagger.io/v2/store/order/123',
                                   headers={'accept':'application/json'})       #Delete order
print(f'Удаление заказа. Ответ сервера: {res_delete_order.status_code}')

#User requests
username = 'username'
res_get_username = requests.get(f'https://petstore.swagger.io/#/user/getUserByName?username={username}')
        #Get user by Username
print(f'Поиск пользователя. Ответ сервера: {res_get_username.status_code}')

user_data = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
}
res_new_user = requests.post(f'https://petstore.swagger.io/v2/user',
                             headers={'accept':'application/json', 'Content-Type': 'application/json'},
                             json=user_data)        #Create new user
print(f'Добавление нового пользователя. Ответ сервера: {res_new_user.status_code}')



