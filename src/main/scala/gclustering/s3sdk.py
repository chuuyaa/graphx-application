import os
import sys
import boto3

if __name__ == "__main__":
    """
        Usage: python s3sdk.py [filename]
        this script will make an authenticated request 
        to download the specified file from a specific 
        DigitalOcean Space. The downloaded file stored
        on the local file-system /tmp
    """
    filename = sys.argv[1]
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='sgp1',
                            endpoint_url='https://sgp1.digitaloceanspaces.com',
                            aws_access_key_id='K5KXJWPF4YQP75TV7H5A',
                            aws_secret_access_key='vyCyjz42sZ3365yE4v0kQH85iZs8T7SWMk1F0774Tg0')

    response = client.list_objects(Bucket='sosc-storage')
    for obj in response['Contents']:
        print(obj['Key'])

    url = client.download_file('sosc-storage',
                               filename,
                               '/tmp/'+filename)