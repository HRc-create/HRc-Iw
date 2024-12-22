import sys,animation
import __main__ as main
sys.path.append("objects")
objects=__import__("objects",fromlist=['*'])
check="d622ee014338d054abbcaa32c270affd"
import random,os
def Init():
    global starttime,deltatime
    game.xy=[0.5,0.5]
    events.Sound("",isbackground=True,play=True)
    events.Sound("",isbackground=False,play=False)
    starttime,deltatime=0,-1
    Save((1,18),{})
    for x in range(50):
        Ground((25+x,19),{})
    for x in range(25):
        Ground((x,19),{lambda self:deltatime > 42000:[lambda self:events.Wait(self,1000*random.randint(1,7)),
                                                     lambda self:events.MoveTo(self,["",21],5000,a=2),
                                                     lambda self:events.MoveTo(self,["",19],1000,a=1/2),"save"]})
        Ground((x,21),{lambda self:deltatime > 50000:[lambda self:events.MoveTo(self,["",19],1000,a=2)]})
        Trap((x,-1),{lambda self:deltatime > 0 and self.xy[1]!=0:[lambda self:events.MoveTo(self,["",0],2000)], 
                     lambda self:self.xy[1]==0:[lambda self:events.Wait(self,1900*random.randint(0,5)),lambda self:events.MoveTo(self,["",25],1000,a=2),
                                                                                                          lambda self:events.MoveTo(self,["",0],900,["",-1],a=1/2),"save"]},rotation=180)
        Trap((x,-1),{lambda self:deltatime > 7000 and self.xy[1]!=0:[lambda self:events.MoveTo(self,["",0],2000)], 
                     lambda self:self.xy[1]==0 and player.xy[0]>self.xy[0]-0.5 and player.xy[0]<self.xy[0]+0.5:[lambda self:events.MoveTo(self,["",25],5000,a=2),
                                                                                                                lambda self:events.MoveTo(self,["",0],3000,["",-1],a=1/2),"save"]},rotation=180)
        Trap((x,-1),{lambda self:deltatime > 14000 and self.xy[1]!=0:[lambda self:events.MoveTo(self,["",0],2000)], 
                     lambda self:self.xy[1]==0 and player.xy[0]>self.xy[0]-0.5 and player.xy[0]<self.xy[0]+0.5:[lambda self:events.MoveTo(self,["",25],3500,a=2),
                                                                                                                lambda self:events.MoveTo(self,["",0],3500,["",-1],a=1/2),"save"]},rotation=180)
        Trap((x,-1),{lambda self:deltatime > 35000 and self.xy[1]!=0:[lambda self:events.MoveTo(self,["",0],2000)], 
                     lambda self:self.xy[1]==0:[lambda self:events.Wait(self,1750*random.randint(0,5)),lambda self:events.MoveTo(self,["",18],3500,a=1/2),
                                                                                   lambda self:events.MoveTo(self,["",0],1750,a=2),"save"]},rotation=180)
    for y in range(19):
        Ground((-1,18-y),{lambda self:deltatime > 21000:[lambda self:events.MoveTo(self,[15,""],2000,a=1/2),lambda self:events.MoveTo(self,[-1,""],5000,a=2)],
                          lambda self:game.stage==1:[lambda self:events.MoveTo(self,[50,""],15000,a=1)]})
        Ground((25,18-y),{lambda self:deltatime > 28000:[lambda self:events.MoveTo(self,[10,""],2000,a=1/2),lambda self:events.MoveTo(self,[25,""],5000,a=2)],
                          lambda self:game.stage==1:[lambda self:events.MoveTo(self,["","-19"],5000,a=1/2)]})
    End((65,15),{lambda self:game.stage==0 and player.xy[0]>3:[lambda self:Funcs(self,0),lambda self:events.Sound(self,isbackground=True,play=False),lambda self:events.Sound(self,os.path.join('sound',"Challenge.mp3"))],
                lambda self:deltatime > 50000:[lambda self:Trap.Clear(self),
                                               lambda self:events.Sound(self,isbackground=True,play=True),
                                               lambda self:events.Sound(self,isbackground=False,play=False),
                                               lambda self:game.SetStage(1)],
                lambda self:game.stage==1:[lambda self:events.MoveTo(game,["-50",""],15000,a=2)]})
def Update(event):
    global deltatime
    if starttime:deltatime=main.pygame.time.get_ticks()-starttime
def OnOutOfScreen(direction):
    if direction=="right":
        game.OnWin()
        player.moveable=(0,0)
    else:
        game.OnDeath()
def Oncollision(collider,globalpoint):
    pass
def Reset():
    Delete()
def Funcs(self,number):
    global starttime
    match number:
        case 0:starttime=main.pygame.time.get_ticks()
    return True
def Check(self,number):
    match number:
        case 0:return (player.xy[0]<1 or self.xy[0]!=1 )and self.xy[0]>0
