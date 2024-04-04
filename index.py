from flask import Flask, render_template, request, session, make_response, redirect
import psycopg2

app = Flask(__name__)
conexao = psycopg2.connect(user="postgres",
                                  password="maysab05",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="estudo_db")
print("Consexão realizada com sucesso")

@app.route("/deletar", methods=['GET','POST'])
def deletar():
        cursor = conexao.cursor()
        sql = "DELETE FROM cliente WHERE id = %s"
        cursor.execute(sql,(request.args.get('id')))
        db.commit()
        return redirect("/")


@app.route("/", methods=['GET','POST'])
def index():
        if request.method == 'POST':
                id = request.form.get('id')
                nome = request.form.get('nome')
                email = request.form.get('email')
                cursor = conexao.cursor()
                sql = "UPDATE cliente SET nome = %s,email = %s WHERE id = %s"

                cursor.execute(sql,(nome,email,id))
                conexao.commit()


                cursor = conexao.cursor()
                sql = "SELECT * FROM cliente"

                cursor.execute(sql)
                conexao.commit()
                results = cursor.fetchall()
                print(results)
                return render_template("index.html",content=results)
        else:
                cursor = conexao.cursor()
                sql = "SELECT * FROM cliente"

                cursor.execute(sql)
                conexao.commit()
                results = cursor.fetchall()
                print(results)
                return render_template("index.html",content=results)
            
        
        
    


@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2>"

@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: "+noticia_slug


if __name__ == "__main__":
    app.run(debug=True)

