from flask import Flask, request
import servis
import json, requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/ozetle', methods=['POST', 'GET'])
def ozetleyen():

    if request.method == 'GET':
        url = request.args.get('url')
        esik = '5'
    else:
        url = request.form.get('url')
        esik = request.form.get('esik')


    if not url:
        url = 'http://www.haber7.com/guncel/haber/2927040-son-dakika-kar-geliyor-uyarilar-pes-pese-iste-il-il-hava-durumu'

    if not esik:
        esik = '5'


    data = requests.get(url, 
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).content

    data = BeautifulSoup(data).find('div',attrs={"class":"news-content"}).text

    ozet= servis.ozetle(data,esik)

    return """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Özet</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <style>
    
    body{
        font-size: 25px;
        margin: 50px 350px 0px 350px;
    }
    .btn{
        margin-left: 10px;
    }
    .form-control{
        margin-left: 10px;;
    }

    </style>
</head>
<body>
    

    <form action="/ozetle" method="post" >
        
        <div class="form-group">
        <label for="url">Url: </label>
            <input class="form-control" type="text" placeholder="url" value='"""+url+"""' id="url" name='url'></div>
        <div class="form-group form-inline">

            
          <label for="esik">Eşik Değeri: </label>
          <input class="form-control" type="text" placeholder="5" value='"""+esik+"""' id="esik" name='esik'>
          <button type="submit" class="btn btn-primary">Yenile</button>
        </div>
        
       
        
      </form>
      <hr>


"""+ozet+"""    
</body>
</html>



    """
        

if __name__ == '__main__':
    app.run()
