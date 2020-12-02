import base64

def get_image_string():
  with open('test.png','rb') as f:
    return base64.b64encode(f.read())
    


if __name__=="__main__":
  print(get_image_string())    
