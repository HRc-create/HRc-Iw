import sys,animation
import __main__ as main
check="49cb846a0691cc1216afcd09de64df1e"
def Init():
    Save((3,13),{})
    for y in 0,3:
        for x in range(25):
            Ground((x,16+y),{lambda self:(player.xy[0]<2 and player.xy[1]>15 and self.xy[0]==1):[lambda self:events.MoveTo(self,["","+5"],500,a=1)]})
    for y in 1,2:
        for x in range(25):
            Fground((x,16+y),{lambda self:(player.xy[0]<2 and player.xy[1]>15 and self.xy[0]==1):[lambda self:events.MoveTo(self,["","+5"],500,a=1)]})
    for y in range(16):
        Ground((25,15-y),{lambda self:game.stage==1:[lambda self:events.MoveTo(self,(2,""),5000,a=2)]})
    Ground((25,17),{lambda self:player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,[0,""],7000,a=1)]})
    Ground((25,18),{lambda self:player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,[0,""],7000,a=1)]})
    for x in range(5):
        Trap((x+1,15),{lambda self:game.stage==0 and player.xy[0]<1:[lambda self:events.MoveTo(self,("-1",""),100)],
                       lambda self:game.stage==0 and player.xy[0]>9:[lambda self:events.MoveTo(self,("+7",""),1000)],
                       lambda self:game.stage==0 and player.xy[0]>15:[lambda self:events.MoveTo(self,("+6",""),1000)],
                       lambda self:game.stage==0 and player.xy[0]>21:[lambda self:events.MoveTo(self,("+6",""),1000)],
                       lambda self:game.stage==1:[lambda self:self.Delete()]})
    Save((24,15),{lambda self:player.xy[0]>24:[lambda self:game.SetStage(1)]})
    Trap((6,9),{lambda self:game.stage==0 and player.xy[0]>6:[lambda self:events.MoveTo(self,("","+5"),500,a=1/2)],
                lambda self:game.stage==1:[lambda self:events.MoveTo(self,("","+20"),1000,a=1)]},270)
    Trap((6,10),{lambda self:game.stage==1 and player.xy[0]<8:[lambda self:events.MoveTo(self,("","+2"),500,a=1)]})
    Trap((6,11),{lambda self:game.stage==1 and player.xy[0]<8:[lambda self:events.MoveTo(self,("","+2"),500,a=1)]},180)
    Trap((6,12),{lambda self:game.stage==1 and player.xy[0]<8:[lambda self:events.MoveTo(self,("","+2"),500,a=1)]})
    Trap((6,13),{lambda self:game.stage==1 and player.xy[0]<8:[lambda self:events.MoveTo(self,("","+2"),500,a=1)]},180)
    Trap((6,15),{lambda self:game.stage==1 and player.xy[0]<8:[lambda self:events.MoveTo(self,("","+3"),500,a=1)]})
    Trap((12,15),{lambda self:player.xy[0]>12:[lambda self:events.MoveTo(self,["",-1],500,a=2)]})
    Trap((18,9),{lambda self:game.stage==0 and player.xy[0]>18:[lambda self:events.MoveTo(self,("","+5"),500,a=1/2)],
                 lambda self:game.stage==1:[lambda self:events.MoveTo(self,("","+20"),1000,a=1)]},90)
    Trap((18,10),{lambda self:game.stage==1 and player.xy[0]<20:[lambda self:events.MoveTo(self,("","+2"),900,a=1/2)]})
    Trap((18,11),{lambda self:game.stage==1 and player.xy[0]<20:[lambda self:events.MoveTo(self,("","+2"),900,a=1/2)]},180)
    Trap((18,12),{lambda self:game.stage==1 and player.xy[0]<20:[lambda self:events.MoveTo(self,("","+2"),900,a=1/2)]})
    Trap((18,13),{lambda self:game.stage==1 and player.xy[0]<20:[lambda self:events.MoveTo(self,("","+2"),900,a=1/2)]},180)
    Trap((18,15),{lambda self:game.stage==1 and player.xy[0]<20:[lambda self:events.MoveTo(self,("","+3"),900,a=1/2)]})
    for i in range(11):
        Trap((7+i,-1),{lambda self:game.stage==1 and player.xy[0]<18:[lambda self:events.MoveTo(self,["","+15"],700,a=1/2),
                                                                      lambda self:events.MoveTo(self,["","-15"],700,a=2)]},180)
        Trap((7+i,20),{lambda self:game.stage==1 and player.xy[0]<9:[lambda self:events.MoveTo(self,["","-8"],1000,a=1/2),
                                                                     lambda self:events.MoveTo(self,["","+3"],1000,a=2)]})
    Trap((0,17),{lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>3:[lambda self:events.MoveTo(self,[6,""],1000,a=1/2)],
                 lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>16:[lambda self:events.MoveTo(self,[18,""],800,a=1/2)],
                 lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,[0,""],1000,a=1/2)]},180)
    Trap((0,18),{lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,[26,""],1000,a=1)]})
    Trap((0,-1),{lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,("",16),8000,a=1)]},180)
    Trap((1,-1),{lambda self:game.stage==1 and player.xy[1]>16 and player.xy[0]>23:[lambda self:events.MoveTo(self,("",16),8000,a=1)]},180)
    Portal((-1,8),(2,1.5,18.5),{})
def Update(event):
    pass
def OnOutOfScreen(direction):
    if direction!="right":
        game.OnDeath()
    else:
        game.Save()
        game.OnChangeLevel(2)
        player.xy=[1.5,18.5]
def Oncollision(collider,globalpoint):
    pass
def Reset():
    Delete()
def Funcs(self,number):
    pass
def Check(self,number):
    pass
