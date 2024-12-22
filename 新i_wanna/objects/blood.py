import __main__ as main
originimage=b"images\\animal.png"
istrigger=1
index=2
variable="speed=1"
supplement="self.speed=[speed,0]"
def Update(self):
    self.speed[1]-=1/100
    self.rect[0]+=self.speed[0]
    self.rect[1]-=self.speed[1]
    for group in main.groups.values():
        colliders=main.pygame.sprite.spritecollide(self,group,0)
        if colliders:
            for collider in colliders:
                self.OnCollision(collider)
                collider.OnCollision(self)
    self.xy=[self.rect.topleft[0]/40,self.rect.topleft[1]/40]
def OnCollision(self,collider):
    if collider != main.player:
        main.Game.OnDeath()
        
