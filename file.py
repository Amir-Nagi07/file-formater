n = int(input('inter the number of your files:'))
image = ['.jpg' ,'.png' ]
documents = ['.pdf', '.xlsx']
video = ['.mp4', '.mp3']
len_image = 0
len_video = 0
len_documents = 0
while n > 0:
        filename = input('inter file name:')
        if filename.lower().endswith(tuple(image)):
            len_image += 1
        elif filename.lower().endswith(tuple(video)):
            len_video += 1
        elif filename.lower().endswith(tuple(documents)):
            len_documents += 1
        else:
             print('you inter invalid format!')
             continue
        n = n - 1
            
        print('ypu inter a invalid format!')
print(f'the number of the image {len_image}')
print(f'the number of the image {len_video}')
print(f'the number of the image {len_documents}')