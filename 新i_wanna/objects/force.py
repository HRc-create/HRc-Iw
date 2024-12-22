import __main__ as main
originimage=b"images\\force.png"
supplement="self.force=force"
istrigger=1
index=1
variable="force=[1,0]"
def Update(self):pass
def OnCollision(self,collider):
    if collider == main.player or collider in main.groups["animal"]:
        collider.jumptwice=1
        for i in 0,1:
            collider.speed[i]+=self.force[i]
        
