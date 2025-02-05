import shutil

def remove_back_slash(path):
    new = []
    if '\\\\' in path:
        path = path.split('\\\\')
        for i in path:
            if '\\' in i:
                new.append(i.replace('\\','\\\\'))
            else:
                new.append(i)
    else:
        path = path.replace('\\','\\\\')
    return path

org_loc = input("Enter your original file location/path:- ")
transfer_loc = input("Enter your location where you transfer the file:- ")

actual_org_loc = remove_back_slash(org_loc)
actual_transfer_loc = remove_back_slash(transfer_loc)

shutil.move(actual_org_loc,actual_transfer_loc)
