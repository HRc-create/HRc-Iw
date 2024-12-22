import __main__ as main
originimage=b"images\\animal.png"
istrigger=1
index=2
variable=""
supplement='flip=(1,0)'
def Update(self):
    game=main.Game
    match game.stage:
        case 0:
            if main.player.xy[0]>10 and main.events.Scale(self,10,5000,2):
                game.SetStage(5)
        case 1:pass
    
def OnCollision(self,collider):
    point=main.pygame.sprite.collide_mask(self,collider)
    rect=self.rect.union(collider.rect).clip(self.rect).clip(collider.rect)
    if point:
        globalpoint=self.xy[0]+point[0],self.xy[1]+point[1]
        if not collider.istrigger:
            self.highdata=0
            if rect[2]>rect[3]:
                if self.xy[1]<collider.xy[1]:
                    self.speed[1]=0
                    #self.speed[1]=5
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
