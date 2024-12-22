import sys,animation
import __main__ as main
sys.path.append("objects")
objects=__import__("objects",fromlist=['*'])
check="4f54513dbd47a855b17884db03824a64"
def Init():
    Save((1,18),{lambda self:game.stage==0 and player.xy[0]>2:[lambda self:events.MoveTo(self,["",0],5000,a=2),lambda self:events.MoveTo(self,["",2],1000,a=2)],
                 lambda self:game.stage==1 :[lambda self:events.MoveTo(self,[1,2],1000,a=2)],
                 lambda self:game.stage in [2,3]:[lambda self:events.MoveTo(self,[2,6],1000,a=2)],
                 lambda self:game.stage in [4,5]:[lambda self:events.MoveTo(self,[1,18],1000,a=2)]})
    for x in range(25):
        Ground((x,19) if game.stage in [0,5]else (x,3) if game.stage==1 else (x,7),
                {lambda self:game.stage==0 and player.xy[0]>2:[lambda self:events.MoveTo(self,["",1],5000,a=2),lambda self:events.MoveTo(self,["",3],1000,a=2),lambda self:main.Game.SetStage(1)],
                 lambda self:game.stage==1 and (player.xy[0]>24 or self.xy[1]==19):[lambda self:events.MoveTo(self,["",5],1000,a=2),lambda self:main.Game.SetStage(2)],
                 lambda self:game.stage==2 and (player.xy[0]<1 or self.xy[1]==19):[lambda self:events.MoveTo(self,["",7],1000,a=2),lambda self:main.Game.SetStage(3)],
                 lambda self:game.stage==3 and (player.xy[0]>24 or self.xy[1]==19):[lambda self:events.MoveTo(self,["",9],1000,a=2),lambda self:main.Game.SetStage(4)],
                 lambda self:game.stage==4 and (player.xy[0]<1 or self.xy[1]==19):[lambda self:events.MoveTo(self,["",19],3000,a=2),lambda self:main.Game.SetStage(5)]})
    Trap((25,1),{lambda self:game.stage>0:[lambda self:events.MoveTo(self,[3,""],1000,a=1/2)]})
    Trap((25,1),{lambda self:game.stage>0:[lambda self:events.MoveTo(self,[14,""],2000,a=1)]})
    Trap((25,2),{lambda self:game.stage>0:[lambda self:events.MoveTo(self,[3,""],5000,a=1/3)]},rotation=180)
    Trap((25,2),{lambda self:game.stage>0:[lambda self:events.MoveTo(self,[14,""],10000,a=1)]},rotation=180)
    Trap((-1,2),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[21,""],8000,a=1/3)]})
    Trap((-1,2),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[8,""],3000,a=4)]})
    Trap((-1,3),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[21,""],6000,a=2)]},rotation=180)
    Trap((-1,3),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[8,""],6000,a=2)]},rotation=180)
    Trap((-1,3),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[5,""],5000,a=1/3)]})
    Trap((-1,3),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[15,""],9000,a=3)]})
    Trap((-1,3),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[24,""],6000,a=1/3)]})
    Trap((-1,4),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[5,""],5000,a=2)]},rotation=180)
    Trap((-1,4),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[15,""],10000,a=3)]},rotation=180)
    Trap((-1,4),{lambda self:game.stage>0 and player.xy[1]>3:[lambda self:events.MoveTo(self,[24,""],1000)]},rotation=180)
    Trap((25,4),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[3,""],3000,a=3)]})
    Trap((25,4),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[10,""],3000)]})
    Trap((25,4),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[18,""],10000)]})
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[3,""],6000,a=2)]},rotation=180)
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[10,""],7000,a=1/2)]},rotation=180)
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[18,""],9000,a=1/2)]},rotation=180)
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[1,""],1000,a=3)]})
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[14,""],8000,a=1/2)]})
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[17,""],2000)]})
    Trap((25,5),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[22,""],5000,a=2)]})
    Trap((25,6),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[1,""],2000)]},rotation=180)
    Trap((25,6),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[14,""],10000,a=2)]},rotation=180)
    Trap((25,6),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[17,""],5000,a=2)]},rotation=180)
    Trap((25,6),{lambda self:game.stage>0 and player.xy[1]>5:[lambda self:events.MoveTo(self,[22,""],1000)]},rotation=180)
    Trap((-1,6),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[6,""],6000,a=1/2)]})
    Trap((-1,6),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[9,""],4000,a=1/2)]})
    Trap((-1,6),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[21,""],2000,a=1/2)]})
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[6,""],1000,a=2)]},rotation=180)
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[9,""],10000,a=1/3)]},rotation=180)
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[21,""],4000,a=1/2)]},rotation=180)
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[1,""],3000,a=2)]})
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[7,""],1000,a=3)]})
    Trap((-1,7),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[13,""],4000,a=1/2)]})
    Trap((-1,8),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[1,""],100,a=2)]},rotation=180)
    Trap((-1,8),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[7,""],1200,a=3)]},rotation=180)
    Trap((-1,8),{lambda self:game.stage>0 and player.xy[1]>7:[lambda self:events.MoveTo(self,[13,""],6000,a=1/2)]},rotation=180)
    for x in range(25):
        Trap((x,-2) if game.stage==0 else (x,0),{lambda self:game.stage==1 or player.xy[1]<1:[lambda self:events.MoveTo(self,["",0])],
                                                lambda self:game.stage>3 and player.xy[0]>self.xy[0] and player.xy[0]<self.xy[0]+1:[lambda self:events.MoveTo(self,["",20],3000,a=2),
                                                                                                                                    lambda self:events.MoveTo(self,["",0],3000,["",-1],a=1/2),"save"]},rotation=180)
    for y in range(3):
        Trap((25,18-y) if game.stage!=5 else (24,18-y),{lambda self:game.stage==0 and player.xy[0]>2:[lambda self:events.MoveTo(self,[0,""],1000,a=1),lambda self:events.MoveTo(self,[24,""],3000,a=2)],
                        lambda self:game.stage==5 and player.xy[1]>self.xy[1] and player.xy[1]<self.xy[1]+1:[lambda self:events.MoveTo(self,[-1,""],5000),
                                                                                                             lambda self:events.MoveTo(self,[24,""],3000,[25,""],a=1/2),"save"]},rotation=90)
    for y in range(16):
        Trap((25,15-y) if game.stage!=5 else (24,15-y),{lambda self:game.stage==5 and player.xy[1]>self.xy[1] and player.xy[1]<self.xy[1]+1:[lambda self:events.MoveTo(self,[-1,""],5000),
                                                                                                             lambda self:events.MoveTo(self,[24,""],1000,[25,""],a=1/2),"save"]},rotation=90)

    for y in range(19):
        Water((-1,18-y) if game.stage!=5 else (0,18-y),(0.5,0.95),{lambda self:game.stage==5 and player.xy[1]>self.xy[1] and player.xy[1]<self.xy[1]+1:[lambda self:events.MoveTo(self,[25,""],5000,a=1),
                                                                                                               lambda self:events.MoveTo(self,[0,""],1000,[-1,""],a=1/2),"save"]},rotation=270)
    for y in range(18):
        Ground((25,18-y),{lambda self:game.stage==5 and player.xy[0]>20:[lambda self:events.MoveTo(self,[13,""],5000,a=2),
                                                       lambda self:events.MoveTo(self,["","-2"],1000,a=1/2),
                                                       lambda self:events.MoveTo(self,["","+2"],1000,a=2),
                                                       lambda self:events.MoveTo(self,[-1,""],5000,a=1/2)]})
def Update(event):
    pass
def OnOutOfScreen(direction):
    if direction!="right":
        game.OnDeath()
    else:
        game.OnChangeLevel(3)
        player.xy=[1.5,18.5]
def Oncollision(collider,globalpoint):
    pass
def Reset():
    Delete()
def Funcs(self,number):
    global stage
    match number:
        case 0:self.xy[0]-=1/50
def Check(self,number):
    match number:
        case 0:return (player.xy[0]<1 or self.xy[0]!=1 )and self.xy[0]>0
