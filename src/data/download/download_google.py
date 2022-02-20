from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = { 'keywords': 'hallway ideas', 
                'limit': 100,
                'size': '>2MP',
                'print_urls': True,
                'output_directory': 'C:\\Users\\mrshu\\lynch-room\\data\\google downloads',
                'chromedriver': 'C:\\Users\\mrshu\\.wdm\\drivers\\chromedriver\\win32\\97.0.4692.71' }
paths = response.download(arguments)
print(paths)