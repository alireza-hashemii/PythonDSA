import os 


def disk_usage(path: str) -> int:

    if os.path.exists(path):
        total = os.path.getsize(path)
        for filesnames in os.listdir(path):
            if os.path.isdir(filesnames):
                npath = os.path.join(path, filesnames)
                total += disk_usage(npath)
        return total
    
    else:
        return "Not Valid Path" 
    

disk = disk_usage(r'C:\Users\AVA\Desktop\startbootstrap-clean-blog-gh-pages')
