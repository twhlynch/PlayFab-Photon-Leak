import json

def main(photonFile, playFabFile):

    photon = getPhotonServerSettings(photonFile)
    playFab = getPlayFabSharedSettings(playFabFile)

    data = {
        "playFab": playFab,
        "photon": photon
    }

    with open("leaks.json", "w") as file:
        json.dump(data, file)

def getPhotonServerSettings(photonFile):

    with open(photonFile, 'rb') as file:

        file.seek(0x38)
        pun = file.read(36).decode('utf-8')

        file.seek(0x68)
        voice = file.read(36).decode('utf-8')

        return { 'pun': pun, 'voice': voice }

def getPlayFabSharedSettings(playFabFile):

    with open(playFabFile, 'rb') as file:

        file.seek(0x3C)
        title = file.read(5).decode('utf-8')

        return { 'title': title }

if __name__ == '__main__':

    photonFileName = "PhotonServerSettings-resources.assets-3654.dat"
    playFabFileName = "PlayFabSharedSettings-resources.assets-3655.dat"
   
    main(photonFileName, playFabFileName)