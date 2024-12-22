import __main__ as main
originimage=b"images\\portal.png"
istrigger=1
index=1
variable="target=[0,0,0]"
supplement="self.target=target"
def OnCollision(self,collider):
    if collider == main.player:
        main.Game.OnChangeLevel(self.target[0])
        main.player.xy=list(self.target[1:])
def Update(self):
    main.events.Rotate(self,-10**10,10**11)
