import __main__ as main
originimage=b"images\\trap.png"
istrigger=1
variable=""
index=2
supplement=""
def Update(self):pass
def OnCollision(self,collider):
    if collider == main.player:main.Game.OnDeath()
