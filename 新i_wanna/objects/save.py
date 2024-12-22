import __main__ as main
originimage=b"images\\save.png"
istrigger=1
index=1
variable=""
supplement="self.data=0"
def OnCollision(self,collider):
    if collider == main.player or collider.type=="bullet":
        self.ImgUpdate(self,size=(1,1),image="images\\save1.png")
        main.Game.Save()
def Update(self):
    if self.data:
        self.offset[1]+=0.1
        if self.offset[1]>=10:
            self.data=not self.data
    else:
        self.offset[1]-=0.1
        if self.offset[1]<=-10:
            self.data=not self.data
