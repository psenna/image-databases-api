import os
from api_client import ApiClient

user_mail = os.getenv('USER_MAIL', 'admin@mail.com')

dataset_directory = os.getenv('DATASET_DIRECTORY', './example')

user_password = os.getenv('USER_PASSWORD', 'admin')

api_url = os.getenv('API_URL', 'http://127.0.0.1:5000')


dataset_name = os.getenv('DATASET_NAME', 'gorgeous_dataset')

api_client = ApiClient(api_url)

api_client.login(user_mail, user_password)

directory_list = os.listdir(dataset_directory)

dataset_id = api_client.create_dataset(dataset_name)

labels = []

for directory in directory_list:
    # Para todas as pastas no diretório
    if os.path.isdir(os.path.join(dataset_directory,directory)):
        directory_full_path = os.path.join(dataset_directory,directory)
        label_id = api_client.create_label(directory)
        labels.append(directory)
        files_list = os.listdir(directory_full_path)
        for file in files_list:
            api_client.upload_image(
                os.path.join(directory_full_path, file), 
                dataset_id=dataset_id, 
                label_id=label_id)

print("Resumo do upload")
total = 0
for label in labels:
    n = api_client.get_number_images_per_label_in_dataset(label, dataset_name)
    total += n
    print(f"{label}: {n}")
print(f"Total: {total}")

