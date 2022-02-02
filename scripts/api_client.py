import base64
import urllib3
import json
import orjson


class ApiClient:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url
        self.token_header = ''
        self.http = urllib3.PoolManager()


    def login(self, username: str, password: str)->None:
        r = self.http.request('POST', 
            self.api_url+'/users/auth-token',
            fields={"username": username, "password": password})
        if r.status != 200:
            print("Erro de login")
            exit()
        self.token_header = {"Authorization": "Bearer " + json.loads(r.data.decode('utf-8'))['access_token']}

    def create_dataset(self, dataset_name: str) -> int:
        encoded_body = orjson.dumps({
            "name": dataset_name
        })

        r = self.http.request('POST', 
            self.api_url+'/datasets/',
            headers=self.token_header,
            body=encoded_body)

        if r.status != 200:
            print(f"Erro ao criar o dataset {dataset_name}")
            return 0

        dataset_id = json.loads(r.data.decode('utf-8'))['id']
        return dataset_id

    def create_label(self, label_name: str) -> int:
        encoded_body = orjson.dumps({
            "name": label_name
        })

        r = self.http.request('POST', 
            self.api_url+'/labels/',
            headers=self.token_header,
            body=encoded_body)

        if r.status != 200:
            print(f"Erro ao criar a label {label_name}")
            return 0

        label_id = json.loads(r.data.decode('utf-8'))['id']
        return label_id

    def get_number_images_per_label_in_dataset(self, label_name: str, dataset_name: str) -> int:
        r = self.http.request('GET', 
            self.api_url+f'/images/?label_name={label_name}&dataset_name={dataset_name}',
            headers=self.token_header)

        if r.status != 200:
            print(f"Erro")
            return -1

        return json.loads(r.data.decode('utf-8'))['total']

    def upload_image(self, image_path: str, dataset_id: int, label_id: int = 0)->None:
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode('ascii')
            image_name  = f.name.split('/')[-1]
        
        encoded_body = orjson.dumps({
                "name": image_name,
                "dataset": dataset_id,
                "data": image_data
                })
        r = self.http.request('POST', 
            self.api_url+'/images/',
            headers=self.token_header,
            body=encoded_body)

        if r.status != 200:
            print(f"Erro ao enviar a imagem {image_path}")
            return

        image_id = json.loads(r.data.decode('utf-8'))['id']

        if label_id:
            r = self.http.request('POST',
                    self.api_url+f'/images/{image_id}/labels/{label_id}',
                    headers=self.token_header)
        
        if r.status != 200:
            print(f"Erro ao atribuir a label na imagem {image_path}")
            return