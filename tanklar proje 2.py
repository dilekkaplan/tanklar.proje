class SilahliKuvvetler():
    def __init__(self,name,yearOfStart):
        self.name=name
        self.yearOfStart=yearOfStart


class Tanklar(SilahliKuvvetler):

    def __init__(self,name,yearOfStart,origin):
        super().__init__(name,yearOfStart)
        self.origin=origin

#info fonksiyonu ile tank isim, kullanım yılı ve menşei ile ilgili bilgileri yazdırıyoruz.

    def info(self):
        print("Tank İsmi:",self.name,"\nKullanıma başlama yılı:",self.yearOfStart,"\nOrijin:",self.origin)




    def agility(self,strength,weight):
        #Tankın ağırlığı ton cinsinden girilir.       

        self.strength=strength
        self.weight=weight

        agility=strength/weight
        #Bir tankın çevikliği tank gücünün ağırlığına bölünmesi ile elde edilir.
        

        if agility>=18:

            #Tankın çevilikiği >18 ise tankın çevik olduğu kabul edilmiştir.

            #Tank ağırlığı 55 tondan büyükse ağır, 50-55 arasındaysa orta ağırlıkta ve 50den küçükse hafif tank olarak kabul edilmiştir.
            
            if weight>=55:
                print(self.name, "atik ve ağır bir tanktır.")

            if 50<weight<55:
                print(self.name, "atik ve orta ağırlıkta bir tanktır.")

            if weight<50:
                print(self.name, "atik ve hafif bir tanktır.")         

        else:
            print(self.name, "atik bir tank değildir.")



    def time2repair(self):

        #içinde bulunulan seneyi kullanabilmek için datetime modülü import ettik.
        from datetime import datetime
        date=datetime.now()
        year=date.year
        #Biz yalnızca yıl ile ilgilendiğimiz için yıl year fonksiyonu ile içinde bulunduğumuz yıl bilgisini çektik.


        if (year-self.yearOfStart)%5==0:
            #Tankların bakımı 5 yılda bir yapılmalıdır.
            #Tankın kullanıma başlandığı yıl esas alınarak bakım yapılması gerken sene hesaplanmıştır

            print(self.yearOfStart, "yılında alınan", self.name, "nin bakımı bu yıl içerisinde yapılmıştır,5 yıl sonra tekrar bakımı yapılacaktır.")

        elif (year-self.yearOfStart)%5!=0:

            print(self.yearOfStart,"yılında alınan",self.name, "nin bakımı", (5-((year-self.yearOfStart)%5)), "yıl sonra yapılacaktır.")

    def is_usable_in_water(self,passwater,passwater_prep):
        self.passwater=passwater
        self.passwater_prep=passwater_prep

        if (passwater_prep-passwater)>200:
            return True

        else:
            return False


#Tanklar child classı altında oluşturduğumuz TSK bünyesinde yer alan farklı tanklara ait nesneler

M48_Patton= Tanklar("M48_Patton",1974,"US")
M60_Patton=Tanklar("M60_Patton",1960,"US")
Leopard_1A3T1= Tanklar("Leopard_1A3T1",1982,"Germany")
Leopard_2A4=Tanklar("Leopard_2A4", 2005,"Germany")
M60T=Tanklar("M60T",2005,"US/Israel")



M48_Patton.info()
M60_Patton.info()
Leopard_1A3T1.info()
Leopard_2A4.info()
M60T.info()

M48_Patton.time2repair()
M60_Patton.time2repair()
Leopard_1A3T1.time2repair()
Leopard_2A4.time2repair()
M60T.time2repair()


M48_Patton.is_usable_in_water(122,240)
M60_Patton.is_usable_in_water(122,240)
Leopard_1A3T1.is_usable_in_water(120,325)
Leopard_2A4.is_usable_in_water(120,400)
M60T.is_usable_in_water(122,244)

M48_Patton.agility(750,49)
M60_Patton.agility(750,52.6)
Leopard_1A3T1.agility(830,42.2)
Leopard_2A4.agility(1479,55)
M60T.agility(1000,59)
