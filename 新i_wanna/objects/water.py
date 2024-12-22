import __main__ as main
originimage=b"images\\water.png"
istrigger=1
index=1
variable="drag=[0.5,0.9]"
supplement="self.drag=drag"
def Update(self):pass
def OnCollision(self,collider):
    if collider == main.player:
        main.player.drag=self.drag
        main.player.jumptwice=1
