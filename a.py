class astareg:

    empcount = 0
    g = 0
    f = [0,0,0,0,0,0,0,0]
    states = {0:'Rajasthan',1:'Tamil Nadu',2:'Maharashtra',3:'Karnataka',4:'West Bengal',5:'Madhya Pradesh',6:'Punjab',7:'Arunachal Pradesh'}
    mins = 0
    closelist = []
    openlist = []
    def isTrue(self,closelistCheck,startnode,I):
        if(closelistCheck[startnode] or closelistCheck[I]):
            return "false"

        else:
            return "true"

    def track_route(self,a,heuristics,startnode,endnode,parent):

        f=[0,0,0,0,0,0,0,0]
        k = len(self.openlist)
        if(k>=0):
            self.closelist.append(startnode)

            for i in range(8):
                if(a[startnode][i]):
                    if(i==endnode):
                        self.closelist.append(i)
                        parent=parent+a[startnode][i]

                        print("Distance to destination",parent)
                        print("Path")

                        for i in (self.closelist):
                            print(self.states.get(i),)
                            print("|\n\/",)
                        print("--------------")
                        return
                    f[i] = parent+a[startnode][i]+heuristics[i] 

                else:
                    f[i]=999
            mins = f.index(min(f))

            parent=parent+a[startnode][mins]

            for i in range(len(f)):
                if(f[i]<999 and f[mins]!=f[i]):
                    self.openlist.append(i)

            self.track_route(a,heuristics,mins,endnode,parent)

astar = astareg()
a = [[0,75,118,140,0,0,0,0],[75,0,0,50,0,0,0,0],[118,0,0,0,0,0,0,0],
[140,50,0,0,0,99,0,80],[0,0,0,0,0,0,101,97],[0,0,0,99,0,0,211,0],
[0,0,0,0,101,211,0,0],[0,0,0,80,97,0,0,0]]        

print("\n\n\t\t\t\t--------A Star---------\n\n\n")
print("----------------------------------------------------------------")
print("-----------Enter below codes to travel---------------------------------")
print("----------------------------------------------------------------------------")
print("------------0:Rajasthan-------------")
print("------------1:Tamil Nadu------------")
print("------------2:Maharashtra-----------")
print("------------3:Karnataka-------------")
print("------------4:West Bengal-----------")
print("------------5:Madhya Pradesh--------")
print("------------6:Punjab----------------")
print("------------7:Arunachal Pradesh----------------")


startnode = int(input("Enter Your Location:"))
endnode = int(input("Enter your destination:"))

parent = 0

heuristics = [366,374,329,253,10,176,0,193]

astar.track_route(a,heuristics,startnode,endnode,parent)
