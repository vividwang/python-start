def makeAlbum(singer,album,songs=''):
    Album = {'singer':singer,'album':album}
    if songs:
        Album['songs'] = songs
    return Album

print(makeAlbum('Taylor Swift','Red'))
print(makeAlbum('Sia','Cheap thrills',1))
print(makeAlbum('Ed Sheeran','Shape of you',1))