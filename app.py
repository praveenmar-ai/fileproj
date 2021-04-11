from  flask import Flask , render_template



app = Flask(__name__)


## default  URL
@app.route('/',methods= ['GET'])
def con():
    with open('file1.txt','r') as fname:
        return render_template("basic.html",text =fname.read() )

        
## DYNAMIC URL FOR ALL FILES 
@app.route('/<var><file>',methods = ['GET'])
def content(var,file  = "file1", fp = 0, lp  = -1):
    try :

    
        if var == 'file1':
            with open('file1.txt','r') as fname:
                return render_template("basic.html",text =fname.read() )

        elif var == 'file2':
            with open('file2.txt','r') as fname:
                return render_template("basic.html",text =fname.read() )
    
        elif var == 'file3':
            with open('file3.txt','r') as fname:
                return render_template("basic.html",text =fname.read() )
    
        elif var == 'file4':
            with open('file4.txt','r',decoding='utf8') as fname:
            
                return render_template("basic.html",text  = fname.read())

    except Exception as ex:
        return ex

def prog(file  = "file1", fp = 0, lp  = -1):
    try:
        fp = int(fp)
        lp = int(lp)
        with open(var+".txt","r",encoding = "cp437") as f1:
            d = f1.readlines()
        if lp == -1:
            lp = len(d)
        return render_template("basic.html",data = d[fp:lp+1])

    except (FileNotFoundError):
        return "file not found "



if __name__ == "__main__":
    app.run(debug=True)
