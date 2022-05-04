import labelbox
from uuid import uuid4 ## to generate unique IDs


    
export LABELBOX_API_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja2xtOGJ3ZnZwN3FmMDc3OXQ5cWhkc3pxIiwib3JnYW5pemF0aW9uSWQiOiJja2xtOGJ3ZjZhYnRsMDczOTZzandyNWEyIiwiYXBpS2V5SWQiOiJjbDJvaTJjbXdjcjA5MHphZTNvaW0zZWNpIiwic2VjcmV0IjoiNjEzMWQzNDU5NTM4YjVjOTIyMjhmM2FkOWYyNzNjZTAiLCJpYXQiOjE2NTE0ODI1NDEsImV4cCI6MjI4MjYzNDU0MX0.3SU12_8bDTZaF9i2b58Vk8QjvcL06QkQA0W3Gw5gAlQ"
python3    

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja2xtOGJ3ZnZwN3FmMDc3OXQ5cWhkc3pxIiwib3JnYW5pemF0aW9uSWQiOiJja2xtOGJ3ZjZhYnRsMDczOTZzandyNWEyIiwiYXBpS2V5SWQiOiJjbDJvaTJjbXdjcjA5MHphZTNvaW0zZWNpIiwic2VjcmV0IjoiNjEzMWQzNDU5NTM4YjVjOTIyMjhmM2FkOWYyNzNjZTAiLCJpYXQiOjE2NTE0ODI1NDEsImV4cCI6MjI4MjYzNDU0MX0.3SU12_8bDTZaF9i2b58Vk8QjvcL06QkQA0W3Gw5gAlQ"
client = labelbox.Client(api_key=API_KEY)

dataset = client.create_dataset(name="google_tesdrive_2")

assets = [{"row_data": "gs://labelbox-vet-dataset/1000000.jpg", "external_id": str(uuid4())},
            {"row_data": "gs://labelbox-vet-dataset/1000002.jpg", "external_id": str(uuid4())}]

task = dataset.create_data_rows(assets)
task.wait_till_done()




if __name__ == '__main__':
    main(name, assets)


