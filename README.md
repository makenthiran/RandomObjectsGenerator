# RandomObjectsGenerator

By running the RandomObjectGenerator.py program, the api exposed in 127.0.0.1:5050 address

Available services are, 
1. http://127.0.0.1:5050/generate
    Method : GET
    Response:
         {
           "alphabets":39664,
           "alphanumeric":39612,
           "fileName":"randomString_1634910235455.txt",
           "integer":26065,
           "realnumber":26468
        }
        
2. http://127.0.0.1:5050/download/randomString_1634910235455.txt
     Method: GET
     Response: if found,     Downloaded File of 2MB size if exist
               if not found,
                        {
                           "error":404,
                           "message":"file not found"
                        }
