------------
expandvr API
------------
Last update: 31 Oct, 2013

Version: 0.1.0 (http://semver.org/ - Semantic Versioning 2.0.0)


Changelog
---------
0.1.0
    - First public development version

Schema
------
All API access is done over HTTP from the voiceapi.expand.com.uy,
authentication is disabled for this version.
Data is received using multipart-form encoded requests, all data sent by this
API is JSON encoded.

-----------------------
Status Code Definitions
-----------------------
Each Status-Code is described below, including a description of which method(s)
it can follow and any metainformation required in the response.


Successful 2xx
--------------

200 OK
------
The request has succeeded.


::

	HTTP/1.1 200 OK

	{
	   "task_id": bf4f25f6682d4d2990cec25a91a15e75, 
	}


Client Error 4xx
----------------
There are four possible types of client errors on API calls that receive
request bodies:


400 Bad Request
---------------
Sending invalid multipart-form encoded messages will result in a
400 Bad Request response.

::

	HTTP/1.1 400 Bad Request
	Content-Length: 35



404 Not Found
-------------
Sending invalid Request-URI will result in a 404 Not Found.

::

	HTTP/1.1 404 Not Found


405 Method Not Allowed
----------------------
Sending invalid method will result in a 405 Method Not Allowed.
The response must include an Allow header containing a list of valid methods
for the requested resource.

::

   HTTP/1.1 405 Method Not Allowed
   Content-Lenght: 41 
   Allow: POST
   



422 Unprocessable Entity
------------------------
Sending invalid data will result in a 422 Unprocessable Entity response.

::

   HTTP/1.1 422 Unprocessable Entity
   Content-Length: 149

   { 
     "message": "Validation Failed",
     "errors": [
                {
                  "resource": "result",
                  "field": "task_id",
                  "code": "missing_field"
                }
               ]
   }



All error objects have resource and field properties so that your client can
tell what the problem is. There’s also an error code to let you know what is
wrong with the field. These are the possible validation error codes:

missing
    This means a resource does not exist.
missing_field
    This means a required field on a resource has not been set.
invalid
    This means the formatting of a field is invalid. The documentation for that resource should be able to give you more specific information.
   
If resources have custom validation errors, they will be documented with the resource.


HTTP Verbs
----------
Where possible, this API strives to use appropriate HTTP verbs for each action,
however in the current version only the POST verb will be accepted.

POST
    Used for creating resources, or performing custom actions (such as speaker or gender recognition). 


----------------
Recognize gender
----------------

Issues a gender recognition on provided audio data. 

Audio data are chunks of raw audio frames of linear PCM 16 bit 8kHz mono audio.

This resource can be queried several times, splitting the audio chunk and
assigning sequence numbers to them so the service can rearrange the complete
audio data. The requests order is not important but there is a total minimum
audio duration of 10 seconds for gender recognition, also all sequences must
be consecutive and start from '1'. For example, you can issue sequences 3, 4,
2 and 1 in that order, or any other order. 
Maximum audio duration for a single task is 60 seconds. Recognition is
speaker's languague agnostic.

The response will indicate if more data is needed and when a result should
be ready.


POST /recognition/gender


Form Parameters
---------------
audio_sequence
   What sequence this audio chunk corresponds to. Valid range '1'-'100'.
audio_samplerate
   Samplerate of the provided raw audio data. Only '8000'.
audio_bitdepth
   Bitdepth of the provided raw audio data. Only '16'.
audio_channels
   How much audio channels do this raw audio data have. Only '1' channel is supported.
audio_sent_frames
   How many frames are you sending in this chunk.
task_id
   Optional task id, used to reference different requests with different sequences.

Appended files
   Binary audio data must be issued with a filename 'file'. 
   Content-type for this part should be: 'application/octet-stream'



Response
--------
Status: 200 OK

::

 {
    'received_sequences': [1, 2],
    'new_result_in': 5,
    'need_more': True,
    'task_id': 'bf4f25f6682d4d2990cec25a91a15e75'
 }


received_sequences
    All received audio sequences.
new_result_in
    Estimated time of arrival for new result given the provided data.
need_more
    Boolean indicating if more audio data is needed to issue a gender recognition task.
task_id
    Task id of the current recognition request. 
    The consumer must use this value to issue new requests with new sequences.


----------------------
Retrieve gender result
----------------------

Retrieves the gender recognition task result.

Fetching the results in a timely manner is the consumer's responsability. 
In this API development stage results will be stored for a relatively short
period of time, just remember to check for results when the api tells you if
you don't want to lose them. Results are one-time only, if you ask for a
result, it will be deleted inmediatly after you got it.


POST /recognition/gender/result


Form Parameters
---------------
task_id
  Task id of the gender recognition.



Response
--------
Status: 200 OK

::

 { 
    'gender': 'F', 
    'score': 1.34569807, 
    'new_result_in': 5
 }

gender
    Recognized gender, defaults to 'n/a' if result is not ready 
score
    Score of recognition, the bigger values the better. Beware, score is still a work in progress, you can get the correct gender and some pretty crazy scores. Defaults to 'n/a' if result is not ready.
new_result_in
    Estimated time of arrival for a new result given the last provided audio data.
