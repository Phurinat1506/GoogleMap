import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")#connect mongoDB

mydb = myclient["MFU"]#connect database
#print(myclient.list_database_names())

mycol = mydb["switches"]#select collection
#print(mydb.list_collection_names())

class Switches:

    def __init__(self,name,ip,cpu,portstatus,portinbound,portoutbound,log):
        self.name = name 
        self.ip = ip 
        self.cpu = cpu
        self.portstatus = portstatus 
        self.portinbound = portinbound
        self.portoutbound = portoutbound
        self.log = log
       
    def insert_SW(self,count_id,lat,lng):
        self.status_sw = 0
        array_detail=["Name:{}".format(self.name),"IP:{}".format(self.ip),"CPU:{}".format(self.cpu+"%"),"PortStatus:{}".format(self.portstatus)
        ,"PortInbound:{}".format(self.portinbound+"bits/sec"),"PortOutbound:{}".format(self.portoutbound+"bits/sec"),"Log:{}".format(self.log)]
        #str_val = " ".join(set_val)
        self.count_id = count_id
        self.lat = lat
        self.lng = lng

        try:
            x = mycol.insert_one({"_id": self.count_id,"detail":array_detail,"lat": self.lat,"lng": self.lng,"status":self.status_sw})#insert one document /array type
        
            print(x.inserted_id)
        except:
            pass
    def update_SW(self,update_id,new_values):
        self.update_id = update_id
        self.new_values = new_values
        self.i = 0
        self.num_cdp = 0
        
        
        array_detail = ["Name:{}".format(self.name),"IP:{}".format(self.ip),"CPU:{}".format(self.cpu),"PortStatus:{}".format(self.portstatus)
        ,"PortInbound:{}".format(self.portinbound),"PortOutbound:{}".format(self.portoutbound),"Log:{}".format(self.log)]
        #update detail field /array type
        
        for self.i in array_detail:

            mycol.update_one( { '_id': update_id},{'$set': { 'detail.0':"Name:{}".format(new_values[0]) } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.1':"IP:{}".format(new_values[1]) } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.2':"CPU:{}".format(new_values[2]+"%") } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.3':"PortStatus:{}".format(new_values[3]) } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.4':"PortInbound:{}".format(new_values[4]+" bits/sec ") } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.5':"PortOutbound:{}".format(new_values[5]+ " bits/sec ") } })
            mycol.update_one( { '_id': update_id},{'$set': { 'detail.6':"Log:{}".format(new_values[6]) } })
            mycol.update_one( { '_id': update_id},{'$set': { 'status':new_values[7]} })
            
    def update_Location(self,update_id,lat,lng):
        mycol.update_one( { '_id': update_id},{'$set': { 'lat':lat}})
        mycol.update_one( { '_id': update_id},{'$set': { 'lng':lng}})
    
    def delete_SW(self,delete_id):
        self.delete_id = delete_id
        mycol.delete_one({'_id': delete_id})
            
   
            


"""
for x in mycol.find():#find all document
    print(x)
"""  
        


     
  
