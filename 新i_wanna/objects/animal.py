import __main__ as main
originimage=b"images\\animal.png"
istrigger=1
index=2
variable="speed=1"
supplement="self.speed,self.img,self.vertically=[speed,0],image,1"
def Update(self):
    self.jumptwice=1
    self.speed[1]-=1/1000
    self.xy[0]+=self.speed[0]
    self.xy[1]-=self.speed[1]
    for group in main.groups.values():
        colliders=main.pygame.sprite.spritecollide(self,group,0)
        if colliders:
            for collider in colliders:
                if collider!=self:
                    self.OnCollision(collider)
                    collider.OnCollision(self)
    if self.vertically*self.speed[0]<0:
        self.ImgUpdate(self,flip=[1,0])
        self.vertically*=-1
def OnCollision(self,collider):
    self.rect.center =[(self.xy[i]+main.Game.xy[i])*40 for i in (0,1)]
    point=main.pygame.sprite.collide_mask(self,collider)
    rect=self.rect.union(collider.rect).clip(self.rect).clip(collider.rect)
    if point:
        globalpoint=self.xy[0]+point[0],self.xy[1]+point[1]
        if not collider.istrigger:
            self.highdata=0
            if rect[2]>rect[3]:
                if self.xy[1]<collider.xy[1]:
                    self.speed[1]=0
                    if collider == main.player:
                        main.Game.OnDeath()
                    else:
                        self.rect.bottom = collider.rect.top+1
                else:
                    if collider == main.player:
                        main.player.speed[1]=1/20
                        self.Delete()
                    else:
                        self.rect.top = collider.rect.bottom
            else:
                if self.xy[0]<collider.xy[0]:
                    self.rect.right = collider.rect.left
                    if collider == main.player:
                        if self.rect.center[1] < collider.rect.bottom:
                            main.player.speed[1]=1/20
                            self.Delete()
                        else:  
                            main.Game.OnDeath()
                    else:
                        self.speed[0]=-self.speed[0]
                else:
                    self.rect.left = collider.rect.right
                    if collider == main.player:
                        if self.rect.center[1] < collider.rect.bottom:
                            main.player.speed[1]=1/20
                            self.Delete()
                        else:  
                            main.Game.OnDeath()
                    else:
                        self.speed[0]=-self.speed[0]
            self.xy=[self.rect.center[i]/40-main.Game.xy[i] for i in (0,1)]
