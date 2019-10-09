import os
import oci
from oci.object_storage.models import CreateBucketDetails

ruta = os.getcwd() + os.sep

config = oci.config.from_file()
compartmentId = config["tenancy"]
objectStorage = oci.object_storage.ObjectStorageClient(config)

namespace = objectStorage.get_namespace().data

bucketName = "VMDK_uploas"
objectName = "archivo.vmdk"
myArchivo = ruta + objectName

print("Creando Bucket {!r} en Compartment {!r}".format(bucketName, compartmentId))
request = CreateBucketDetails()
request.compartment_id = compartmentId
request.name = bucketName
bucket = objectStorage.create_bucket(namespace, request)
uri = bucket.headers['location'] + "/o/" + objectName

print("Subiendo objeto {!r}".format(objectName))
obj = objectStorage.put_object(namespace, bucketName, objectName, myArchivo)
