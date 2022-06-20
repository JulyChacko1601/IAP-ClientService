#addons_bp

Client & Service DB Connect
=============================================================================

This modules helps to communicate with client and service DB and can requests
services from client to service DB.

Module Name : connect_service_db

Basic Configurations
====================

Backend Side
============

Go to Settings ==> Technical ==> System Parameters

create a parameter bloopark.endpoint and configure the endpoint.

----

1. CONNECTION

----

 Settings ==> Technical ==> IAP Connect ==> IAP Service

* Service Name : Name of the service (Eg: public_holidays)

* Contract Reference : Service contract reference (From service DB)

* Service URL : Request to be call

* Description : Brief description

* Status : Status of the response (Failed / Success)

* Message : Response message

For a test connection, create a record with following data:

* Service URL : /service/test/connect

Upon connecting the request, a success or failure message will update.
