import sys,animation
import __main__ as main
check="c8d4a11d7faf8580a2b67dbf1b672d01"
txt=main.UI.Text("文档",(0,0),"按↑或W跳跃（可以二段跳），按←→或AD键移动",(255,255,128),wordsize=40,page=None)
def Init():
    Save((17,14),{"Collision":[lambda self:Funcs(self,1)]})
    Trap((13,14),{lambda self:player.xy[0]>13:[lambda self:events.MoveTo(self,(13,-1),1000,a=1/2)]})
    Trap((15,15),{lambda self:player.xy[0]>14:[lambda self:events.MoveTo(self,(15,6),1000,a=1/2)]},180)
    Trap((15,20),{lambda self:player.xy[0]<16 and player.xy[1]>16:[lambda self:events.MoveTo(self,(15,20),500,(15,6),a=1/2)]},180)
    Ground((4,19),{lambda self:True:[lambda self:txt.Draw()]})
    Ground((17,15),{})
    Ground((13,15),{})
    for y in 0,1,2,3:
        for x in range(26):
            if x==16 and y==2:
                Water((15,18),(0.5,0.95),{})
            else:Ground((x-1,16+y),{lambda self:player.xy[0]>18:[lambda self:events.MoveTo(self,("","+5"),500,a=1/2)]})
    for x in range(3):
        Trap((14+x,14),{lambda self:player.xy[0]>14:[lambda self:events.MoveTo(self,("",5),700,a=1/2)]})
        for y in range(10)if x!=1 else range(3):Ground((14+x,15+y),{lambda a:player.xy[0]>14:[lambda self:events.MoveTo(self,("","-9"),500,a=1/2)]})
    for y in range(20):Trap((25,y),{lambda self:player.xy[0]>18:[lambda self:events.MoveTo(self,("-20",""),5000,a=2),
                                    lambda self:events.MoveTo(self,("+23",""),1000,a=2)]},90)
    for y in range(20):Trap((-2,y),{lambda self:player.xy[0]<5 and player.xy[1]>17:[lambda self:events.MoveTo(self,("+6",""),3000,a=1/5),
                                    lambda self:events.MoveTo(self,("+20",""),3000,a=2),
                                    lambda self:events.MoveTo(self,("-25",""),1000,a=2)]},270)
    Force((10,10),(1,0),{lambda self:player.xy[0]>10:[lambda self:events.MoveTo(self,("+2",""),500,a=1/2)],
                         lambda self:player.xy[1]>16:[lambda self:events.MoveTo(self,("","-11"),1000,a=1/2)]})
    Force((10,10),(1,0),{lambda self:player.xy[0]>10:[lambda self:events.MoveTo(self,("+1",""),500,a=1/2)],
                         lambda self:player.xy[1]>16:[lambda self:events.MoveTo(self,("","-11"),1000,a=1/2)]})
    Force((10,10),(1,0),{lambda self:player.xy[1]>16:[lambda self:events.MoveTo(self,("","-11"),1000,a=1/2)]})
    Animal((-1,15),0,{lambda self:player.xy[0]>3:[lambda self:Funcs(self,0)]})
    Portal((-1,8),(1,3,13),{lambda self:player.xy[0]>10:[lambda self:events.MoveTo(self,("","-5"))]})#作者通道
def OnOutOfScreen(direction):
    if direction!="right":
        game.OnDeath()
    else:
        game.Save()
        game.OnChangeLevel(1)
        player.xy=[3,13]
def Oncollision(collider,point):pass
def Funcs(self,number):
    match number:
        case 0:
            self.speed[0]=0.02
        case 1:
            txt.value="存档成功~（>w<）~"
            txt.Update()
            self.Delete()
    return True
def Check(self,number):pass
def Update(event):pass
