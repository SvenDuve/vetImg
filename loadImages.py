import labelbox
from uuid import uuid4 ## to generate unique IDs


    
client = labelbox.Client(api_key=API_KEY)

dataset = client.create_dataset(name="google_tesdrive_2")

assets = [{"row_data": "gs://labelbox-vet-dataset/1000000.jpg", "external_id": str(uuid4())},
            {"row_data": "gs://labelbox-vet-dataset/1000002.jpg", "external_id": str(uuid4())}]

task = dataset.create_data_rows(assets)
task.wait_till_done()




if __name__ == '__main__':
    main(name, assets)


