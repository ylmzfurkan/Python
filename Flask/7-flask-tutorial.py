# flask kütüphanesinden Flask, redirect, url_for, render_template, request, session, flash modülleri çağırılır.
# datetime modülünden timedelta sınıfı çağırılır.
# flask_sqlalchemy modülünden SQLAlchemy sınıfı çağırılır.
from flask import Flask, redirect , url_for , render_template , request , session , flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# Flask uygulaması oluşturulur.
app = Flask(__name__)

# Uygulamaya bir anahtar değer atanır.
app.secret_key = "hello"

# Veritabanı URL'si belirtilir.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"

# SQLAlchemy için izleme özelliği devre dışı bırakılır.
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

# Oturum süresi 5 dakika olarak belirlenir.
app.permanent_session_lifetime = timedelta(minutes=5)

# Veritabanı için bir nesne oluşturulur.
db = SQLAlchemy(app)

# users sınıfı oluşturulur.
class users(db.Model):
    _id = db.Column("id" , db.Integer , primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self , name , email):
        self.name = name
        self.email = email

# Anasayfa yönlendirmesi yapılır.
@app.route("/")
def home():
    return render_template("index.html")

# Giriş sayfası oluşturulur.
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        # Veritabanı sorgusu yapılır.
        found_user = users.query.filter_by(name = user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            # Veritabanına kullanıcı eklenir.
            usr = users(user , None)
            db.session.add(usr)
            db.commit()

        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

# Kullanıcı sayfası oluşturulur.
@app.route("/user" , methods=["POST" , "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
                
        return render_template("user.html" , email = email)
    else:
        flash("You are not Logged In!")
        return redirect(url_for("login"))
    
# Çıkış sayfası oluşturulur.
    
@app.route("/logout")
def logout():
    flash("You have been logged out!" , "info")
    session.pop("user" , None)
    session.pop("email" , None)
    return redirect(url_for("login"))    

#Bu kısımda ise uygulamanın çalıştırılması ve veritabanının oluşturulması yer alıyor. "db.create_all()" fonksiyonu kullanılarak "users" adlı veritabanı oluşturuluyor. 
#Daha sonra "app.run(debug=True)" fonksiyonu kullanılarak uygulama çalıştırılıyor. "debug=True" parametresi uygulamanın hata durumlarında daha ayrıntılı bir hata mesajı göstermesini sağlar
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)