from google.cloud import storage
from google.oauth2 import service_account

# Path to your service account key file
service_account_key_path = 'key.json'

# Initialize a GCS client with the service account
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
client = storage.Client(credentials=credentials, project=credentials.project_id)

# Define your bucket name
bucket_name = 'akshay-akshay-ak'
bucket = client.get_bucket(bucket_name)

# List objects in the bucket
def list_objects(bucket):
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(blob.name)

# Upload an object to the bucket
def upload_object(bucket, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Delete an object from the bucket
def delete_object(bucket, blob_name):
    blob = bucket.blob(blob_name)
    blob.delete()
    print(f"Blob {blob_name} deleted.")

# Example usage:
list_objects(bucket)
upload_object(bucket, '/home/akshay/a.txt', '/a.txt')
delete_object(bucket, '/a.txt')


####################################

Role: 
Storage Object Admin

IAM Condition
resource.name.startsWith("projects/_/buckets/akshay")

####################################

Dependencies

json key file
pip install google-cloud-storage

####################################
