import __main__ as main
istrigger=1
index=5
originimage=b"images\\ground.png"
supplement="self.delete=False"
variable=""
def Update(self):pass
def OnCollision(self,collider):
    if collider == main.player or collider == "fground":
        self.delete=True
        self.rect=main.pygame.rect.Rect(self.rect[0]-1,self.rect[1]-1,self.rect[2]+2,self.rect[3]+2)
        colliders=main.pygame.sprite.spritecollide(self,main.groups["fground"],0)
        if colliders:
            for collider in colliders:
                if not collider.delete:
                    collider.OnCollision("fground")
        self.Delete()
