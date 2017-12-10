def makeAlbum(singer,album,songs=''):
    Album = {'singer':singer,'album':album}
    if songs:
        Album['songs'] = songs
    return Album

while True:
    print("input q to quit")
    singer = input('Please input a singer name:')
    if singer == 'q':
        break
    album = input('Please input a album name:')
    if album == 'q':
        break
    print(makeAlbum(singer,album))