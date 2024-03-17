import requests

headers = {
    'X-Api-Key': 'YOUR_API_KEY',
    'content-type': 'application/json', 
}
 
json_data = { 
    'slides': [
        {
            'overlays': [ 
                {
                    'type': 'AvatarOverlay',
                    'assetId': '1a901a33-8783-418e-af6a-a66dae945673',
                    'voiceId': 'en-US-JennyMultilingualNeural',
                    'script': "Well done! This is your first video using Yepic's API.",
                    'xPosition': 448,
                    'yPosition': 56,
                    'width': 1024,
                    'height': 1024,
                },
            ],
        },
    ],
    'videoTitle': 'My first video',
}
 
response = requests.post('https://api.yepic.ai/v1/videos', headers=headers, json=json_data)
print(response)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{     "slides": [          {               "overlays": [                    {                         "type": "AvatarOverlay",                         "assetId": "1a901a33-8783-418e-af6a-a66dae945673",                         "voiceId": "en-US-JennyMultilingualNeural",                         "script": "Well done! This is your first video using Yepic\'s API.",                         "xPosition": 448,                         "yPosition": 56,                         "width": 1024,                         "height": 1024                    }               ]          }     ],     "videoTitle": "My first video"}'
#response = requests.post('https://api.yepic.ai/v1/videos', headers=headers, data=data)
