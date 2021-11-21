from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
islem_yapilan_kullanici=""
app = Flask(__name__)
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asy@localhost/users'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Kullanicilar(db.Model):
    __tablename__ = 'Kullanicilar'
    KullaniciAdi = db.Column(db.String(15),unique=True, primary_key=True)
    Sifre = db.Column(db.String(30), nullable=False)
    
    def __init__(self,KullaniciAdi, Sifre):
        self.KullaniciAdi =KullaniciAdi        
        self.Sifre =Sifre
class ProblemBirim(db.Model):
    __tablename__ = 'ProblemBirim'
    ProblemID = db.Column(db.Integer,primary_key=True,nullable=False)
    BirimID = db.Column(db.Integer,nullable=False)
    EslesmeTarihi = db.Column(db.String(30), nullable=True)
    
    def __init__(self,ProblemID, BirimID,EslesmeTarihi):
        self.ProblemID =ProblemID        
        self.BirimID =BirimID  
        self.EslesmeTarihi =EslesmeTarihi 
class PersonelProblem(db.Model):
    __tablename__ = 'PersonelProblem'
    ProblemID = db.Column(db.Integer,primary_key=True,nullable=False)
    KullaniciAdi = db.Column(db.String,nullable=False)    
    
    def __init__(self,ProblemID, KullaniciAdi):
        self.ProblemID =ProblemID        
        self.KullaniciAdi =KullaniciAdi 
class PersonelCiktiDegerlendirme(db.Model):
    __tablename__ = 'PersonelProblemDegerlendirme'
    ProblemID = db.Column(db.Integer,nullable=False)
    BelirtecID = db.Column(db.Integer,primary_key=True,nullable=False)
    skor = db.Column(db.Integer,nullable=False)
    skorTarihi = db.Column(db.Integer,nullable=True)
    
    def __init__(self,ProblemID, BelirtecID,skor,skorTarihi):
        self.ProblemID =ProblemID        
        self.BelirtecID =BelirtecID 
        self.skor =skor
        self.skorTarihi =skorTarihi                         
              
class Personel(db.Model):   
    __tablename__ = 'Personel'
    KullaniciAdi = db.Column(db.String(15), primary_key=True)
    Email = db.Column(db.String(30), unique=True,nullable=False)
    Ad = db.Column(db.String(30),nullable=False)
    Soyad = db.Column(db.String(30),nullable=False)
    SicilNo = db.Column(db.String(30),unique=True,nullable=False)
    Cep = db.Column(db.String(11), nullable=False)
    Ev_adresi = db.Column(db.String(200), nullable=False)
    IlKodu = db.Column(db.Integer,nullable=False)
    IlceKodu = db.Column(db.Integer,nullable=False)
    PostaKodu = db.Column(db.Integer,nullable=False)
    UstKullaniciAdi = db.Column(db.String(30))
    CalistigiBirimKodu = db.Column(db.Integer,nullable=False)

    def __init__(self,KullaniciAdi, Email, Ad, Soyad, SicilNo, Cep, Ev_adresi, IlKodu, IlceKodu, PostaKodu, UstKullaniciAdi, CalistigiBirimKodu):
        self.KullaniciAdi =KullaniciAdi        
        self.Email =Email
        self.Ad =Ad
        self.Soyad =Soyad
        self.SicilNo =SicilNo
        self.Cep =Cep
        self.Ev_adresi =Ev_adresi
        self.IlKodu =IlKodu
        self.IlceKodu =IlceKodu
        self.PostaKodu =PostaKodu
        self.UstKullaniciAdi =UstKullaniciAdi
        self.CalistigiBirimKodu =CalistigiBirimKodu  
class Birimler(db.Model):
    __tablename__ = 'Birimler'
    BirimKodu = db.Column(db.Integer,primary_key=True,nullable=False)
    BirimAdi = db.Column(db.String(35),nullable=False)
    UstBirimKodu = db.Column(db.Integer,nullable=False)
    BulunduguAdres   = db.Column(db.String(200),nullable=False) 
    IlKodu = db.Column(db.Integer,nullable=False)
    IlceKodu = db.Column(db.Integer,primary_key=True,nullable=False)
    PostaKodu = db.Column(db.Integer,nullable=False)
    BirimMudurKullaniciAdi = db.Column(db.Integer,nullable=False)
    
    def __init__(self,BirimKodu, BirimAdi, UstBirimKodu, BulunduguAdres, IlKodu, IlceKodu, PostaKodu, BirimMudurKullaniciAdi):
        self.BirimKodu=BirimKodu
        self.BirimAdi=BirimAdi
        self.UstBirimKodu=UstBirimKodu
        self.BulunduguAdres=BulunduguAdres
        self.IlKodu=IlKodu
        self.IlceKodu=IlceKodu
        self.PostaKodu=PostaKodu
        self.BirimMudurKullaniciAdi=BirimMudurKullaniciAdi
class Problemler(db.Model):
    __tablename__ = 'Problemler'
    ProblemTipiID= db.Column(db.Integer,primary_key=True,nullable=False)
    ProblemTanimi= db.Column(db.String(200),primary_key=True,nullable=False)
    ProblemiTanimlayiciAdi= db.Column(db.String(30),nullable=False)
    ProblemiTanimlayiciSoyadi= db.Column(db.String(30),nullable=False)
    ProblemiTanimlayanTCNOPasaportno= db.Column(db.String(30),nullable=False)
    HedeflenenAmacTanimi   = db.Column(db.String(200))
    def __init__(self, ProblemTipiID,ProblemTanimi, ProblemiTanimlayiciAdi, ProblemiTanimlayiciSoyadi, ProblemiTanimlayanTCNOPasaportno, HedeflenenAmacTanimi):                    
        self.ProblemTipiID=ProblemTipiID
        self.ProblemTanimi=ProblemTanimi
        self.ProblemiTanimlayiciAdi=ProblemiTanimlayiciAdi
        self.ProblemiTanimlayiciSoyadi=ProblemiTanimlayiciSoyadi
        self.ProblemiTanimlayanTCNOPasaportno=ProblemiTanimlayanTCNOPasaportno
        self.HedeflenenAmacTanimi= HedeflenenAmacTanimi 
class Alanlar(db.Model):
    __tablename__ = 'Alanlar'
    AlanID= db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    AlanAdi= db.Column(db.String(30),nullable=False)
    AlanTipi= db.Column(db.Boolean,nullable=False)   
    def __init__(self,AlanID, AlanAdi, AlanTipi):
        self.AlanID=AlanID
        self.AlanAdi=AlanAdi
        self.AlanTipi=AlanTipi
class Siniflar(db.Model):
    __tablename__ = 'Siniflar'
    SinifID= db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    SinifAdi= db.Column(db.String(30),nullable=False)
    AlanTipi= db.Column(db.Boolean,nullable=False)   
    def __init__(self,SinifID, SinifAdi, AlanTipi):
        self.AlanID=SinifID
        self.AlanAdi=SinifAdi
        self.AlanTipi=AlanTipi
class Mudahale(db.Model):
    __tablename__ = 'Mudahale'
    AlanID= db.Column(db.Integer,unique=True,nullable=False)
    SinifID= db.Column(db.Integer,nullable=False)
    MudaheleID= db.Column(db.Integer,primary_key=True,nullable=False) 
    MudahaleAdi= db.Column(db.String(),nullable=False)    
    def __init__(self,AlanID,SinifID, MudaheleID, MudahaleAdi):
        self.AlanID=AlanID
        self.SinifID=SinifID
        self.MudaheleID=MudaheleID
        self.MudahaleAdi=MudahaleAdi 
class Aktiviteler(db.Model):
    __tablename__ = 'Aktiviteler'
    AktiviteID= db.Column(db.Integer,unique=True,primary_key=True,nullable=False)    
    AktiviteTanimi= db.Column(db.String(200),nullable=False)
    def __init__(self,AktiviteID,AktiviteTanimi):
        self.AktiviteID=AktiviteID
        self.AktiviteTanimi=AktiviteTanimi          
class MudahaleDetay(db.Model):
    __tablename__ = 'MudahaleDetay'
    AlanID= db.Column(db.Integer,unique=True,nullable=False)
    SinifID= db.Column(db.Integer,nullable=False)
    MudaheleID= db.Column(db.Integer,primary_key=True,nullable=False) 
    AktiviteID= db.Column(db.Integer,unique=True,nullable=False)
    Sira= db.Column(db.Integer(),nullable=False)    
    def __init__(self,AlanID,SinifID, MudaheleID, AktiviteID,Sira):
        self.AlanID= AlanID
        self.SinifID=SinifID
        self.MudaheleID=MudaheleID
        self.AktiviteID=AktiviteID
        self.Sira=Sira
class Cikti(db.Model):
    __tablename__ = 'Cikti'
    AlanID= db.Column(db.Integer,unique=True,nullable=False)
    SinifID= db.Column(db.Integer,nullable=False)
    CiktiID= db.Column(db.Integer,primary_key=True,nullable=False) 
    CiktiAdi= db.Column(db.String(30),unique=True,nullable=False)       
    def __init__(self,AlanID,SinifID, CiktiID, CiktiAdi):
        self.AlanID= AlanID
        self.SinifID=SinifID
        self.CiktiID=CiktiID
        self.CiktiAdi=CiktiAdi
class Belirtecler(db.Model):
    __tablename__ = 'Belirtecler'
    BelirtecID= db.Column(db.Integer,primary_key=True,nullable=False) 
    BelirtecAdi= db.Column(db.String(30),unique=True,nullable=False) 
    def __init__(self,BelirtecID,BelirtecAdi):
        self.BelirtecID=BelirtecID
        self.BelirtecAdi=BelirtecAdi  
class CiktiDetay(db.Model):
    __tablename__ = 'CiktiDetay'
    AlanID= db.Column(db.Integer,unique=True,nullable=False)
    SinifID= db.Column(db.Integer,nullable=False)
    CiktiID= db.Column(db.Integer,primary_key=True,nullable=False) 
    BelirtecID= db.Column(db.String(30),unique=True,nullable=False)       
    Sira= db.Column(db.Integer(),nullable=False) 
    def __init__(self,AlanID,SinifID, CiktiID, BelirtecID,Sira):
        self.AlanID= AlanID
        self.SinifID=SinifID
        self.CiktiID=CiktiID
        self.BelirtecID=BelirtecID
        self.Sira=Sira        
class Iller(db.Model):

    __tablename__ = 'Iller'
    IlKodu = db.Column(db.Integer,primary_key=True,nullable=False)
    IlAdi = db.Column(db.String(30),nullable=False)
    def __init__(self,IlKodu, IlAdi):
        self.IlKodu =IlKodu        
        self.IlAdi =IlAdi
class Ilceler(db.Model):
    __tablename__ = 'Ilceler'
    IlceKodu = db.Column(db.Integer,primary_key=True,nullable=False)
    IlKodu = db.Column(db.Integer,nullable=False)   
    IlceAdi = db.Column(db.String(30),nullable=False)
    def __init__(self,IlceKodu,IlKodu , IlceAdi):
        self.IlceKodu =IlceKodu
        self.IlKodu =IlKodu                 
        self.IlceAdi =IlceAdi          

        
@app.route('/')
def home():    
    if(request.method == "GET"):

        return render_template('home.html')           
@app.route('/submit', methods=['GET', 'POST'])  
def giris(): 
    if request.method == 'POST':
        customer = request.form.get("username")
        islem_yapilan_kullanici=customer
        sifre = request.form.get("sifre")
        tur = request.form.get("Kullanici")
        print(tur)
        if tur=="Yonetici":
            if customer!="Ahmed_Said" and customer!="Mertcan":
                 return render_template('home.html', message="yonetici degilsiniz")      
        records = db.session.query(Kullanicilar.Sifre).filter(Kullanicilar.KullaniciAdi.like(customer)).first()        
        if records==None:            
            return render_template('home.html', message="yanlis kullaniciAdi: ")
        elif records=="0":
            return render_template('kayit.html') 
              
        elif sifre in records:
            if tur=="Yonetici":
                if  customer=='Ahmed_Said':  
                    return render_template('admin.html', message="Hosgeldiniz: "+customer,nmbr=7)
                else :                
                   return render_template('BirimYonetici.html', message="Hosgeldiniz: "+customer,nmbr=7) 
               
            return render_template('personel.html', message="Hosgeldiniz: "+customer,nmbr=7)    
        else : 
            return render_template('home.html', message="yanlis sifre: ")
@app.route('/islem', methods=['GET', 'POST'])  
def adminIslem():     
    if request.method == 'POST':
        islem = request.form.get("islem")
        if islem=='Personel_ekleme' :       
            return render_template('AdminIslem1.html')
        if islem=='problem_ekleme' :       
            return render_template('AdminIslem2.html',kontrol=True)
        if islem=='Mudehale_ekleme' :        
            return render_template('AdminIslem3.html')
        if islem=='il_ekleme' :       
            return render_template('AdminIslem4.html')
        if islem=='ilce_ekleme' :       
            return render_template('AdminIslem5.html')
        if islem=='Birim_ekleme' :        
            return render_template('AdminIslem6.html') 
        if islem=='eslesme' :        
            return render_template('Eslesme.html')     
        else:        
            return render_template('AdminIslemO.html')       
@app.route('/islemP', methods=['GET', 'POST'])  
def problemGirmeIslemi():    
    if request.method == 'POST':                       
        return render_template('problem.html')              
@app.route('/islem1', methods=['GET', 'POST'])  
def personel_Ekleme(): 
    if request.method == 'POST':
        islem=request.form.get("islem")
        KullaniciAdi =request.form.get("KullaniciAdi") 
        if islem=="personel_ekleme":                 
            Email =request.form.get("Email")
            Ad =request.form.get("Ad")
            Soyad =request.form.get("Soyad")
            SicilNo =request.form.get("SicilNo")
            Cep =request.form.get("Cep")
            Ev_adresi =request.form.get("Ev_adresi")
            if Ev_adresi is None:
                Ev_adresi=""
            IlKodu =int(request.form.get("IlKodu"))
            IlceKodu =int(request.form.get("IlceKodu"))
            PostaKodu =int(request.form.get("PostaKodu"))
            UstKullaniciAdi =request.form.get("UstKullaniciAdi")
            CalistigiBirimKodu =request.form.get("CalistigiBirimKodu") 
            data1=db.session.query(Ilceler.IlceKodu).filter(Ilceler.IlceKodu==IlceKodu).first()
            data2=db.session.query(Iller.IlKodu).filter(Iller.IlKodu==IlKodu).first()
            if data1 is None:
                return render_template('AdminIslem1.html', message="Boyle bir ilce yok") 
            if data2 is None:
                return render_template('AdminIslem1.html', message="Boyle bir il yok")
            print(UstKullaniciAdi)    
            if UstKullaniciAdi!="":    
                data1=db.session.query(Kullanicilar.KullaniciAdi).filter(Kullanicilar.KullaniciAdi==UstKullaniciAdi).first()
                if data1 is  None:
                    return render_template('AdminIslem1.html', message="Boyle bir ust kullanici yok") 
            if CalistigiBirimKodu =="":    
                data1=db.session.query(Birimler.BirimKodu).filter(Birimler.BirimKodu==CalistigiBirimKodu).first()
                if data1 is  None:
                    return render_template('AdminIslem1.html', message="Boyle bir birim kullanici yok")
            data=Kullanicilar(KullaniciAdi,0) 
            db.session.add(data)
            db.session.commit()            
            data=Personel(KullaniciAdi, Email, Ad, Soyad, SicilNo, Cep, Ev_adresi, IlKodu, IlceKodu, PostaKodu, UstKullaniciAdi, CalistigiBirimKodu) 
            db.session.add(data)
            db.session.commit()        
             
        else:             
            person = Personel.query.filter_by(KullaniciAdi=KullaniciAdi).first()
            db.session.delete(person)
            db.session.commit()
            person = Kullanicilar.query.filter_by(KullaniciAdi=KullaniciAdi).first()              
            db.session.delete(person)
            db.session.commit()  
        return render_template('admin.html', message="Yeni isleminiz nedir?")               
@app.route('/islem2', methods=['GET', 'POST'])  
def problemEkleme_Y(): 
    if request.method == 'POST':        
        ProblemTipiID =request.form.get("ProblemTipiID")      
        ProblemTanimi =request.form.get("ProblemTanimi")
        request.form_data_parser_class
        Problemi_TanimlayiciAdi =request.form.get("Problemi_TanimlayiciAdi")
        Problemi_TanimlayiciSoyadi =request.form.get("Problemi_TanimlayiciSoyadi")
        ProblemiTanimlayanTCNOPasaportno =request.form.get("ProblemiTanimlayanTCNOPasaportno")
        HedeflenenAmacTanimi =request.form.get("HedeflenenAmacTanimi")
        data=Problemler( ProblemTipiID,ProblemTanimi, Problemi_TanimlayiciAdi, Problemi_TanimlayiciSoyadi, ProblemiTanimlayanTCNOPasaportno, HedeflenenAmacTanimi)        
        db.session.add(data)
        db.session.commit()
        return render_template('admin.html', message="Yeni isleminiz nedir?")  
@app.route('/islem3', methods=['GET', 'POST'])  
def MudehaleEkleme(): 
    if request.method == 'POST':        
        AlanID =int(request.form.get("AlanID"))      
        SinifID =int(request.form.get("SinifID"))
        MudaheleID =int(request.form.get("MudaheleID"))
        MudahaleAdi =request.form.get("MudahaleAdi")        
        data=Mudahale( AlanID,SinifID, MudaheleID, MudahaleAdi) 
        data1=db.session.query(Alanlar.AlanID).filter(Alanlar.AlanID==AlanID).first()
        data2=db.session.query(Siniflar.SinifID).filter(Siniflar.SinifID==SinifID).first()
        if data1 is None:
            return render_template('AdminIslem3.html', message="Boyle bir alan yok") 
        if data2 is None:
            return render_template('AdminIslem3.html', message="Boyle bir sinif yok")       
        db.session.add(data)
        db.session.commit()         
        return render_template('admin.html', message="Yeni isleminiz nedir?")
@app.route('/islem4', methods=['GET', 'POST'])  
def ilEkleme(): 
    if request.method == 'POST':        
        ilAdi =request.form.get("il_Adi")     
        ilKodu =int(request.form.get("il_kodu"))
        islem= request.form.get("islem")  
        records = db.session.query(Iller.IlKodu).filter(Iller.IlKodu==ilKodu).first()
        if  islem=='il_ekleme'   :           
            if records is None:
                data=Iller( ilKodu,ilAdi)        
                db.session.add(data)
                db.session.commit()
                return render_template('admin.html', message="Yeni isleminiz nedir?")        
            return render_template('AdminIslem4.html', message="Bu il zaten var")
        elif  records is None:
            return render_template('AdminIslem4.html', message="Boyle bir il yok")  
        elif islem=='il_guncelleme'   :
            il = Iller.query.filter_by(IlKodu=ilKodu).first()                                 
            il.IlAdi = ilAdi                    
            db.session.commit() 
        else:
            il = Iller.query.filter_by(IlKodu=ilKodu).first()
            ilce = Ilceler.query.filter_by(IlKodu=ilKodu).first()  
            person = Personel.query.filter_by(IlKodu=ilKodu).first()             
            if ilce is None :
                 if person is None :
                    db.session.delete(il)
                    db.session.commit()
                    return render_template('admin.html', message="Yeni isleminiz nedir?")              
            return render_template('AdminIslem4.html', message="bu il silinemez")  
@app.route('/islem5', methods=['GET', 'POST'])  
def ilceEkleme(): 
    if request.method == 'POST':        
        ilceAdi =request.form.get("ilce_Adi")     
        ilKodu =int(request.form.get("il_kodu"))  
        ilceKodu =int(request.form.get("ilce_kodu")) 
        islem= request.form.get("secim")
        records = db.session.query(Ilceler.IlceKodu).filter(Ilceler.IlceKodu==ilceKodu).first()
        if  islem=='ilce_ekleme'   :           
            if records is None:
                data=Ilceler( ilceKodu,ilKodu,ilceAdi)          
                db.session.add(data)
                db.session.commit()
                db.session.commit()
                return render_template('admin.html', message="Yeni isleminiz nedir?")        
            return render_template('AdminIslem5.html', message="Bu ilce zaten var")
        elif  records is None:
            return render_template('AdminIslem5.html', message="Boyle bir ilce yok")  
        elif islem=='ilce_guncelleme'   :
            ilce = Ilceler.query.filter_by(IlceKodu=ilceKodu).first()
            if ilceAdi is not None:                                 
                ilce.IlceAdi = ilceAdi
            if ilKodu is not None:
                  ilce.IlKodu = ilKodu                  
            db.session.commit() 
        else:            
            ilce = Ilceler.query.filter_by(IlKodu=ilKodu).first()  
            person = Personel.query.filter_by(IlceKodu=ilceKodu).first()             
            if person is None :
                db.session.delete(ilce)
                db.session.commit()
                return render_template('admin.html', message="Yeni isleminiz nedir?")              
            return render_template('AdminIslem5.html', message="bu ilce silinemez")
        return render_template('AdminIslem5.html', message="Bu ilce zaten var")     
@app.route('/islem6', methods=['GET', 'POST'])  
def BirimEkleme(): 
    if request.method == 'POST':
        islem= request.form.get("secim")
        BirimKodu=int(request.form.get("birim_kodu"))
        BirimAdi=request.form.get("birim_adi")
        UstBirimKodu=int(request.form.get("ustbirim_kodu"))
        BulunduguAdres=request.form.get("bulundugu_adres")
        IlKodu=int(request.form.get("il_kodu"))
        IlceKodu=int(request.form.get("ilce_kodu"))
        PostaKodu=int(request.form.get("posta_kodu"))
        ustbirim = Birimler.query.filter_by(BirimKodu=UstBirimKodu).first()             
        data1=db.session.query(Ilceler.IlceKodu).filter(Ilceler.IlceKodu==IlceKodu).first()
        data2=db.session.query(Iller.IlKodu).filter(Iller.IlKodu==IlKodu).first()
        BirimMudurKullaniciAdi=request.form.get("Birim_mudur_kullanici_Adi")
        if islem=="birim_ekleme" :
            if ustbirim is None:
                return render_template('AdminIslem6.html', message="Boyle bir ust birim yok")            
            data=Birimler( BirimKodu,BirimAdi, UstBirimKodu, BulunduguAdres,IlKodu,IlceKodu, PostaKodu, BirimMudurKullaniciAdi) 
            data1=db.session.query(Ilceler.IlceKodu).filter(Ilceler.IlceKodu==IlceKodu).first()
            data2=db.session.query(Iller.IlKodu).filter(Iller.IlKodu==IlKodu).first()
            if data1 is None:
                return render_template('AdminIslem6.html', message="Boyle bir ilce yok") 
            if data2 is None:
                return render_template('AdminIslem6.html', message="Boyle bir il yok")              
            db.session.add(data)
            db.session.commit()
            return render_template('admin.html', message="Yeni isleminiz nedir?") 
        elif islem=="birim_duzenleme" :
            birim = Birimler.query.filter_by(BirimKodu=BirimKodu).first()            
            if UstBirimKodu is not None:
                 if ustbirim is None:                     
                    return render_template('AdminIslem6.html', message="Boyle bir ust birim yok")
                 else:
                     birim.UstBirimKodu=UstBirimKodu               
            if IlKodu is not None:
                if data1 in None:
                    return render_template('AdminIslem6.html', message="Boyle bir ilce yok")
                else:
                    birim.IlceKodu=IlceKodu      
            if IlKodu is not None:
                if data2 in None:
                    return render_template('AdminIslem6.html', message="Boyle bir il yok")
                else:
                    birim.IlKodu=IlKodu               
            db.session.commit()
            return render_template('admin.html', message="Yeni isleminiz nedir?")
@app.route('/islemP3', methods=['GET', 'POST'])  
def problemEkleme(): 
    if request.method == 'POST':        
        ProblemTipiID =request.form.get("ProblemTipiID")      
        ProblemTanimi =request.form.get("ProblemTanimi")
        request.form_data_parser_class
        Problemi_TanimlayiciAdi =request.form.get("Problemi_TanimlayiciAdi")
        Problemi_TanimlayiciSoyadi =request.form.get("Problemi_TanimlayiciSoyadi")
        ProblemiTanimlayanTCNOPasaportno =request.form.get("ProblemiTanimlayanTCNOPasaportno")
        HedeflenenAmacTanimi= ""
        data=Problemler( ProblemTipiID,ProblemTanimi, Problemi_TanimlayiciAdi, Problemi_TanimlayiciSoyadi, ProblemiTanimlayanTCNOPasaportno, HedeflenenAmacTanimi)        
        db.session.add(data)
        db.session.commit()
        return render_template('home.html')  
@app.route('/returner',methods=['GET', 'POST'])
def Rhome():
    if(request.method == "POST"):
        return render_template('home.html') 
@app.route('/kayitAcma',methods=['GET', 'POST'])
def kayitGirme():
    if(request.method == "POST"):        
        customer = request.form.get("username")
        return render_template('kayit.html',message="sayin kullanici") 
@app.route('/kayit',methods=['GET', 'POST'])
def kayit():    
    if(request.method == "POST"):
        asifre = request.form.get("sifre")
        customer = request.form.get("kullanici")
        data=db.session.query(Kullanicilar.Sifre).filter(Kullanicilar.KullaniciAdi==customer).first()       
        if data is not None and len(data)>10:
            return render_template('kayit.html',message="bu kullanicinin zaten sifresi var degistiremezsiniz") 
        a=0
        b=0
        c=0
        for x in range(len(asifre)):           
            if(asifre[x].isalpha()):                               
                a=a+1
            if(c==0&ord(asifre[x])<91&ord(asifre[x])>64):               
                c=c+1     
            if(b==0&ord(asifre[x])<48&ord(asifre[x])>32):                
                b=b+1            
             
        if a>7 :
            if b>0:
                if c>0: 
                    personel = Kullanicilar.query.filter_by(KullaniciAdi=customer).first()                                 
                    personel.Sifre = asifre                    
                    db.session.commit() 
                    return render_template('home.html')         
        return render_template('kayit.html',message="hatali sifre tekrar deneyiniz")                         
@app.route('/islemO',methods=['GET', 'POST'])
def islemO():

    if(request.method == "POST"):
        returnValue=""
        Alanlarv =request.form.get("Alanlar") 
        Sinifv =request.form.get("Sinif")
        Mudehalev =request.form.get("Mudehale")
        Aktivitelerv =request.form.get("Aktiviteler")
        ciktiv =request.form.get("cikti")
        Belirtecv =request.form.get("Belirtec")
        if Alanlarv=="1":
            AlanID1=int(request.form.get("AlanID")) 
            Alantanim1=request.form.get("AlanAdi") 
            Alandeger=int(request.form.get("AlanTipiA")) 
            alaninfo = Alanlar.query.filter_by(AlanID=AlanID1).first() 
            if alaninfo is None:
                base=True
                if Alandeger==1:
                    base=False
                data=Alanlar(AlanID1,Alantanim1,base)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir alan zaten var\n"
        elif  Alanlarv=="2":
            AlanID1=int(request.form.get("AlanID"))             
            Mudahale1 = Mudahale.query.filter_by(AlanID=AlanID1).first()
            cikti1 = Cikti.query.filter_by(AlanID=AlanID1).first()
            alaninfo = Alanlar.query.filter_by(AlanID=AlanID1).first()
            if alaninfo is None: 
                if cikti1 is not None and Mudahale1 is not None :
                    returnValue+="bu alan silinemez\n"
                else :                                 
                    db.session.delete(alaninfo)
                    db.session.commit()
        if Sinifv=="1":
            sinifID=int(request.form.get("sinifID")) 
            SinifAdi=request.form.get("SinifAdi") 
            AlanTipiS=int(request.form.get("AlanTipiS")) 
            sinifinfo = Siniflar.query.filter_by(AlanID=AlanID1).first() 
            if sinifinfo is None:
                base=True
                if AlanTipiS==1:
                    base=False
                data=Siniflar(sinifID,SinifAdi,base)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir sinif zaten var\n"
        elif  Sinifv=="2":
            sinifID=int(request.form.get("AlanID"))             
            Mudahale1 = Mudahale.query.filter_by(SinifID=sinifID).first()
            cikti1 = Cikti.query.filter_by(SinifID=sinifID).first()
            alaninfo = Siniflar.query.filter_by(SinifID=sinifID).first()
            if alaninfo is None: 
                if cikti1 is not None and Mudahale1 is not None :
                    returnValue+="bu sinif silinemez\n"
                else :                                 
                    db.session.delete(alaninfo)
                    db.session.commit()
        if Mudehalev=="1":
            AlanID=int(request.form.get("AlanID"))
            sinifID=int(request.form.get("sinifID"))             
            MudehaleID=int(request.form.get("MudehaleID")) 
            MudehaleAdi=request.form.get("MudehaleAdi")
            Mudahaleinfo = Mudahale.query.filter_by(AlanID=AlanID1).first() 
            if Mudahaleinfo is None:
                data=Mudahale(AlanID,sinifID,MudehaleID,MudehaleAdi)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir mudehale zaten var\n"
        elif  Mudehalev=="2":
            MudehaleID=int(request.form.get("MudehaleID"))            
            Mudahale1 = MudahaleDetay.query.filter_by(MudehaleID=MudehaleID).first()           
            Mudahaleinfo = Mudahale.query.filter_by(SinifID=sinifID).first()
            if Mudahaleinfo is None: 
                if Mudahale1 is not None :
                    returnValue+="bu mudehale silinemez\n"
                else :                                 
                    db.session.delete(Mudahaleinfo)
                    db.session.commit()
        if Aktivitelerv=="1":
            AktiviteID=int(request.form.get("AktiviteID"))            
            AktiviteTanimi=request.form.get("AktiviteTanimi")
            Aktiviteinfo = Aktiviteler.query.filter_by(AktiviteID=AktiviteID).first() 
            if Aktiviteinfo is None:
                data=Aktiviteler(AktiviteID,AktiviteTanimi)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir mudehale zaten var\n"
        elif  Aktivitelerv=="2":
            AktiviteID=int(request.form.get("AktiviteID"))            
            Aktiviteinfo = Aktiviteler.query.filter_by(AktiviteID=AktiviteID).first()                                     
            db.session.delete(Mudahaleinfo)
            db.session.commit()    
        if ciktiv=="1":
            AlanID=int(request.form.get("AlanID")) 
            SinifID=int(request.form.get("SinifID")) 
            CiktiID=int(request.form.get("CiktiID")) 
            CiktiAdi=request.form.get("CiktiAdi")
            alaninfo = Cikti.query.filter_by(CiktiID=CiktiID).first() 
            if alaninfo is None:               
                data=Cikti(AlanID,SinifID,CiktiID,CiktiAdi)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir cikti zaten var\n"
        elif  ciktiv=="2":
            CiktiID=int(request.form.get("CiktiID"))             
            Cikti1 = CiktiDetay.query.filter_by(CiktiID=CiktiID).first()
            alaninfo = Cikti.query.filter_by(CiktiID=CiktiID).first()
            if alaninfo is None: 
                if Cikti1 is not None  :
                    returnValue+="bu cikti silinemez\n"
                else :                                 
                    db.session.delete(alaninfo)
                    db.session.commit()  
        if Belirtecv=="1":
            BelirtecID=int(request.form.get("BelirtecID")) 
            BelirtecTanimi=request.form.get("BelirtecTanimi")            
            alaninfo = Belirtecler.query.filter_by(BelirtecID=BelirtecID).first() 
            if alaninfo is None:               
                data=Cikti(BelirtecID,BelirtecTanimi)
                db.session.add(data)
                db.session.commit()
            else:
                returnValue+="boyle bir belirtec zaten var\n"
        elif  Belirtecv=="2":
            BelirtecID=int(request.form.get("BelirtecID"))
            Cikti1 = CiktiDetay.query.filter_by(CiktiID=CiktiID).first()            
            alaninfo = Belirtecler.query.filter_by(BelirtecID=BelirtecID).first()
            if alaninfo is None: 
                if Cikti1 is not None  :
                    returnValue+="bu belirtec silinemez\n"
                else :                                 
                    db.session.delete(alaninfo)
                    db.session.commit() 
        return render_template('home.html')
@app.route('/eslesme',methods=['GET', 'POST'])
def eslesmeIslemi():
    if(request.method == "POST"):
        problemID = int(request.form.get("problemID"))
        BirimID = int(request.form.get("BirimID"))        
        problem = Problemler.query.filter_by(ProblemTipiID=problemID).first()
        eslesmeTarihi=""
        birim = Birimler.query.filter_by(BirimKodu=BirimID).first()
        if problem is None or birim is None :
            return render_template('Eslesme.html',message="girilen degerler hatali")
        else:
            data=ProblemBirim(problemID,BirimID,eslesmeTarihi) 
            db.session.add(data)
            db.session.commit()
            return render_template('admin.html', message="Yeni isleminiz nedir?")  
@app.route('/birimesleme',methods=['GET', 'POST'])
def eBirimElesmeIslemi():
        if(request.method == "POST"):
            problemID = int(request.form.get("problemID"))
            kullaniciADi = request.form.get("KullaniciADi")        
            problem = Problemler.query.filter_by(ProblemTipiID=problemID).first()            
            birim = Kullanicilar.query.filter_by(KullaniciAdi=kullaniciADi).first()
            if problem is None or birim is None :                
                return render_template('BirimYonetici.html',message="girilen degerler hatali")
            else:
                data=PersonelProblem(problemID,kullaniciADi) 
                db.session.add(data)
                db.session.commit()
            return render_template('BirimYonetici.html', message="Yeni isleminiz nedir?") 
@app.route('/personel',methods=['GET', 'POST'])
def personelislem():
    if(request.method == "POST"):
        e_posta = request.form.get("e_posta")
        cep = request.form.get("cep")
        ev_adresi = request.form.get("ev_adresi")  
        personel = Kullanicilar.query.filter_by(KullaniciAdi=islem_yapilan_kullanici).first()                                 
        if e_posta is not None:
            personel.Email = e_posta
        if cep is not None:       
             personel.Cep = cep 
        if ev_adresi is not None:       
            personel.Ev_adresi = ev_adresi                    
        db.session.commit() 
        return render_template('BirimYonetici.html', message="Yeni isleminiz nedir?") 
@app.route('/degerlendirme',methods=['GET', 'POST'])
def degerlendirme():
    if(request.method == "POST"):
      return render_template('degerlendir.html')
@app.route('/degerlendirmeGirdi',methods=['GET', 'POST'])
def degerlendirmeGirdi():
    if(request.method == "POST"):
        problemID = int(request.form.get("problemID"))
        belirtecID = int(request.form.get("belirtecID"))
        skor = int(request.form.get("skor"))
        problem = Problemler.query.filter_by(ProblemTipiID=problemID).first()            
        belirtec = Birimler.query.filter_by(BirimKodu=belirtecID).first()
        if problem is None or belirtec is None :
            print("asdfv") 
            return render_template('degerlendir.html',message="degerlendirme yanlis") 
        else :
           data=PersonelCiktiDegerlendirme(problemID,belirtecID,skor,21) 
           db.session.add(data)
           db.session.commit() 

    return render_template('home.html')               
if __name__ == '__main__':
    app.run()
    