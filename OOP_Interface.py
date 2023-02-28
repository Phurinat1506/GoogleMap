import pymongo
import sys 
import os
sys.path.append(os.path.abspath("C:/xampp/htdocs/GoogleMap/"))
from OOP_Switch import Switches 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")#connect mongoDB


mydb = myclient["MFU"]#connect database
#print(myclient.list_database_names())


mycol = mydb["interfaces"]#select collection
#print(mydb.list_collection_names())


class Interfaces:
    def __init__(self,name_1,interface_1,name_2,interface_2):
        self.name_1 = name_1
        self.interface_1 = interface_1
        self.name_2 = name_2
        self.interface_2 = interface_2
        
    def insert_INT(self,count_id,lat_point1,lng_point1,lat_point2,lng_point2):
        array_int=["Interfaces:{}".format(self.name_1+" : "+ self.interface_1),"Interfaces:{}".format(self.name_2+" : "+ self.interface_2)]

        self.lat_point1 = lat_point1
        self.lng_point1 = lng_point1
        self.lat_point2 = lat_point2
        self.lng_point2 = lng_point2
        array_point=[ {"lat":self.lat_point1,"lng":self.lng_point1},{"lat":self.lat_point2,"lng":self.lng_point2}]
        #str_val = " ".join(set_val)
        self.count_id = count_id
       
        try:
            x = mycol.insert_one({"_id": self.count_id,"int":array_int,"path":array_point})#insert one document /array type
        
            print(x.inserted_id)
        
        except:
            pass

    def update_INT(self,update_id,new_values):
        self.update_id = update_id
        self.new_values = new_values
        self.i = 0
       
        
        array_detail = [self.name_1,self.interface_1,self.name_2,self.interface_2]
        #update detail field /array type
        
        for self.i in array_detail:
            mycol.update_one( { '_id': update_id},{'$set': { 'int.0':"Interfaces:{}".format(new_values[0]+":"+new_values[1]) } })
            mycol.update_one( { '_id': update_id},{'$set': { 'int.1':"Interfaces:{}".format(new_values[2]+":"+new_values[3]) } })
           


    def update_Point(self,update_id,lat_point1,lng_point1,lat_point2,lng_point2):
        
        mycol.update_one( { '_id': update_id},{'$set': { 'path.0.lat':lat_point1}})
        mycol.update_one( { '_id': update_id},{'$set': { 'path.0.lng':lng_point1}})
        mycol.update_one( { '_id': update_id},{'$set': { 'path.1.lat':lat_point2}})
        mycol.update_one( { '_id': update_id},{'$set': { 'path.1.lng':lng_point2}})
        

    def delete_INT(self,delete_id):
        self.delete_id = delete_id
        mycol.delete_one({'_id': delete_id})

    
            


#-------------------------------------------------Manage Interface-----------------------------------------------------------------------#










